# S04 Laboratorium --- Cwiczenia

## Pandas: czyszczenie danych, merge i agregacja

**Czas:** 90 minut
**Notebook:** utworz nowy plik `S04_lab.ipynb` w VS Code
**Dataset:** syntetyczny e-commerce --- brudne zamowienia + czysta tabela klientow
**Commit:** na koncu zajec wykonaj `git commit -m "S04: czyszczenie, merge, groupby, pivot"`

---

## Przydatne materiały

| Temat | Link |
|-------|------|
| Pandas — Working with missing data | https://pandas.pydata.org/docs/user_guide/missing_data.html |
| Pandas — Merge, join, concatenate | https://pandas.pydata.org/docs/user_guide/merging.html |
| Pandas — Group by | https://pandas.pydata.org/docs/user_guide/groupby.html |
| Pandas — Duplicate Labels | https://pandas.pydata.org/docs/user_guide/duplicates.html |
| Pandas — IO Tools (Excel, Parquet, JSON) | https://pandas.pydata.org/docs/user_guide/io.html |
| requests — HTTP dla Pythona | https://requests.readthedocs.io/en/latest/ |

> **Warto wiedzieć:** W praktyce dane w firmach rzadko są w CSV — częściej w Excel (`pd.read_excel()`), JSON (`pd.read_json()`) lub Parquet (`pd.read_parquet()`). Dane można też pobierać ze stron WWW za pomocą `requests` + `BeautifulSoup` (web scraping) lub `pd.read_html()`. Więcej w rozdziale 4.23 skryptu studenta.

---

## Dane startowe --- wklej jako pierwsza komorke notebooka

