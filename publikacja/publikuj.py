#!/usr/bin/env python3
"""
Skrypt publikacji materiałów dla studentów.

Kopiuje odpowiednie pliki z repo roboczego (lecturesPythonII)
do repo studenckiego (python2-materialy) według harmonogramu.

Użycie:
    python publikuj.py                    # publikuj materiały wg dzisiejszej daty
    python publikuj.py --all              # publikuj WSZYSTKO co jest do dzisiaj
    python publikuj.py --tydzien W03      # publikuj konkretny tydzień
    python publikuj.py --preview          # pokaż co zostanie opublikowane (dry run)
    python publikuj.py --force-date 2026-03-09  # symuluj publikację na inną datę
"""

import json
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

# Ścieżki
SCRIPT_DIR = Path(__file__).parent
REPO_ROBOCZE = SCRIPT_DIR.parent  # lecturesPythonII
REPO_STUDENCKIE = REPO_ROBOCZE.parent / "python2-materialy"
CONFIG_FILE = SCRIPT_DIR / "harmonogram_publikacji.json"

# Pliki wykluczone z publikacji (materiały prowadzącego)
WYKLUCZONE = {
    "plan_zajec.md",    # stenogram wykładu
    "plan_lab.md",      # instrukcja dla doktoranta
}

# Quizy publikowane z opóźnieniem 1 tydzień (spaced repetition)
QUIZ_DELAY_WEEKS = 1


def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)


def get_publication_date(args):
    """Zwraca datę publikacji (domyślnie dziś)."""
    for i, arg in enumerate(args):
        if arg == "--force-date" and i + 1 < len(args):
            return datetime.strptime(args[i + 1], "%Y-%m-%d").date()
    return date.today()


def get_weeks_to_publish(config, pub_date, target_week=None):
    """Zwraca listę tygodni do opublikowania."""
    weeks = []

    for week in config["dzienne"]["tygodnie"]:
        week_date = datetime.strptime(week["data"], "%Y-%m-%d").date()
        if target_week and week["nr"] != target_week:
            continue
        if week_date <= pub_date:
            weeks.append(week)

    for zjazd in config["zaoczne"]["zjazdy"]:
        zjazd_date = datetime.strptime(zjazd["data"], "%Y-%m-%d").date()
        if target_week and zjazd["nr"] != target_week:
            continue
        if zjazd_date <= pub_date:
            weeks.append(zjazd)

    return weeks


def should_publish_quiz(week_nr, all_weeks, pub_date):
    """Quiz z tygodnia N jest publikowany w tygodniu N+1."""
    # Znajdź datę następnego tygodnia
    prefix = week_nr[0]  # 'W' lub 'S'
    nr = int(week_nr[1:])
    next_nr = f"{prefix}{nr + 1:02d}"

    for w in all_weeks:
        if w["nr"] == next_nr:
            next_date = datetime.strptime(w["data"], "%Y-%m-%d").date()
            return pub_date >= next_date

    # Ostatni tydzień — publikuj po sesji
    return False


def copy_materials(src_dir, dst_dir, week_nr, all_weeks, pub_date, preview=False):
    """Kopiuje materiały z katalogu źródłowego do docelowego."""
    src = REPO_ROBOCZE / src_dir
    if not src.exists():
        print(f"  ⚠ Brak katalogu: {src}")
        return []

    copied = []

    for subdir in ["wyklad", "lab"]:
        src_sub = src / subdir
        if not src_sub.exists():
            continue

        dst_sub = dst_dir / subdir if subdir == "wyklad" else dst_dir / "lab"

        for file in sorted(src_sub.iterdir()):
            # Pomijaj wykluczone pliki
            if file.name in WYKLUCZONE:
                continue

            # Quizy — z opóźnieniem
            if file.name.startswith("quiz_"):
                if not should_publish_quiz(week_nr, all_weeks, pub_date):
                    continue

            if preview:
                print(f"  📄 {file.name} → {dst_sub.name}/")
                copied.append(file.name)
            else:
                dst_sub.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, dst_sub / file.name)
                copied.append(file.name)

    return copied


def copy_skrypt(pub_date, preview=False):
    """Kopiuje skrypt studenta."""
    src = REPO_ROBOCZE / "skryptdlastudentow" / "skrypt.md"
    if not src.exists():
        return

    dst = REPO_STUDENCKIE / "skrypt"
    if preview:
        print(f"  📘 skrypt.md → skrypt/")
    else:
        dst.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst / "skrypt.md")


def git_commit_and_push(message):
    """Commituje i pushuje zmiany w repo studenckim."""
    import os
    cwd = REPO_STUDENCKIE
    env = os.environ.copy()

    subprocess.run(["git", "add", "-A"], cwd=cwd, env=env)

    # Sprawdź czy są zmiany
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=cwd, env=env
    )
    if result.returncode == 0:
        print("Brak nowych zmian do opublikowania.")
        return False

    subprocess.run(
        ["git", "commit", "-m", message],
        cwd=cwd, env=env
    )
    subprocess.run(["git", "push"], cwd=cwd, env=env)
    return True


def main():
    args = sys.argv[1:]
    preview = "--preview" in args
    publish_all = "--all" in args

    target_week = None
    for i, arg in enumerate(args):
        if arg == "--tydzien" and i + 1 < len(args):
            target_week = args[i + 1]

    pub_date = get_publication_date(args)
    config = load_config()

    print(f"📅 Data publikacji: {pub_date}")
    if preview:
        print("👀 PODGLĄD (dry run)\n")

    # Sprawdź czy repo studenckie istnieje
    if not preview and not REPO_STUDENCKIE.exists():
        print(f"Klonuję repo studenckie do {REPO_STUDENCKIE}...")
        subprocess.run([
            "git", "clone",
            "https://github.com/sp6jaz/python2-materialy.git",
            str(REPO_STUDENCKIE)
        ])

    # Pobierz tygodnie do opublikowania
    all_weeks = config["dzienne"]["tygodnie"] + config["zaoczne"]["zjazdy"]
    weeks = get_weeks_to_publish(config, pub_date, target_week)

    if not weeks:
        print("Brak materiałów do opublikowania na tę datę.")
        return

    published_any = False

    for week in weeks:
        nr = week["nr"]
        src_dir = week["katalog"]

        # Nazwa katalogu w repo studenckim
        if nr.startswith("W"):
            dst_name = f"tydzien-{nr[1:]}"
            form = "dzienne"
        else:
            dst_name = f"zjazd-{nr[1:]}"
            form = "zaoczne"

        dst_dir = REPO_STUDENCKIE / form / dst_name

        print(f"\n{'='*50}")
        print(f"📚 {nr} ({week['data']}) → {form}/{dst_name}/")
        print(f"{'='*50}")

        copied = copy_materials(src_dir, dst_dir, nr, all_weeks, pub_date, preview)
        if copied:
            published_any = True

    # Kopiuj skrypt
    print(f"\n{'='*50}")
    print("📘 Skrypt studenta")
    print(f"{'='*50}")
    copy_skrypt(pub_date, preview)

    if not preview and published_any:
        message = f"Publikacja materiałów na {pub_date}"
        if target_week:
            message = f"Publikacja {target_week}"
        git_commit_and_push(message)
        print(f"\n✅ Opublikowano! https://github.com/sp6jaz/python2-materialy")


if __name__ == "__main__":
    main()
