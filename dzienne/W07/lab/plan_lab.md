# L07 — Plan laboratorium dla prowadzącego

## Temat: Pandas — czyszczenie danych

**Programowanie w Pythonie II** | Laboratorium 7
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne przy komputerze
**Prowadzący:** doktorant (laboratoria prowadzone samodzielnie)

---

## Efekty uczenia się (Bloom)

Po tych zajęciach osoba studiująca:
1. **Identyfikuje** brakujące wartości w DataFrame metodami `isna()` i `info()` (Bloom 2)
2. **Stosuje** `fillna()` i `dropna()` z uzasadnionym wyborem strategii (Bloom 3)
3. **Wykrywa i usuwa** duplikaty metodami `duplicated()` i `drop_duplicates()` (Bloom 3)
4. **Konwertuje** typy danych: teksty na liczby i daty (`pd.to_numeric`, `pd.to_datetime`) (Bloom 3)
5. **Czyści** kolumny tekstowe używając `str.strip()`, `str.title()`, `str.replace()`, `str.contains()` (Bloom 3)
6. **Buduje** kompletny pipeline czyszczenia od brudnych danych do gotowych do analizy (Bloom 4)

---

## Plan minutowy

| Czas | Etap | Opis | Uwagi |
|------|------|------|-------|
| 0:00-0:05 | Organizacja | Sprawdzenie listy, weryfikacja środowiska | Otwierają VS Code + .venv |
| 0:05-0:10 | Wprowadzenie | Kontekst: czyszczenie = 60-80% pracy analityka | Krótko, bez live coding |
| 0:10-0:30 | Ćwiczenie 1 | Brakujące wartości (isna, fillna, dropna) | Para + samodzielnie |
| 0:30-0:50 | Ćwiczenie 2 | Duplikaty + konwersja typów | Samodzielnie |
| 0:50-1:20 | Ćwiczenie 3 | Pełny pipeline czyszczenia — samodzielna praca | Samodzielnie |
| 1:20-1:35 | Ćwiczenie 4 | Operacje tekstowe + commit | Samodzielnie |
| 1:35-1:45 | Podsumowanie | Omówienie wyników, zapowiedź L08 | Dyskusja |

---

## Organizacja sali

- Studenci pracują w parach (pair programming) lub samodzielnie — do wyboru
- Plik ćwiczeń: `cwiczenia.md` — studenci tworzą własny notebook `.ipynb`
- Notebook nazywają: `lab07_cleaning.ipynb`
- Commit na koniec zajęć (Ćwiczenie 4)

### Środowisko
```bash
# Aktywacja środowiska
cd ~/python2_projekt
source .venv/bin/activate   # Linux/Mac
# lub
.venv\Scripts\activate      # Windows

# Otwarcie VS Code
code .
```

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przed zajęciami (10 min wcześniej)
- [ ] Sprawdź, czy sala ma działający internet (dataset wczytywany z kodu, ale też lokalnie)
- [ ] Miej gotowy własny notebook z rozwiązaniami (do podglądu gdy student utknął)
- [ ] Przygotuj plik z datasetu do wklejenia (jeśli internet nie działa — patrz niżej)

### Błąd krytyczny: brak internetu w sali
Jeśli nie ma internetu, dataset można wczytać z kodu (definicja w `cwiczenia.md`).
Dataset jest zdefiniowany bezpośrednio jako Python dict — nie wymaga pobierania.

### Podczas zajęć
- Pierwsze 5 min: sprawdź czy wszyscy uruchomili notebook i wczytali dane
- Ćwiczenie 3 (pipeline) — najtrudniejsze, studenci mogą potrzebować wskazówek
- Nie dawaj gotowego kodu — naprowadzaj pytaniami: "Co chcesz zrobić? Jakiej metody użyć?"

### Tempo grup
- Szybcy studenci: zachęć do Ćwiczenia 3, punkt "Rozszerzenie biznesowe"
- Wolni studenci: Ćwiczenie 1 + 2 + commit wystarczą — 3 i 4 na plus

---