```python
import pandas as pd
import numpy as np

# --- TABELA 1: ZAMOWIENIA (brudna!) ---
zamowienia_raw = pd.DataFrame({
    'id_zamowienia': list(range(1, 26)) + [5, 12, 18],  # 3 duplikaty!
    'data_zamowienia': [
        '2024-01-05', '2024-01-12', '2024-01-18', '2024-02-03', '2024-02-08',
        '2024-02-14', '2024-02-22', '2024-03-01', '2024-03-10', '2024-03-15',
        '2024-03-22', '2024-04-05', '2024-04-12', '2024-04-18', '2024-04-25',
        '2024-05-03', '2024-05-10', '2024-05-18', '2024-05-25', '2024-06-02',
        '2024-06-10', '2024-06-15', '2024-06-22', '2024-06-28', None,
        '2024-02-08', '2024-04-05', '2024-05-18'
    ],
    'klient_id': [1, 2, 3, 4, 5, 1, 6, 7, 8, 2,
                  3, 9, 10, 1, 4, 5, 6, 7, 8, 9,
                  10, 2, 3, 1, 5,
                  5, 9, 7],
    'produkt': ['Laptop', 'mysz', 'MONITOR', 'Klawiatura',
                'Sluchawki', 'kamera', 'Laptop', 'MYSZ', 'monitor',
                'Pendrive', 'Tablet', 'Sluchawki', 'laptop', 'Mysz',
                'Kamera', ' Laptop ', 'klawiatura', 'Monitor',
                'Tablet', 'PENDRIVE', 'Sluchawki', 'mysz',
                'Kamera', 'Klawiatura', 'Monitor',
                'Sluchawki', 'Sluchawki', 'Monitor'],
    'kategoria': ['Komputery', 'akcesoria', 'KOMPUTERY', 'akcesoria',
                  'Audio', 'akcesoria', 'komputery', 'AKCESORIA', 'Komputery',
                  'storage', 'Komputery', 'audio', 'komputery', 'Akcesoria',
                  'akcesoria', 'Komputery', 'AKCESORIA', 'komputery',
                  'Komputery', 'STORAGE', 'Audio', 'akcesoria',
                  'Akcesoria', 'akcesoria', 'Komputery',
                  'Audio', 'audio', 'komputery'],
    'ilosc': [1, 2, 1, 1, 1, 1, 1, 3, 1, 5,
              2, 1, 2, 1, 2, 1, 1, 1, 1, 3,
              1, 2, 1, 1, 1,
              1, 1, 1],
    'cena_jednostkowa': ['3999.99', '89.99', '1299.99', '249.99',
                         '399.99', '199.99', '3999.99', '89.99', '1299.99',
                         '49.99', '1499.99', '399.99', '3999.99', '89.99',
                         '199.99', '3999.99', '249.99', '1299.99',
                         '1499.99', '49.99', '399.99', '89.99',
                         '199.99', '249.99', 'brak',
                         '399.99', '399.99', '1299.99'],
    'status': ['zrealizowane', 'Zrealizowane', 'ZREALIZOWANE', 'zrealizowane',
               'anulowane', 'zrealizowane', 'zrealizowane', 'ZREALIZOWANE',
               'zrealizowane', 'zrealizowane', 'Anulowane', 'zrealizowane',
               'zrealizowane', 'zrealizowane', 'ANULOWANE', 'zrealizowane',
               'zrealizowane', 'Zrealizowane', 'anulowane', 'zrealizowane',
               'zrealizowane', 'zrealizowane', 'zrealizowane', 'zrealizowane',
               None,
               'anulowane', 'zrealizowane', 'Zrealizowane']
})

# --- TABELA 2: KLIENCI (czysta) ---
klienci = pd.DataFrame({
    'id': range(1, 11),
    'imie': ['Anna Kowalska', 'Piotr Nowak', 'Maria Wisniewska',
             'Jan Kowalczyk', 'Katarzyna Zielinska', 'Tomasz Lewandowski',
             'Agnieszka Wojcik', 'Michal Kaminski', 'Ewa Kaczmarek',
             'Robert Szymanski'],
    'miasto': ['Warszawa', 'Krakow', 'Gdansk', 'Wroclaw', 'Poznan',
               'Warszawa', 'Lodz', 'Krakow', 'Gdansk', 'Wroclaw'],
    'segment': ['VIP', 'Standard', 'VIP', 'Standard', 'Premium',
                'Premium', 'Standard', 'VIP', 'Standard', 'Premium']
})

print("Dane zaladowane.")
print(f"zamowienia_raw: {zamowienia_raw.shape}")
print(f"klienci: {klienci.shape}")
```

---

## Cwiczenie 1: Czyszczenie brudnego datasetu (20 min)

### Cel
Osoba studiujaca identyfikuje problemy w danych (NaN, duplikaty, zle typy) i stosuje pipeline czyszczenia.

### Zadanie 1a --- Diagnoza

Zanim zaczniesz czyscic --- musisz wiedziec **co** jest brudne.

```python
# 1. Wyswietl info() --- jakie typy maja kolumny? Czy sa braki?
zamowienia_raw.info()

# 2. Policz brakujace wartosci per kolumna
print(zamowienia_raw.isna().sum())

# 3. Ile jest pelnych duplikatow (identycznych wierszy)?
print(f"Duplikaty: {zamowienia_raw.duplicated().sum()}")

# 4. Ile unikalnych nazw produktow widzisz? (produkt.nunique())
#    Spodziewasz sie 8 produktow --- dlaczego jest wiecej?
print(f"Unikalne produkty: {zamowienia_raw['produkt'].nunique()}")

# 5. Jaki typ ma kolumna cena_jednostkowa? Czy to liczba?
print(f"Typ ceny: {zamowienia_raw['cena_jednostkowa'].dtype}")
```

### Zadanie 1b --- Pipeline czyszczenia

Przeprowadz czyszczenie krok po kroku. Pracuj na kopii.

