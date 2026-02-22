# S03 Wykład zaoczny — Plan zajęć dla prowadzącego

## Temat: Pandas — od DataFrame do precyzyjnych pytań o danych

### Informacje organizacyjne
- **Czas:** 90 min (wykład, pierwsza polowa spotkania S03)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z pandas/numpy
- **Kontekst zaoczny:** wykład + lab = 180 min, prowadzi ta sama osoba
- **Treść:** W05 (Pandas intro) + W06 (selekcja i filtrowanie) — skondensowane

### Efekty uczenia sie (Bloom)
Po tym wykladzie osoba studiujaca:
1. **Tworzy** Series i DataFrame z dict, listy i pliku CSV (Bloom 3)
2. **Stosuje** metody eksploracyjne: info(), describe(), head(), value_counts() (Bloom 3)
3. **Rozroznia** loc (etykiety) i iloc (pozycje) i stosuje je poprawnie (Bloom 2-3)
4. **Filtruje** dane z warunkami logicznymi (&, |, ~, isin, between, query) (Bloom 3)
5. **Analizuje** dane odpowiadajac na pytania biznesowe (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **WPROWADZENIE** | NumPy -> Pandas, plan spotkania | Rozmowa |
| 0:05-0:20 | **MATERIAL 1** | Series i DataFrame — tworzenie, atrybuty | Live coding |
| 0:20-0:35 | **MATERIAL 2** | read_csv, EDA: info, describe, value_counts | Live coding |
| 0:35-0:45 | **PRZERWA** | 10 minut | -- |
| 0:45-1:05 | **MATERIAL 3** | loc, iloc — selekcja wierszy i kolumn | Live coding |
| 1:05-1:20 | **MATERIAL 4** | Filtrowanie, isin, between, query, sortowanie | Live coding |
| 1:20-1:30 | **MATERIAL 5** | Nowe kolumny, segmentacja, podsumowanie | Live coding + rozmowa |

---

## STENOGRAM — co mowic i robic

### 0:00-0:05 — WPROWADZENIE

> "Na S02 poznaliscie NumPy — szybkie tablice liczbowe. NumPy jest potezny, ale ma jeden problem."

**[Wpisz w notebook na zywo]**

```python
import numpy as np

sprzedaz = np.array([340, 120, 560, 90, 420])
print(sprzedaz)
# [340 120 560  90 420]
```

> "Patrze na to i pytam: 340 czego? Ktory to produkt? Ktory miesiac? NumPy nie wie. Ma tylko liczby. Zadnych etykiet, zadnych nazw kolumn."

> "**Pandas** rozwiazuje ten problem. Pandas to NumPy z etykietami. Pod spodem — te same tablice. Na wierzchu — nazwy kolumn, indeksy wierszy, metody do wczytywania CSV, czyszczenia, filtrowania, grupowania."

> "Pandas to **narzedzie numer jeden** analityka danych. Dlatego poswiecamy mu az 4 spotkania: S03-S06."

> "Dzisiaj: dwie struktury danych (Series, DataFrame), eksploracja, i **selekcja z filtrowaniem** — czyli odpowiadanie na konkretne pytania biznesowe. Na labach przećwiczycie to na prawdziwym datasecie."

---

### 0:05-0:20 — MATERIAL 1: Series i DataFrame (15 min)

#### Series (7 min)

> "Zaczynamy od **Series**. Jednowymiarowa tablica z etykietami — jak kolumna w arkuszu kalkulacyjnym."

```python
import pandas as pd
import numpy as np

# Series z listy — domyślny indeks
sprzedaz = pd.Series([340, 120, 560, 90, 420])
print(sprzedaz)
```

> "Wyglada jak tablica NumPy, ale po lewej stronie sa **indeksy**: 0, 1, 2, 3, 4."

```python
# Series z wlasnymi etykietami
sprzedaz = pd.Series(
    [340, 120, 560, 90, 420],
    index=['Laptop', 'Tablet', 'Smartfon', 'Akces.', 'Monitor']
)
print(sprzedaz)
print(f"\nSmartfon: {sprzedaz['Smartfon']}")
print(f"Max: {sprzedaz.max()} ({sprzedaz.idxmax()})")
```

> "Teraz widze — 'Laptop: 340 sztuk'. To jest sila Pandas — dane z kontekstem. `idxmax()` zwraca **nazwe**, nie numer pozycji."

```python
# Tworzenie z dict — najnaturalniejszy sposob
populacja = pd.Series({
    'Warszawa': 1_794_000,
    'Krakow': 800_000,
    'Opole': 128_000
})
print(populacja)
```

> "Dict — klucze staja sie indeksem. Proste i czytelne."

```python
# Operacje wektorowe — jak w NumPy!
popularne = sprzedaz[sprzedaz > 200]
print(f"Popularne (>200 szt.):\n{popularne}")
print(f"\nSrednia: {sprzedaz.mean():.0f}")   # 306
print(f"Suma: {sprzedaz.sum()}")              # 1530
```

> "Filtrowanie boolean, mean, sum — identycznie jak w NumPy. Ale z etykietami."

#### DataFrame (8 min)

> "Series to jedna kolumna. **DataFrame** to tabela — wiele kolumn obok siebie."

```python
# DataFrame z dict list
dane = pd.DataFrame({
    'produkt': ['Laptop', 'Tablet', 'Smartfon', 'Akces.', 'Monitor'],
    'cena': [3500, 1800, 2500, 150, 2200],
    'sprzedaz': [340, 120, 560, 90, 420],
    'kategoria': ['Komputery', 'Mobilne', 'Mobilne', 'Akcesoria', 'Komputery']
})
print(dane)
```

> "Dict list — klucze to nazwy kolumn, wartosci to dane. Jak arkusz w Excelu, ale w kodzie."

```python
# Atrybuty DataFrame
print(f"Ksztalt: {dane.shape}")          # (5, 4)
print(f"Kolumny: {list(dane.columns)}")  # nazwy kolumn
print(f"Indeks: {dane.index}")           # RangeIndex(0, 5)
print(f"Rozmiar: {dane.size}")           # 20 (5x4)
```

> "`.shape` — (5, 4), piec wierszy, cztery kolumny. `.columns` — nazwy kolumn. Dokladnie jak w NumPy."

```python
# Wybor kolumn
rachunki = dane['cena']              # jedna kolumna -> Series
print(type(rachunki))

pieniadze = dane[['cena', 'sprzedaz']]  # wiele kolumn -> DataFrame
print(type(pieniadze))
print(pieniadze)
```

> "Jedna kolumna w nawiasach — **Series**. Dwie lub wiecej w **podwojnych** nawiasach — **DataFrame**. Podwojne — bo wewnatrz jest lista nazw."

---

### 0:20-0:35 — MATERIAL 2: Wczytywanie CSV i EDA (15 min)

> "W praktyce nie wpisujecie danych recznie. Wczytujecie CSV — to 90% waszej pracy."

```python
# Wczytanie prawdziwego datasetu
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(url)
print(f"Rozmiar: {tips.shape}")   # (244, 7)
print(tips.head())
```

> "Jedna linia kodu — 244 wiersze, 7 kolumn. Dataset o napiwkach w restauracji. `head()` — pierwsze 5 wierszy. Zawsze zaczynacie od `head()`."

> "Pierwsze 5 minut z kazdym nowym zestawem danych to **EDA — Exploratory Data Analysis**. Muszę wiedziec: ile wierszy, jakie kolumny, jakie typy, ile braków."

```python
# info() — RTG danych
tips.info()
```

> "`info()` — to jest RTG waszych danych. 244 wpisy, 7 kolumn, typy danych, ile wartosci nie-null. Tu wszystko jest kompletne — 244 non-null wszedzie. W realnych danych tak pieknie nie bedzie."

```python
# describe() — statystyki opisowe
tips.describe()
```

> "`describe()` — statystyki dla kolumn liczbowych. Sredni rachunek ~20 dolarow, sredni napiwek ~3 dolary, grupy od 1 do 6 osob."

```python
# value_counts() — rozklady wartosci kategorycznych
print("=== Dzien ===")
print(tips['day'].value_counts())

print("\n=== Pora dnia ===")
print(tips['time'].value_counts())
```

> "`value_counts()` — ile razy kazda wartosc wystapila. Sobota dominuje — 87 rachunkow. Obiad: 176, lunch: 68."

```python
# Brakujace wartosci
print(tips.isna().sum())
print(f"\nLacznie brakow: {tips.isna().sum().sum()}")  # 0
```

> "Sprawdzenie brakow — tu zero, dane kompletne. **Zawsze** robicie to jako jeden z pierwszych krokow."

```python
# value_counts z normalize — procenty
print(tips['day'].value_counts(normalize=True).round(2))
```

> "`normalize=True` — proporcje. Sobota = 36%. Przydatne w raportach."

---

### 0:35-0:45 — PRZERWA (10 min)

---

### 0:45-1:05 — MATERIAL 3: loc i iloc (20 min)

> "Umiecie juz eksplorować dane — wiecie co macie. Teraz przechodzimy od 'co mam?' do '**pokaz mi dokladnie TO**'. Narzedzia: `loc` i `iloc`."

#### iloc — pozycja (7 min)

```python
# iloc — Integer Location — po POZYCJI
print("Wiersz 0:")
print(tips.iloc[0])              # pierwszy wiersz -> Series

print("\nWiersze 0-2, kolumny 0-1:")
print(tips.iloc[0:3, 0:2])      # slice: wiersze 0-2, kolumny 0-1
```

> "`iloc` — **i** jak integer. Pozycja liczbowa. Dokladnie jak indeksowanie w NumPy."

```python
# Dalsze przyklady iloc
print("Ostatni wiersz:")
print(tips.iloc[-1])

print("\nCo piaty wiersz, kolumny 0 i 1:")
print(tips.iloc[::5, [0, 1]].head())

print("\nWiersze 10, 20, 30:")
print(tips.iloc[[10, 20, 30], [0, 4]])
```

> "`iloc[-1]` — ostatni. `iloc[::5]` — co piaty. `iloc[[10, 20, 30]]` — konkretne pozycje."

#### loc — etykiety (7 min)

```python
# loc — Label Location — po ETYKIETACH
produkty = pd.DataFrame({
    'cena': [3500, 1800, 2500, 350, 2200],
    'magazyn': [45, 120, 200, 500, 75],
    'kategoria': ['Komputery', 'Mobilne', 'Mobilne', 'Akcesoria', 'Komputery']
}, index=['Laptop', 'Tablet', 'Smartfon', 'Sluchawki', 'Monitor'])

print(produkty.loc['Laptop'])              # wiersz po etykiecie
print(f"\nCena Laptopa: {produkty.loc['Laptop', 'cena']}")
```

> "`loc` — po etykiecie. 'Laptop' — nie numer, ale nazwa. Czytelne, naturalne."

```python
# loc z wieloma etykietami
print(produkty.loc[['Laptop', 'Monitor'], ['cena', 'magazyn']])

# loc z warunkiem — kluczowe!
print(f"\nDrogie produkty (>2000):")
print(produkty.loc[produkty['cena'] > 2000])
```

> "`loc` + warunek = filtrowanie. To jest **kluczowe** — 90% waszej pracy z danymi."

#### loc vs iloc — podsumowanie (3 min)

```python
# iloc = pozycja (numer)
# tips.iloc[0]       — pierwszy wiersz
# tips.iloc[:, 0]    — pierwsza kolumna

# loc = etykieta (nazwa/warunek)
# tips.loc[:, 'total_bill']      — kolumna 'total_bill'
# tips.loc[tips['day'] == 'Sun'] — filtrowanie
```

> "Prosta zasada: **iloc = numer**, **loc = nazwa**. W 90% przypadkow bedziecie uzywac `loc` z warunkami."

#### Filtrowanie z loc na tips (3 min)

```python
# loc + warunek na tips
niedziele = tips.loc[tips['day'] == 'Sun', ['total_bill', 'tip']]
print(f"Niedziele: {len(niedziele)} wierszy")  # 76
print(niedziele.head())

# Wszystkie kolumny
drogie = tips.loc[tips['total_bill'] > 40]
print(f"\nRachunki > 40$: {len(drogie)}")       # 10
```

---

### 1:05-1:20 — MATERIAL 4: Filtrowanie, sortowanie (15 min)

#### Warunki logiczne (6 min)

> "Filtrowanie — serce pracy analityka. Odpowiedz na pytanie: 'pokaz mi wiersze spelniajace warunek'."

```python
# Filtr prosty
drogie = tips[tips['total_bill'] > 30]
print(f"Rachunki > 30$: {len(drogie)}")  # 32

# AND — oba warunki (&)
sobota_drogie = tips[(tips['day'] == 'Sat') & (tips['total_bill'] > 30)]
print(f"Sobota + rachunek > 30$: {len(sobota_drogie)}")

# OR — przynajmniej jeden (|)
weekend = tips[(tips['day'] == 'Sat') | (tips['day'] == 'Sun')]
print(f"Weekend: {len(weekend)}")         # 163

# NOT — negacja (~)
niepalacze = tips[~(tips['smoker'] == 'Yes')]
print(f"Niepalacze: {len(niepalacze)}")   # 151
```

> "AND to `&`, OR to `|`, NOT to `~`. **Nawiasy obowiazkowe** wokol kazdego warunku! Bez nawiasow Python zle interpretuje priorytety."

```python
# Zlozony filtr — 4 warunki
wynik = tips[
    (tips['size'] >= 4) &
    (tips['day'].isin(['Sat', 'Sun'])) &
    (tips['smoker'] == 'No') &
    (tips['total_bill'] > 20)
]
print(f"Duze grupy, weekend, niepalacze, >20$: {len(wynik)}")
```

> "Kazdy warunek w osobnej linii — czytelne formatowanie. W prawdziwej analizie takie filtry to codziennosc."

#### isin, between, query (5 min)

```python
# isin — lista wartosci
popularne_dni = tips[tips['day'].isin(['Sat', 'Sun'])]
print(f"Sobota + Niedziela: {len(popularne_dni)}")  # 163

# between — zakres
srednie = tips[tips['total_bill'].between(15, 25)]
print(f"Rachunki 15-25$: {len(srednie)}")

# query — jak SQL WHERE
wynik = tips.query("total_bill > 30 and day == 'Sat' and smoker == 'No'")
print(f"Query: {len(wynik)}")
```

> "`isin` — krotsze niz OR dla wielu wartosci. `between` — zakres, oba konce wlaczone. `query` — filtr jak SQL, czytelny i zwiezly."

#### Sortowanie (4 min)

```python
# Sortowanie po jednej kolumnie
print("Top 5 rachunkow:")
print(tips.sort_values('total_bill', ascending=False).head())

# Top-N skrot
print("\nTop 5 (nlargest):")
print(tips.nlargest(5, 'total_bill')[['total_bill', 'tip', 'day']])

# Sortowanie po wielu kolumnach
print("\nDzien (A-Z), potem rachunek (malejaco):")
print(tips.sort_values(['day', 'total_bill'], ascending=[True, False]).head(10))
```

> "`sort_values` + `head` = ranking. `nlargest` i `nsmallest` — szybszy odpowiednik. Pattern: `nlargest(5, 'kolumna')` — Wasz go-to na TOP-N."

---

### 1:20-1:30 — MATERIAL 5: Nowe kolumny i podsumowanie (10 min)

#### Nowe kolumny (5 min)

```python
# Nowa kolumna — procent napiwku
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
print(tips[['total_bill', 'tip', 'tip_pct']].head())
print(f"\nSredni napiwek: {tips['tip_pct'].mean():.1f}%")  # 16.1%
```

> "Tworzenie nowej kolumny — prosta operacja na istniejacych. Pandas robi to element po elemencie."

```python
# Segmentacja klientow z pd.cut
tips['segment'] = pd.cut(
    tips['total_bill'],
    bins=[0, 15, 30, 100],
    labels=['Niski', 'Sredni', 'Wysoki']
)
print(tips['segment'].value_counts())
# Niski      80
# Sredni    132
# Wysoki     32
```

> "`pd.cut` — dzieli wartosci liczbowe na kategorie. Biny [0, 15, 30, 100] tworza 3 grupy. Niski = rachunek do 15$, Sredni = 15-30$, Wysoki = powyzej 30$. **Na labach przećwiczycie to szczegolowo.**"

```python
# Sredni napiwek per segment
for seg in ['Niski', 'Sredni', 'Wysoki']:
    subset = tips[tips['segment'] == seg]
    print(f"{seg}: n={len(subset)}, sr. tip = {subset['tip_pct'].mean():.1f}%")
# Niski:   n=80,  sr. tip = 18.4%
# Sredni:  n=132, sr. tip = 15.6%
# Wysoki:  n=32,  sr. tip = 12.2%
```

> "Ciekawy wynik — im wyzszy rachunek, tym **nizszy procent** napiwku! Niskie rachunki = 18.4%, wysokie = 12.2%. To jest insight biznesowy — takie rzeczy znajdujecie dzieki Pandas."

#### Podsumowanie (5 min)

> "Podsumujmy dzisiejszy wyklad:"

> "1. **Series** — jednowymiarowa tablica z etykietami. Jak kolumna w Excelu z supermocami."
> "2. **DataFrame** — tabela. Tworzycie z dict lub wczytujecie z CSV (`read_csv`)."
> "3. **EDA** — `head()`, `info()`, `describe()`, `value_counts()`, `isna().sum()` — piec metod na KAZDY nowy dataset."
> "4. **loc vs iloc** — loc = nazwa/warunek, iloc = numer pozycji."
> "5. **Filtrowanie** — `&`, `|`, `~`, `isin`, `between`, `query`. Nawiasy obowiazkowe!"
> "6. **Sortowanie** — `sort_values()`, `nlargest()`, `nsmallest()`."
> "7. **Nowe kolumny** — `pd.cut` do segmentacji."

> "Teraz przechodzimy do laboratorium. Bedziecie sami pracowac na datasecie tips — tworzenie, eksploracja, filtrowanie, segmentacja. 90 minut — 5 cwiczen."

> "Na S04: **czyszczenie danych** (NaN, duplikaty, typy) i **laczenie tabel** (merge, groupby). W realnym zyciu 60-80% czasu analityka to czyszczenie — wiec bedzie to wazne spotkanie."
