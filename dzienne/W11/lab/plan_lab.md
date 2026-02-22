# L11 — Plan laboratorium dla prowadzącego

## Temat: Statystyka opisowa w Pythonie

**Programowanie w Pythonie II** | Laboratorium 11
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne przy komputerze
**Prowadzący:** doktorant (laboratoria prowadzone samodzielnie)

---

## Efekty uczenia się (Bloom poziom 2-3)

Po tych zajęciach osoba studiująca:
1. **Oblicza** miary tendencji centralnej (średnia, mediana, dominanta) i rozproszenia (std, IQR, rozstęp) na danych biznesowych oraz interpretuje różnice między nimi (Bloom 2)
2. **Analizuje** korelację między zmiennymi numerycznymi używając `stats.pearsonr()` i `stats.spearmanr()`, interpretuje siłę, kierunek i istotność statystyczną (Bloom 3)
3. **Stosuje** `scipy.stats.describe()` do opisu rozkładu — skośność, kurtoza, percentyle (Bloom 3)
4. **Wykrywa** wartości odstające metodą IQR i z-score oraz ocenia ich wpływ na miary statystyczne (Bloom 3)
5. **Interpretuje** wyniki analizy statystycznej w kontekście biznesowym (HR, wynagrodzenia) i formułuje wnioski (Bloom 3)

---

## Przydatne linki dla prowadzącego

