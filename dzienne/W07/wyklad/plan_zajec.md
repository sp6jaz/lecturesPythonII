# W07 Wykład — Plan zajęć dla prowadzącego

## Temat: Pandas — czyszczenie danych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z pandas/numpy
- **Przed wykładem:** otwórz `pandas_cleaning_demo.ipynb`
- **Kontekst:** Zajęcia po przerwie wielkanocnej

### Efekty uczenia się (Bloom)
Po tym wykładzie osoba studiująca:
1. **Identyfikuje** brakujące wartości w DataFrame metodami `isna()`, `isnull()`, `info()` (Bloom 2)
2. **Stosuje** strategie uzupełniania braków: `fillna()`, `dropna()` z uzasadnieniem wyboru (Bloom 3)
3. **Wykrywa i usuwa** duplikaty metodami `duplicated()`, `drop_duplicates()` (Bloom 3)
4. **Konwertuje** typy danych metodami `astype()`, `pd.to_numeric()`, `pd.to_datetime()` (Bloom 3)
5. **Czyści** kolumny tekstowe operacjami `str.lower()`, `str.strip()`, `str.replace()`, `str.contains()` (Bloom 3)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W06 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | Po przerwie wielkanocnej — czyszczenie danych | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Brakujące wartości — isna, dropna, fillna | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | Duplikaty — duplicated, drop_duplicates | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | Konwersja typów — astype, to_datetime, to_numeric | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Operacje na tekstach — str.lower, strip, replace, contains | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Wyczyszczenie brudnego datasetu | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Przejście do W08: merge, groupby, pivot | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W06)

> "Pięć pytań z zeszłego tygodnia — zanim przerwa wielkanocna wymaże nam pamięć."

**[Użyj quiz_w06.md]**

Pytania losuj lub wyświetl jedno po drugim na projektorze. Daj 3 minuty, potem omów odpowiedzi.

> "Odpowiedzi: 1-B, 2-B, 3-B, 4-B, 5-B. Kto miał 5/5? Kto 4? Dobra robota."

---

### 0:05-0:10 — WPROWADZENIE

> "Witamy po przerwie wielkanocnej. Mam nadzieję, że odpoczęliście. Dzisiaj wracamy do Pandy i zajmujemy się czymś, co każdy analityk danych dobrze zna — czyszczeniem danych."

> "Kiedy dostaniecie plik CSV z prawdziwymi danymi — z ERP firmy, z eksportu z Excela, z ankiety online — to data będzie brudna. Gwarantuję. Brakujące wartości, duplikaty, liczby zapisane jako tekst, 'IT' zapisane 50 razy na 50 różnych sposobów: 'IT', 'it', 'It', 'it ', '  IT'. To jest rzeczywistość pracy analityka."

> "W badaniach branżowych mówi się, że analityk spędza 60-80% czasu na czyszczeniu danych, a tylko 20-40% na właściwej analizie. Niektórzy mówią 90/10. Więc to nie jest nudna część — to jest większość waszej pracy."

> "Dzisiaj poznacie wszystkie kluczowe narzędzia: brakujące wartości, duplikaty, konwersja typów, operacje tekstowe. Będziecie pracować z brudnym datasetem działu HR — 30 pracowników, dużo problemów."

**[Wyświetl schemat na tablicy lub projektorze]**

```
Brudne dane
    │
    ├── Brakujące wartości (NaN) → isna / fillna / dropna
    ├── Duplikaty → duplicated / drop_duplicates
    ├── Złe typy → astype / to_numeric / to_datetime
    └── Brudny tekst → str.strip / str.lower / str.replace
    │
Czyste dane → Analiza
```

---

### 0:10-0:30 — MATERIAŁ 1: Brakujące wartości (20 min)

**[Otwórz notebook — komórka 1]**

> "Zaczynamy od wczytania brudnego datasetu HR. Stworzyłem go specjalnie na te zajęcia — odzwierciedla typowe problemy, jakie spotykacie w prawdziwych danych."

