# W08 Laboratorium — Ćwiczenia

## Pandas: łączenie i agregacja

**Czas:** 90 minut
**Notebook:** utwórz nowy plik `W08_lab.ipynb` w VS Code
**Dataset:** sklep TechShop — trzy tabele: klienci, produkty, zamówienia
**Commit:** na końcu zajęć wykonaj `git commit -m "W08: merge, groupby, pivot"`

---

## Przydatne materiały

| Temat | Link |
|-------|------|
| Pandas — `merge()` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html |
| Pandas — `concat()` | https://pandas.pydata.org/docs/reference/api/pandas.concat.html |
| Pandas — `groupby()` | https://pandas.pydata.org/docs/user_guide/groupby.html |
| Pandas — `pivot_table()` | https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html |
| Pandas — Merge, join, concatenate guide | https://pandas.pydata.org/docs/user_guide/merging.html |

### Typy łączenia (`merge`) — wizualnie

| `how=` | Co robi | Wynik |
|--------|---------|-------|
| `'inner'` | Tylko wspólne klucze | A ∩ B |
| `'left'` | Wszystko z lewej + pasujące z prawej | A + (A ∩ B) |
| `'right'` | Wszystko z prawej + pasujące z lewej | (A ∩ B) + B |
| `'outer'` | Wszystko z obu tabel | A ∪ B |

Przykład: jeśli klient złożył zamówienie ale nie ma go w tabeli klientów → `inner` go pominie, `left` zachowa zamówienie z NaN w danych klienta.

---

## Dane startowe — wklej jako pierwszą komórkę notebooka

```python
import pandas as pd
import numpy as np

# --- DANE STARTOWE ---
klienci = pd.DataFrame({
    'id': range(1, 11),
    'imie': ['Anna Kowalska', 'Piotr Nowak', 'Maria Wiśniewska', 'Jan Kowalczyk',
             'Katarzyna Zielińska', 'Tomasz Lewandowski', 'Agnieszka Wójcik',
             'Michał Kamiński', 'Ewa Kaczmarek', 'Robert Szymański'],
    'miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań',
               'Warszawa', 'Łódź', 'Kraków', 'Gdańsk', 'Wrocław'],
    'segment': ['VIP', 'Standard', 'VIP', 'Standard', 'Premium',
                'Premium', 'Standard', 'VIP', 'Standard', 'Premium']
})

produkty = pd.DataFrame({
    'id': range(1, 9),
    'nazwa': ['Laptop ProX', 'Mysz bezprzewodowa', 'Monitor 27"', 'Klawiatura mechaniczna',
              'Słuchawki BT', 'Webcam HD', 'Pendrive 128GB', 'Hub USB-C'],
    'kategoria': ['Komputery', 'Akcesoria', 'Komputery', 'Akcesoria',
                  'Audio', 'Akcesoria', 'Storage', 'Akcesoria'],
    'cena': [3999.99, 89.99, 1299.99, 249.99, 399.99, 199.99, 49.99, 149.99]
})

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
    'produkt_id': [1, 2, 3, 4, 5, 6, 1, 2, 3, 7,
                   4, 5, 8, 2, 6, 1, 3, 7, 5, 4],
    'ilosc': [1, 2, 1, 1, 1, 1, 1, 3, 1, 5, 2, 1, 2, 1, 2, 1, 1, 2, 1, 3]
})

print("Dane załadowane.")
print(f"klienci: {klienci.shape}, produkty: {produkty.shape}, zamowienia: {zamowienia.shape}")
```

---

## Ćwiczenie 1: merge — łączenie tabel (20 min)

**Cel:** Połączyć trzy tabele w jeden kompletny widok danych sprzedaży.

### Zadanie 1.1 — Prosty merge (zamówienia + klienci)

Połącz tabelę `zamowienia` z tabelą `klienci` za pomocą merge. Klucz to `klient_id` w zamówieniach i `id` w klientach.

```python
# Uzupełnij: ??? to miejsce na twój kod
zam_kl = zamowienia.merge(
    klienci,
    left_on=???       # klucz w tabeli zamowienia
    right_on=???      # klucz w tabeli klienci
    how='inner',
    suffixes=('_zam', '_kl')
)
print(f"Wynik: {zam_kl.shape}")
print(zam_kl[['id_zam', 'data', 'imie', 'miasto', 'segment', 'ilosc']].head(5))
```

