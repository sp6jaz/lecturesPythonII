# L05 — Ćwiczenia laboratoryjne

## Temat: Pandas — Series, DataFrame, eksploracja danych

**Programowanie w Pythonie II** | Laboratorium 5
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne

---

## Ćwiczenie 1: Series — tworzenie i operacje (20 min)

### Cel
Utwórz Series z różnych źródeł i wykonaj podstawowe operacje.

### Krok 1 — Series z listy i dict

```python
import pandas as pd
import numpy as np

# Series z listy — domyślny indeks (0, 1, 2, ...)
oceny = pd.Series([4.5, 3.0, 5.0, 3.5, 4.0])
print(oceny)
```

**Zadanie 1a:** Utwórz Series `pensje` z dict:
```python
# Klucze: 'Anna', 'Jan', 'Ewa', 'Marek', 'Kasia'
# Wartości: 5500, 7200, 4800, 9100, 6300
```

**Zadanie 1b:** Odpowiedz na pytania o `pensje`:
```python
# 1. Kto zarabia najwięcej? (użyj idxmax())
# 2. Ile wynosi średnia pensja?
# 3. Kto zarabia powyżej średniej? (filtrowanie boolean)
# 4. Ile osób zarabia poniżej 6000?
```

### Krok 2 — Operacje na Series

**Zadanie 1c:** Oblicz pensje po zmianach:
```python
# 1. Podwyżka 10% dla wszystkich
# 2. Premia 500 zł dla wszystkich
# 3. Nowa pensja = (pensja * 1.10) + 500
# 4. Wyświetl ranking od najwyższej nowej pensji
```

### Sprawdzenie ✅

- 1a: `pensje['Marek']` = 9100
- 1b: Najwięcej: Marek; Średnia: 6580.0; Powyżej średniej: Jan (7200), Marek (9100) — Kasia (6300 < 6580) nie łapie się
- 1c: Nowa pensja Anny = 5500 * 1.10 + 500 = 6550.0

---

## Ćwiczenie 2: DataFrame — tworzenie i atrybuty (20 min)

### Cel
Utwórz DataFrame z dict i wczytaj dane z pliku CSV.

### Krok 1 — DataFrame z dict

```python
# Dane o produktach sklepu internetowego
sklep = pd.DataFrame({
    'produkt': ['Laptop', 'Tablet', 'Smartfon', 'Słuchawki', 'Monitor'],
    'cena': [3500, 1800, 2500, 350, 2200],
    'stan_magazynowy': [45, 120, 200, 500, 75],
    'kategoria': ['Komputery', 'Mobilne', 'Mobilne', 'Akcesoria', 'Komputery']
})
```

**Zadanie 2a:** Zbadaj DataFrame:
```python
# 1. Wyświetl kształt (shape)
# 2. Wyświetl nazwy kolumn
# 3. Wyświetl typy danych (dtypes)
# 4. Wyświetl head(3)
```

**Zadanie 2b:** Dodaj kolumny:
```python
# 1. 'wartosc_magazynu' = cena * stan_magazynowy
# 2. 'cena_z_vat' = cena * 1.23
# Wyświetl cały DataFrame
```

### Krok 2 — Wczytanie CSV

```python
# Wczytaj dataset tips
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(url)
```

**Zadanie 2c:** Podstawowa eksploracja tips:
```python
# 1. Ile wierszy i kolumn? (shape)
# 2. Wyświetl ostatnie 5 wierszy (tail)
# 3. Wyświetl 3 losowe wiersze (sample)
# 4. Jakie typy danych mają kolumny? (dtypes)
```

### Sprawdzenie ✅

- 2a: shape = (5, 4); kolumny = ['produkt', 'cena', 'stan_magazynowy', 'kategoria']
- 2b: Wartość magazynu Laptop = 3500 × 45 = 157500
- 2c: tips.shape = (244, 7)

---

## Ćwiczenie 3: Eksploracja datasetu — samodzielna analiza (30 min)

### Cel
Przeprowadź pełną eksplorację EDA na prawdziwym datasecie.

### Dane

```python
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv'
penguins = pd.read_csv(url)
```

### Zadania

**Zadanie 3a: Pierwszy rzut oka**
```python
# 1. Wyświetl head(10)
# 2. Wyświetl shape
# 3. Uruchom info() — ile brakujących wartości widzisz?
```

**Zadanie 3b: Statystyki opisowe**
```python
# 1. Uruchom describe() — co mówią ci średnie i odchylenia?
# 2. Uruchom describe(include='all') — co dodają kolumny tekstowe?
# 3. Jaka jest mediana masy ciała (body_mass_g)?
```

**Zadanie 3c: Rozkłady wartości**
```python
# 1. Ile jest pingwinów każdego gatunku? (value_counts na 'species')
# 2. Ile pingwinów na każdej wyspie? (value_counts na 'island')
# 3. Rozkład płci (value_counts na 'sex') — czy jest zbalansowany?
# 4. Jaki procent to gatunek Adelie? (normalize=True)
```

**Zadanie 3d: Brakujące dane**
```python
# 1. Policz brakujące wartości w każdej kolumnie (isna().sum())
# 2. Jaki procent danych brakuje w kolumnie 'sex'?
# 3. Ile wierszy ma JAKIKOLWIEK brak? (isna().any(axis=1).sum())
```

**Zadanie 3e: Wnioski**
W komórce Markdown napisz 5 obserwacji o datasecie, np.:
- "Dataset zawiera X pingwinów z Y gatunków..."
- "Najczęstszy gatunek to..."
- "Brakuje danych w kolumnach..."
- "Średnia masa ciała to... g"
- "Pingwiny mieszkają na X wyspach, najliczniej na..."

### Sprawdzenie ✅

- 3a: shape = (344, 7); info() pokaże, że 4 kolumny mają po 342 non-null, sex ma 333 non-null
- 3b: Mediana body_mass_g = 4050.0 g
- 3c: Adelie: 152, Gentoo: 124, Chinstrap: 68; Adelie = 44.2%
- 3d: sex: 11 braków → 11/344 = 3.2%

---

## Ćwiczenie 4: Pytania biznesowe + commit (15 min)

### Cel
Odpowiedz na pytania biznesowe o danych i zapisz pracę w Git.

### Dane — wróć do datasetu tips

```python
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# Dodaj kolumnę z procentem napiwku
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
```

### Pytania

**Zadanie 4a:**
```python
# 1. Jaki jest średni rachunek (total_bill)?
# 2. Jaki jest średni napiwek w procentach?
# 3. Który dzień ma najwięcej rachunków? (value_counts na 'day')
# 4. Ile rachunków jest od palaczy? (value_counts na 'smoker')
# 5. Jaki jest najwyższy napiwek procentowy? Kto go dał? (idxmax na tip_pct, potem tips.loc[idx])
```

### Commit

```bash
git add lab05_pandas_intro.ipynb
git commit -m "L05: Pandas — Series, DataFrame, eksploracja EDA"
git push
```

---

## Podsumowanie

Po dzisiejszych zajęciach umiesz:
- ✅ Tworzyć Series z listy, dict i z kolumny DataFrame
- ✅ Tworzyć DataFrame z dict i wczytywać z CSV
- ✅ Eksplorować dane: head(), info(), describe(), value_counts(), isna()
- ✅ Dodawać nowe kolumny obliczone z istniejących
- ✅ Wyciągać wnioski z danych (EDA)

**Na następnych zajęciach:** loc/iloc, filtrowanie z warunkami logicznymi, sortowanie — zaczniecie odpowiadać na precyzyjne pytania o danych.
