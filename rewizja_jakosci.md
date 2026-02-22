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

## Rewizja 2 — Intuicyjność i profesjonalizm (commit `b2b95e8`)

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

## Rewizja 3 — Wzbogacenie z analizy starych materiałów

### Zakres
Analiza starych materiałów z `python2OLD.zip` (606 notebooków, foldery 1-11 + NS, lato 2025). Identyfikacja wartościowych treści brakujących w nowej edycji. Weryfikacja kodu i dodanie do skryptu studenta + materiałów zaocznych.

### Audyt starych materiałów

| Kategoria | Status | Szczegóły |
|-----------|--------|-----------|
| Deprecated pandas (inplace=True) | ~15 plików OLD | Nie kopiujemy — nowy kod jest czysty |
| OneHotEncoder(sparse=False) | 2 pliki OLD | Usunięty w sklearn 1.4+ |
| Mutable default `context=[]` | 4 pliki OLD | Klasyczny Python bug |
| Deprecated freq='H' | 3 pliki OLD | Od pandas 2.2 → 'h' |
| Conda metadane | 50+ plików OLD | Nie kopiujemy |
| pip install | 30+ plików OLD | Nowy kod używa uv |
| numpy 2.0 deprecated | BRAK | Czysto |
| Broken imports | BRAK | Czysto |

### Decyzja o dodaniu treści

| Temat | Decyzja | Uzasadnienie |
|-------|---------|-------------|
| Szeregi czasowe (ARIMA, dekompozycja) | DODANO do skryptu (6.9) | Fundament analityki biznesowej — prognozowanie |
| Formaty plików (Parquet, Excel, JSON) | DODANO do skryptu (4.4) | W firmach dane NIE są w CSV |
| Web scraping (requests + BS4) | DODANO do skryptu (4.23) | Pozyskiwanie danych = pierwszy krok pipeline |
| Seaborn regplot + FacetGrid | DODANO do skryptu (5.9) | Analiza zależności, siatki kategorii |
| Polars lazy API | DODANO do skryptu (7.6) | Kluczowa przewaga Polars nad Pandas |
| TensorFlow/CNN/LSTM | ODRZUCONO | Za duży temat, osobny kurs |
| Matplotlib animacje | ODRZUCONO | Gadżet, nie narzędzie analityka |
| Lokalne LLM (Ollama) | ODRZUCONO | Wymaga GPU, studenci na słabych laptopach |
| Selenium web scraping | ODRZUCONO | Za ciężkie, requests+BS4 wystarczy |

### Zmiany wprowadzone

#### A. Skrypt studenta (skryptdlastudentow/skrypt.md)
- **4.4** — "Inne formaty plików": read_excel, read_json, read_parquet, multi-sheet Excel, tabela porównawcza
- **4.23** — "Pobieranie danych z internetu": requests, BeautifulSoup, pd.read_html(StringIO()), uwaga etyczna
- **5.9** — "Wykresy regresji i siatki": regplot, lmplot, FacetGrid, jointplot (renumeracja 5.10→5.11)
- **6.9** — "Analiza szeregów czasowych": rolling, resample, pct_change, shift, dekompozycja, ARIMA, auto_arima
- **7.6** — rozszerzenie Polars: lazy evaluation, scan_csv, explain(), collect(), Parquet

#### B. Materiały zaoczne (cwiczenia.md)
- **S03** — linki: IO Tools, requests, BeautifulSoup + wzmianka o formatach plików
- **S04** — linki: IO Tools, requests + wzmianka o web scrapingu i formatach
- **S05** — linki: regplot, FacetGrid, jointplot + wzmianka o regresji na wykresach
- **S06** — linki: statsmodels TSA, seasonal_decompose, Pandas Time Series + wzmianka o szeregach czasowych
- **S08** — linki: Polars User Guide, Lazy API + wzmianka o lazy evaluation

### Weryfikacja kodu
Cały dodany kod zweryfikowany lokalnie (Python 3.10, pandas 2.3.3, statsmodels 0.14.6, polars, pmdarima):
- Formaty plików: CSV, Excel, JSON, Parquet — odczyt i zapis OK
- Web scraping: requests + BS4 + pd.read_html(StringIO()) — bez FutureWarning
- Seaborn: regplot, lmplot, FacetGrid, jointplot — wykresy generują się poprawnie
- Szeregi czasowe: rolling, resample, dekompozycja, ARIMA(1,1,1), auto_arima — bez warningów
- Polars: eager, lazy (scan_csv), explain(), collect(), write_parquet — OK

---

## Notatki do przyszłych rewizji

### Do rozważenia
1. **Fill-in-the-blanks W02-W07** — wcześniejsze ćwiczenia mają za dużo gotowego kodu, powinny mieć `???` i `___`
2. **Quizy zaoczne S02-S10** — brak quizów spaced repetition z poprzednich spotkań
3. **Gamifikacja** — elementy punktowe, wyzwania — niska priorytetowość
4. ~~**Skrypt studenta** — brak linków do dokumentacji w rozdziałach~~ ✅ ZROBIONE (Rewizja 2)

### Zasady kontroli jakości (ustalone)
- Każdy `pip install` → `uv pip install`
- Każde `groupby()` → `groupby(..., observed=True)` dla danych kategorycznych
- Brak deprecated API: `df.append()`, `np.bool`, `np.int`, `np.float`
- Seed losowości (`np.random.seed(42)`) na początku każdego bloku generującego dane
- Sekcja "Sprawdzenie ✅" po każdym ćwiczeniu
- Linki do dokumentacji na początku każdego pliku ćwiczeń
- Przed dodaniem nowych treści: oceń sensowność, sprawdź spójność z cyklem, zapytaj użytkownika