```python
import pandas as pd
import numpy as np

# Brudny dataset HR — typowy eksport z systemu ERP
data = {
    'id_pracownika': [1,2,3,4,5,6,7,8,9,10,
                      11,12,13,14,15,16,17,18,19,20,
                      3,7,12,18,5,   # duplikaty!
                      21,22,23,24,25],
    'imie': ['Anna', 'Bartek', 'CELINA', 'darek', 'Ewa',
             'Filip', 'Gosia', 'HENRYK', 'irena', 'Jan',
             'Kasia', 'Leszek', 'Marta', 'norbert', 'OLGA',
             'Piotr', 'Renata', 'sławek', 'Teresa', 'Urszula',
             'CELINA', 'Gosia', 'Leszek', 'sławek', 'Ewa',
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

> "30 wierszy, 6 kolumn. Dane działu HR pewnej firmy. Widać już pierwsze problemy — wynagrodzenie to tekst, nie liczba. Imiona pisane różnie. Ale żeby zobaczyć wszystkie problemy, musimy użyć narzędzi diagnostycznych."

**[Komórka 2 — diagnoza]**

```python
# Pierwsza diagnoza — info() pokazuje typy i braki
print("=== INFO ===")
df.info()

print("\n=== BRAKUJĄCE WARTOŚCI ===")
print(df.isna().sum())

print("\n=== PROCENT BRAKÓW ===")
print((df.isna().sum() / len(df) * 100).round(1))
```

> "Patrzcie — `info()` od razu mówi nam kilka rzeczy: wynagrodzenie jest typu `object` (tekst!), data_zatrudnienia też. To są liczby i daty zapisane jako stringi — klasyczny problem z eksportem z Excela lub starych systemów."

> "`isna().sum()` — liczba NaN per kolumna. ocena_roczna ma 6 braków — 20% danych. To dużo. wynagrodzenie ma 1 brak (None w Pythonie → NaN w Pandas). Ale uwaga — jedno wynagrodzenie ma wartość 'brak' zamiast NaN! `isna()` tego nie wykryje."

**[Komórka 3 — isna w szczegółach]**

```python
# isna() / isnull() — to samo, dwa warianty nazwy
print("isna() == isnull():", df.isna().equals(df.isnull()))

# Mapa braków — True tam gdzie NaN
print("\nMapa braków (pierwsze 10 wierszy):")
print(df.isna().head(10))

# Wiersze z JAKIMKOLWIEK brakiem
wiersze_z_brakiem = df[df.isna().any(axis=1)]
print(f"\nWiersze z przynajmniej jednym NaN: {len(wiersze_z_brakiem)}")
print(wiersze_z_brakiem)
```

> "`isna()` na całym DataFrame daje tabelę True/False. `any(axis=1)` — True jeśli JAKIKOLWIEK element w wierszu jest True. Czyli: pokaż mi wiersze z przynajmniej jednym brakiem."

**[Komórka 4 — dropna]**

```python
# dropna — usuwa wiersze z brakującymi wartościami

# Domyślnie: usuwa wiersz jeśli MA JAKIKOLWIEK NaN
df_clean_drop = df.dropna()
print(f"Przed dropna: {len(df)}")
print(f"Po dropna (domyślnie): {len(df_clean_drop)}")

# subset= — usuwa tylko jeśli NaN jest w KONKRETNYCH kolumnach
df_clean_subset = df.dropna(subset=['data_zatrudnienia'])
print(f"Po dropna(subset=['data_zatrudnienia']): {len(df_clean_subset)}")

# thresh= — usuwa jeśli mniej niż thresh wartości NIE-NaN
df_thresh = df.dropna(thresh=5)  # co najmniej 5 kolumn z wartościami
print(f"Po dropna(thresh=5): {len(df_thresh)}")
```

> "Ważna decyzja: kiedy usuwać, a kiedy uzupełniać? Jeśli 80% klientów nie podało adresu email — usuwamy kolumnę. Jeśli 5% produktów nie ma ceny — możemy uzupełnić medianą lub usunąć te wiersze. Kontekst biznesowy decyduje."

**[Komórka 5 — fillna, strategie]**

```python
# fillna — uzupełnia NaN wartością

# Strategia 1: stała wartość
df_s1 = df.copy()
df_s1['ocena_roczna'] = df_s1['ocena_roczna'].fillna(0)
print("fillna(0):", df_s1['ocena_roczna'].isna().sum(), "braków")

# Strategia 2: średnia (numeryczne, symetryczny rozkład)
df_s2 = df.copy()
srednia = df_s2['ocena_roczna'].mean()
df_s2['ocena_roczna'] = df_s2['ocena_roczna'].fillna(srednia)
print(f"fillna(mean={srednia:.2f}):", df_s2['ocena_roczna'].isna().sum(), "braków")