```python
df = zamowienia_raw.copy()

# KROK 1: Usun duplikaty i zresetuj indeks
df = df.drop_duplicates().reset_index(drop=True)
print(f"Po dedup: {df.shape}")

# KROK 2: Napraw cene --- zamien 'brak' na NaN, skonwertuj na float
df['cena_jednostkowa'] = df['cena_jednostkowa'].replace('brak', np.nan)
df['cena_jednostkowa'] = pd.to_numeric(df['cena_jednostkowa'], errors='coerce')

# Ile NaN w cenie? Uzupelnij mediana
mediana = df['cena_jednostkowa'].median()
print(f"Mediana ceny: {mediana}")
df['cena_jednostkowa'] = df['cena_jednostkowa'].fillna(mediana)

# KROK 3: Skonwertuj date na datetime
df['data_zamowienia'] = pd.to_datetime(df['data_zamowienia'], errors='coerce')
print(f"NaN w dacie: {df['data_zamowienia'].isna().sum()}")

# KROK 4: Znormalizuj status (str.strip + str.lower)
df['status'] = df['status'].str.strip().str.lower()
print(f"Statusy: {sorted(df['status'].dropna().unique())}")

# WERYFIKACJA
print(f"\nShape: {df.shape}")
print(f"Dtypes:\n{df.dtypes}")
print(f"NaN per kolumna:\n{df.isna().sum()}")
```

### Sprawdzenie 1 ✅

- **1a.** Shape surowy: **(28, 8)**
- **1a.** NaN total (isna().sum().sum()): **2** (1 w data_zamowienia, 1 w status)
- **1a.** Duplikaty pelne: **3**
- **1a.** Unikalne produkty (surowe): **17** (zamiast 8 --- bo 'Laptop', 'laptop', 'LAPTOP', ' Laptop ' to rozne stringi)
- **1a.** Typ ceny: **object** (string, nie float!)
- **1b.** Shape po dedup: **(25, 8)**
- **1b.** NaN w cenie po replace+to_numeric: **1**
- **1b.** Mediana ceny: **324.99**
- **1b.** NaN w dacie: **1**
- **1b.** Statusy po lower(): **['anulowane', 'zrealizowane']**
- **1b.** NaN total po czyszczeniu (data + status): **2**
- **1b.** Typ cena_jednostkowa: **float64**, data_zamowienia: **datetime64[ns]**

---

## Cwiczenie 2: Operacje na tekstach (15 min)

### Cel
Osoba studiujaca normalizuje kolumny tekstowe i stosuje str.contains() do filtrowania.

### Zadanie 2a --- Normalizacja nazw produktow

```python
# Pracuj na df z Cwiczenia 1 (po krokach 1-4)

# 1. Wyswietl unikalne wartosci kolumny 'produkt' PRZED normalizacja
print(f"Przed: {df['produkt'].nunique()} unikalnych")
print(sorted(df['produkt'].unique()))

# 2. Zastosuj str.strip() + str.title() na kolumnie 'produkt'
df['produkt'] = df['produkt'].str.strip().str.title()

# 3. Ile unikalnych produktow teraz?
print(f"\nPo: {df['produkt'].nunique()} unikalnych")
print(sorted(df['produkt'].unique()))
```

### Zadanie 2b --- Normalizacja kategorii

```python
# 1. Znormalizuj kolumne 'kategoria': str.strip() + str.title()
df['kategoria'] = df['kategoria'].str.strip().str.title()

# 2. Wyswietl unikalne kategorie
print(f"Kategorie: {sorted(df['kategoria'].unique())}")
```

### Zadanie 2c --- Filtrowanie z str.contains()

```python
# 1. Ile zamowien dotyczy produktu 'Mysz'?
mysz = df[df['produkt'].str.contains('Mysz', na=False)]
print(f"Zamowienia na Mysz: {len(mysz)}")

# 2. Ile zamowien jest w kategorii 'Audio'?
audio = df[df['kategoria'] == 'Audio']
print(f"Zamowienia Audio: {len(audio)}")

# 3. Znajdz zamowienia na produkty zawierajace litere 'a'
#    (case=False = bez rozrozniana wielkosci liter)
z_a = df[df['produkt'].str.contains('a', case=False, na=False)]
print(f"Produkty z 'a' w nazwie: {len(z_a)}")
```