## Tabela rozwiązywania problemów (Troubleshooting)

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `AttributeError: Can only use .str accessor with string values` | Kolumna już jest numeryczna lub ma mieszane typy | Sprawdź `df.dtypes`. Jeśli kolumna ma typ `float64`, nie potrzeba `.str`. Jeśli `object` z mieszanymi typami: `df['kol'].astype(str).str.strip()` |
| `ValueError: could not convert string to float: 'brak'` | Użyto `astype(float)` zamiast `pd.to_numeric(errors='coerce')` | Zamień na `pd.to_numeric(df['kol'], errors='coerce')`. Wcześniej też `replace('brak', np.nan)` |
| `SettingWithCopyWarning` | Modyfikacja kopii fragmentu DataFrame | Użyj `.copy()` po filtrowaniu: `df2 = df[...].copy()`, potem modyfikuj `df2` |
| `KeyError: 'kolumna'` | Literówka w nazwie kolumny | Sprawdź `df.columns.tolist()`. Nazwy są case-sensitive |
| `TypeError: '<' not supported between instances of 'str' and 'float'` | Mieszane typy w kolumnie — część to string, część NaN | `df['kol'] = pd.to_numeric(df['kol'], errors='coerce')` |
| `df.duplicated().sum()` zwraca 0, a dane wyglądają na duplikaty | Duplikaty w podzbiorze kolumn, nie pełne wiersze | `df.duplicated(subset=['id'])` — sprawdź konkretne kolumny |
| `pd.to_datetime()` daje NaT dla wszystkich wartości | Format daty niezgodny | Dodaj `format=` : `pd.to_datetime(df['data'], format='%d.%m.%Y', errors='coerce')` |
| `df.shape` ma inny kształt niż oczekiwany | Duplikaty nie zostały usunięte lub indeks się nie zresetował | Sprawdź `df.duplicated().sum()`. Po `drop_duplicates()` zrób `reset_index(drop=True)` |
| `str.title()` zamienia 'IT' na 'It' | `title()` konwertuje wszystko — wielka tylko pierwsza litera | Po `str.title()` zrób `str.replace('It', 'IT', regex=False)` i `str.replace('Hr', 'HR', regex=False)` |
| `fillna()` nie zmienia NaN | Nie przypisano wyniku z powrotem | `df['kol'] = df['kol'].fillna(wartosc)` — trzeba przypisać! (lub `inplace=True`) |
| `isna()` nie wykrywa 'brak', 'N/A', '-' | To są poprawne stringi, nie NaN | Najpierw `df['kol'].replace({'brak': np.nan, 'N/A': np.nan}, inplace=True)` |

---

## Weryfikacja wyników — klucz odpowiedzi

### Ćwiczenie 1 (Brakujące wartości)
- Całkowita liczba NaN w oryginalnym df: **8** (6 w ocena_roczna + 1 None w wynagrodzenie + 1 None w data_zatrudnienia)
- NaN w wynagrodzenie po `replace('brak', np.nan)` + `to_numeric`: **2**
- Mediana wynagrodzenia (przed fillna): **5150.0**
- Średnia ocena_roczna (przed fillna): **4.34** (zaokrąglona do 2 miejsc)
- Liczba wierszy po `dropna(subset=['data_zatrudnienia'])`: **29**

### Ćwiczenie 2 (Duplikaty + typy)
- Pełne duplikaty (wiersze): **5**
- Po `drop_duplicates()`: **25 wierszy**
- Typ data_zatrudnienia po konwersji: **datetime64[ns]**
- Unikalne lata zatrudnienia: **2017, 2018, 2019, 2020, 2021, 2022, 2023**
- Pracownicy zatrudnieni >= 2021: **10**
- Pracownicy z wynagrodzeniem > 6000: **7**

### Ćwiczenie 3 (Pipeline)
- Shape po pełnym pipeline: **(25, 6)**
- NaN w data_zatrudnienia (zostaje): **1**
- Unikalne działy po czyszczeniu: **HR, IT, Sprzedaz** (3)
- Wynagrodzenie dtype: **float64**

### Ćwiczenie 4 (Stringi)
- Imiona pisane WSZYSTKIMI WIELKIE: **4** (CELINA, HENRYK, OLGA + jedna z duplikatów)
- Imiona zaczynające się małą literą: **5** (darek, irena, norbert, sławek + duplikat)
- Wiersze zawierające 'sprzedaz' w dziale (case-insensitive): **10**

---

## Zapowiedź L08

> "Na kolejnych zajęciach: merge (łączenie DataFramów — jak JOIN w SQL), groupby (agregacja po grupach), pivot_table. To są narzędzia do właściwej analizy — dlatego musieliśmy najpierw nauczyć się czyszczenia."
