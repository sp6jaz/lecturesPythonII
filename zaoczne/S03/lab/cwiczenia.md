# S03 Lab — Cwiczenia laboratoryjne

## Temat: Pandas — od tworzenia danych do precyzyjnych pytan biznesowych

**Programowanie w Pythonie II** | Spotkanie zaoczne 3 — laboratorium
**Czas:** 90 min | **Forma:** cwiczenia praktyczne

---

## Przydatne materiały

| Temat | Link |
|-------|------|
| Pandas — oficjalna dokumentacja | https://pandas.pydata.org/docs/ |
| Pandas — 10 Minutes to Pandas | https://pandas.pydata.org/docs/user_guide/10min.html |
| Pandas — Indexing and selecting | https://pandas.pydata.org/docs/user_guide/indexing.html |
| Pandas — DataFrame.loc | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html |
| Pandas — IO Tools (CSV, Excel, Parquet, JSON) | https://pandas.pydata.org/docs/user_guide/io.html |
| requests — dokumentacja | https://requests.readthedocs.io/en/latest/ |
| BeautifulSoup — dokumentacja | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ |

> **Warto wiedzieć:** Pandas obsługuje wiele formatów plików poza CSV: `pd.read_excel()` (raporty firmowe), `pd.read_json()` (dane z API), `pd.read_parquet()` (szybki format kolumnowy). W praktyce biznesowej dane rzadko są w CSV — warto znać te metody. Więcej w rozdziale 4 skryptu studenta.

---

## Cwiczenie 1: Tworzenie Series i DataFrame, wczytanie danych (15 min)

### Cel
Utworz Series i DataFrame z roznych zrodel, wczytaj prawdziwy dataset.

### Krok 1 — Series

```python
import pandas as pd
import numpy as np
```

**Zadanie 1a:** Utworz Series `pensje` z dict:
```python
# Klucze: 'Anna', 'Jan', 'Ewa', 'Marek', 'Kasia'
# Wartosci: 5500, 7200, 4800, 9100, 6300
pensje = pd.Series(...)
```

**Zadanie 1b:** Odpowiedz na pytania o `pensje`:
```python
# 1. Kto zarabia najwiecej? (uzyj idxmax())
# 2. Ile wynosi srednia pensja? (mean())
# 3. Kto zarabia powyzej sredniej? (filtrowanie boolean)
# 4. Ile osob zarabia ponizej 6000? (filtr + len())
```

### Krok 2 — DataFrame z dict

```python
sklep = pd.DataFrame({
    'produkt': ['Laptop', 'Tablet', 'Smartfon', 'Sluchawki', 'Monitor'],
    'cena': [3500, 1800, 2500, 350, 2200],
    'sprzedaz': [340, 120, 560, 90, 420],
    'kategoria': ['Komputery', 'Mobilne', 'Mobilne', 'Akcesoria', 'Komputery']
})
```

**Zadanie 1c:** Zbadaj DataFrame i dodaj kolumne:
```python
# 1. Wyswietl shape, columns, dtypes
# 2. Dodaj kolumne 'przychod' = cena * sprzedaz
# 3. Jaki jest laczny przychod? (sum())
# 4. Ktory produkt ma najwyzszy przychod? (idxmax na kolumnie 'przychod', potem loc)
```

### Krok 3 — Wczytanie CSV

```python
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(url)
```

**Zadanie 1d:** Pierwszy rzut oka:
```python
# 1. Wyswietl head(3)
# 2. Wyswietl tail(3)
# 3. Wyswietl shape — ile wierszy i kolumn?
# 4. Wyswietl dtypes — jakie typy danych?
```

### Sprawdzenie

- 1a: `pensje['Marek']` = 9100
- 1b: Najwiecej: Marek; Srednia: 6580.0; Powyzej sredniej: Jan (7200) i Marek (9100); Ponizej 6000: 2 osoby (Anna i Ewa)
- 1c: shape = (5, 4); przychod Laptop = 1 190 000; laczny przychod = 3 761 500; najwyzszy przychod: Smartfon (lub iloc[2])
- 1d: shape = (244, 7); total_bill i tip = float64, size = int64, reszta = object

---

## Cwiczenie 2: EDA — describe, info, brakujace dane (15 min)

### Cel
Przeprowadz pelna eksploracje datasetu tips.

### Dane

```python
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
```

### Zadania

**Zadanie 2a: Struktura danych**
```python
# 1. Uruchom info() — ile kolumn? Ile non-null wartosci?
# 2. Czy sa jakiekolwiek brakujace wartosci? (isna().sum())
# 3. Ile lacznie brakow? (isna().sum().sum())
```

**Zadanie 2b: Statystyki opisowe**
```python
# 1. Uruchom describe() — jaka jest srednia, mediana i max total_bill?
# 2. Uruchom describe(include='all') — jaki dzien wystepuje najczesciej?
# 3. Jaka jest mediana napiwku (tip)? (median())
```

