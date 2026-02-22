# W06 Wykład — Plan zajęć dla prowadzącego

## Temat: Pandas — selekcja i filtrowanie

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z pandas/numpy
- **Przed wykładem:** otwórz `pandas_selection_demo.ipynb`

### Efekty uczenia się (Bloom)
Po tym wykładzie osoba studiująca:
1. **Rozróżnia** `loc` (etykiety) i `iloc` (pozycje) i stosuje je poprawnie (Bloom 2-3)
2. **Filtruje** dane z warunkami logicznymi (AND, OR, isin, between, query) (Bloom 3)
3. **Sortuje** DataFrame po jednej lub wielu kolumnach (Bloom 3)
4. **Analizuje** dane sprzedażowe odpowiadając na pytania biznesowe (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W05 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | Od eksploracji do precyzyjnych pytań | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | loc i iloc — selekcja wierszy i kolumn | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | Filtrowanie z warunkami logicznymi | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | isin, between, query, sortowanie | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Zastosowanie: segmentacja klientów | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Analiza danych sprzedażowych | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Przejście do czyszczenia danych na W07 | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W05)

> "Pięć pytań z zeszłego tygodnia — 3 minuty."

**[Użyj quiz_w05.md]**

---

### 0:05-0:10 — WPROWADZENIE

> "Zeszły tydzień — Series, DataFrame, read_csv, eksploracja. Wiecie co macie w danych: ile wierszy, jakie kolumny, jakie typy."

> "Dzisiaj przechodzimy od pytania 'co mam?' do pytania 'pokaż mi dokładnie TO'. Np.: 'Pokaż rachunki powyżej 30 dolarów, z soboty, od niepalących, posortowane malejąco'. To jest selekcja i filtrowanie — kluczowa umiejętność analityka."

> "Dwie główne narzędzia: **loc** i **iloc**. Plus warunki logiczne."

---

### 0:10-0:30 — MATERIAŁ 1: loc i iloc (20 min)

**[Otwórz notebook]**

```python
import pandas as pd
import numpy as np

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips.head()
```

> "Zaczynamy od datasetu tips — znacie go już dobrze."

**[Komórka 1 — iloc: pozycja]**

```python
# iloc — Integer Location — po POZYCJI (jak w NumPy)
print("Wiersz 0:")
print(tips.iloc[0])          # pierwszy wiersz → Series

print("\nWiersze 0-2, kolumny 0-1:")
print(tips.iloc[0:3, 0:2])   # slice: wiersze 0-2, kolumny 0-1
```

> "`iloc` — **i** jak integer. Pozycja liczbowa: wiersz 0, kolumna 0. Dokładnie jak indeksowanie w NumPy. Slicing: `0:3` = wiersze 0, 1, 2."

**[Komórka 2 — iloc: dalsze przykłady]**

```python
# Ostatni wiersz
print("Ostatni wiersz:")
print(tips.iloc[-1])

# Co piąty wiersz, kolumny 0 i 1
print("\nCo piąty wiersz:")
print(tips.iloc[::5, [0, 1]].head())

# Konkretne wiersze i kolumny
print("\nWiersze 10, 20, 30 — kolumny 0, 4:")
print(tips.iloc[[10, 20, 30], [0, 4]])
```

> "`iloc[-1]` — ostatni wiersz. `iloc[::5]` — co piąty. `iloc[[10, 20, 30]]` — konkretne pozycje. Elastyczność jak w NumPy."

**[Komórka 3 — loc: etykiety]**

```python
# loc — Label Location — po ETYKIETACH
# Ustawmy indeks na coś czytelnego
dane = pd.DataFrame({
    'produkt': ['Laptop', 'Tablet', 'Smartfon', 'Monitor', 'Słuchawki'],
    'cena': [3500, 1800, 2500, 2200, 350],
    'sprzedaz': [340, 120, 560, 420, 800],
    'kategoria': ['Komputery', 'Mobilne', 'Mobilne', 'Komputery', 'Akcesoria']
})
dane.index = dane['produkt']   # ustawiamy indeks

print(dane.loc['Laptop'])              # wiersz po etykiecie
print(f"\n{dane.loc['Laptop', 'cena']}")    # wiersz + kolumna
```

