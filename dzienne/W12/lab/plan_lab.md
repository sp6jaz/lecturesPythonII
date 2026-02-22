# L12 — Plan laboratorium dla prowadzącego

## Temat: Statystyka — rozkłady i testy hipotez

**Programowanie w Pythonie II** | Laboratorium 12
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne przy komputerze
**Prowadzący:** doktorant (laboratoria prowadzone samodzielnie)

---

## Efekty uczenia się (Bloom poziom 3-4)

Po tych zajęciach osoba studiująca:
1. **Stosuje** `scipy.stats.norm` do obliczania prawdopodobieństw i kwantyli, interpretując wyniki w kontekście praktycznym (Bloom 3)
2. **Analizuje** dane pod kątem normalności używając QQ-plotu i testu Shapiro-Wilka, wyciągając wnioski o zasadności stosowania testów parametrycznych (Bloom 4)
3. **Stosuje** jednorodkowy, niezależny i sparowany t-test do porównywania grup, dobierając właściwą wersję do scenariusza (Bloom 3)
4. **Projektuje** i przeprowadza pełną analizę A/B testu — od eksploracji danych po sformułowanie rekomendacji biznesowej (Bloom 4)
5. **Interpretuje** wyniki testu chi-kwadrat i przedziałów ufności, formułując wnioski w języku zrozumiałym dla osoby bez wykształcenia statystycznego (Bloom 4)

---

## Plan minutowy

| Czas | Etap | Opis | Uwagi |
|------|------|------|-------|
| 0:00-0:05 | Organizacja | Sprawdzenie listy, weryfikacja środowiska, import scipy.stats | Otwierają VS Code + .venv |
| 0:05-0:10 | Wprowadzenie | Krótki kontekst: "mierzymy żeby decydować, nie żeby opisywać" | Bez live coding |
| 0:10-0:30 | Ćwiczenie 1 | Rozkład normalny i testy normalności (20 min) | Para lub samodzielnie |
| 0:30-0:50 | Ćwiczenie 2 | T-testy — porównywanie grup (20 min) | Samodzielnie |
| 0:50-1:20 | Ćwiczenie 3 | Pełna analiza A/B testu (30 min) — samodzielna praca | Samodzielnie |
| 1:20-1:35 | Ćwiczenie 4 | Chi-kwadrat, przedziały ufności, commit (15 min) | Samodzielnie |
| 1:35-1:45 | Podsumowanie | Omówienie wyników, zapowiedź L13 | Dyskusja |

---

## Organizacja sali

- Studenci pracują samodzielnie lub w parach (Ćwiczenie 1 polecane w parach)
- Tworzą własny notebook `.ipynb`
- Notebook nazywają: `lab12_hypothesis_testing.ipynb`
- Commit na koniec zajęć (Ćwiczenie 4)

### Środowisko
```bash
# Aktywacja środowiska
cd ~/python2_projekt
source .venv/bin/activate   # Linux/Mac
# lub
.venv\Scripts\activate      # Windows

# Weryfikacja
python -c "import scipy; print(scipy.__version__)"
python -c "from scipy import stats; print('scipy.stats OK')"

# Otwarcie VS Code
code .
```

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przed zajęciami (10 min wcześniej)
- [ ] Sprawdź scipy: `python -c "import scipy; print(scipy.__version__)"`
- [ ] Weryfikacja kluczowych importów: `from scipy import stats; stats.ttest_ind([1,2],[3,4])`
- [ ] Miej gotowy notebook z przykładowymi rozwiązaniami (do podglądu gdy student utknął)
- [ ] Upewnij się że numpy i matplotlib są dostępne (są wymagane w ćwiczeniach)

### Podczas zajęć
- Pierwsze 5 min: sprawdź czy wszyscy mają `scipy.stats` dostępny
- Ćwiczenie 3 (A/B test) — najtrudniejsze, 30 minut może nie wystarczyć wolniejszym studentom
- Kluczowe naprowadzenie: "Czy Twoje grupy są niezależne czy powiązane? → dobierasz test"
- Nie dawaj gotowego kodu — naprowadzaj pytaniami:
  - "Jakiego testu użyjesz — `ttest_1samp`, `ttest_ind` czy `ttest_rel`? Dlaczego?"
  - "Co mówi p < 0.05 w tym scenariuszu biznesowym?"
  - "Jak przeliczysz wynik testu na decyzję managera?"
- Przy Ćwiczeniu 4: commit musi zawierać plik `.ipynb`

### Tempo grup
- Szybcy studenci: Ćwiczenie 3 rozszerzenie (sekcja "Rozszerzenie") + własne dane
- Wolni studenci: Ćwiczenia 1 + 2 + commit podstawowy wystarczają — 3 i 4 bonusowe

### Typowe błędy koncepcyjne (poprawiaj natychmiast)
- Mylenie `ttest_ind` z `ttest_rel` — zapytaj "czy to te same osoby czy różne grupy?"
- Interpretacja p-wartości jako "prawdopodobieństwo że H₀ jest prawdą" — błąd! Popraw
- Używanie `equal_var=True` — zawsze `equal_var=False` (Welch) jeśli nie wiadomo nic o wariancjach
- Brak sprawdzenia normalności przed t-testem — przypomnij Shapiro + QQ-plot

---