**Sprawdzenie 1.1** ✅
Wynik powinien mieć **20 wierszy**. Jeśli masz inną liczbę — sprawdź klucze.

---

### Zadanie 1.2 — Łańcuchowy merge (trzy tabele)

Dołącz teraz tabelę `produkty` do wyniku z 1.1. Klucz: `produkt_id` → `id`.
Następnie dodaj kolumnę `wartosc = ilosc * cena`.

```python
kompletne = (
    zamowienia
    .merge(klienci, left_on='klient_id', right_on='id', suffixes=('_zam', '_kl'))
    .merge(???)  # dołącz produkty po produkt_id
)

# Dodaj kolumnę wartości
kompletne['wartosc'] = ???  # ilosc * cena

# Wyświetl kluczowe kolumny
kolumny = ['id_zam', 'data', 'imie', 'miasto', 'segment', 'nazwa', 'kategoria', 'cena', 'ilosc', 'wartosc']
print(kompletne[kolumny].head(5))
print(f"\nŁączna wartość sprzedaży: {kompletne['wartosc'].sum():.2f} zł")
```

**Sprawdzenie 1.2** ✅
- Łączna wartość sprzedaży: **20 389,67 zł**
- Kształt tabeli: **(20, 14)**

---

### Zadanie 1.3 — Typy złączeń (eksploracja)

Stwórz dwie dodatkowe tabele i sprawdź różnicę między inner/left/outer:

```python
# Symulacja: co jeśli klient_id=99 nie istnieje w klientach?
zamowienia_test = zamowienia.copy()
zamowienia_test.loc[0, 'klient_id'] = 99  # nieistniejący klient

# inner
wynik_inner = zamowienia_test.merge(klienci, left_on='klient_id', right_on='id', how='inner')
# left
wynik_left = zamowienia_test.merge(klienci, left_on='klient_id', right_on='id', how='left')

print(f"Inner: {len(wynik_inner)} wierszy (zamówienie klienta 99 znikło)")
print(f"Left:  {len(wynik_left)} wierszy (zamówienie klienta 99 zostało z NaN)")

# Sprawdź wiersz z NaN
print("\nWiersz z brakującym klientem:")
print(wynik_left[wynik_left['imie'].isna()][['id_x', 'klient_id', 'imie', 'miasto']])
```

**Sprawdzenie 1.3** ✅
- Inner: **19 wierszy** (jedno zamówienie "zniknęło" bo klient 99 nie istnieje)
- Left: **20 wierszy** (jedno zamówienie ma NaN w polach klienta)

---

### Wyzwanie dodatkowe (jeśli skończyłeś wcześniej)
Znajdź klientów, którzy **NIE złożyli żadnego zamówienia** (outer merge + filtrowanie NaN).

```python
# Wskazówka: użyj how='right' lub how='outer' i poszukaj NaN w kolumnie 'id_zam'
brak_zamowien = klienci.merge(zamowienia, left_on='id', right_on='klient_id', how='left')
bez_zamowienia = brak_zamowien[brak_zamowien['id_y'].isna()]
print(f"Klienci bez zamówień: {len(bez_zamowienia)}")
print(bez_zamowienia[['id_x', 'imie', 'miasto', 'segment']])
```

---

## Ćwiczenie 2: groupby — agregacja KPI (20 min)

**Cel:** Obliczyć kluczowe wskaźniki sprzedaży (KPI) za pomocą groupby i agg.

Używaj tabeli `kompletne` z Ćwiczenia 1.

### Zadanie 2.1 — Sprzedaż per miasto

```python
# Oblicz łączną sprzedaż per miasto, posortuj malejąco
sprzedaz_miasto = ???

print("Sprzedaż per miasto [PLN]:")
print(sprzedaz_miasto)
```

**Sprawdzenie 2.1** ✅
Kolejność miast (od największej sprzedaży): **Warszawa, Poznań, Gdańsk, Kraków, Wrocław, Łódź**
Warszawa: **9 589,95 zł**

---

