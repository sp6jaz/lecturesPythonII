# W08 Laboratorium — Plan zajęć dla prowadzącego (doktoranta)

## Temat: Pandas — łączenie i agregacja (merge, groupby, pivot)

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** samodzielna praca przy komputerze, para programming dozwolony
- **Sala:** laboratorium komputerowe z VS Code
- **Wymagane:** Python + venv z pandas/numpy, dostęp do GitHub
- **Plik dla studentów:** `cwiczenia.md` — udostępnij przez Moodle lub Teams przed zajęciami

---

## Przydatne linki dla prowadzącego

- [Pandas — Merge, join, concatenate](https://pandas.pydata.org/docs/user_guide/merging.html)
- [Pandas — Group by](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [Pandas — Pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html)

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przygotowanie przed zajęciami (15 min przed)
1. Upewnij się, że środowisko działa: `python -c "import pandas; print(pandas.__version__)"`
2. Sprawdź, czy studenci mają dostęp do pliku `cwiczenia.md`
3. Miej gotowe rozwiązania wszystkich ćwiczeń (poniżej + w cwiczenia.md)
4. Przygotuj plik weryfikacyjny `verify_w08.py` na wypadek gdyby ktoś miał błędne wyniki

### Struktura laboratorium

| Czas | Etap | Treść |
|------|------|-------|
| 0:00-0:05 | **Wstęp** | Organizacja, cel, przypomnienie z wykładu |
| 0:05-0:25 | **Ćwiczenie 1** | merge — łączenie tabel (20 min) |
| 0:25-0:45 | **Ćwiczenie 2** | groupby — agregacja KPI (20 min) |
| 0:45-0:75 | **Ćwiczenie 3** | Pełna analiza — merge + groupby + pivot (30 min) |
| 0:75-0:90 | **Ćwiczenie 4** | pivot_table, crosstab, commit (15 min) |

### Jak prowadzić zajęcia

**Zasada pierwsza: daj czas**
- Ćwiczenia są zaprojektowane tak, żeby było ciasno z czasem — to zamierzone
- Jeśli student skończy wcześniej, ma "wyzwanie dodatkowe" w każdym ćwiczeniu
- Nie śpiesz grupy — ważniejsze jest rozumienie niż przebrnięcie przez wszystko

**Zasada druga: scaffolding**
- Każde ćwiczenie ma kod startowy — studenci nie zaczynają od zera
- Sprawdzenie jest po każdym podpunkcie — szybka informacja zwrotna
- Jeśli ktoś utknął na tym samym miejscu — daj 2-minutową wskazówkę całej grupie

**Zasada trzecia: commit na koniec**
- Każde ćwiczenie to osobna komórka w notebooku
- Na koniec zajęć: `git add . && git commit -m "W08: merge, groupby, pivot"`
- Brak commita = brak zaliczenia ćwiczenia

### Pair programming
- Studenci mogą pracować w parach: **pilot** (pisze kod) + **navigator** (czyta instrukcję, podpowiada, sprawdza)
- Co 15-20 minut zamiana ról
- Pair programming zmniejsza frustrację i przyspiesza naukę — zachęcaj, ale nie wymuszaj

---

## Ścieżka prowadzenia — co mówić

### 0:00-0:05 — Wstęp

> "Na wykładzie poznaliście merge, concat, groupby i pivot_table. Dzisiaj to ćwiczymy — na tych samych danych co wykład, ale z nowymi pytaniami."

> "Otwórzcie VS Code, nowy notebook `W08_lab.ipynb`. Pierwsze ćwiczenie musi być gotowe w 20 minut."

> "Pracujecie samodzielnie lub w parach. Na końcu każdego ćwiczenia jest sekcja Sprawdzenie — porównajcie swoje wyniki z podanymi liczbami. Jeśli się różni — jest błąd do znalezienia."

---

### 0:05-0:25 — Ćwiczenie 1 (obserwuj, pomagaj gdy ≥3 osoby mają ten sam problem)

**Najczęstsze problemy i odpowiedzi:**

Patrz tabela Troubleshooting poniżej.

**Po 20 minutach:**
> "Wszyscy widzą wynik 20 wierszy po merge inner? Kto dostał inną liczbę — sprawdź left_on i right_on."

---

### 0:25-0:45 — Ćwiczenie 2 (groupby — tu studenci często się gubią)

**Obserwuj:** czy studenci wiedzą, że wynik groupby to Series, nie DataFrame — i jak dodać `.reset_index()`

> "Jeśli wasz raport segmentów nie ma tytułów kolumn tylko liczby — dodajcie `.reset_index()` po agg."

---

### 0:45-0:75 — Ćwiczenie 3 (samodzielne — nie pomagaj za wcześnie)

> "Ćwiczenie 3 jest samodzielne — łączycie wszystko czego nauczyliście się w ćwiczeniach 1 i 2. Mam do was prośbę: przez pierwsze 10 minut spróbujcie sami, zanim zapytacie mnie."

**Obserwuj:** kto jest daleko w tyle. Po 15 minutach możesz dać klasie wskazówkę "połowiczną" — np. napisać na tablicy schemat kroków.

---

### 0:75-0:90 — Ćwiczenie 4 + commit

> "Ćwiczenie 4 to pivot_table i crosstab. Zwróćcie uwagę na margins=True — to daje sumy brzegowe."

> "Na koniec: commit! Kto nie ma commita, proszę zrobić teraz. Sprawdzę na GitHub."

---

## Tabela troubleshooting

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `KeyError: 'klient_id'` | Brak podanej kolumny | Sprawdź `zamowienia.columns` — czy kolumna istnieje |
| Wynik merge ma 0 wierszy | Błędny klucz lub different dtype | Sprawdź typy: `zamowienia.dtypes` vs `klienci.dtypes` |
| Po merge zbyt wiele wierszy (>20) | Duplikaty kluczy w jednej z tabel | `klienci['id'].duplicated().sum()` — czy są duplikaty? |
| `id_x`, `id_y` w kolumnach | Dwie tabele mają kolumnę `id` | Dodaj `suffixes=('_zam', '_kl')` do merge |
| `groupby` zwraca Series zamiast DataFrame | Brak `.reset_index()` | Dodaj `.reset_index()` po `.agg()` |
| pivot_table z NaN zamiast 0 | Brakujące kombinacje | Dodaj `fill_value=0` do `pd.pivot_table()` |
| `AttributeError: 'DataFrameGroupBy' has no attribute 'wartosc'` | Nawiasy w złej kolejności | `df.groupby('x')['wartosc'].sum()` — `['wartosc']` po `groupby('x')` |
| `concat` daje zduplikowany indeks | Brak `ignore_index=True` | `pd.concat([df1, df2], ignore_index=True)` |
| Błąd przy `dt.month` | Kolumna daty nie jest dtype datetime | Konwersja: `pd.to_datetime(df['data'])` |
| Git: nothing to commit | Notebook nie zapisany | Ctrl+S w VS Code, potem `git add .` |

---

## Weryfikacja odpowiedzi — liczby kontrolne

Prowadzący może sprawdzić poprawność pracy studenta porównując z poniższymi wartościami:

### Ćwiczenie 1
- Wynik inner merge (zamowienia + klienci + produkty): **20 wierszy, 14 kolumn**
- Łączna wartość sprzedaży: **20 389,67 zł**
- Liczba zamówień VIP: **7**
- Liczba zamówień Standard: **8**
- Liczba zamówień Premium: **5**
- Zamówienia bez danych klienta (left merge testy): **0** (wszyscy klienci istnieją)

### Ćwiczenie 2
- Miasto z największą sprzedażą: **Warszawa (9 589,95 zł)**
- Segment z najwyższą średnią wartością: **Premium (1 999,99 zł)**
- Kategoria z liczbą 9 zamówień: **Akcesoria**
- Kategoria z największą sprzedażą: **Komputery (15 899,94 zł)**

### Ćwiczenie 3
- Najlepiej sprzedający miesiąc: **Styczeń 2024 (5 729,95 zł)**
- Top 1 produkt per przychód: **Laptop ProX (11 999,97 zł)**, Top 2: Monitor 27" (3 899,97 zł)
- Klient z największą łączną wartością: **Anna Kowalska (1, VIP)**

### Ćwiczenie 4
- pivot_table Premium × Komputery: **9 299,97 zł**
- pivot_table miesiac=1 × Komputery: **5 299,98 zł**
- crosstab VIP × Warszawa: **3 zamówienia**
- crosstab Standard × Łódź: **2 zamówienia**

---

## Zadanie domowe (dla chętnych)

Dla studentów, którzy skończyli wcześniej lub chcą poćwiczyć w domu:

> "Znajdź w tabeli kompletnych danych: którzy klienci kupowali w co najmniej 2 różnych miesiącach? Użyj groupby i nunique()."

Rozwiązanie:
```python
wielomiesiac = (
    kompletne.groupby('imie')['miesiac']
    .nunique()
    .reset_index(name='liczba_miesiecy')
    .query('liczba_miesiecy >= 2')
    .sort_values('liczba_miesiecy', ascending=False)
)
print(wielomiesiac)
```