# Strategia 3: mediana (lepsza przy wartościach odstających)
df_s3 = df.copy()
mediana = df_s3['ocena_roczna'].median()
df_s3['ocena_roczna'] = df_s3['ocena_roczna'].fillna(mediana)
print(f"fillna(median={mediana:.2f}):", df_s3['ocena_roczna'].isna().sum(), "braków")

# Strategia 4: wartość z poprzedniego wiersza (szeregi czasowe)
df_s4 = df.copy()
df_s4['ocena_roczna'] = df_s4['ocena_roczna'].ffill()
print("ffill():", df_s4['ocena_roczna'].isna().sum(), "braków")
```

> "Cztery strategie — każda ma swoje miejsce:"
> "- Stała wartość: jeśli brak = 'nie dotyczy'. Np. brak alergenów w produktach spożywczych → 0."
> "- Średnia: klasyczna imputation dla symetrycznych danych. Używajcie gdy nie ma mocnych wartości odstających."
> "- Mediana: lepsza gdy mamy outliers. Np. wynagrodzenia — jeden CEO nie psuje mediany, ale psuje średnią."
> "- `ffill()` (forward fill): dla szeregów czasowych — brak dziennego raportu? Wziął wartość z dnia poprzedniego. W HR i finansach popularne."

---

### 0:30-0:45 — MATERIAŁ 2: Duplikaty (15 min)

> "Duplikaty. Drugi wielki wróg czystych danych. W naszym datasecie mamy 30 wierszy, ale 5 z nich to duplikaty — ten sam pracownik zapisany dwa razy."

**[Komórka 6 — wykryj duplikaty]**

```python
# duplicated() — zwraca Series True/False
# True = wiersz jest duplikatem (był już wcześniej)

print("Liczba zduplikowanych wierszy:", df.duplicated().sum())

# Pokaż duplikaty
print("\nZduplikowane wiersze:")
print(df[df.duplicated()])

# Wyświetl oryginał + duplikat razem (keep=False)
print("\nOryginały I duplikaty (keep=False):")
print(df[df.duplicated(keep=False)].sort_values('id_pracownika').head(10))
```

> "Domyślnie `duplicated()` oznacza jako duplikat DRUGI i kolejne wystąpienia — pierwszy zostawia. `keep=False` oznacza WSZYSTKIE wystąpienia. Wtedy możecie porównać oryginał z duplikatem."

> "W naszym datasecie: wiersze 20-24 (id 3, 7, 12, 18, 5) to duplikaty wierszy 2, 6, 11, 17, 4. Dokładnie te same wartości — ktoś dwa razy zaimportował te same dane."

**[Komórka 7 — duplikaty w podzbiorze]**

```python
# Czasem duplikat to samo id, ale inne dane (np. aktualizacja)
# Możemy sprawdzić duplikaty tylko po wybranych kolumnach

print("Duplikaty wg id_pracownika:")
print(df.duplicated(subset=['id_pracownika']).sum())

# Możemy też sprawdzić ile razy pojawia się każde id
print("\nLiczność id_pracownika:")
print(df['id_pracownika'].value_counts().sort_index().head(10))
```

> "Ważne rozróżnienie: czy duplikat to ta sama informacja (błąd importu) czy inna informacja (np. pracownik zmienił dział). W tym przypadku te same dane — czysty błąd."

**[Komórka 8 — usuń duplikaty]**

```python
# drop_duplicates() — usuwa zduplikowane wiersze

przed = len(df)
df_bez_dup = df.drop_duplicates()
print(f"Przed: {przed}, po: {len(df_bez_dup)}")

# keep= kontroluje które zostawić
# keep='first' (domyślnie) — zostaw pierwsze wystąpienie
# keep='last' — zostaw ostatnie (przydatne gdy późniejszy = aktualniejszy)
# keep=False — usuń WSZYSTKIE duplikaty

df_keep_last = df.drop_duplicates(keep='last')
print(f"Po drop_duplicates(keep='last'): {len(df_keep_last)}")

# subset= — duplikat tylko jeśli te kolumny się powtarzają
df_subset = df.drop_duplicates(subset=['id_pracownika'])
print(f"Po drop_duplicates(subset=['id_pracownika']): {len(df_subset)}")
```

> "W naszym przypadku wynik jest ten sam dla wszystkich opcji — 25 unikalnych pracowników. Ale w realnych danych: jeśli masz dane sprzedażowe zaktualizowane co dzień — zostawiasz `keep='last'` (najnowszy rekord)."

**[Komórka 9 — reset_index po czyszczeniu]**

```python
# Po usunięciu wierszy — indeks ma 'dziury'
df_clean = df.drop_duplicates().copy()
print("Indeks po drop_duplicates:")
print(df_clean.index.tolist())