> "`loc` — po etykiecie. `loc['Laptop']` — wiersz o etykiecie 'Laptop'. `loc['Laptop', 'cena']` — konkretna komórka. Czytelne, naturalne."

**[Komórka 4 — loc: slice i wybór kolumn]**

```python
# loc z wieloma etykietami
print(dane.loc[['Laptop', 'Monitor'], ['cena', 'sprzedaz']])

# loc z warunkiem — zapowiedź filtrowania
print(f"\nDrogie produkty:")
print(dane.loc[dane['cena'] > 2000])
```

> "`loc` ze slice etykiet i z warunkami boolean. To jest kluczowe — `loc` + warunek = filtrowanie."

**[Komórka 5 — loc vs iloc podsumowanie]**

> "Kiedy co?"

```python
# iloc — pozycja (numer)
# tips.iloc[0]      — pierwszy wiersz
# tips.iloc[0:5]    — wiersze 0-4
# tips.iloc[:, 0]   — pierwsza kolumna

# loc — etykieta (nazwa)
# dane.loc['Laptop']           — wiersz 'Laptop'
# tips.loc[:, 'total_bill']    — kolumna 'total_bill'
# tips.loc[tips['day'] == 'Sun']  — filtrowanie

# Zasada: iloc = pozycja, loc = nazwa/warunek
```

> "Prosta zasada: **iloc = numer**, **loc = nazwa**. W 90% przypadków będziecie używać `loc` z warunkami. `iloc` przydaje się gdy potrzebujecie n-ty wiersz bez znajomości etykiety."

---

### 0:30-0:45 — MATERIAŁ 2: Filtrowanie (15 min)

> "Filtrowanie — serce pracy analityka. Odpowiedź na pytanie: 'pokaż mi tylko wiersze spełniające warunek'."

**[Komórka 6 — filtr prosty]**

```python
# Rachunki powyżej 30 dolarów
drogie = tips[tips['total_bill'] > 30]
print(f"Rachunki > 30$: {len(drogie)} z {len(tips)}")
print(drogie.head())
```

> "Warunek `tips['total_bill'] > 30` tworzy Series True/False. Podajecie ją jako indeks — Pandas zwraca tylko wiersze z True. Identycznie jak filtrowanie boolean w NumPy."

**[Komórka 7 — AND, OR]**

```python
# AND — oba warunki spełnione (operator &)
sobota_drogie = tips[(tips['day'] == 'Sat') & (tips['total_bill'] > 30)]
print(f"Sobota + rachunek > 30$: {len(sobota_drogie)}")
print(sobota_drogie.head())

# OR — przynajmniej jeden warunek (operator |)
weekend = tips[(tips['day'] == 'Sat') | (tips['day'] == 'Sun')]
print(f"\nWeekend: {len(weekend)}")
```

> "AND to `&`, OR to `|`. **Nawiasy obowiązkowe!** Bez nawiasów Python źle interpretuje priorytety. Częsty błąd: `tips[tips['day'] == 'Sat' & tips['total_bill'] > 30]` — to nie zadziała. Nawiasy wokół każdego warunku."

**[Komórka 8 — negacja]**

```python
# NOT — negacja (operator ~)
niepalacze = tips[~(tips['smoker'] == 'Yes')]
print(f"Niepalacze: {len(niepalacze)}")

# Alternatywa
niepalacze2 = tips[tips['smoker'] == 'No']
print(f"Niepalacze (alt): {len(niepalacze2)}")
```