### Sprawdzenie 2 ✅

- **2a.** Unikalne produkty PRZED: **17**
- **2a.** Unikalne produkty PO title(): **8** (Kamera, Klawiatura, Laptop, Monitor, Mysz, Pendrive, Sluchawki, Tablet)
- **2b.** Unikalne kategorie PO: **4** (Akcesoria, Audio, Komputery, Storage)
- **2c.** Zamowienia na Mysz: **4**
- **2c.** Zamowienia Audio: **3**
- **2c.** Produkty z 'a' w nazwie: **15**

---

## Cwiczenie 3: Merge dwoch tabel (20 min)

### Cel
Osoba studiujaca laczy tabele merge() i rozumie roznice miedzy inner/left/outer.

### Zadanie 3a --- Laczenie zamowien z klientami

```python
# 1. Polacz df (oczyszczone zamowienia) z tabela klienci
#    Klucz: klient_id w zamowieniach = id w klientach
#    Uzyj how='left' zeby zachowac wszystkie zamowienia
pelne = df.merge(
    klienci,
    left_on='klient_id',
    right_on='id',
    how='left',
    suffixes=('', '_kl')
)

# 2. Wyswietl shape i pierwsze wiersze
print(f"Shape po merge: {pelne.shape}")
print(pelne[['id_zamowienia', 'data_zamowienia', 'imie', 'miasto',
             'produkt', 'cena_jednostkowa', 'ilosc']].head(5))

# 3. Czy sa zamowienia bez dopasowania (NaN w imie)?
print(f"Zamowienia bez klienta: {pelne['imie'].isna().sum()}")
```

### Zadanie 3b --- Wartosc zamowienia

```python
# 1. Dodaj kolumne 'wartosc' = ilosc * cena_jednostkowa
pelne['wartosc'] = pelne['ilosc'] * pelne['cena_jednostkowa']

# 2. Laczna wartosc WSZYSTKICH zamowien
print(f"Laczna wartosc: {pelne['wartosc'].sum():.2f} zl")

# 3. Odfiltruj tylko zrealizowane zamowienia
zreal = pelne[pelne['status'] == 'zrealizowane'].copy()
print(f"Zrealizowane: {len(zreal)} zamowien")
print(f"Wartosc zrealizowanych: {zreal['wartosc'].sum():.2f} zl")

# 4. Ile zamowien anulowano?
anul = pelne[pelne['status'] == 'anulowane']
print(f"Anulowane: {len(anul)} zamowien")
```

### Zadanie 3c --- Porownanie typow merge

```python
# Porownaj inner vs left vs outer --- ile wierszy w kazdym?
for how in ['inner', 'left', 'outer']:
    result = df.merge(klienci, left_on='klient_id', right_on='id', how=how)
    print(f"how='{how}': {len(result)} wierszy")
```

### Sprawdzenie 3 ✅

- **3a.** Shape po merge: **(25, 13)**
- **3a.** Zamowienia bez klienta (NaN w imie): **0** (wszyscy klienci maja dopasowanie)
- **3b.** Laczna wartosc wszystkich: **32 594,62 zl**
- **3b.** Zrealizowane zamowienia: **20**
- **3b.** Wartosc zrealizowanych: **26 969,69 zl**
- **3b.** Anulowane zamowienia: **4**
- **3c.** Inner i left daja po **25 wierszy** (bo kazdy klient_id istnieje w tabeli klientow)

---

## Cwiczenie 4: Groupby --- pytania biznesowe (20 min)

### Cel
Osoba studiujaca agreguje dane z groupby + agg i odpowiada na pytania biznesowe.

**Uwaga:** Pracuj na tabeli `zreal` (tylko zrealizowane zamowienia) --- analiza biznesowa nie uwzglednia anulowanych.

### Zadanie 4a --- Przychod per kategoria

