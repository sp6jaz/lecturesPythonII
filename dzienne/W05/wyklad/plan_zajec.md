# W05 Wykład — Plan zajęć dla prowadzącego

## Temat: Pandas — Series i DataFrame

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z pandas/numpy/matplotlib
- **Przed wykładem:** otwórz `pandas_intro_demo.ipynb`

### Efekty uczenia się (Bloom)
Po tym wykładzie osoba studiująca:
1. **Wyjaśnia** czym jest Pandas i dlaczego jest kluczowy w analizie danych (Bloom 2)
2. **Tworzy** Series i DataFrame z różnych źródeł (dict, lista, CSV) (Bloom 3)
3. **Stosuje** metody eksploracyjne: info(), describe(), head(), tail(), dtypes (Bloom 3)
4. **Rozróżnia** typy danych w DataFrame i rozumie ich wpływ na operacje (Bloom 2)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W04 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | NumPy → Pandas, plan wykładu | Rozmowa |
| 0:10-0:25 | **MATERIAŁ 1** | Series — tworzenie, indeks, operacje | Live coding |
| 0:25-0:45 | **MATERIAŁ 2** | DataFrame — tworzenie, read_csv, atrybuty | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | Eksploracja: info(), describe(), value_counts(), dtypes | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Selekcja kolumn, pierwszy rzut oka na wiersze | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Eksploracja datasetu — odpowiedzi na pytania biznesowe | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Co Pandas daje ponad NumPy, zapowiedź W06 | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W04)

> "Pięć pytań z zeszłego tygodnia — 3 minuty."

**[Użyj quiz_w04.md]**

---

### 0:05-0:10 — WPROWADZENIE

> "Dwa tygodnie z NumPy za nami. NumPy jest szybki, potężny — ale ma jeden problem. Pokażę na przykładzie."

**[Wpisz w notebook na żywo]**

```python
import numpy as np

sprzedaz = np.array([340, 120, 560, 90, 420])
print(sprzedaz)
# [340 120 560  90 420]
```

> "Patrzę na to i pytam: 340 czego? Który to produkt? Który to miesiąc? NumPy nie wie. Ma tylko liczby. Żadnych etykiet, żadnych nazw kolumn, żadnych dat."

> "**Pandas** rozwiązuje ten problem. Pandas to NumPy z etykietami. Pod spodem — te same szybkie tablice NumPy. Na wierzchu — nazwy kolumn, indeksy wierszy, typy danych, metody do wczytywania CSV, czyszczenia, filtrowania, grupowania."

> "Pandas to **narzędzie numer jeden** analityka danych. Jeśli z tego kursu zapamiętacie jedną bibliotekę — niech to będzie Pandas. Dlatego poświęcamy mu aż 4 tygodnie: W05-W08."

> "Dzisiaj: **Series i DataFrame** — dwie podstawowe struktury danych. Nauczycie się tworzyć je, wczytywać z pliku CSV i eksplorować."

---

### 0:10-0:25 — MATERIAŁ 1: Series (15 min)

**[Otwórz notebook]**

> "Zaczynamy od **Series**. To jednowymiarowa tablica z etykietami — jak kolumna w arkuszu kalkulacyjnym."

**[Komórka 1 — tworzenie Series]**

```python
import pandas as pd
import numpy as np

# Series z listy
sprzedaz = pd.Series([340, 120, 560, 90, 420])
print(sprzedaz)
```

> "Wygląda jak tablica NumPy, ale po lewej stronie pojawiły się **indeksy**: 0, 1, 2, 3, 4. Pandas automatycznie dodał indeks liczbowy."

**[Komórka 2 — Series z etykietami]**

```python
# Series z własnymi etykietami
sprzedaz = pd.Series(
    [340, 120, 560, 90, 420],
    index=['Laptop', 'Tablet', 'Smartfon', 'Akces.', 'Monitor']
)
print(sprzedaz)
print(f"\nTyp: {type(sprzedaz)}")
```

> "Teraz widzę od razu — 'Laptop: 340 sztuk'. To jest siła Pandas — dane z kontekstem. Już nie 'element numer 0', tylko 'Laptop'."

