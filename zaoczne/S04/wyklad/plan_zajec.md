# S04 Wykład — Plan zajęć dla prowadzącego

## Temat: Pandas — czyszczenie danych, merge i agregacja

### Informacje organizacyjne
- **Czas:** 90 min (wykład, pierwsza część bloku 180 min)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z pandas/numpy
- **Kontekst:** Studia zaoczne, S04 = spotkanie 4. Studenci znają Pandas z S03 (Series, DataFrame, loc/iloc, filtrowanie)
- **Po wykładzie:** od razu lab (90 min) — ta sama osoba prowadzi

### Efekty uczenia sie (Bloom)
Po tym wykladzie osoba studiujaca:
1. **Identyfikuje** brakujace wartosci w DataFrame metodami `isna()`, `info()` i **stosuje** strategie `fillna()` / `dropna()` (Bloom 2-3)
2. **Wykrywa i usuwa** duplikaty metodami `duplicated()`, `drop_duplicates()` (Bloom 3)
3. **Konwertuje** typy danych: `astype()`, `pd.to_numeric(errors='coerce')`, `pd.to_datetime(errors='coerce')` (Bloom 3)
4. **Czyści** kolumny tekstowe operacjami `str.lower()`, `str.strip()`, `str.contains()`, `str.replace()` (Bloom 3)
5. **Laczy** DataFrames za pomoca `merge()` (inner/left/outer) i `pd.concat()` (Bloom 3)
6. **Agreguje** dane z `groupby()` + `agg()` (sum, mean, count) i stosuje nazwa agregacje (Bloom 3)
7. **Konstruuje** raporty podsumowujace z `pivot_table()` i `pd.crosstab()` (Bloom 3-4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **WPROWADZENIE** | Cel: od brudnych danych do raportu | Rozmowa |
| 0:05-0:20 | **MATERIAL 1** | Brakujace wartosci: isna, dropna, fillna | Live coding |
| 0:20-0:30 | **MATERIAL 2** | Duplikaty: duplicated, drop_duplicates | Live coding |
| 0:30-0:40 | **MATERIAL 3** | Konwersja typow: astype, to_numeric, to_datetime | Live coding |
| 0:40-0:50 | **MATERIAL 4** | Operacje na tekstach: str.lower, strip, replace, contains | Live coding |
| 0:50-0:55 | **PRZERWA** | 5 minut | --- |
| 0:55-1:10 | **MATERIAL 5** | Laczenie tabel: merge (inner, left, outer), pd.concat | Live coding |
| 1:10-1:20 | **MATERIAL 6** | Grupowanie: groupby + agg, named aggregation | Live coding |
| 1:20-1:30 | **MATERIAL 7** | Tabele przestawne: pivot_table, pd.crosstab | Live coding |

---

## STENOGRAM --- co mowic i robic

### 0:00-0:05 --- WPROWADZENIE

> "Dzisiaj laczimy dwa kluczowe tematy: czyszczenie danych i ich analize. Na studiach dziennych to sa dwa oddzielne wykłady, ale u nas idziemy szybciej."

> "Przypomnijcie sobie S03 --- umiecic tworzyc DataFrame, filtrowac go, uzywac loc i iloc. To swietnie, ale tamte dane byly czyste. Dzisiaj beda brudne."

> "W branzy mowi sie, ze analityk spedza 60-80% czasu na czyszczeniu danych, a 20-40% na analizie. Wiec to nie jest nudna czesc --- to wiekszosc waszej pracy."

> "Plan: czyszczenie (NaN, duplikaty, typy, tekst) --- potem laczenie tabel (merge), grupowanie (groupby) i tabele przestawne (pivot_table). Na koncu bedziecie mieli kompletny pipeline: od brudnego CSV do raportu dla zarzadu."

**[Wyswietl schemat na tablicy lub projektorze]**

```
Brudne dane
    |
    +-- Brakujace wartosci (NaN)  --> isna / fillna / dropna
    +-- Duplikaty                 --> duplicated / drop_duplicates
    +-- Zle typy                  --> astype / to_numeric / to_datetime
    +-- Brudny tekst              --> str.strip / str.lower / str.replace
    |
Czyste dane
    |
    +-- Laczenie tabel            --> merge / concat
    +-- Grupowanie                --> groupby + agg
    +-- Tabele przestawne         --> pivot_table / crosstab
    |
Raport
```

---

### 0:05-0:20 --- MATERIAL 1: Brakujace wartosci (15 min)

> "Zaczynamy od wczytania brudnego datasetu. To dane z działu HR --- 30 wierszy, duzo problemow. Typowy eksport z systemu ERP."

**[Live coding]**

```python
import pandas as pd
import numpy as np

data = {
    'id_pracownika': [1,2,3,4,5,6,7,8,9,10,
                      11,12,13,14,15,16,17,18,19,20,
                      3,7,12,18,5,
                      21,22,23,24,25],
    'imie': ['Anna', 'Bartek', 'CELINA', 'darek', 'Ewa',
             'Filip', 'Gosia', 'HENRYK', 'irena', 'Jan',
             'Kasia', 'Leszek', 'Marta', 'norbert', 'OLGA',
             'Piotr', 'Renata', 'slawek', 'Teresa', 'Urszula',
             'CELINA', 'Gosia', 'Leszek', 'slawek', 'Ewa',
             'Wanda', 'Xawery', 'Yvonne', 'Zbyszek', 'Agata'],
    'dzial': ['Sprzedaz', 'IT', 'HR', 'sprzedaz', 'IT',
              'HR', 'Sprzedaz', 'it', 'HR', 'Sprzedaz',
              'IT', 'HR', 'sprzedaz', 'IT', 'HR',
              'Sprzedaz', 'it', 'HR', 'Sprzedaz', 'IT',
              'HR', 'Sprzedaz', 'HR', 'HR', 'IT',
              'Sprzedaz', 'IT', 'hr', 'Sprzedaz', 'IT'],
    'wynagrodzenie': ['4500', '6200', '3800', '5100', '7500',
                      '4200', '5800', '6900', '3500', '4800',
                      '7200', '4100', '5500', '6800', '3900',
                      '5200', '4700', '6100', '3800', '5400',
                      '3800', '5800', '4100', '6100', '7500',
                      'brak', '5000', None, '4300', '6600'],
    'data_zatrudnienia': ['2020-03-15', '2019-07-22', '2021-01-10',
                          '2018-05-30', '2022-11-01', '2020-08-14',
                          '2019-12-05', '2021-06-18', '2017-09-23',
                          '2023-02-07', '2020-04-11', '2018-11-28',
                          '2022-07-15', '2019-03-19', '2021-10-08',
                          '2020-06-25', '2018-08-31', '2022-02-14',
                          '2019-05-07', '2021-09-20', '2021-01-10',
                          '2019-12-05', '2018-11-28', '2022-02-14',
                          '2022-11-01', '2023-01-15', '2022-05-20',
                          None, '2020-10-11', '2019-08-03'],
    'ocena_roczna': [4.5, 3.8, None, 4.2, 5.0,
                     3.5, 4.7, None, 4.1, 3.9,
                     5.0, 4.3, 3.6, None, 4.8,
                     3.7, 4.4, 4.9, None, 3.8,
                     None, 4.7, 4.3, 4.9, 5.0,
                     4.6, None, 4.9, 3.5, 4.1]
}

df = pd.DataFrame(data)
print(f"Shape: {df.shape}")
df.head(10)
```

> "30 wierszy, 6 kolumn. Widac pierwsze problemy --- wynagrodzenie to tekst, imiona pisane rozniej. Ale zeby zobaczyc wszystkie problemy, uzyjmy diagnostyki."

```python
# Pierwsza diagnoza
print("=== INFO ===")
df.info()

print("\n=== BRAKUJACE WARTOSCI ===")
print(df.isna().sum())

print("\n=== PROCENT BRAKOW ===")
print((df.isna().sum() / len(df) * 100).round(1))
```

> "`info()` mowi: wynagrodzenie jest typu `object` --- to tekst, nie liczba! `isna().sum()` --- ocena_roczna ma 6 brakow (20%). wynagrodzenie ma 1 brak (None). Ale uwaga --- jedno wynagrodzenie ma wartosc 'brak' zamiast NaN. `isna()` tego nie wykryje."

> "Trzy strategie radzenia sobie z brakami:"

```python
# dropna --- usun wiersze z brakami
df_drop = df.dropna()
print(f"dropna: {len(df)} -> {len(df_drop)} wierszy")

# dropna z subset --- usun tylko jesli NaN w konkretnej kolumnie
df_subset = df.dropna(subset=['data_zatrudnienia'])
print(f"dropna(subset=['data_zatrudnienia']): {len(df_subset)} wierszy")

# fillna --- uzupelnienie wartoscia
df_fill = df.copy()
srednia = df_fill['ocena_roczna'].mean()
df_fill['ocena_roczna'] = df_fill['ocena_roczna'].fillna(srednia)
print(f"fillna(mean={srednia:.2f}): {df_fill['ocena_roczna'].isna().sum()} brakow")
```

> "Kiedy usuwac, a kiedy uzupelniac? Jesli 80% brakow --- usun kolumne. 5% brakow w cenach --- uzupelnij mediana. Kontekst biznesowy decyduje."

> "Wazna zasada: **mediana jest lepsza niz srednia** przy wartosciach odstajacych. CEO z pensja 50 000 psuje srednia, ale nie mediane."

---

### 0:20-0:30 --- MATERIAL 2: Duplikaty (10 min)

> "Drugi wrog czystych danych --- duplikaty. W naszym datasecie 5 pracownikow jest zapisanych dwukrotnie."

```python
# Ile duplikatow?
print(f"Duplikaty: {df.duplicated().sum()}")

# Pokaz zduplikowane wiersze
print(df[df.duplicated()])

# Duplikaty po kluczu (id_pracownika)
print(f"Duplikaty wg id: {df.duplicated(subset=['id_pracownika']).sum()}")
```

> "`duplicated()` domyslnie oznacza DRUGI i kolejne wystapienia. `keep=False` oznacza WSZYSTKIE. `subset=` sprawdza duplikaty tylko po wybranych kolumnach."

```python
# Usun duplikaty
df_clean = df.drop_duplicates().reset_index(drop=True)
print(f"Przed: {len(df)}, po: {len(df_clean)}")
```

> "Zawsze `reset_index(drop=True)` po usunieciu wierszy. Inaczej indeks ma dziury: 0, 1, 2, ..., 19, 25, 26..."

---

### 0:30-0:40 --- MATERIAL 3: Konwersja typow (10 min)

> "Trzecia kategoria: zle typy. Wynagrodzenie jako string, daty jako tekst. Pandas nie policzy sredniej ze stringow."

```python
# Problem: wynagrodzenie to tekst
df_work = df.drop_duplicates().reset_index(drop=True).copy()
print(f"Typ wynagrodzenia: {df_work['wynagrodzenie'].dtype}")

# astype(float) wywali blad jesli jest 'brak'
try:
    df_work['wynagrodzenie'].astype(float)
except ValueError as e:
    print(f"Blad: {e}")

# Rozwiazanie 1: replace + to_numeric
df_work['wynagrodzenie'] = df_work['wynagrodzenie'].replace('brak', np.nan)
df_work['wynagrodzenie'] = pd.to_numeric(df_work['wynagrodzenie'], errors='coerce')
print(f"Typ po to_numeric: {df_work['wynagrodzenie'].dtype}")
print(f"Srednie wynagrodzenie: {df_work['wynagrodzenie'].mean():.2f}")
```

> "`pd.to_numeric(errors='coerce')` --- kluczowy parametr. Zamiast bledu dla wartosci niemozliwych do konwersji, wstawia NaN. Analogicznie `pd.to_datetime(errors='coerce')` dla dat."

```python
# Konwersja dat
df_work['data_zatrudnienia'] = pd.to_datetime(
    df_work['data_zatrudnienia'], errors='coerce'
)
print(f"Typ daty: {df_work['data_zatrudnienia'].dtype}")

# .dt accessor --- rok, miesiac, dzien
df_work['rok'] = df_work['data_zatrudnienia'].dt.year
print(f"Lata: {sorted(df_work['rok'].dropna().unique().astype(int))}")
```

> "Po konwersji na datetime mozecie uzywac `.dt.year`, `.dt.month`, `.dt.dayofweek`. To otwiera analizy temporalne."

---

### 0:40-0:50 --- MATERIAL 4: Operacje na tekstach (10 min)

> "Ostatni obszar czyszczenia: brudny tekst. Dane z formularzy, eksportow --- literowki, wielkie litery, spacje. Pandas ma accessor `.str` z zestawem metod."

```python
# str.lower(), str.upper(), str.title()
print("Imiona RAW:", df['imie'].head(5).tolist())
print("str.title():", df['imie'].str.title().head(5).tolist())

# str.strip() --- spacje
test = pd.Series(['  Anna  ', 'Bartek ', ' CELINA'])
print("str.strip():", test.str.strip().tolist())
```

> "`.str` accessor --- kazda metoda stringowa Pythona dziala na calej kolumnie. Nie musicie pisac petli for."

```python
# Normalizacja dzialow
df_work['dzial'] = df_work['dzial'].str.strip().str.title()
print("Po title():", df_work['dzial'].unique())

# str.replace --- zamiana tekstu
df_work['dzial'] = df_work['dzial'].str.replace('Hr', 'HR', regex=False)
df_work['dzial'] = df_work['dzial'].str.replace('It', 'IT', regex=False)
print("Po replace:", sorted(df_work['dzial'].unique()))
# Wynik: ['HR', 'IT', 'Sprzedaz']
```

> "`str.contains()` to filtrowanie po zawartosci. `str.replace()` z `regex=False` szuka dokladnego tekstu. Przy `regex=True` mozecie uzywac wyrazen regularnych."

```python
# str.contains --- filtrowanie
sprzedaz = df_work[df_work['dzial'].str.contains('Sprzedaz', na=False)]
print(f"Pracownicy w Sprzedazy: {len(sprzedaz)}")
```

---

### 0:50-0:55 --- PRZERWA (5 min)

---

### 0:55-1:10 --- MATERIAL 5: Laczenie tabel --- merge i concat (15 min)

> "Teraz dane sa czyste. Ale w prawdziwym zyciu dane sa rozrzucone po wielu tabelach. Tabela zamowien, tabela klientow, tabela produktow. Osobno to fragmenty. Razem --- pelna analiza."

> "Przesiadziemy sie na inny dataset --- sklep internetowy TechShop. Trzy tabele, jak w prawdziwym e-commerce."

```python
# Tabela klientow
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

# Tabela zamowien
zamowienia = pd.DataFrame({
    'id': range(1, 21),
    'data': pd.to_datetime([
        '2024-01-05', '2024-01-12', '2024-01-15', '2024-01-20',
        '2024-02-03', '2024-02-08', '2024-02-14', '2024-02-19',
        '2024-03-01', '2024-03-07', '2024-03-12', '2024-03-18',
        '2024-04-02', '2024-04-09', '2024-04-15', '2024-04-22',
        '2024-05-05', '2024-05-11', '2024-05-18', '2024-05-25'
    ]),
    'klient_id': [1, 2, 3, 4, 5, 1, 6, 7, 8, 2,
                  3, 9, 10, 1, 4, 5, 6, 7, 8, 9],
    'produkt': ['Laptop', 'Mysz', 'Monitor', 'Klawiatura',
                'Sluchawki', 'Kamera', 'Laptop', 'Mysz', 'Monitor',
                'Pendrive', 'Klawiatura', 'Sluchawki', 'Tablet',
                'Mysz', 'Kamera', 'Laptop', 'Monitor', 'Pendrive',
                'Sluchawki', 'Klawiatura'],
    'kategoria': ['Komputery', 'Akcesoria', 'Komputery', 'Akcesoria',
                  'Audio', 'Akcesoria', 'Komputery', 'Akcesoria',
                  'Komputery', 'Storage', 'Akcesoria', 'Audio',
                  'Komputery', 'Akcesoria', 'Akcesoria', 'Komputery',
                  'Komputery', 'Storage', 'Audio', 'Akcesoria'],
    'cena': [3999.99, 89.99, 1299.99, 249.99,
             399.99, 199.99, 3999.99, 89.99, 1299.99,
             49.99, 249.99, 399.99, 1499.99,
             89.99, 199.99, 3999.99, 1299.99, 49.99,
             399.99, 249.99],
    'ilosc': [1, 2, 1, 1, 1, 1, 1, 3, 1, 5,
              2, 1, 2, 1, 2, 1, 1, 2, 1, 3]
})

print(f"Klienci: {len(klienci)} wierszy")
print(f"Zamowienia: {len(zamowienia)} wierszy")
```

> "Zamowien jest 20, klientow 10. W zamowieniach jest klient_id --- to klucz laczacy obie tabele. Merge dziala jak JOIN w SQL."

```python
# Podstawowy merge --- inner (domyslny)
pelne = zamowienia.merge(
    klienci,
    left_on='klient_id',
    right_on='id',
    how='inner',
    suffixes=('_zam', '_kl')
)
print(f"Po merge: {pelne.shape}")
pelne[['id_zam', 'data', 'imie', 'miasto', 'produkt', 'cena', 'ilosc']].head(5)
```

> "Cztery typy merge --- inner (tylko wspólne), left (wszystko z lewej + pary), right, outer (wszystko z obu). Kluczowa zasada: **inner gdy chcemy tylko kompletne dane, left gdy lewa tabela jest bazowa**."

```python
# Ilustracja 4 typow
A = pd.DataFrame({'id': [1, 2, 3], 'nazwa': ['X', 'Y', 'Z']})
B = pd.DataFrame({'id': [2, 3, 4], 'cena': [10, 20, 30]})

for how in ['inner', 'left', 'outer']:
    r = A.merge(B, on='id', how=how)
    print(f"{how:6s}: {len(r)} wierszy -> {r['id'].tolist()}")
```

> "Inner: 2 wiersze (id 2, 3). Left: 3 wiersze (id 1 z NaN cena). Outer: 4 wiersze (id 1 bez ceny, id 4 bez nazwy)."

```python
# concat --- sklejanie tabel o tych samych kolumnach
q1 = pd.DataFrame({'miesiac': ['Styczen', 'Luty'], 'sprzedaz': [45000, 39000]})
q2 = pd.DataFrame({'miesiac': ['Marzec', 'Kwiecien'], 'sprzedaz': [52000, 48000]})

polrocze = pd.concat([q1, q2], ignore_index=True)
print(polrocze)
```

> "Merge laczy po kluczu --- poziomo, dodaje kolumny. Concat klei --- pionowo, dodaje wiersze. Typowy case: dane za styczen + luty z tego samego raportu."

---

### 1:10-1:20 --- MATERIAL 6: Grupowanie --- groupby (10 min)

> "Mamy kompletna tabele. Teraz wyciagamy z niej wiedze --- nie wiersz po wierszu, ale zagregowana. Groupby dziala wg wzorca: Split-Apply-Combine."

```python
# Dodaj wartosc zamowienia
pelne['wartosc'] = pelne['ilosc'] * pelne['cena']

# Podstawowy groupby --- sprzedaz per miasto
sprzedaz_miasto = pelne.groupby('miasto')['wartosc'].sum().sort_values(ascending=False)
print("Sprzedaz per miasto:")
print(sprzedaz_miasto)
```

> "Wynik to Series z indeksem bedacym wartosciami grupy. Warszawa lideruje."

```python
# Wiele funkcji jednoczesnie --- agg()
stats = pelne.groupby('kategoria')['wartosc'].agg(['sum', 'mean', 'count'])
print("\nStatystyki per kategoria:")
print(stats.round(2))
```

> "`.agg()` pozwala zastosowac kilka funkcji naraz. Komputery dominuja --- 6 zamowien o lacznej wartosci prawie 16 000 zl."

```python
# Nazwana agregacja --- czytelne kolumny wynikowe
raport = pelne.groupby('segment').agg(
    liczba_zamowien=('id_zam', 'count'),
    laczna_wartosc=('wartosc', 'sum'),
    srednia_wartosc=('wartosc', 'mean'),
    max_zamowienie=('wartosc', 'max')
).round(2)
print("\nRaport segmentow:")
print(raport)
```

> "Nazwana agregacja: `nazwa_kolumny=('zrodlo', 'funkcja')`. W kodzie produkcyjnym **zawsze tak** --- kolumna 'sum' nic nie mowi, 'laczna_wartosc' juz tak."

---

### 1:20-1:30 --- MATERIAL 7: Tabele przestawne --- pivot_table i crosstab (10 min)

> "pivot_table to deklaratywny sposob na to, co robil groupby + unstack. Jesli znacie tabele przestawne z Excela --- to dokladnie to samo."

```python
# Tabela przestawna: segment x kategoria
pivot = pd.pivot_table(
    pelne,
    values='wartosc',     # co agregujemy
    index='segment',      # wiersze
    columns='kategoria',  # kolumny
    aggfunc='sum',        # funkcja
    fill_value=0,         # NaN -> 0
    margins=True          # sumy brzegowe
)
print("Sprzedaz: Segment x Kategoria [PLN]")
print(pivot.round(2))
```

> "Margins=True dodaje wiersz i kolumne 'All' z sumami. To gotowy format raportowy --- mozecie wyeksportowac do Excela i pokazac szefowi."

```python
# crosstab --- liczy wystapienia (liczebnosci)
ct = pd.crosstab(
    pelne['segment'],
    pelne['miasto'],
    margins=True
)
print("\nLiczba zamowien: Segment x Miasto")
print(ct)

# Z normalizacja --- procenty per wiersz
ct_pct = pd.crosstab(
    pelne['segment'],
    pelne['miasto'],
    normalize='index'
)
print("\nUdzialy procentowe per segment:")
print((ct_pct * 100).round(1))
```

> "crosstab liczy ile razy wystepuje kombinacja dwoch zmiennych. Normalize='index' zamienia na procenty per wiersz."

> "I to tyle --- od brudnych danych, przez czyszczenie, laczenie tabel, grupowanie, az do gotowego raportu."

---

### 1:27-1:30 --- AKTYWNOŚĆ — Mini-quiz (3 min)

> **Prowadzący mówi:** "Zanim podsumujemy — szybki quiz. Odpowiedzcie na kartce lub w parach."

1. Jaka jest roznica miedzy `merge(how='inner')` a `merge(how='left')`? Kiedy uzyjesz ktorego?
2. Co zwraca `df.groupby('dzial')['wynagrodzenie'].mean()` — Series czy DataFrame?
3. Napisz jedno zdanie: czemu `fillna(mediana)` jest lepsze niz `fillna(srednia)` dla wynagrodzen?

> **[Po 2 min]** "Kto chce odpowiedzieć? [Omów odpowiedzi: 1) inner = tylko wspólne klucze, left = wszystko z lewej + dopasowania z prawej (NaN gdzie brak); 2) Series z indeksem = nazwy działów; 3) Mediana jest odporna na outliery — jeden prezes z pensją 200 tys. nie zaburza mediany, ale zaburza średnią]"

---

### 1:30 --- PODSUMOWANIE

> "Podsumujmy. Dzis przeszlismy pelny pipeline: od brudnych danych do raportu."

> "**Czyszczenie:** `isna()` + `fillna()` / `dropna()` — braki. `drop_duplicates()` — duplikaty. `pd.to_numeric(errors='coerce')` — zle typy. `str.strip().str.title()` — brudny tekst."

> "**Laczenie:** `merge()` — laczy po kluczu (jak JOIN w SQL). `concat()` — klei tabele pionowo."

> "**Agregacja:** `groupby()` + `agg()` — Split-Apply-Combine. Nazwana agregacja daje czytelne kolumny."

> "**Tabele przestawne:** `pivot_table()` — deklaratywny groupby + reshape. `crosstab()` — liczebnosci."

> "Na laboratorium bedziecie robic to sami na datasecie e-commerce. Gotowi? Przerwa 5 minut i zaczynamy lab."

---

## Notatki i wskazowki dla prowadzacego

### Tempo zaoczne vs dzienne
- Na dziennych to sa 2 osobne wyklady (W07 + W08, kazdy 90 min). Tu masz 90 min na oba tematy.
- Skupiaj sie na **kluczowych koncepcjach**, nie na wariacjach. Np. fillna --- pokaz 2 strategie (mediana i srednia), nie 4.
- Duplikaty --- szybko, 10 min, bez szczegolowego omowienia keep=False.
- Merge --- pokaz inner i left, wzmiankuj outer. Right mozna pominac.

### Czas na zywo
- Jesli studentom idzie wolniej --- pominac crosstab z normalizacja. Wroca do tego na labach.
- Przerwa 5 min (nie 10) --- studia zaoczne, czas jest cenny.

### Pytania kontrolne (mozna zadawac w trakcie)
- "Czemu mediana jest lepsza niz srednia dla wynagrodzen?"
- "Kiedy merge inner, a kiedy left?"
- "Co zrobi groupby bez funkcji agregujcej?"

### Typowe bledy studentow
| Blad | Reakcja |
|------|---------|
| `astype(float)` na kolumnie z 'brak' | "Uzyj `pd.to_numeric(errors='coerce')` --- bezpieczne" |
| Merge po zlym kluczu | "Sprawdz left_on i right_on --- musza wskazywac te same dane" |
| groupby daje Series zamiast DataFrame | "Dodaj `.reset_index()` na koncu" |
| pivot_table z NaN zamiast 0 | "Dodaj `fill_value=0`" |