# Resetujemy indeks
df_clean = df_clean.reset_index(drop=True)
print("\nIndeks po reset_index:")
print(df_clean.index.tolist()[:10])
print(f"Shape: {df_clean.shape}")
```

> "Po usunięciu duplikatów indeks ma 'dziury': 0, 1, 2, 3, 4, ... 19, 25, 26, ... Żeby mieć czyste 0-24, robimy `reset_index(drop=True)`. `drop=True` — stary indeks wyrzucamy, nie potrzebujemy go jako kolumny."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: Konwersja typów (20 min)

> "Wracamy. Trzecia kategoria problemów: złe typy danych. Wynagrodzenie zapisane jako string, daty jako text, kategorie jako liczby. Pandas nie może liczyć średniej ze stringów."

**[Komórka 10 — diagnoza typów]**

```python
# Wróćmy do oryginalnego df (z duplikatami już usuniętymi)
df_work = df.drop_duplicates().reset_index(drop=True).copy()

print("Typy danych:")
print(df_work.dtypes)
print()

# Problem 1: wynagrodzenie jako object (string)
print("Wynagrodzenie — sample:")
print(df_work['wynagrodzenie'].head(10).tolist())
print(f"Typ: {df_work['wynagrodzenie'].dtype}")

# Czy można obliczać?
try:
    print(df_work['wynagrodzenie'].mean())
except Exception as e:
    print(f"Błąd: {e}")
```

> "Klasyczny problem z eksportem z Excela lub starego systemu. Liczby jako tekst. Nie możecie policzyć średniej — dostaniecie błąd lub złe wyniki."

**[Komórka 11 — astype, ale z problemem]**

```python
# astype() — prosta konwersja, ale wymaga czystych danych

# Najpierw sprawdźmy co mamy
print("Unikalne wartości wynagrodzenia:")
print(sorted(df_work['wynagrodzenie'].unique()))

# astype(float) wywali błąd gdy są 'brak' lub None
try:
    df_work['wynagrodzenie'].astype(float)
except ValueError as e:
    print(f"\nBłąd astype(float): {e}")

# Musimy najpierw naprawić 'brak'
df_work['wynagrodzenie'] = df_work['wynagrodzenie'].replace('brak', np.nan)
print("\nPo replace 'brak' → NaN:")
print(df_work['wynagrodzenie'].isna().sum(), "braków")
```

> "`astype()` to prosta konwersja — działa gdy dane są czyste. Ale jeśli jest choćby jedno 'brak', 'N/A', '-' zamiast NaN — astype wywali błąd. Dlatego musimy najpierw wyczyścić wartości tekstowe."

**[Komórka 12 — pd.to_numeric z errors='coerce']**

```python
# pd.to_numeric() — bezpieczna konwersja na liczby
# errors='coerce' — zamiast błędu wstawia NaN gdy konwersja niemożliwa

df_work['wynagrodzenie'] = pd.to_numeric(df_work['wynagrodzenie'], errors='coerce')
print(f"Typ po to_numeric: {df_work['wynagrodzenie'].dtype}")
print(f"NaN po konwersji: {df_work['wynagrodzenie'].isna().sum()}")
print(f"Średnie wynagrodzenie: {df_work['wynagrodzenie'].mean():.2f}")

# Uzupełniamy braki medianą
mediana_wyn = df_work['wynagrodzenie'].median()
df_work['wynagrodzenie'] = df_work['wynagrodzenie'].fillna(mediana_wyn)
print(f"Po fillna(mediana={mediana_wyn}): {df_work['wynagrodzenie'].isna().sum()} braków")
```

> "`errors='coerce'` — kluczowy parametr. Zamiast rzucić błąd dla wartości których nie da się zamienić na liczbę, wstawia NaN. Potem możecie te NaN obsłużyć fillna. Bezpieczny, zalecany sposób."

**[Komórka 13 — pd.to_datetime]**

```python
# pd.to_datetime() — konwersja stringów na daty
print("data_zatrudnienia przed konwersją:")
print(df_work['data_zatrudnienia'].head(5))
print(f"Typ: {df_work['data_zatrudnienia'].dtype}")

# Konwersja
df_work['data_zatrudnienia'] = pd.to_datetime(df_work['data_zatrudnienia'], errors='coerce')
print(f"\nTyp po konwersji: {df_work['data_zatrudnienia'].dtype}")
print(df_work['data_zatrudnienia'].head(5))