**[Komórka 3 — dostęp do elementów]**

```python
# Dostęp po etykiecie
print(f"Smartfon: {sprzedaz['Smartfon']}")

# Dostęp po pozycji
print(f"Pierwszy: {sprzedaz.iloc[0]}")

# Slice
print(f"\nPierwsze 3:\n{sprzedaz[:3]}")
```

> "Dwa sposoby dostępu: po **etykiecie** (nazwa) lub po **pozycji** (numer). Na W06 poznamy to dokładniej — `loc` i `iloc`."

**[Komórka 4 — operacje na Series]**

```python
# Operacje wektorowe — jak w NumPy!
sprzedaz_z_vat = sprzedaz * 1.23
print(f"Z VAT:\n{sprzedaz_z_vat}")

# Filtrowanie boolean
popularne = sprzedaz[sprzedaz > 200]
print(f"\nPopularne (>200 szt.):\n{popularne}")

# Agregacje
print(f"\nŚrednia: {sprzedaz.mean():.0f}")
print(f"Suma: {sprzedaz.sum()}")
print(f"Max: {sprzedaz.max()} ({sprzedaz.idxmax()})")
```

> "Operacje wektorowe — identyczne jak w NumPy! Mnożenie, filtrowanie boolean, mean, sum — wszystko działa. Ale jest bonus: `idxmax()` — nie tylko wartość maksymalna, ale **nazwa** produktu. W NumPy mieliśmy argmax() — numer pozycji. Tu mamy etykietę."

**[Komórka 5 — Series z dict]**

```python
# Tworzenie z dict — naturalne w Pythonie
populacja = pd.Series({
    'Warszawa': 1_794_000,
    'Kraków': 800_000,
    'Wrocław': 643_000,
    'Opole': 128_000
})
print(populacja)
print(f"\nOpole: {populacja['Opole']:,}")
```

> "Dict to najnaturalniejszy sposób tworzenia Series — klucze stają się indeksem. Proste i czytelne."

---

### 0:25-0:45 — MATERIAŁ 2: DataFrame (20 min)

> "Series to jedna kolumna. **DataFrame** to tabela — wiele kolumn obok siebie, każda kolumna to Series."

**[Komórka 6 — tworzenie DataFrame z dict]**

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

> "Dict list — klucze to nazwy kolumn, wartości to dane w kolumnach. To jak arkusz w Excelu — wiersze i kolumny, ale w kodzie."

**[Komórka 7 — atrybuty DataFrame]**

```python
print(f"Kształt: {dane.shape}")         # (5, 4)
print(f"Kolumny: {list(dane.columns)}")  # nazwy kolumn
print(f"Indeks: {dane.index}")           # RangeIndex
print(f"Rozmiar: {dane.size}")           # 20 (5×4)
print(f"Wymiary: {dane.ndim}")           # 2
```

> "`.shape` — (5, 4), pięć wierszy, cztery kolumny. `.columns` — nazwy kolumn. `.index` — indeks wierszy (domyślnie 0-4). Dokładnie jak `shape` i `ndim` w NumPy."

**[Komórka 8 — read_csv z URL]**

> "W praktyce nie wpisujecie danych ręcznie. Wczytujesz CSV — i to jest 90% waszej pracy."

```python
# Wczytanie prawdziwego datasetu
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(url)
print(f"Rozmiar: {tips.shape}")
print(tips.head())
```

> "Jedna linia kodu — 244 wiersze, 7 kolumn. To ten sam dataset co na W02. `head()` — pierwsze 5 wierszy. Zawsze zaczynacie od `head()` — żeby zobaczyć co macie."

**[Komórka 9 — head, tail, sample]**

```python
print("=== Pierwsze 3 wiersze ===")
print(tips.head(3))

print("\n=== Ostatnie 3 wiersze ===")
print(tips.tail(3))

print("\n=== Losowe 3 wiersze ===")
print(tips.sample(3, random_state=42))
```