**Zadanie 2c: Rozklady wartosci**
```python
# 1. Ile rachunkow w kazdy dzien? (value_counts na 'day')
# 2. Ile rachunkow od palaczy vs niepalacych? (value_counts na 'smoker')
# 3. Ile rachunkow od kobiet vs mezczyzn? (value_counts na 'sex')
# 4. Jaki procent rachunkow to obiad (Dinner)? (value_counts z normalize=True)
```

**Zadanie 2d: Wnioski**
W komorce Markdown napisz 3-5 obserwacji o datasecie, np.:
- "Dataset zawiera ... rachunkow z ... kolumnami"
- "Najczestszy dzien to ... (... rachunkow)"
- "Sredni rachunek wynosi ... $"
- "... % rachunkow to obiad"

### Sprawdzenie

- 2a: 7 kolumn, 244 non-null w kazdej, 0 brakow
- 2b: mean total_bill = 19.79; median total_bill = 17.795; max total_bill = 50.81; najczestszy dzien = Sat (87); mediana tip = 2.9
- 2c: Sat: 87, Sun: 76, Thur: 62, Fri: 19; No: 151, Yes: 93; Male: 157, Female: 87; Dinner: 72% (176/244)

---

## Cwiczenie 3: loc i iloc — selekcja wierszy i kolumn (15 min)

### Cel
Naucz sie precyzyjnie wybierac wiersze i kolumny z DataFrame.

### Dane

```python
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
```

### Zadania iloc (pozycja)

**Zadanie 3a:**
```python
# 1. Wyswietl wiersz nr 0 (iloc) — jaki to rachunek?
# 2. Wyswietl wiersz nr 10 — jaki total_bill?
# 3. Wyswietl wiersze 5-9, kolumny 0-2 (slice)
# 4. Wyswietl ostatni wiersz (iloc[-1])
# 5. Wyswietl co 50-ty wiersz (iloc[::50])
```

### Zadania loc (etykieta/warunek)

**Zadanie 3b:**
```python
# 1. Wyswietl kolumne 'total_bill' za pomoca loc (wszystkie wiersze, head 5)
# 2. Wyswietl kolumny 'total_bill' i 'tip' (loc, head 5)
# 3. Wyswietl wiersze, gdzie total_bill > 40 (loc + warunek) — ile ich jest?
# 4. Wyswietl wiersze z niedzieli (day == 'Sun'), tylko kolumny 'total_bill' i 'tip' — ile?
```

### Zadanie z wlasnym indeksem

**Zadanie 3c:**
```python
produkty = pd.DataFrame({
    'cena': [3500, 1800, 2500, 350, 2200],
    'magazyn': [45, 120, 200, 500, 75],
    'kategoria': ['Komputery', 'Mobilne', 'Mobilne', 'Akcesoria', 'Komputery']
}, index=['Laptop', 'Tablet', 'Smartfon', 'Sluchawki', 'Monitor'])

# 1. Wyswietl cene Laptopa (loc)
# 2. Wyswietl cene i magazyn dla Tablet i Monitor (loc z lista)
# 3. Wyswietl produkty z kategorii 'Mobilne' (loc + warunek)
```

### Sprawdzenie

- 3a: wiersz 0 total_bill = 16.99; wiersz 10 total_bill = 10.27; ostatni total_bill = 18.78
- 3b: total_bill > 40: 10 wierszy; niedziele: 76 wierszy
- 3c: cena Laptopa = 3500; Mobilne: Tablet i Smartfon

---

## Cwiczenie 4: Filtrowanie — pytania biznesowe (25 min)

### Cel
Odpowiedz na precyzyjne pytania biznesowe filtrujac dane.

### Dane

```python
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
```

### Zadania — filtry proste

**Zadanie 4a:**
```python
# 1. Ile rachunkow jest > 30$?
# 2. Ile rachunkow jest od kobiet (sex == 'Female')?
# 3. Ile rachunkow jest z obiadu (time == 'Dinner')?
# 4. Ile rachunkow pochodzi z grup >= 4 osob?
```

### Zadania — AND, OR

**Zadanie 4b:**
```python
# 1. Obiad w sobote — ile rachunkow? (day == 'Sat' AND time == 'Dinner')
# 2. Sobota LUB niedziela (uzyj isin) — ile?
# 3. Rachunki miedzy 10 a 20 dolarow (uzyj between) — ile?
# 4. Rachunki z piatkow LUB sobot (isin) — ile?
```

### Zadania — pytania biznesowe

**Zadanie 4c: Scenariusze analityczne**
```python
# 1. "Pokaz mi rachunki powyzej 30$ z obiadu w sobote"
#    Ile ich jest?

# 2. "Ile razy niepalaczki (smoker == 'No', sex == 'Female') daly napiwek > 20%?"
#    Wskazowka: 3 warunki polaczone &

# 3. "Czy w czwartek sa lunche? Ile rachunkow to czwartek + lunch?"
#    (Podpowiedz: tak, 61 z 62 czwartkowych rachunkow to lunch!)

# 4. "Pokaz TOP-5 najdrozszych rachunkow z weekendu"
#    Wskazowka: filtr isin + nlargest
```

### Zadanie — query