# Dostęp do elementów daty — .dt accessor
df_work['rok_zatrudnienia'] = df_work['data_zatrudnienia'].dt.year
df_work['miesiac_zatrudnienia'] = df_work['data_zatrudnienia'].dt.month
print(f"\nLata zatrudnienia: {sorted(df_work['rok_zatrudnienia'].dropna().unique().astype(int).tolist())}")
```

> "`pd.to_datetime()` z `errors='coerce'` — daty których nie da się sparsować → NaN. Po konwersji możecie używać `.dt` accessor: `.dt.year`, `.dt.month`, `.dt.day`, `.dt.dayofweek`. To otwiera analizy temporalne — kto był zatrudniony w którym roku, ile dni minęło od zatrudnienia, itp."

**[Komórka 14 — astype dla kategorii]**

```python
# astype('category') — dla kolumn z ograniczoną liczbą unikalnych wartości

# Najpierw wyczyśćmy dzial (o tym w MATERIAŁ 4, ale podglądamy)
df_work['dzial'] = df_work['dzial'].str.strip().str.title()
print("Unikalne działy:", df_work['dzial'].unique())

# Zamiana na typ category
df_work['dzial'] = df_work['dzial'].astype('category')
print(f"\nTyp po astype('category'): {df_work['dzial'].dtype}")
print(f"Kategorie: {df_work['dzial'].cat.categories.tolist()}")

# Porównanie pamięci
import sys
przed = sys.getsizeof(df['dzial'])
po = sys.getsizeof(df_work['dzial'])
print(f"\nPamięć przed: {przed} B, po: {po} B")
```

> "Typ `category` to specjalne kodowanie Pandas — zamiast trzymać string 30 razy, trzyma go raz i używa liczby. Oszczędność pamięci przy dużych danych. Warto używać gdy kolumna ma mniej niż ~20 unikalnych wartości."

---

### 1:15-1:25 — MATERIAŁ 4: Operacje na tekstach (10 min)

> "Ostatni dział: brudne teksty. Dane z ankiet, pól formularzy, exportów — są pełne literówek, wielkich liter, spacji. Pandas ma cały zestaw metod `str.` do czyszczenia."

**[Komórka 15 — str. podstawy]**

```python
# .str — accessor dla operacji na stringach

print("Imiona przed czyszczeniem (sample):")
print(df['imie'].head(10).tolist())

# str.lower() — wszystkie małe
print("\nstr.lower():", df['imie'].str.lower().head(5).tolist())

# str.upper() — wszystkie wielkie
print("str.upper():", df['imie'].str.upper().head(5).tolist())

# str.title() — Pierwsza Litera Wielka
print("str.title():", df['imie'].str.title().head(5).tolist())

# str.strip() — usuwa spacje na początku i końcu
test = pd.Series(['  Anna  ', 'Bartek ', ' CELINA'])
print("\nstr.strip():", test.str.strip().tolist())
```

> "`str.` accessor — każda metoda stringowa Pythona dostępna dla całej kolumny. `lower()`, `upper()`, `title()`, `strip()`. Nie musicie pisać pętli for — Pandas robi to dla każdego elementu."

**[Komórka 16 — str.replace, str.contains]**

```python
# str.replace() — zamiana tekstu
# Normalizujemy nazwy działów
df_work['dzial'] = df_work['dzial'].str.strip().str.title()
print("Po title():", df_work['dzial'].unique())

# str.replace żeby zamienić 'Hr' → 'HR', 'It' → 'IT'
df_work['dzial'] = df_work['dzial'].str.replace('Hr', 'HR', regex=False)
df_work['dzial'] = df_work['dzial'].str.replace('It', 'IT', regex=False)
print("Po replace:", df_work['dzial'].unique())

# str.contains() — filtrowanie po zawartości
sprzedaz = df_work[df_work['dzial'].str.contains('Sprzedaz', na=False)]
print(f"\nPracownicy w Sprzedaży: {len(sprzedaz)}")
```

> "`str.replace()` — find and replace dla całej kolumny. `regex=False` gdy szukacie dokładnego tekstu. `str.contains()` — filtrowanie: pokaż wiersze gdzie tekst zawiera dany ciąg. Parametr `na=False` sprawia, że NaN traktowane jako False (nie rzuca błędu)."

**[Komórka 17 — kompletne czyszczenie tekstów]**

```python
# Kompletne czyszczenie kolumn tekstowych
df_final = df.drop_duplicates().reset_index(drop=True).copy()