> "Negacja: `~` (tylda). Ale zwykle prościej odwrócić warunek — `== 'No'` zamiast `~(== 'Yes')`."

**[Komórka 9 — złożony filtr]**

```python
# Pytanie biznesowe: duże grupy (4+) w weekend, niepalacze, rachunek > 20$
wynik = tips[
    (tips['size'] >= 4) &
    (tips['day'].isin(['Sat', 'Sun'])) &
    (tips['smoker'] == 'No') &
    (tips['total_bill'] > 20)
]
print(f"Znalezionych: {len(wynik)}")
print(wynik)
```

> "Złożony filtr — 4 warunki. Czytelne formatowanie: każdy warunek w osobnej linii. W prawdziwej analizie takie filtry to codzienność."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: isin, between, query, sortowanie (20 min)

**[Komórka 10 — isin]**

> "`isin` — gdy mamy listę wartości do sprawdzenia."

```python
# isin — czy wartość jest na liście
popularne_dni = tips[tips['day'].isin(['Sat', 'Sun'])]
print(f"Sobota + Niedziela: {len(popularne_dni)}")

# To samo co OR, ale krótsze przy wielu wartościach
# tips[(tips['day'] == 'Sat') | (tips['day'] == 'Sun')]  ← dłuższe
```

> "`isin(['Sat', 'Sun'])` — to samo co `day == 'Sat' | day == 'Sun'`, ale krótsze. Przy 5 wartościach OR jest nieczytelny — `isin` jest czytelny."

**[Komórka 11 — between]**

```python
# between — zakres wartości
srednie_rachunki = tips[tips['total_bill'].between(15, 25)]
print(f"Rachunki 15-25$: {len(srednie_rachunki)}")
print(srednie_rachunki.head())
```

> "`between(15, 25)` — to samo co `>= 15` AND `<= 25`, ale w jednym wywołaniu. Oba końce włączone (inclusive)."

**[Komórka 12 — query]**

```python
# query — filtrowanie stringiem (jak SQL WHERE)
wynik = tips.query("total_bill > 30 and day == 'Sat' and smoker == 'No'")
print(f"Query: {len(wynik)}")
print(wynik.head())
```

> "`query()` — filtr napisany jak SQL. Czytelny, zwięzły. Nie potrzebujecie `tips['...']` i `&` — piszecie naturalny warunek. Wielu analityków preferuje query dla złożonych filtrów."

**[Komórka 13 — sortowanie]**

```python
# Sortowanie po jednej kolumnie
print("Top 5 rachunków:")
print(tips.sort_values('total_bill', ascending=False).head())

# Sortowanie po wielu kolumnach
print("\nSortowanie: dzień (A-Z), potem rachunek (malejąco):")
print(tips.sort_values(['day', 'total_bill'], ascending=[True, False]).head(10))
```

> "`sort_values` — sortowanie. Domyślnie rosnąco. `ascending=False` — malejąco. Wiele kolumn — lista nazw + lista kierunków."

**[Komórka 14 — sort_values + head = TOP-N]**

```python
# TOP-5 napiwków
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)

print("TOP-5 napiwków (%):")
print(tips.sort_values('tip_pct', ascending=False).head()[['total_bill', 'tip', 'tip_pct', 'day']])
```

> "Pattern: `sort_values(ascending=False).head(5)` = TOP-5. To jest Wasz go-to pattern do rankingów."

**[Komórka 15 — nlargest, nsmallest]**

```python
# Szybszy sposób na TOP/BOTTOM
print("Top 5 rachunków (nlargest):")
print(tips.nlargest(5, 'total_bill')[['total_bill', 'tip', 'day']])

print("\nNajmniejsze 5 rachunków (nsmallest):")
print(tips.nsmallest(5, 'total_bill')[['total_bill', 'tip', 'day']])
```

> "`nlargest` i `nsmallest` — szybszy odpowiednik sort + head. Bardziej czytelny, lepszy na dużych danych."