```python
# Ktora kategoria generuje najwiekszy przychod?
przychod_kat = zreal.groupby('kategoria')['wartosc'].sum().sort_values(ascending=False)
print("Przychod per kategoria:")
print(przychod_kat.round(2))
```

### Zadanie 4b --- Top 3 klienci

```python
# Ktory klient wydal najwiecej?
top_klienci = zreal.groupby('imie')['wartosc'].sum().sort_values(ascending=False)
print("Top 3 klienci wg wydatkow:")
print(top_klienci.head(3).round(2))
```

### Zadanie 4c --- Raport segmentow (named aggregation)

```python
# Stworz raport segmentow: liczba zamowien, laczny przychod, srednia wartosc
raport_seg = zreal.groupby('segment').agg(
    zamowienia=('id_zamowienia', 'count'),
    przychod=('wartosc', 'sum'),
    sr_wartosc=('wartosc', 'mean')
).round(2)

print("Raport segmentow klientow:")
print(raport_seg)
```

### Zadanie 4d --- Przychod per miasto

```python
# W ktorym miescie sprzedaz jest najwyzsza?
przychod_miasto = zreal.groupby('miasto')['wartosc'].sum().sort_values(ascending=False)
print("Przychod per miasto:")
print(przychod_miasto.round(2))
```

### Sprawdzenie 4 ✅

**Przychod per kategoria (zrealizowane):**

| Kategoria | Przychod |
|-----------|----------|
| Komputery | 23 899,92 zl |
| Akcesoria | 1 869,87 zl |
| Audio | 799,98 zl |
| Storage | 399,92 zl |

**Top 3 klienci:**

| Klient | Wydatki |
|--------|---------|
| Robert Szymanski | 8 399,97 zl |
| Anna Kowalska | 4 539,96 zl |
| Tomasz Lewandowski | 4 249,98 zl |

**Raport segmentow:**

| Segment | Zamowienia | Przychod | Srednia |
|---------|-----------|----------|---------|
| Premium | 5 | 16 649,94 zl | 3 329,99 zl |
| Standard | 8 | 2 979,82 zl | 372,48 zl |
| VIP | 7 | 7 339,93 zl | 1 048,56 zl |

**Top miasto:** Warszawa (8 789,94 zl), Wroclaw (8 649,96 zl), Poznan (3 999,99 zl)

---

## Cwiczenie 5: Pivot table --- analiza cross-tabulacyjna (15 min)

### Cel
Osoba studiujaca konstruuje tabele przestawne (pivot_table) i tabulacje krzyzowe (crosstab).

### Zadanie 5a --- Pivot: segment x kategoria

```python
# Stworz tabele przestawna: przychod per segment i kategoria
# Dodaj sumy brzegowe (margins=True)
pivot_seg = pd.pivot_table(
    zreal,
    values='wartosc',
    index='segment',
    columns='kategoria',
    aggfunc='sum',
    fill_value=0,
    margins=True
)
print("Przychod [PLN]: Segment x Kategoria")
print(pivot_seg.round(2))
```

### Zadanie 5b --- Crosstab: segment x miasto

```python
# Ile zamowien zlozyly poszczegolne segmenty w kazdym miescie?
ct = pd.crosstab(
    zreal['segment'],
    zreal['miasto'],
    margins=True
)
print("Liczba zamowien: Segment x Miasto")
print(ct)

# Wersja procentowa (udzial miast w kazdym segmencie)
ct_pct = pd.crosstab(
    zreal['segment'],
    zreal['miasto'],
    normalize='index'
)
print("\nUdzialy % per segment:")
print((ct_pct * 100).round(1))
```

### Zadanie 5c --- Pivot: miesiac x kategoria