### Zadanie 2.2 — Raport kategorii produktów (agg)

Stwórz raport kategorii używając `.agg()`. Oblicz jednocześnie: liczbę zamówień, łączną sprzedaż i średnią wartość.

```python
raport_kategorii = kompletne.groupby('kategoria').agg(
    liczba_zamowien=???,   # ('id_zam', 'count')
    laczna_sprzedaz=???,   # ('wartosc', 'sum')
    srednia_wartosc=???    # ('wartosc', 'mean')
).round(2)

print("Raport kategorii:")
print(raport_kategorii.sort_values('laczna_sprzedaz', ascending=False))
```

**Sprawdzenie 2.2** ✅
| Kategoria | Zamówienia | Sprzedaż | Średnia |
|-----------|-----------|----------|---------|
| Komputery | 6 | 15 899,94 | 2 649,99 |
| Akcesoria | 9 | 2 939,83 | 326,65 |
| Audio | 3 | 1 199,97 | 399,99 |
| Storage | 2 | 349,93 | 174,96 |

---

### Zadanie 2.3 — Raport segmentów klientów (named aggregation)

Stwórz pełny raport segmentów z czterema wskaźnikami: liczba zamówień, łączna wartość, średnia wartość, maksymalne zamówienie.

```python
raport_segmentow = kompletne.groupby('segment').agg(
    ???  # użyj named aggregation: nazwa=('kolumna', 'funkcja')
).round(2)

print("Raport segmentów klientów:")
print(raport_segmentow)
```

**Sprawdzenie 2.3** ✅
| Segment | Zamówienia | Łącznie | Średnia | Max |
|---------|-----------|---------|---------|-----|
| Premium | 5 | 9 999,94 | 1 999,99 | 3 999,99 |
| Standard | 8 | 2 599,81 | 324,98 | 749,97 |
| VIP | 7 | 7 789,92 | 1 112,85 | 3 999,99 |

---

### Zadanie 2.4 — Groupby po dwóch kolumnach

Oblicz sprzedaż per **miasto i kategoria** jednocześnie. Następnie użyj `.unstack()` żeby uzyskać tabelę 2D.

```python
sprzedaz_2d = (
    kompletne
    .groupby([???, ???])['wartosc']  # dwie kolumny grupowania
    .sum()
    .round(2)
    .unstack(fill_value=0)
)
print("Sprzedaż per miasto i kategoria:")
print(sprzedaz_2d)
```

**Sprawdzenie 2.4** ✅
Warszawa → Komputery: **9 299,97 zł**
Gdańsk → Akcesoria: **1 249,95 zł**
Łódź → Komputery: **0,00 zł** (brak zamówień)

---

### Wyzwanie dodatkowe
Oblicz jaki procent łącznej sprzedaży stanowi każde miasto. Wskazówka: `transform('sum')`.

```python
kompletne['pct_sprzedazy'] = (
    kompletne['wartosc'] / kompletne.groupby('miasto')['wartosc'].transform('sum') * 100
).round(1)
# ... pokaż wynik
```

---

## Ćwiczenie 3: Pełna analiza — merge + groupby + pivot (30 min)

**Cel:** Przeprowadzić samodzielnie pełną analizę sprzedaży sklep TechShop i odpowiedzieć na pytania zarządu.

To jest ćwiczenie **samodzielne** — spróbuj przez 10 minut sam zanim poprosisz o pomoc.

---

### Zadanie 3.1 — Top 5 produktów wg przychodu

Który produkt zarobił dla sklepu najwięcej? Oblicz łączny przychód per produkt i pokaż top 5.

```python
# Twój kod:
top_produkty = ???

print("Top 5 produktów wg przychodu:")
print(top_produkty)
```

**Sprawdzenie 3.1** ✅
Nr 1: **Laptop ProX** z przychodem **11 999,97 zł**
Nr 2: **Monitor 27"** z przychodem **3 899,97 zł**
Nr 3: **Klawiatura mechaniczna** z przychodem **1 499,94 zł**

---

### Zadanie 3.2 — Trend miesięczny sprzedaży

Oblicz łączną sprzedaż per miesiąc. Wyodrębnij numer miesiąca z kolumny `data`.

