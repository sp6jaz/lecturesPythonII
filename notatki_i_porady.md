# Notatki i porady agenta

Plik gromadzi analizy, rekomendacje i przemyślenia powstałe podczas pracy nad materiałami.

---

## 2026-02-22 — Analiza sylabusa

Sylabus jest dość ogólnikowy — 8 tematów na 15 tygodni (30h wykładu = 15×2h). To daje dużo swobody w rozłożeniu materiału. Spostrzeżenia:

1. **NumPy, Pandas, Matplotlib** — to rdzeń, ale każdy z tych tematów zasługuje na 2-3 wykłady, nie jeden
2. **"Zaawansowane biblioteki"** — to szeroka kategoria, można tu wcisnąć seaborn, scikit-learn, scipy, albo nawet polars/plotly
3. **Brak konkretnego rozkładu tydzień-po-tygodniu** — musimy go stworzyć
4. **Literatura jest przestarzała** — McKinney ma 3rd ed. (2022), VanderPlas 2nd ed. (2023). Warto bazować na nowszych wersjach
5. **Brak tematów o czyszczeniu danych** (missing values, merge, groupby) — a to kluczowa umiejętność w analizie danych, trzeba to wpleść w Pandas

---

## 2026-02-22 — Wykład 1: warsztat pracy analityka

Efekt uboczny ustalenia Git/GitHub od pierwszych zajęć: każdy student wyjdzie z kursu z publicznym repo na GitHubie — to gotowe portfolio dla pracodawcy.

---

## 2026-02-22 — Materiały laboratoryjne a doktorant

Laboratorium dzienne prowadzi doktorant — materiały L01-L15 muszą być na tyle jasne i kompletne, żeby doktorant mógł je poprowadzić bez dodatkowych wyjaśnień. Warto o tym pamiętać przy tworzeniu.

---

## 2026-02-22 — Dlaczego rezygnujemy z Anacondy

**Problemy z Anacondą:**
- Ciężka (~3-5 GB), instaluje setki paczek, z których studenci użyją może 10
- Licencja się zmieniła — Anaconda jest komercyjna dla organizacji powyżej 200 osób (od 2020)
- Conda vs pip — dwa menedżery pakietów, konflikty, chaos u studentów
- Studenci uczą się "conda world" zamiast prawdziwego ekosystemu Pythona
- Nie pasuje do workflow Git/GitHub — conda environments są ciężkie i lokalne

**Rekomendacja — uv + VS Code:**

| Narzędzie | Rola |
|-----------|------|
| **Python 3.12+** | z python.org lub apt |
| **uv** | ultraszybki menedżer pakietów i venv (Astral, 2025 standard) — zastępuje pip+venv+pyenv |
| **VS Code** | edytor + wbudowana obsługa Jupyter Notebooks + Git + terminal |
| **Jupyter Notebook** | przez VS Code (extension) lub klasycznie w przeglądarce |

**Dlaczego uv + VS Code:**
- `uv` tworzy venv i instaluje numpy+pandas+matplotlib w **sekundach** (10-100× szybciej niż pip)
- Studenci uczą się prawdziwego Pythona — `venv`, `pip install`, `requirements.txt`
- VS Code to standard branży, darmowy, lekki, ma Git wbudowany
- Jupyter działa w VS Code natywnie — nie trzeba odpalać osobnego serwera
- Workflow: `uv venv` → `uv pip install` → kod w `.py` lub `.ipynb` → git commit → push
- Jeden spójny ekosystem zamiast "otwórz Anaconda Navigator"

**Bonus dydaktyczny:** studenci wychodzą z kursu znając narzędzia, które faktycznie spotkają w pracy — żadna firma analityczna nie wymaga Anacondy, ale Python + venv + VS Code + Git to standard.

---

## 2026-02-22 — Format skryptu

Markdown to idealny wybór na skrypt:
- Renderuje się pięknie na GitHubie (studenci od razu widzą sformatowany tekst)
- Obsługuje Mermaid, bloki kodu z kolorowaniem składni, tabele, linki
- Łatwo konwertować do PDF/DOCX przez pandoc (komenda `md2docx` już zainstalowana)
- Na koniec semestru można wydać jako PDF do druku albo hostować na GitHub Pages

---

## 2026-02-22 — VS Code vs PyCharm