# Imiona: strip + title
df_final['imie'] = df_final['imie'].str.strip().str.title()
print("Imiona po czyszczeniu:", df_final['imie'].tolist()[:10])

# Działy: strip + title + replace
df_final['dzial'] = df_final['dzial'].str.strip().str.title()
df_final['dzial'] = df_final['dzial'].str.replace('Hr', 'HR', regex=False)
df_final['dzial'] = df_final['dzial'].str.replace('It', 'IT', regex=False)
print("\nDziały po czyszczeniu:", sorted(df_final['dzial'].unique()))

# Weryfikacja
print(f"\nUnikalnych działów: {df_final['dzial'].nunique()}")
print(df_final['dzial'].value_counts())
```

> "Teraz dane są czyste. 'Sprzedaz', 'HR', 'IT' — każdy dział ma dokładnie jedną formę zapisu. Moglibyśmy teraz policzyć średnie wynagrodzenia per dział, porównać oceny — i wyniki będą poprawne."

---

### 1:25-1:35 — AKTYWNOŚĆ: Wyczyszczenie brudnego datasetu (10 min)

> "Wasza kolej. Macie 10 minut żeby przeprowadzić kompletny pipeline czyszczenia na naszym datasecie."

**[Wyświetl na projektorze]**

```python
# ZADANIE — Przeprowadź pełny pipeline czyszczenia:
# Użyj oryginalnego df (zdefiniowanego na początku)

df_zadanie = df.copy()

# Krok 1: Zamień 'brak' na NaN i skonwertuj wynagrodzenie na float
# Krok 2: Wypełnij NaN w wynagrodzeniu medianą
# Krok 3: Wypełnij NaN w ocena_roczna średnią (zaokrąglij do 2 miejsc)
# Krok 4: Usuń duplikaty (pełne wiersze)
# Krok 5: Wyczyść imie (strip + title)
# Krok 6: Wyczyść dzial (strip + title + replace Hr→HR, It→IT)
# Krok 7: Skonwertuj data_zatrudnienia na datetime

# Po czyszczeniu sprawdź:
# a) df_zadanie.shape — powinno być (25, 6)
# b) df_zadanie.dtypes — wynagrodzenie: float64, data_zatrudnienia: datetime64
# c) df_zadanie.isna().sum() — maximum 1 NaN (w data_zatrudnienia)
# d) df_zadanie['dzial'].unique() — ['HR', 'IT', 'Sprzedaz']
```

**Oczekiwane wyniki:**
- Shape: (25, 6)
- Wynagrodzenie — float64, bez NaN
- data_zatrudnienia — datetime64, 1 NaN (jedna osoba bez daty)
- Działy: HR, IT, Sprzedaz (3 unikalne)

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy cztery obszary czyszczenia danych:"

> "**1. Brakujące wartości** — `isna()` do diagnozy, `dropna()` gdy wiersz bezużyteczny, `fillna()` ze strategią (stała / średnia / mediana / ffill). Mediana lepsza niż średnia przy wartościach odstających."

> "**2. Duplikaty** — `duplicated()` do wykrycia, `drop_duplicates()` do usunięcia. Zawsze resetować indeks po usunięciu."

> "**3. Konwersja typów** — `pd.to_numeric(errors='coerce')` i `pd.to_datetime(errors='coerce')` — zawsze z `errors='coerce'` dla bezpieczeństwa. `astype('category')` dla danych kategorycznych — oszczędza pamięć."

> "**4. Czyszczenie tekstów** — `str.strip()` usuwa spacje, `str.lower()`/`str.title()` normalizuje wielkość liter, `str.replace()` zamienia tekst, `str.contains()` filtruje."

> "Te cztery kroki to standardowy pipeline czyszczenia. W prawdziwym projekcie robicie to na samym początku — przed jakąkolwiek analizą."

> "Następny tydzień: **W08 — merge, groupby, pivot**. Nauczycie się łączyć DataFramy (merge jak JOIN w SQL), agregować dane po grupach (groupby), i tworzyć tabele przestawne (pivot_table). Ale to tylko wtedy gdy dane są czyste — dlatego dzisiejszy wykład był niezbędny."

**Zadanie domowe (nieoceniane):**
> "Wczytajcie dowolny publiczny dataset CSV z Kaggle lub data.gov. Uruchomcie pipeline diagnostyczny: info(), isna().sum(), duplicated().sum(). Zobaczcie co macie. Notebook na GitHub."