> "`head(n)` — pierwsze n. `tail(n)` — ostatnie n. `sample(n)` — losowe n. Na początek zawsze `head()`, żeby wiedzieć co jest w danych."

**[Komórka 10 — dtypes]**

```python
print(tips.dtypes)
```

> "Typy danych. `float64` — liczby zmiennoprzecinkowe (total_bill, tip). `int64` — liczby całkowite (size). `object` — tekst/kategorie (sex, smoker, day, time). Typy są ważne — nie można policzyć średniej z tekstu."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: Eksploracja danych (20 min)

> "Macie dataset. Co dalej? Pierwsze 5 minut z każdym nowym zestawem danych to **eksploracja**. Muszę wiedzieć: ile wierszy, ile kolumn, jakie typy, ile brakujących, jakie wartości."

**[Komórka 11 — info()]**

```python
tips.info()
```

> "`info()` — to jest **RTG waszych danych**. Widzicie: 244 wpisy, 7 kolumn, typy danych, ile wartości nie-null. Tutaj wszystko jest kompletne — 244 non-null wszędzie. W realnych danych tak pięknie nie będzie."

**[Komórka 12 — describe()]**

```python
tips.describe()
```

> "`describe()` — statystyki opisowe dla **kolumn liczbowych**. Średnia, odchylenie standardowe, min, max, kwartyle. Jeden rzut oka i widzicie: średni rachunek ~20 dolarów, średni napiwek ~3 dolary, grupy od 1 do 6 osób."

**[Komórka 13 — describe z include]**

```python
# Statystyki dla WSZYSTKICH kolumn (też tekstowych)
tips.describe(include='all')
```

> "`include='all'` — teraz widzicie też kolumny tekstowe. `unique` — ile unikalnych wartości. `top` — najczęstsza wartość. `freq` — ile razy wystąpiła. Kolumna 'day' — 4 unikalne dni, najczęstszy 'Sat' (87 razy)."

**[Komórka 14 — value_counts()]**

```python
print("=== Dzień ===")
print(tips['day'].value_counts())

print("\n=== Pora dnia ===")
print(tips['time'].value_counts())

print("\n=== Palacz? ===")
print(tips['smoker'].value_counts())
```

> "`value_counts()` — ile razy każda wartość wystąpiła. Sobota dominuje — 87 rachunków. Obiad (Dinner) — 176 vs lunch 68. Niepalący: 151 vs palący 93. Jedno wywołanie — i znacie rozkład danych."

**[Komórka 15 — value_counts z normalize]**

```python
# Procenty zamiast liczb
print(tips['day'].value_counts(normalize=True).round(2))
```

> "`normalize=True` — proporcje zamiast liczebności. Sobota = 36%, niedziela = 31%. Przydatne w raportach — procenty są bardziej czytelne."

**[Komórka 16 — isna() i brakujące dane]**

```python
# Ile brakujących wartości?
print(tips.isna().sum())
print(f"\nŁącznie braków: {tips.isna().sum().sum()}")
```

> "Sprawdzenie braków. Tu zero — dane kompletne. W realnych danych **zawsze** robicie to jako jeden z pierwszych kroków. `isna()` tworzy tablicę True/False, `.sum()` liczy ile True."

---

### 1:15-1:25 — MATERIAŁ 4: Selekcja kolumn (10 min)

> "Jak wybrać konkretną kolumnę? Dwa sposoby."

**[Komórka 17 — wybór kolumn]**

```python
# Jedna kolumna — zwraca Series
rachunki = tips['total_bill']
print(type(rachunki))
print(rachunki.head())

# Wiele kolumn — zwraca DataFrame
pieniadze = tips[['total_bill', 'tip']]
print(f"\n{type(pieniadze)}")
print(pieniadze.head())
```

> "Jedna kolumna w nawiasach kwadratowych — dostajecie **Series**. Dwie lub więcej kolumn w **podwójnych** nawiasach — dostajecie **DataFrame**. Podwójne nawiasy — bo wewnątrz jest lista nazw."

**[Komórka 18 — obliczenia na kolumnach]**