```python
# Wyodrębnij miesiąc
kompletne['miesiac'] = kompletne['data'].dt.month

# Oblicz sprzedaż per miesiąc
sprzedaz_miesiec = ???

print("Sprzedaż miesięczna [PLN]:")
print(sprzedaz_miesiec)
```

**Sprawdzenie 3.2** ✅
| Miesiąc | Sprzedaż |
|---------|---------|
| 1 (Styczeń) | 5 729,95 |
| 2 (Luty) | 4 869,94 |
| 3 (Marzec) | 2 449,91 |
| 4 (Kwiecień) | 4 789,94 |
| 5 (Maj) | 2 549,93 |

Najlepszy miesiąc: **Styczeń** (5 729,95 zł)

---

### Zadanie 3.3 — Profil klienta VIP

Wyfiltruj tylko zamówienia klientów VIP i oblicz:
- Ile zamówień złożyli łącznie?
- Jaka jest ich średnia wartość zamówienia?
- Jakie produkty kupują najczęściej?

```python
# Filtrowanie klientów VIP
vip = kompletne[kompletne['segment'] == 'VIP']

print(f"Liczba zamówień VIP: {???}")
print(f"Średnia wartość zamówienia VIP: {vip['wartosc'].mean():.2f} zł")
print(f"Łączna wartość zakupów VIP: {vip['wartosc'].sum():.2f} zł")
print()
print("Produkty kupowane przez VIP:")
print(???)  # groupby po nazwie, count lub sum wartości
```

**Sprawdzenie 3.3** ✅
- Liczba zamówień VIP: **7**
- Średnia wartość: **1 112,85 zł**
- Łączna wartość: **7 789,92 zł**

---

### Zadanie 3.4 — Klient miesiąca

Znajdź klienta z największą łączną wartością zakupów w całym analizowanym okresie.

```python
klient_roku = (
    kompletne
    .groupby(['imie', 'segment'])['wartosc']
    .sum()
    .round(2)
    .sort_values(ascending=False)
    .reset_index()
)
print("Top 5 klientów wg wartości zakupów:")
print(klient_roku.head(5))
```

**Sprawdzenie 3.4** ✅
Klient #1: **Anna Kowalska** (VIP, Warszawa)
Jej łączna wartość zakupów: **4 289,97 zł**
*Zamówienia Anny: Laptop ProX (3 999,99) + Webcam HD (199,99) + Mysz bezprzewodowa (89,99)*

---

## Ćwiczenie 4: pivot_table + crosstab + commit (15 min)

**Cel:** Stworzyć gotowe raporty tabelaryczne z sumami brzegowymi.

### Zadanie 4.1 — Tabela przestawna: segment × kategoria

Zbuduj tabelę przestawną pokazującą sprzedaż [PLN] dla każdej kombinacji segment × kategoria. Dodaj sumy brzegowe.

```python
pivot_seg_kat = pd.pivot_table(
    kompletne,
    values='wartosc',
    index=???,          # segment → wiersze
    columns=???,        # kategoria → kolumny
    aggfunc='sum',
    fill_value=0,
    margins=???         # True = sumy brzegowe
)

print("Sprzedaż [PLN]: Segment × Kategoria")
print(pivot_seg_kat.round(2))
```

**Sprawdzenie 4.1** ✅
| | Akcesoria | Audio | Komputery | Storage | All |
|--|-----------|-------|-----------|---------|-----|
| **Premium** | 299,98 | 399,99 | 9 299,97 | 0,00 | 9 999,94 |
| **Standard** | 1 849,89 | 399,99 | 0,00 | 349,93 | 2 599,81 |
| **VIP** | 789,96 | 399,99 | 6 599,97 | 0,00 | 7 789,92 |
| **All** | 2 939,83 | 1 199,97 | 15 899,94 | 349,93 | 20 389,67 |

---

### Zadanie 4.2 — pivot_table: miesiąc × kategoria

Zbuduj tabelę przestawną z miesiącami w wierszach i kategoriami w kolumnach.

```python
pivot_czas = pd.pivot_table(
    kompletne,
    values='wartosc',
    index='miesiac',
    columns='kategoria',
    aggfunc=???,        # suma
    fill_value=0,
    margins=True
)
print("Sprzedaż miesięczna per kategoria [PLN]:")
print(pivot_czas.round(2))
```