**Zadanie 4d:**
```python
# Przepisz filtr z 4c.1 uzywajac query():
# "Rachunki > 30$ z obiadu w sobote"
wynik = tips.query("...")
print(f"Wynik: {len(wynik)}")
```

### Sprawdzenie

- 4a: >30$: 32; kobiety: 87; obiad: 176; grupy>=4: 46
- 4b: obiad w sobote: 87; Sat|Sun: 163; 10-20$: 130; Fri|Sat: 106
- 4c:
  - Sob + Dinner + >30$: wynik bedzie podzbiorem 32 rachunkow >30$
  - Niepalaczki z tip>20%: 6
  - Czwartek + lunch: 61
  - TOP-5 weekend: najwyzszy = 50.81$ (Sat)
- 4d: query powinien dac ten sam wynik co filtr w 4c.1

---

## Cwiczenie 5: Segmentacja — pd.cut, nowa kolumna, value_counts (20 min)

### Cel
Podziel klientow na segmenty i przeanalizuj kazdy segment.

### Dane

```python
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
```

### Krok 1 — Segmentacja rachunkow

**Zadanie 5a:**
```python
# Uzyj pd.cut do podzialu rachunkow na 3 segmenty:
# 'Niski' (0-15$), 'Sredni' (15-30$), 'Wysoki' (30-100$)
tips['segment'] = pd.cut(
    tips['total_bill'],
    bins=[0, 15, 30, 100],
    labels=['Niski', 'Sredni', 'Wysoki']
)

# 1. Ile rachunkow w kazdym segmencie? (value_counts)
# 2. Jaki procent stanowi kazdy segment? (value_counts z normalize=True)
```

### Krok 2 — Analiza per segment

**Zadanie 5b:**
```python
# Dla kazdego segmentu oblicz:
# - sredni napiwek (tip) w dolarach
# - sredni napiwek procentowy (tip_pct)
# - liczbe rachunkow
# Wskazowka: petla for + filtrowanie

for seg in ['Niski', 'Sredni', 'Wysoki']:
    subset = tips[tips['segment'] == seg]
    print(f"{seg}: n={len(subset)}, "
          f"sr. tip = {subset['tip'].mean():.2f}$, "
          f"sr. tip_pct = {subset['tip_pct'].mean():.1f}%")
```

**Zadanie 5c:** Odpowiedz na pytanie:
> "Czy klienci z wyzszymi rachunkami daja wyzszy napiwek procentowo?"

Zapisz odpowiedz w komorce Markdown.

### Krok 3 — Segmentacja napiwkow

**Zadanie 5d:**
```python
# Utwórz kolumne 'kat_tip' dzieleaca napiwki procentowe:
# 'Skapy' (0-10%), 'Przecietny' (10-15%), 'Hojny' (15-20%), 'Bardzo hojny' (20-100%)
tips['kat_tip'] = pd.cut(
    tips['tip_pct'],
    bins=[0, 10, 15, 20, 100],
    labels=['Skapy', 'Przecietny', 'Hojny', 'Bardzo hojny']
)

# 1. Ile osob w kazdej kategorii? (value_counts)
# 2. Jaki dzien ma najwyzszy odsetek "Bardzo hojnych"?
#    Wskazowka: filtr kat_tip == 'Bardzo hojny', potem value_counts na 'day'
```

### Krok 4 — Commit

```bash
git add lab_s03_pandas.ipynb
git commit -m "S03: Pandas — Series, DataFrame, filtrowanie, segmentacja"
git push
```

### Sprawdzenie

- 5a: Niski: 80 (32.8%), Sredni: 132 (54.1%), Wysoki: 32 (13.1%)
- 5b:
  - Niski: n=80, sr. tip=2.05$, sr. tip_pct=18.4%
  - Sredni: n=132, sr. tip=3.03$, sr. tip_pct=15.6%
  - Wysoki: n=32, sr. tip=4.22$, sr. tip_pct=12.2%
- 5c: NIE — paradoksalnie klienci z nizszymi rachunkami daja **wyzszy procent** napiwku (18.4% vs 12.2%). Kwota rosnie (2.05$ vs 4.22$), ale proporcja maleje.
- 5d: Skapy: 27, Przecietny: 84, Hojny: 95, Bardzo hojny: 38

---

## Podsumowanie

Po dzisiejszych zajeciach umiesz:
- Tworzyc Series z listy, dict i z kolumny DataFrame
- Tworzyc DataFrame z dict i wczytywac z CSV
- Eksplorowac dane: head(), info(), describe(), value_counts(), isna()
- Uzywac iloc (pozycja) i loc (etykieta/warunek) do selekcji
- Filtrowac dane z &, |, ~, isin, between, query
- Tworzyc rankingi (sort_values, nlargest)
- Segmentowac dane na grupy (pd.cut) i analizowac wyniki

**Na nastepnym spotkaniu (S04):** Czyszczenie danych (NaN, duplikaty, konwersja typow) i laczenie tabel (merge, concat, groupby). Prawdziwa praca analityka zaczyna sie od brudnych danych!