- [SciPy — Stats module](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [SciPy — Descriptive statistics](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.describe.html)
- [Pandas — Correlation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)

## Plan minutowy

| Czas | Etap | Opis | Uwagi |
|------|------|------|-------|
| 0:00-0:05 | Organizacja | Sprawdzenie listy, weryfikacja środowiska | Otwierają VS Code + .venv |
| 0:05-0:10 | Wprowadzenie | Kontekst: "Mamy dane — teraz pytamy co ZNACZĄ" | Bez live coding |
| 0:10-0:30 | Ćwiczenie 1 | Statystyki opisowe na danych biznesowych (20 min) | Para lub samodzielnie |
| 0:30-0:50 | Ćwiczenie 2 | Analiza korelacji (20 min) | Samodzielnie |
| 0:50-1:20 | Ćwiczenie 3 | Pełna analiza statystyczna datasetu HR (30 min) | Samodzielnie |
| 1:20-1:35 | Ćwiczenie 4 | Wykrywanie outlierów + commit (15 min) | Samodzielnie |
| 1:35-1:45 | Podsumowanie | Omówienie wyników, zapowiedź L12 | Dyskusja |

---

## Organizacja sali

- Studenci pracują w parach lub samodzielnie — do wyboru (Ćwiczenie 1 polecane w parach)
- Tworzą własny notebook `.ipynb`
- Notebook nazywają: `lab11_statystyka.ipynb`
- Commit na koniec zajęć (Ćwiczenie 4)

### Środowisko
```bash
# Aktywacja środowiska
cd ~/python2_projekt
source .venv/bin/activate   # Linux/Mac
# lub
.venv\Scripts\activate      # Windows

# Weryfikacja
python -c "from scipy import stats; print('scipy OK')"
python -c "import numpy; print(numpy.__version__)"

# Otwarcie VS Code
code .
```

### Dataset (generowany w notebooku — nie wymaga internetu)
```python
import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(42)
n = 200
dzialy = np.random.choice(['IT', 'Sprzedaż', 'HR', 'Marketing', 'Finanse'], n,
                           p=[0.30, 0.25, 0.15, 0.20, 0.10])
staz = np.random.gamma(shape=3, scale=2, size=n).clip(0.5, 20).round(1)
baza = {'IT': 9000, 'Sprzedaż': 7000, 'HR': 6500, 'Marketing': 7500, 'Finanse': 8500}
wynagrodzenie = np.array([
    baza[d] + staz[i] * 300 + np.random.normal(0, 1200)
    for i, d in enumerate(dzialy)
]).clip(4000, 25000).round(-2)
wynagrodzenie[np.random.choice(n, 5, replace=False)] = np.random.choice(
    [2000, 2500, 35000, 40000, 38000], 5, replace=False
)
df = pd.DataFrame({
    'dział': dzialy,
    'staż_lat': staz,
    'wynagrodzenie': wynagrodzenie,
    'wiek': (25 + staz + np.random.normal(0, 3, n)).clip(22, 65).round().astype(int),
    'ocena_roczna': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.10, 0.40, 0.35, 0.10])
})
```

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przed zajęciami (10 min wcześniej)
- [ ] Sprawdź, czy scipy jest zainstalowane: `python -c "from scipy import stats; print('OK')"`
- [ ] Zweryfikuj import numpy i pandas
- [ ] Miej gotowe rozwiązania Ćwiczenia 3 (najtrudniejsze — do podglądu gdy student utknął)
- [ ] Upewnij się, że scipy zainstalowane w środowisku studentów: `uv pip install scipy` jeśli brak

### Podczas zajęć
- Pierwsze 5 min: sprawdź czy wszyscy mogą `from scipy import stats` bez błędu
- Ćwiczenie 3 (pełna analiza HR) — najtrudniejsze, 30 minut może nie wystarczyć dla wolniejszych
- Nie dawaj gotowego kodu — naprowadzaj: "Jakiej funkcji scipy użyjesz? Co zwraca `stats.pearsonr()`? Jak interpretujesz skośność?"
- Przy Ćwiczeniu 4: commit musi zawierać plik `.ipynb` — sprawdź na ekranie studenta

### Tempo grup
- Szybcy studenci: Ćwiczenie 3 rozszerzone — analiza per dział, wizualizacja boxplotów, pairplot
- Wolni studenci: Ćwiczenia 1 + 2 + commit podstawowy wystarczają — 3 i 4 bonusowe

### Pair programming
- Studenci mogą pracować w parach: **pilot** (pisze kod) + **navigator** (czyta instrukcję, podpowiada, sprawdza)
- Co 15-20 minut zamiana ról
- Pair programming zmniejsza frustrację i przyspiesza naukę — zachęcaj, ale nie wymuszaj

---

## Tabela rozwiązywania problemów (Troubleshooting)

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `ModuleNotFoundError: No module named 'scipy'` | scipy nie zainstalowane w aktywnym venv | `uv pip install scipy` w aktywowanym środowisku |
| `from scipy import stats` — ImportError | Uszkodzona instalacja scipy | `uv pip install --upgrade scipy` |
| `stats.pearsonr()` zwraca obiekt zamiast tuple | scipy >= 1.9 zwraca `PearsonRResult` | Użyj `result.statistic` i `result.pvalue` lub rozpakuj: `r, p = stats.pearsonr(x, y)` |
| `stats.spearmanr()` zwraca `SpearmanrResult` | Nowe API scipy >= 1.9 | `result = stats.spearmanr(x, y); rho = result.statistic; p = result.pvalue` |
| `df.groupby('dział')['wynagrodzenie'].agg(...)` — FutureWarning | Kategoryczne kolumny z `observed=False` | Dodaj `observed=True`: `df.groupby('dział', observed=True)` |
| Histogram nie wyświetla się w VS Code | Brak `%matplotlib inline` lub zły backend | Dodaj `%matplotlib inline` jako pierwszą komórkę notebooka |
| `np.percentile()` vs `df.quantile()` — różne wyniki | Różne metody interpolacji | Obie są poprawne — różnica wynika z metody interpolacji. Dla ćwiczeń używaj jednej spójnie. |
| `stats.zscore()` — TypeError: can't convert str | Kolumna zawiera typ tekstowy (str) | Oblicz z-score tylko na kolumnach numerycznych: `stats.zscore(df['wynagrodzenie'])` |
| Outliery metodą IQR — inne wyniki niż w sprawdzeniu | Inny seed lub kolejność operacji | Upewnij się, że `np.random.seed(42)` jest na początku przed generowaniem danych |
| `df.mode()[0]` — IndexError lub błędna wartość | `mode()` zwraca DataFrame — indeks [0] to pierwsza kolumna | Dla jednej kolumny: `df['wynagrodzenie'].mode()[0]` — `[0]` to pierwsza dominanta |
| Boxplot: `plt.suptitle('')` nie usuwa tytułu | `df.boxplot()` dodaje automatyczny tytuł w starszym matplotlib | Użyj `sns.boxplot()` zamiast `df.boxplot()`, albo: `fig.suptitle('', y=0)` |
| `stats.describe()` — `kurtosis` różni się od `df.kurt()` | scipy liczy kurtozę nadmiarową (Fisher), pandas identycznie | Są spójne. Rozkład normalny → kurtosis ≈ 0 (nadmiarowa). |
| Wykres scatter — punkty nachodzą na siebie | Wiele punktów z podobnymi wartościami | Dodaj `alpha=0.5` i `jitter`: `df['ocena_roczna'] + np.random.uniform(-0.2, 0.2, len(df))` |
| `np.polyfit` — `RankWarning: Polyfit may be poorly conditioned` | Zła skala danych | Znormalizuj dane przed polyfit lub ignoruj ostrzeżenie przy wizualizacji |
| Git commit nie działa — brak konfiguracji | git user.name lub user.email nie ustawione | `git config user.name "Imię Nazwisko"` i `git config user.email "email@example.com"` |
| `stats.pearsonr` — p-value bardzo małe (e-10, e-20) | Silna korelacja w małym datasecie | Normalny wynik. Wyświetl: `f"p = {p:.2e}"` (notacja naukowa) |

---

## Weryfikacja wyników — klucz odpowiedzi

### Ćwiczenie 1 (Statystyki opisowe)
- Średnia wynagrodzenie: ~9 200–9 500 PLN (z outlierami zawyżającymi)
- Mediana wynagrodzenie: ~8 500–9 000 PLN
- Mediana < Średnia → rozkład prawostronnie skośny (outlierzy wysokich pensji)
- Std wynagrodzenie: ~5 000–6 000 PLN (wysoka przez outlierów)
- IQR wynagrodzenie: ~3 500–4 500 PLN (stabilny)
- IT: najwyższa mediana spośród działów

### Ćwiczenie 2 (Korelacja)
- Pearson staż–wynagrodzenie: r ≈ 0.55–0.65 (umiarkowana pozytywna), p < 0.001
- Spearman staż–wynagrodzenie: rho ≈ 0.55–0.65 (podobna do Pearsona)
- Pearson marketing_spend–revenue (dane syntetyczne): r ≈ 0.85–0.90 (silna)
- Macierz korelacji: staż i wiek mocno skorelowane (oba mierzą "upływ czasu")

### Ćwiczenie 3 (Pełna analiza HR)
- `stats.describe()` skośność wynagrodzenia: > 1.0 (silnie prawoskośny przez outlierów)
- P90 wynagrodzenie: ~14 000–16 000 PLN
- P99 wynagrodzenie: powyżej 35 000 PLN (outlierzy)
- Dział IT: najwyższa mediana i najwyższe STD

### Ćwiczenie 4 (Outliery + commit)
- IQR outlierów w wynagrodzeniu: 5 obserwacji (te, które wstawiliśmy)
- z-score outlierów (|z| > 3): 3–5 obserwacji (może się nieznacznie różnić)
- Różnica mediany z/bez outlierów: < 500 PLN (mediana stabilna)
- Różnica średniej z/bez outlierów: > 2 000 PLN (średnia niestabilna)
- `git log` — widoczny commit z plikiem `lab11_statystyka.ipynb`

---

## Zapowiedź L12

> "Na kolejnych zajęciach: testy hipotez z scipy. Będziemy odpowiadać na pytanie 'Czy IT zarabia statystycznie istotnie więcej niż HR?' — nie tylko 'więcej w tych danych', ale 'więcej w całej populacji'. t-test, Mann-Whitney, chi-kwadrat. Będziemy też robić symulację testu A/B. Ten sam dataset HR — będziecie znali go już na pamięć, więc skupimy się na interpretacji wyników testów."