**Sprawdzenie 4.2** ✅
Styczeń (miesiac=1) × Komputery: **5 299,98 zł**
Marzec (miesiac=3) × Audio: **399,99 zł**

---

### Zadanie 4.3 — crosstab: segment × miasto

Policz ile zamówień złożyli klienci z poszczególnych miast według segmentu. Użyj `normalize='index'` żeby zobaczyć procenty.

```python
# Liczebności
ct_liczby = pd.crosstab(
    kompletne['segment'],
    kompletne['miasto'],
    margins=True
)
print("Liczba zamówień: Segment × Miasto")
print(ct_liczby)
print()

# Procenty per wiersz (jak dany segment rozkłada się po miastach)
ct_pct = pd.crosstab(
    kompletne['segment'],
    kompletne['miasto'],
    normalize=???       # 'index' = procenty per wiersz (segment)
)
print("Udziały procentowe per segment:")
print((ct_pct * 100).round(1))
```

**Sprawdzenie 4.3** ✅
- VIP × Warszawa: **3 zamówienia**
- Standard × Kraków: **2 zamówienia**
- Premium × Poznań: **2 zamówienia**
- crosstab VIP %: Warszawa = **42,9%**, Kraków = **28,6%**, Gdańsk = **28,6%**

---

### Zadanie 4.4 — Commit na GitHub

Zapisz notebook i wykonaj commit.

```bash
# W terminalu VS Code (Ctrl+`)
git add W08_lab.ipynb
git commit -m "W08: merge, groupby, pivot_table — ćwiczenia"
git push
```

Sprawdź na GitHub czy commit jest widoczny. Pokaż prowadzącemu link do swojego commita.

---

## Podsumowanie — co dziś zrobiłeś

```
merge()          → łączenie tabel po kluczu relacyjnym
  ├── inner      → tylko wspólne (SQL: INNER JOIN)
  ├── left       → wszystkie z lewej + pary z prawej
  ├── right      → wszystkie z prawej + pary z lewej
  └── outer      → wszystkie z obu tabel

pd.concat()      → sklejanie tabel o tych samych kolumnach (SQL: UNION)

groupby()        → agregacja po grupach (SQL: GROUP BY)
  ├── .sum()     → suma
  ├── .mean()    → średnia
  ├── .count()   → liczenie
  ├── .agg()     → wiele funkcji naraz
  └── .transform() → wartość grupowa w każdym wierszu

pd.pivot_table() → tabela przestawna (deklaratywnie)
pd.crosstab()    → tabela liczebności / częstości
```

### Wymagania do zaliczenia laboratorium W08
- [ ] Ćwiczenie 1: merge trzech tabel + wartość 20 389,67 zł
- [ ] Ćwiczenie 2: raport kategorii z named aggregation
- [ ] Ćwiczenie 3: samodzielna analiza — top produkty + trend miesięczny
- [ ] Ćwiczenie 4: pivot_table z margins + crosstab z normalize
- [ ] Commit na GitHub z komunikatem zawierającym "W08"

---

## Jeśli utkniesz

| Problem | Rozwiązanie |
|---------|-------------|
| `MergeError: columns overlap` | Tabele mają kolumny o tych samych nazwach. Użyj `suffixes=('_left', '_right')` |
| Po merge za dużo/za mało wierszy | Sprawdź typ merge: `how='inner'` wycina, `how='left'` zachowuje. Sprawdź duplikaty w kluczu |
| `groupby()` nie pokazuje wszystkich kolumn | `groupby()` domyślnie pokazuje tylko grupowane i agregowane kolumny. Dodaj `as_index=False` |
| `pivot_table` — ValueError | Sprawdź czy `values=`, `index=`, `columns=` wskazują na istniejące kolumny |
| `agg()` — nie wiem jak podać wiele funkcji | `df.groupby('kol').agg({'cena': ['mean', 'sum'], 'ilość': 'count'})` |
| Wynik groupby ma MultiIndex | Spłaszcz: `df.columns = ['_'.join(col) for col in df.columns]` lub użyj named agg |