```python
# Dodaj kolumne miesiac i stworz tabele miesieczna
zreal['miesiac'] = zreal['data_zamowienia'].dt.month

pivot_mc = pd.pivot_table(
    zreal,
    values='wartosc',
    index='miesiac',
    columns='kategoria',
    aggfunc='sum',
    fill_value=0,
    margins=True
)
print("Sprzedaz miesieczna per kategoria [PLN]:")
print(pivot_mc.round(2))

# Ktory miesiac byl najlepszy?
sprzedaz_m = zreal.groupby('miesiac')['wartosc'].sum()
print(f"\nNajlepszy miesiac: {sprzedaz_m.idxmax()} ({sprzedaz_m.max():.2f} zl)")
```

### Sprawdzenie 5 ✅

**Pivot: segment x kategoria:**

| | Akcesoria | Audio | Komputery | Storage | All |
|--|-----------|-------|-----------|---------|-----|
| **Premium** | 249,99 | 399,99 | 15 999,96 | 0,00 | 16 649,94 |
| **Standard** | 879,92 | 399,99 | 1 299,99 | 399,92 | 2 979,82 |
| **VIP** | 739,96 | 0,00 | 6 599,97 | 0,00 | 7 339,93 |
| **All** | 1 869,87 | 799,98 | 23 899,92 | 399,92 | 26 969,69 |

**Crosstab: segment x miasto:**

| | Gdansk | Krakow | Lodz | Poznan | Warszawa | Wroclaw | All |
|--|--------|--------|------|--------|----------|---------|-----|
| **Premium** | 0 | 0 | 0 | 1 | 2 | 2 | 5 |
| **Standard** | 2 | 3 | 2 | 0 | 0 | 1 | 8 |
| **VIP** | 2 | 1 | 0 | 0 | 4 | 0 | 7 |
| **All** | 4 | 4 | 2 | 1 | 6 | 3 | 20 |

**Crosstab % (VIP):** Warszawa = 57,1%, Gdansk = 28,6%, Krakow = 14,3%

**Najlepszy miesiac:** 4 (kwiecien) z kwota **8 489,96 zl**

---

## Commit

```bash
# Zapisz notebook (Ctrl+S w VS Code)
git add S04_lab.ipynb
git commit -m "S04: czyszczenie danych, merge, groupby, pivot_table"
git push
```

Sprawdz na GitHub czy commit jest widoczny.

---

## Podsumowanie --- co dzis zrobilismy

```
CZYSZCZENIE DANYCH
  +-- isna() / info()           --> diagnoza brakow
  +-- dropna()                  --> usuwanie wierszy/kolumn z NaN
  +-- fillna(mediana)           --> uzupelnianie brakow
  +-- drop_duplicates()         --> usuwanie duplikatow
  +-- pd.to_numeric(coerce)     --> konwersja string -> float
  +-- pd.to_datetime(coerce)    --> konwersja string -> datetime
  +-- str.strip().str.title()   --> normalizacja tekstu
  +-- str.contains()            --> filtrowanie po tekscie

LACZENIE I AGREGACJA
  +-- merge(how='left')         --> laczenie tabel po kluczu (SQL JOIN)
  +-- pd.concat()               --> sklejanie tabel (SQL UNION)
  +-- groupby().agg()           --> agregacja per grupa
  +-- named aggregation         --> czytelne nazwy kolumn wynikowych
  +-- pivot_table(margins=True) --> tabela przestawna z sumami
  +-- pd.crosstab(normalize)    --> tabulacja krzyzowa z procentami
```

### Wymagania do zaliczenia S04
- [ ] Cwiczenie 1: Czyszczenie --- shape (25, 8), brak duplikatow, poprawne typy
- [ ] Cwiczenie 2: Normalizacja --- 8 produktow, 4 kategorie
- [ ] Cwiczenie 3: Merge --- shape (25, 13), wartosc zrealizowanych 26 969,69 zl
- [ ] Cwiczenie 4: Groupby --- raport segmentow, top klienci, przychod per miasto
- [ ] Cwiczenie 5: Pivot --- tabela segment x kategoria z margins, crosstab z procentami
- [ ] Commit na GitHub z komunikatem zawierajacym "S04"
