# Quiz W12 — Statystyka: rozkłady i testy hipotez

**Temat:** Powtórka W11 (statystyka opisowa, histogramy) + nowy materiał W12 (testy hipotez, rozkład normalny)
**Czas:** 5 minut | **Forma:** kartka lub Mentimeter

---

## Pytania (do wyświetlenia na projektorze — po jednym)

---

### Pytanie 1 (powtórka W11 — statystyka opisowa)

Masz kolumnę `DataFrame` z zarobkami pracowników. Większość zarabia 5 000–7 000 PLN, ale kilku menedżerów zarabia powyżej 30 000 PLN. Która miara jest **najbardziej odpowiednia** do opisu typowego zarobku w tej firmie?

**A)** Średnia arytmetyczna (`df['zarobki'].mean()`)

**B)** Mediana (`df['zarobki'].median()`)

**C)** Odchylenie standardowe (`df['zarobki'].std()`)

**D)** Maksimum (`df['zarobki'].max()`)

**Odpowiedź: B** — Mediana jest odporna na wartości odstające (outliers). Kilku menedżerów z wysokimi zarobkami silnie zawyża średnią, przez co nie odzwierciedla ona typowego pracownika. Mediana dzieli próbę na pół i jest standardową miarą dla asymetrycznych rozkładów (zarobki, ceny nieruchomości, czas trwania).

---

### Pytanie 2 (powtórka W11 — histogramy i rozkłady)

Co oznacza **prawostronna asymetria** (positive skew) na histogramie?

**A)** Histogram jest symetryczny — lewy i prawy ogon są równe

**B)** Większość obserwacji leży po prawej stronie, ogon ciągnie się w lewo

**C)** Większość obserwacji skupia się po lewej stronie, długi ogon ciągnie się w prawo — średnia > mediana

**D)** Rozkład ma dwa szczyty (bimodalny)

**Odpowiedź: C** — Prawostronny skos (skewness > 0) oznacza, że dane skupiają się blisko małych wartości, ale zdarzają się rzadkie, bardzo duże wartości, które "ciągną" ogon w prawo. Klasyczny przykład: zarobki, ceny nieruchomości, czasy awarii. Konsekwencja: średnia > mediana, bo wysokie outliery zawyżają średnią.

---

### Pytanie 3 (nowy — p-wartość i hipotezy)

Przeprowadzasz A/B test nowej funkcji w aplikacji. Wynik: **p-wartość = 0.03**. Co to oznacza?

**A)** Jest 3% szansy, że nowa funkcja NAPRAWDĘ działa lepiej

**B)** Jest 97% szansy, że hipoteza zerowa jest prawdą

**C)** Gdyby nie było różnicy między wersjami (H₀ prawdziwa), szansa uzyskania takich wyników jak zaobserwowane wynosi tylko 3% — odrzucamy H₀ przy α=0.05

**D)** Różnica między wersjami wynosi 3%

**Odpowiedź: C** — P-wartość to prawdopodobieństwo uzyskania takich (lub bardziej ekstremalnych) wyników przy założeniu, że H₀ jest prawdą. Nie jest to prawdopodobieństwo prawdziwości H₀ ani H₁. P = 0.03 < α = 0.05, więc odrzucamy H₀ — różnica jest statystycznie istotna. To NIE znaczy, że różnica jest ważna biznesowo — 0.03% wzrost konwersji może być istotny statystycznie, ale bezwartościowy praktycznie.

---

### Pytanie 4 (nowy — wybór rodzaju t-testu)

Firma mierzy satysfakcję 40 pracowników **przed** i **po** programie szkoleń. Który test zastosować?

**A)**
```python
stats.ttest_1samp(satysfakcja_po, popmean=7.0)
```

**B)**
```python
stats.ttest_ind(satysfakcja_przed, satysfakcja_po, equal_var=False)
```

**C)**
```python
stats.ttest_rel(satysfakcja_przed, satysfakcja_po)
```

**D)**
```python
stats.chi2_contingency(tabela)
```

**Odpowiedź: C** — Te same 40 osób zmierzono dwukrotnie — to dane **powiązane** (paired). Używamy `ttest_rel()` (rel = related). Test niezależny (`ttest_ind`) byłby błędem — traktowałby obie grupy jakby nie miały ze sobą związku, tracąc informację że to ci sami ludzie. Chi-kwadrat jest dla danych kategorycznych, nie ciągłych.

---

### Pytanie 5 (nowy — QQ-plot i normalność)

Patrząc na QQ-plot, jak rozpoznać że dane **NIE są normalne**?

**A)** Punkty leżą ściśle wzdłuż linii prostej — im bliżej, tym bardziej normalne

**B)** Punkty silnie odchylają się od linii prostej — np. wyginają się w górę na prawym końcu (asymetria prawostronno) lub tworzą kształt litery S

**C)** Histogram danych jest symetryczny

**D)** Wartość statystyki testu Shapiro-Wilka jest bliska 1.0

**Odpowiedź: B** — QQ-plot porównuje kwantyle empiryczne danych z kwantylami teoretycznego rozkładu normalnego. Dane normalne: punkty na linii prostej. Dane nie-normalne: charakterystyczne wzorce odchyleń. Wygięcie w górę prawego końca = asymetria prawostronno (np. zarobki). Wygięcie w obie strony (kształt S) = grube ogony (np. dane finansowe). A to właśnie opis danych normalnych (niepoprawna dla NIE-normalnych). D opisuje normalność (W bliskie 1 = normalne).

---

## Klucz odpowiedzi (dla prowadzącego)

| Pytanie | Odpowiedź | Temat |
|---------|-----------|-------|
| 1 | B | W11 — mediana vs średnia, odporność na outliery |
| 2 | C | W11 — asymetria histogramu, skewness |
| 3 | C | W12 — interpretacja p-wartości |
| 4 | C | W12 — sparowany t-test (`ttest_rel`) |
| 5 | B | W12 — QQ-plot, diagnostyka normalności |
