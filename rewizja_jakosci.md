# Rewizja jakości materiałów — log analiz

**Projekt:** lecturesPythonII — Programowanie w Pythonie II
**Data:** 2026-02-22
**Ostatni commit przed rewizją:** `7839fca`

---

## Rewizja 1 — Poprawki techniczne (commit `7839fca`)

### Zakres
Pełny audyt 6-wymiarowy: Bloom, struktura 4-częściowa, narzędzia, metody dydaktyczne, kod, kompletność.

### Znalezione i naprawione problemy

| # | Problem | Pliki | Poprawka |
|---|---------|-------|----------|
| 1 | `pip install` zamiast `uv pip install` (18 wystąpień) | W10, W11, W12, W13 plan_lab.md; W13 plan_zajec.md; S08 plan_zajec.md | Zamieniono na `uv pip install` |
| 2 | Deprecated `df.append()` w quizie W08 | W08/wyklad/quiz_w08.md:56 | Zamieniono na `df1.join(df2, how='outer')` |
| 3 | Brak sekcji "Pair programming" w 9 plikach lab | W06, W08-W15 plan_lab.md | Dodano sekcję pilot/navigator |
| 4 | Pliki .html i .~lock w staging | .gitignore | Dodano `*.html` i `.~lock*` |

### Wyniki audytu

| Wymiar | Wynik | Uwagi |
|--------|-------|-------|
| Taksonomia Blooma | 100% PASS | Wszystkie efekty z czasownikami Blooma |
| Struktura 4-częściowa | 28/28 PASS (A+) | Wprowadzenie → Materiał → Aktywność → Podsumowanie |
| Narzędzia (uv, VS Code) | PASS | Po poprawkach pip→uv pip |
| Metody dydaktyczne | PASS z uwagami | Brak fill-in-the-blanks W02-W07, quizów zaocznych |
| Kod Python | PASS | Po poprawce quiz W08 |
| Kompletność materiałów | 15/15 dzienne, 10/10 zaoczne | Skrypt 8 rozdziałów kompletny |

### Zidentyfikowane luki (do poprawy w Rewizji 2)
- Brak linków do oficjalnej dokumentacji w ćwiczeniach
- Brak sekcji "Jeśli utkniesz" w materiałach laboratoryjnych
- Brak opisów datasetów (tips, penguins) w ćwiczeniach
- Brak sekcji "Sprawdzenie" w W13 ćwiczenia (ćw. 1-3)
- Niedostateczny scaffolding w niektórych ćwiczeniach

---

## Rewizja 2 — Intuicyjność i profesjonalizm (w toku)

### Zakres
Kompleksowe wzbogacenie materiałów o: linki do dokumentacji, opisy kluczowych pojęć, sekcje "Jeśli utkniesz", opisy datasetów, brakujące sekcje "Sprawdzenie".

### Audyt kodu Python (commit `7839fca`)

| Kategoria | Status | Szczegóły |
|-----------|--------|-----------|
| Deprecacje pandas 2.x | ✅ BRAK problemów | Brak `df.append()`, prawidłowe `pd.concat()` |
| Deprecacje numpy 2.x | ✅ BRAK problemów | Brak `np.bool`, `np.int`, `np.float` |
| Deprecacje scipy 1.14+ | ✅ OK | `stats.t.interval(0.95, ...)` — parametr pozycyjny |
| Deprecacje matplotlib 3.10+ | ✅ BRAK problemów | `cmap='string'` prawidłowe |
| `np.random.seed()` | ✅ Konsekwentne | 70+ użyć z `seed(42)` |
| `groupby(observed=True)` | ✅ Konsekwentne | 20+ prawidłowych użyć |
| `uv pip` (nie `pip`) | ✅ Konsekwentne | 50+ prawidłowych wzmianek |
| VS Code (nie PyCharm/Anaconda) | ✅ Konsekwentne | Zgodne z wytycznymi |

### Zmiany wprowadzane w Rewizji 2

#### A. Ćwiczenia dzienne (cwiczenia.md) — W01 do W15
- Dodanie sekcji "Przydatne materiały" z linkami do oficjalnej dokumentacji
- Dodanie sekcji "Kluczowe pojęcia" z definicjami
- Dodanie sekcji "Jeśli utkniesz" z tabelą typowych problemów i rozwiązań
- Dodanie opisów datasetów (tips, penguins) z opisem kolumn
- Dodanie brakujących sekcji "Sprawdzenie" w W13 (ćw. 1-3)

#### B. Instrukcje prowadzącego (plan_lab.md) — W01 do W15
- Dodanie sekcji "Przydatne linki dla prowadzącego" z dokumentacją

#### C. Materiały zaoczne (cwiczenia.md) — S01 do S10
- Dodanie sekcji "Przydatne materiały" z linkami do dokumentacji

### Statystyki zmian
- Plików edytowanych: ~40
- Linków do dokumentacji dodanych: ~200
- Sekcji "Jeśli utkniesz" dodanych: ~15
- Opisów kluczowych pojęć dodanych: ~15
- Opisów datasetów dodanych: ~5
- Sekcji "Sprawdzenie" dodanych: 3 (W13 ćw. 1-3)

---

## Notatki do przyszłych rewizji

### Do rozważenia
1. **Fill-in-the-blanks W02-W07** — wcześniejsze ćwiczenia mają za dużo gotowego kodu, powinny mieć `???` i `___`
2. **Quizy zaoczne S02-S10** — brak quizów spaced repetition z poprzednich spotkań
3. **Gamifikacja** — elementy punktowe, wyzwania — niska priorytetowość
4. **Skrypt studenta** — brak linków do dokumentacji w rozdziałach

### Zasady kontroli jakości (ustalone)
- Każdy `pip install` → `uv pip install`
- Każde `groupby()` → `groupby(..., observed=True)` dla danych kategorycznych
- Brak deprecated API: `df.append()`, `np.bool`, `np.int`, `np.float`
- Seed losowości (`np.random.seed(42)`) na początku każdego bloku generującego dane
- Sekcja "Sprawdzenie ✅" po każdym ćwiczeniu
- Linki do dokumentacji na początku każdego pliku ćwiczeń