---

### 1:15-1:25 — MATERIAŁ 4: Segmentacja klientów (10 min)

> "Zastosowanie biznesowe — segmentacja. Dzielenie klientów na grupy na podstawie ich zachowań."

**[Komórka 16 — segmentacja z np.where]**

```python
# Segmentacja wg wielkości grupy
tips['segment'] = np.where(tips['size'] >= 4, 'Duża grupa', 'Mała grupa')
print(tips['segment'].value_counts())

# Segmentacja wg napiwku
tips['hojnosc'] = np.where(
    tips['tip_pct'] > 20, 'Hojny',
    np.where(tips['tip_pct'] > 10, 'Przeciętny', 'Skąpy')
)
print(f"\n{tips['hojnosc'].value_counts()}")
```

> "Segmentacja: `np.where` dzieli dane na grupy. Zagnieżdżony `np.where` dla 3+ grup — poznaliście to na NumPy. W Pandas to się łączy z filtrami."

**[Komórka 17 — analiza per segment]**

```python
# Średni rachunek per segment
for segment in tips['hojnosc'].unique():
    grupa = tips[tips['hojnosc'] == segment]
    print(f"{segment}: śr. rachunek = {grupa['total_bill'].mean():.2f}$, "
          f"śr. napiwek = {grupa['tip'].mean():.2f}$, "
          f"n = {len(grupa)}")
```

> "Filtrowanie per segment — zobaczcie jak to działa. 'Hojny' daje średnio 3.40$ napiwku, 'Skąpy' — 2.15$. Ale na W08 poznacie `groupby` — to zrobi to samo w jednej linii."

---

### 1:25-1:35 — AKTYWNOŚĆ: analiza danych (10 min)

> "Zadanie. Odpowiedzcie na pytania o datasecie tips."

**[Wyświetl na projektorze]**

```python
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
```

**Pytania (5 min):**
1. Ile rachunków jest z piątku? (`day == 'Fri'`)
2. Jakie jest 5 najdroższych rachunków z niedzieli?
3. Ile rachunków od palaczy przekracza 25 dolarów?
4. Jaki jest średni napiwek (%) w sobotę vs niedzielę?
5. Znajdź osoby dające napiwek powyżej 30% — ile ich jest?

**Odpowiedzi:**
1. 19
2. sort_values na Sunday → top: 48.17, 45.35, 40.55, 38.07, 35.26
3. 28
4. Sat: ~15.3%, Sun: ~16.7%
5. tips[tips['tip_pct'] > 30] → 3 osoby

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy:"

> "1. **loc vs iloc** — loc po etykiecie/nazwie, iloc po numerze pozycji."
> "2. **Filtrowanie** — warunek boolean + `&` (AND), `|` (OR). Nawiasy obowiązkowe!"
> "3. **isin, between, query** — skróty do częstych filtrów."
> "4. **Sortowanie** — `sort_values()`, `nlargest()`, `nsmallest()`. Pattern: sort + head = ranking."

> "To co dzisiaj robiliście to **serce analizy danych**. Każdy raport biznesowy zaczyna się od pytania → filtrowania → sortowania → odpowiedzi."

> "Następny tydzień: **czyszczenie danych**. Brakujące wartości (NaN), duplikaty, błędne typy, literówki w danych. Po przerwie świątecznej. W prawdziwym życiu 60-80% czasu analityka to czyszczenie — więc to będzie ważny wykład."

**Zadanie domowe (nieoceniane):**
> "Wczytajcie dataset penguins. Odpowiedzcie na 5 pytań: (1) Ile pingwinów gatunku Chinstrap? (2) Jakie 3 wyspy mają pingwiny? (3) Pingwiny z wyspy Dream — jaka średnia masa? (4) TOP-3 najdłuższe dzioby (bill_length_mm). (5) Ile samic waży powyżej 4000g? Notebook na GitHub."