## Tabela rozwiązywania problemów (Troubleshooting)

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `ModuleNotFoundError: No module named 'scipy'` | scipy nie jest zainstalowany w aktywnym venv | `pip install scipy` w aktywowanym środowisku |
| `from scipy import stats` — ImportError | Uszkodzona instalacja scipy | `pip uninstall scipy && pip install scipy` |
| `stats.shapiro()` — RuntimeWarning: p-value can be inaccurate for n > 5000 | Shapiro najlepszy dla n < 5000 | Użyj podpróby: `stats.shapiro(data[:200])` lub `stats.normaltest()` (D'Agostino-Pearson) |
| `stats.ttest_ind` zwraca p=NaN | Wszystkie wartości w grupie identyczne (zerowa wariancja) | Sprawdź dane: `print(np.unique(data))`, dane muszą mieć zmienność |
| Shapiro-Wilk zawsze odrzuca normalność na dużych próbach | Test bardzo czuły przy n > 1000 | Normalne zachowanie — patrz QQ-plot wizualnie, nie wyłącznie na p-wartość |
| `stats.probplot()` nie rysuje na ax | Przekazywanie parametru `plot=ax` jest wymagane | Użyj: `stats.probplot(data, dist='norm', plot=ax)` (nie `plot=plt`) |
| `chi2_contingency` — `ValueError: The internally computed table of expected frequencies has a zero element` | Tabela kontyngencji ma komórkę z wartością 0 | Połącz rzadkie kategorie lub zwiększ próbę |
| `stats.t.interval()` zwraca błąd | Błędny typ argumentu `confidence` (w starszych scipy był `alpha`) | Użyj: `stats.t.interval(0.95, df=n-1, loc=mean, scale=se)` — pierwszy argument to poziom ufności |
| `ttest_rel` — `ValueError: unequal length arrays` | Sparowany t-test wymaga równej liczby obserwacji w obu grupach | Sprawdź `len(before) == len(after)`, usuń brakujące pary |
| QQ-plot zakrzywiony ale Shapiro mówi p > 0.05 | Mała próba (n < 30) — Shapiro ma małą moc | Zaufaj QQ-plotowi — przy małych próbach wizualizacja ważniejsza |
| `stats.sem()` zwraca inne SE niż oczekiwane | `stats.sem()` domyślnie ddof=1 (korygowany błąd próby) | Normalne zachowanie — to prawidłowe SE dla przedziału ufności |
| Wartości z `ttest_ind` różnią się zależnie od `equal_var` | Welch (False) i Student (True) to różne testy | Prawie zawsze używaj `equal_var=False` — nie zakłada równości wariancji |
| `DeprecationWarning: scipy.stats.norm.interval alpha parameter` | Zmiana API w scipy 1.9+ | W scipy >= 1.9: `stats.norm.interval(confidence=0.95, ...)` lub pozycyjny `stats.norm.interval(0.95, ...)` |
| `np.random.normal` generuje wartości poniżej 0 dla danych > 0 | Brak clip/abs | Użyj `.clip(min=0)` lub `np.abs()` zależnie od kontekstu |
| Dashboard wykresów statystycznych nie mieści się | `figsize` zbyt małe | Dla 2x2 paneli minimum `figsize=(12, 8)`, dla 2x3 minimum `(14, 9)` |

---

## Weryfikacja wyników — klucz odpowiedzi

### Ćwiczenie 1 (Rozkład normalny i normalność)
- `stats.norm.cdf(185, loc=170, scale=8)` ≈ 0.9699 → P(wzrost > 185) ≈ 3.0%
- `stats.norm.ppf(0.90, loc=170, scale=8)` ≈ 180.3 cm
- Shapiro na danych normalnych (`seed=42`, n=100): p > 0.05 (normalny)
- Shapiro na danych exponential: p bardzo małe < 0.001 (nie-normalny)
- QQ-plot danych normalnych: punkty blisko linii prostej

### Ćwiczenie 2 (T-testy)
- Jednorodkowy (`seed=42`, n=50, mu=5.4, test vs 5.0): t > 0, p < 0.05 → istotna różnica
- Niezależny (`seed=42`, A~N(250,60), B~N(270,65), n=80 każda): p < 0.05 → istotna różnica; uwaga: z innym seed wynik może się różnić
- Sparowany (`seed=42`, efekt +15%): p bardzo małe → szkolenie istotnie zwiększa sprzedaż

### Ćwiczenie 3 (A/B test)
- Dane `seed=42`: czas_A~N(45,15), czas_B~N(52,18), n=120
- Welch's t-test: p < 0.05 → reklama wideo statystycznie istotnie zwiększa czas na stronie
- 95% CI dla różnicy: powinien być całkowicie powyżej 0
- Wniosek biznesowy: rekomendacja wdrożenia wideo, +X sekund/sesję

### Ćwiczenie 4 (Chi-kwadrat i CI)
- Chi-kwadrat: tabela 3x3 preferencji → p < 0.05 → preferencje zależą od wieku
- CI NPS 95%: `stats.t.interval(0.95, df=n-1, loc=mean, scale=se)` → zakres ~[6.8, 7.6]
- `git log` — widoczny commit z plikiem `lab12_hypothesis_testing.ipynb`

---

## Zapowiedź L13

> "Na kolejnych zajęciach: scikit-learn i Plotly. Pierwsze modele uczenia maszynowego — regresja liniowa do predykcji, interaktywne wykresy Plotly zamiast statycznych Matplotlib. Statystyka z dzisiaj przyda się do oceny jakości modeli (R², p-wartości dla współczynników regresji). Kto chce się przygotować — zajrzyjcie na stronę scikit-learn.org, sekcja 'Getting started'."