```python
# Nowa kolumna — procent napiwku
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
print(tips[['total_bill', 'tip', 'tip_pct']].head())

print(f"\nŚredni napiwek: {tips['tip_pct'].mean():.1f}%")
print(f"Max napiwek: {tips['tip_pct'].max():.1f}%")
```

> "Tworzenie nowej kolumny — prosta operacja na istniejących. Dzielenie, mnożenie — Pandas robi to element po elemencie, jak NumPy. Średni napiwek to ~16%. Kto daje 71%? Sprawdzicie na laborkach."

**[Komórka 19 — powiązanie z NumPy]**

```python
# Pod spodem to NumPy!
wartosci = tips['total_bill'].values
print(f"Typ: {type(wartosci)}")     # numpy.ndarray
print(f"Dtype: {wartosci.dtype}")   # float64

# Można używać funkcji NumPy na kolumnach Pandas
print(f"np.median: {np.median(tips['total_bill']):.2f}")
print(f"pd.median: {tips['total_bill'].median():.2f}")
```

> "`.values` — wyciąga surową tablicę NumPy z Series. Pod spodem to **ten sam NumPy** co poznaliście. Funkcje NumPy działają na kolumnach Pandas. Ale Pandas ma swoje odpowiedniki — `.median()` zamiast `np.median()`. Używajcie tych z Pandas — są wygodniejsze."

---

### 1:25-1:35 — AKTYWNOŚĆ: eksploracja datasetu (10 min)

> "Zadanie. Wczytajcie dataset 'penguins' i odpowiedzcie na pytania."

**[Wyświetl na projektorze]**

```python
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv'
penguins = pd.read_csv(url)
```

**Pytania (5 min):**
1. Ile wierszy i kolumn ma dataset?
2. Jakie są typy danych w kolumnach?
3. Ile brakujących wartości jest w każdej kolumnie?
4. Ile jest gatunków pingwinów i ile osobników każdego gatunku?
5. Jaka jest średnia masa ciała (body_mass_g) pingwinów?

> "5 minut — otwórzcie notebook i sprawdźcie. Kto pierwszy — podnosi rękę."

**Odpowiedzi:**
1. (344, 7)
2. species/island/sex → object, bill_length/bill_depth/flipper_length → float64, body_mass_g → float64
3. bill_length_mm: 2, bill_depth_mm: 2, flipper_length_mm: 2, body_mass_g: 2, sex: 11
4. Adelie: 152, Gentoo: 124, Chinstrap: 68
5. ~4201.8 g

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy. Dzisiaj poznaliście:"

> "1. **Series** — jednowymiarowa tablica z etykietami. Jak kolumna w Excelu, ale z supermocami."
> "2. **DataFrame** — tabela z wierszami i kolumnami. Tworzycie z dict lub wczytujescie z CSV."
> "3. **Eksploracja** — `head()`, `info()`, `describe()`, `value_counts()`, `isna().sum()`. Pięć metod, które odpalicie na KAŻDYM nowym datasecie."
> "4. **Selekcja kolumn** — jedna kolumna = Series, wiele kolumn = DataFrame."

> "To co dzisiaj robiliście to **EDA — Exploratory Data Analysis**. W każdym projekcie analitycznym pierwsza godzina to EDA. Zanim odpowiecie na jakiekolwiek pytanie biznesowe — musicie znać swoje dane."

> "Następny tydzień: **Pandas — selekcja i filtrowanie**. `loc`, `iloc`, warunki logiczne, sortowanie. Zaczniecie odpowiadać na pytania: 'Pokaż mi rachunki powyżej 30 dolarów z soboty, niepalących, posortowane malejąco'."

**Zadanie domowe (nieoceniane):**
> "Znajdźcie dowolny dataset CSV w internecie (Kaggle, seaborn-data na GitHubie, dane.gov.pl). Wczytajcie go w notebooku. Zróbcie pełną eksplorację: shape, head, info, describe, value_counts na 2-3 kolumnach. Napiszcie 3 obserwacje o danych. Wrzućcie notebook na GitHub."