**Decyzja: VS Code jako oficjalne narzędzie, PyCharm dozwolony bez wsparcia.**

Dlaczego VS Code jako standard:
- Darmowy, lekki, działa na każdym sprzęcie (studenci mają różne komputery)
- Jupyter Notebook natywnie (extension), Git wbudowany, terminal wbudowany
- Jeden ekosystem: `uv` + `git` + `python` + Jupyter w jednym oknie
- Standard branży data science/analytics w 2025-2026

Dlaczego nie blokować PyCharma:
- Studenci znają go z Python I — niektórzy będą chcieli zostać
- PyCharm Community darmowy, obsługuje Jupyter i Git
- Blokowanie rodzi opór — lepiej "oficjalnie VS Code, PyCharm na własną rękę"

Kluczowa zasada: **nie robimy podwójnych instrukcji** — materiały, screenshoty, tutoriale wyłącznie pod VS Code. To chroni projekt przed rozrostem i utrzymuje spójny przekaz

---

## 2026-02-22 — Harmonogram: kluczowe decyzje projektowe

**Pandas dostaje największą wagę (27%)** — to #1 narzędzie analityka danych. NumPy, Matplotlib, statystyka po ~13%.

**Projekt przewodni "Analiza firmy X"** — jeden spójny dataset e-commerce (zamówienia, klienci, produkty, kampanie) przewija się przez cały semestr. Każdy tydzień dodaje nową warstwę analizy tych samych danych. Student buduje kompletną analizę portfolio-ready na GitHubie.

**Trzy dodatkowe mechanizmy zaangażowania:**
1. Mini-quizy na początku wykładu (spaced repetition, 5 min, nieoceniane)
2. "Wyzwanie tygodnia" — opcjonalne zadanie dla ambitnych
3. Peer review kodu na GitHub (2× w semestrze) — realizuje K1_K04 z sylabusa

**Zaoczne = skondensowane dzienne:** 10 spotkań mapuje się na 15 tygodni. Pandas i statystyka mają po 2 spotkania, reszta po 1. Najważniejsze: nie ciąć Pandas — raczej skrócić NumPy.

---

## 2026-02-22 — VM z Linuxem vs natywna instalacja

Rozważano pomysł maszyn wirtualnych z Ubuntu dla studentów. Odrzucony na rzecz natywnej instalacji:

- VM = ogromny próg wejścia, problemy ze słabymi laptopami (4GB RAM), VT-x w BIOS
- Podwójna złożoność (Python + Linux) — to nie kurs Linuxa
- Nasz stack (Python + uv + VS Code + Git) jest w 100% cross-platform — działa identycznie na Windows i Linux
- Alternatywa dla zaawansowanych: WSL2 (`wsl --install`) — lekki Linux na Windows bez VM

---

## 2026-02-22 — Jupyter Notebook: jak używać

Jupyter to must-have w data science, ale kluczowe jest jak:

- **Głównie przez VS Code** (Jupyter extension) — IntelliSense, Git, debugger, terminal w jednym oknie
- **Pokazać też klasyczny w przeglądarce** (1 zajęcia) — studenci spotkają go w pracy, Colabie, JupyterHub
- Studenci znają Colaba z Python I — Jupyter w przeglądarce będzie znajomy, VS Code da więcej
- Format: `.ipynb` do eksploracji i wykresów, `.py` do czystego kodu i modułów — oba w Git
- Ważne: nauczyć studentów kiedy notebook, a kiedy skrypt — to częsty problem początkujących

---

### Apki mobilne do ćwiczenia (analiza 2026-02-22)

**Decyzja:** NIE tworzymy własnej apki mobilnej — za duży nakład przy niepewnym zwrocie. Zamiast tego używamy istniejących narzędzi:

1. **Anki** (fiszki z spaced repetition) — przygotujemy decki z pojęciami i składnią od W03-W04
2. **Kahoot/Quizizz** — quizy na żywo na wykładzie (zamiennik papierowych quizów, element gamifikacji)
3. **GitHub Mobile** — studenci sprawdzają repo na telefonie (zero pracy z naszej strony)
4. **Jupyter Lite** — Python w przeglądarce mobilnej bez instalacji (do rozważenia później)

Kluczowa zasada: 80% efektu przy 5% nakładu. Własna apka to miesiące pracy, Anki deck to godzina.
