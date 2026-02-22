# W08 Wykład — Plan zajęć dla prowadzącego

## Temat: Pandas — łączenie i agregacja

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z pandas/numpy
- **Przed wykładem:** otwórz `pandas_merge_demo.ipynb`

### Efekty uczenia się (Bloom poziom 3-4)
Po tym wykładzie osoba studiująca:
1. **Łączy** wiele DataFrame za pomocą `merge()` stosując odpowiedni typ złączenia (inner/left/right/outer) do konkretnego problemu biznesowego (Bloom 3)
2. **Scala** dane z wielu źródeł za pomocą `pd.concat()` i rozróżnia kiedy stosować concat zamiast merge (Bloom 3)
3. **Agreguje** dane z `groupby()` stosując wiele funkcji jednocześnie (sum, mean, count) i nazwaną agregację (Bloom 3)
4. **Konstruuje** raporty podsumowujące z `pivot_table()` i `crosstab()` (Bloom 3-4)
5. **Analizuje** wielotabelowy dataset biznesowy i odpowiada na pytania KPI (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W07 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | Od jednej tabeli do bazy danych | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | merge — inner, left, right, outer | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | concat — sklejanie DataFrame | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | groupby — split-apply-combine | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | pivot_table i crosstab — raporty | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Raport biznesowy z trzech tabel | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Przejście do Matplotlib na W09 | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W07)

> "Pięć pytań z zeszłego tygodnia — 3 minuty, bez zaglądania do notatek."

**[Użyj quiz_w07.md]**

---

### 0:05-0:10 — WPROWADZENIE

> "Zeszły tydzień czyściliśmy dane — NaN, duplikaty, złe typy. Teraz mamy czyste dane, ale w jednej tabeli."

> "W prawdziwym życiu dane są rozrzucone po wielu tabelach. Mamy tabelę zamówień, tabelę klientów i tabelę produktów. Osobno każda tabela to zaledwie fragment obrazka. Razem — pełna analiza sprzedaży."

> "Dzisiaj nauczymy się je łączyć. To jest jedna z najważniejszych umiejętności analityka danych — bo to jest dokładnie to samo, co robi SQL z JOIN. Jeśli kiedyś będziecie pracować z bazą danych, a będziecie — to ta wiedza jest bezpośrednio przenoszalna."

> "Plan na dzisiaj: merge — cztery typy złączeń, concat — klejenie tabel, groupby — grupowanie i agregacja, pivot_table — raporty podsumowujące. Brzmi dużo, ale te narzędzia logicznie wynikają jedno z drugiego."

**[Otwórz notebook pandas_merge_demo.ipynb, pokaż slajd z diagramem relacji tabel]**

> "Nasz zestaw danych — fikcyjny sklep internetowy TechShop. Trzy tabele: zamówienia, klienci i produkty. Taki sam układ jak w prawdziwym sklepie online."

---

### 0:10-0:30 — MATERIAŁ 1: merge — łączenie tabel (20 min)

**[Live coding — Cell 1: Tworzenie danych]**

> "Zaczynam od zbudowania naszych trzech tabel. Patrzcie na relacje — zamówienia mają `klient_id` i `produkt_id`, które są kluczami do pozostałych tabel. To jest klasyczna relacja wiele-do-jednego."

```python
import pandas as pd
import numpy as np

# Tabela klientów
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

# Tabela produktów
produkty = pd.DataFrame({
    'id': range(1, 9),
    'nazwa': ['Laptop ProX', 'Mysz bezprzewodowa', 'Monitor 27"', 'Klawiatura mechaniczna',
              'Słuchawki BT', 'Webcam HD', 'Pendrive 128GB', 'Hub USB-C'],
    'kategoria': ['Komputery', 'Akcesoria', 'Komputery', 'Akcesoria',
                  'Audio', 'Akcesoria', 'Storage', 'Akcesoria'],
    'cena': [3999.99, 89.99, 1299.99, 249.99, 399.99, 199.99, 49.99, 149.99]
})

# Tabela zamówień
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

print(f"Klienci: {len(klienci)} wierszy")
print(f"Produkty: {len(produkty)} wierszy")
print(f"Zamówienia: {len(zamowienia)} wierszy")
```

**[Uruchom, pokaż wyniki]**

> "Zauważcie: zamówień jest 20, klientów 10, produktów 8. W tabeli zamówień jest tylko ID klienta i produktu — nie wiemy jeszcze kto zamawiał i co. Do tego potrzebujemy merge."

**[Live coding — Cell 2: Pierwszy merge]**

> "Zaczynam od podstawowego merge — łączę zamówienia z klientami po kluczu. Składnia jest bardzo podobna do SQL JOIN."

```python
# Podstawowy merge — zamówienia + klienci
zam_kl = zamowienia.merge(
    klienci,
    left_on='klient_id',   # klucz w lewej tabeli
    right_on='id',         # klucz w prawej tabeli
    how='inner'            # typ złączenia
)
print(zam_kl.shape)
print(zam_kl[['id_x', 'data', 'imie', 'miasto', 'segment', 'ilosc']].head(5))
```

> "Domyślnie merge robi `how='inner'` — zwraca tylko wiersze, które mają pary w obu tabelach. Mamy dwie kolumny `id`, pandas automatycznie dodał sufiks `_x` i `_y`. Można to kontrolować parametrem `suffixes`."

**[Live coding — Cell 3: Cztery typy złączeń z diagramem]**

> "Teraz najważniejsza część — cztery typy złączeń. Zobrazuję to na małym przykładzie."

```python
# Przykład ilustracyjny — 4 typy merge
tabela_A = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'produkt': ['Laptop', 'Monitor', 'Mysz', 'Klawiatura']
})

tabela_B = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'cena': [249.99, 199.99, 89.99, 149.99]
})

print("Tabela A:")
print(tabela_A)
print("\nTabela B:")
print(tabela_B)
print()

for how in ['inner', 'left', 'right', 'outer']:
    result = tabela_A.merge(tabela_B, on='id', how=how)
    print(f"how='{how}': {len(result)} wierszy")
    print(result.to_string())
    print()
```

> "Popatrzcie na wyniki:"

> "**INNER** — tylko id=3 i id=4, które są w obu tabelach. To przecięcie zbiorów."

> "**LEFT** — wszystkie z tabeli A (4 wiersze), plus dopasowania z B. Laptop i Monitor nie mają cen — dostają NaN."

> "**RIGHT** — wszystkie z tabeli B, plus dopasowania z A. Produkty o id=5 i 6 nie mają nazw z A — NaN."

> "**OUTER** — wszystkie wiersze z obu tabel, brakujące wartości uzupełnione NaN. 6 wierszy, bo 4+4 minus 2 wspólne."

> "Kiedy którego używać? Inner — gdy chcemy tylko kompletne dane. Left — gdy tabela lewa jest 'bazowa' i chcemy zachować wszystkie jej rekordy. Right — rzadko, zwykle możemy zamienić tabele. Outer — audyt, ile danych nie ma par."

**[Live coding — Cell 4: Łańcuchowy merge z trzech tabel]**

> "W praktyce często łączymy więcej niż dwie tabele. Robimy to kolejno, przez chaining:"

```python
# Kompletne złączenie: zamówienia + klienci + produkty
kompletne = (
    zamowienia
    .merge(klienci, left_on='klient_id', right_on='id', suffixes=('_zam', '_kl'))
    .merge(produkty, left_on='produkt_id', right_on='id', suffixes=('', '_prod'))
)

# Dodajemy kolumnę wartości zamówienia
kompletne['wartosc'] = kompletne['ilosc'] * kompletne['cena']

print(f"Kompletna tabela: {kompletne.shape}")
print(kompletne[['id_zam', 'data', 'imie', 'miasto', 'segment',
                  'nazwa', 'kategoria', 'cena', 'ilosc', 'wartosc']].head(5))
print(f"\nŁączna wartość sprzedaży: {kompletne['wartosc'].sum():.2f} zł")
```

> "20 zamówień, teraz wiemy kto kupił, co kupił i za ile. Wartość zamówienia to ilość razy cena — prosta operacja wektorowa."

> "To jest właśnie to, co robi analityk: bierze kilka tabel z różnych źródeł i łączy w jeden widok. W SQL to by wyglądało: `SELECT ... FROM zamowienia JOIN klienci ON ... JOIN produkty ON ...`."

---

### 0:30-0:45 — MATERIAŁ 2: concat — sklejanie DataFrame (15 min)

**[Live coding — Cell 5: Concat wierszy]**

> "Merge łączy tabele po kluczu — poziomo, dodaje kolumny. `concat` klei tabele — pionowo, dodaje wiersze. Typowy przypadek: dane za styczeń i dane za luty, chcemy je złożyć razem."

```python
# Dane sprzedaży z dwóch kwartałów — ta sama struktura
q1 = pd.DataFrame({
    'miesiac': ['Styczeń', 'Luty', 'Marzec'],
    'sprzedaz': [45230, 38920, 52100],
    'zwroty': [1200, 890, 1450]
})

q2 = pd.DataFrame({
    'miesiac': ['Kwiecień', 'Maj', 'Czerwiec'],
    'sprzedaz': [48700, 55200, 62300],
    'zwroty': [1100, 1350, 1800]
})

print("Q1:")
print(q1)
print("\nQ2:")
print(q2)

# Concat — sklej jeden pod drugim
polrocze = pd.concat([q1, q2], ignore_index=True)
print("\nPierwsze półrocze:")
print(polrocze)
```

> "`ignore_index=True` — resetuje indeks, bo Q1 ma 0-2, Q2 też 0-2. Bez tego dostaniemy duplikaty indeksów."

**[Live coding — Cell 6: Concat z kluczami i concat kolumn]**

```python
# Concat z kluczami — zachowuje informację o źródle
polrocze_z_kwartałem = pd.concat(
    [q1, q2],
    keys=['Q1', 'Q2'],
    names=['Kwartał', 'Nr']
)
print("Z kluczami (MultiIndex):")
print(polrocze_z_kwartałem)
print()

# Concat kolumn (axis=1) — rzadziej używany
budżet = pd.DataFrame({
    'miesiac': ['Styczeń', 'Luty', 'Marzec'],
    'budzet': [50000, 45000, 55000]
})
q1_z_budzetem = pd.concat([q1, budżet[['budzet']]], axis=1)
print("Q1 z budżetem:")
print(q1_z_budzetem)
```

> "Z `keys` dostajemy MultiIndex — hierarchiczny indeks. Przydatne gdy chcemy wiedzieć skąd pochodzi każdy wiersz, np. przy scalaniu danych z wielu arkuszy Excel."

> "Axis=1 to concat poziomy — skleja kolumny. Ale uwaga: to nie to samo co merge — nie sprawdza klucza, po prostu przykleja obok. Używać tylko gdy wiersze są w tej samej kolejności."

> "Praktyczna zasada: merge gdy masz klucz relacyjny, concat gdy masz te same kolumny z różnych źródeł/okresów."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: groupby — split-apply-combine (20 min)

**[Live coding — Cell 7: Koncepcja split-apply-combine]**

> "Wracamy po przerwie. Mamy kompletną tabelę ze wszystkimi danymi. Teraz chcemy wyciągnąć z niej wiedzę — nie wierszami, ale agregując po grupach."

> "groupby działa według wzorca: Split — Apply — Combine."

> "Split: podziel DataFrame na grupy. Apply: zastosuj funkcję do każdej grupy. Combine: zbierz wyniki w jeden DataFrame."

> "To jest jeden z najważniejszych wzorców w analizie danych. SQL GROUP BY — dokładnie to samo."

```python
# Podstawowy groupby — sprzedaż per miasto
sprzedaz_miasto = kompletne.groupby('miasto')['wartosc'].sum()
print("Sprzedaż per miasto:")
print(sprzedaz_miasto.sort_values(ascending=False))
print(f"\nTyp wyniku: {type(sprzedaz_miasto)}")
```

> "Wynik to Series z indeksem będącym wartościami grupy. Warszawa lideruje — 9589.95 zł."

**[Live coding — Cell 8: Wiele funkcji agregujących]**

```python
# Wiele funkcji jednocześnie — metoda agg()
stats_segment = kompletne.groupby('segment')['wartosc'].agg(['sum', 'mean', 'count', 'max'])
print("Statystyki per segment klienta:")
print(stats_segment.round(2))
```

> "`.agg()` pozwala zastosować kilka funkcji naraz. Segment Premium ma najwyższą sumę: 9999.94 zł. Standard ma 8 zamówień ale mniejszą wartość — to są klienci kupujący tanie akcesoria."

**[Live coding — Cell 9: Nazwana agregacja (Named Aggregation)]**

```python
# Nazwana agregacja — bardziej czytelne kolumny wynikowe
raport_segmentow = kompletne.groupby('segment').agg(
    liczba_zamowien=('id_zam', 'count'),
    laczna_wartosc=('wartosc', 'sum'),
    srednia_wartosc=('wartosc', 'mean'),
    max_zamowienie=('wartosc', 'max')
).round(2)

print("Raport segmentów (nazwana agregacja):")
print(raport_segmentow)
```

> "Składnia: `nazwa_kolumny=('kolumna_źródłowa', 'funkcja')`. To jest pandas-owy sposób na czytelne, dobrze nazwane kolumny wynikowe. W kodzie produkcyjnym — zawsze tak. Kolumna `sum` w raporcie nic nie mówi, `laczna_wartosc` — już tak."

**[Live coding — Cell 10: Groupby po wielu kolumnach]**

```python
# Grupowanie po dwóch wymiarach
sprzedaz_miasto_kat = (
    kompletne
    .groupby(['miasto', 'kategoria'])['wartosc']
    .sum()
    .round(2)
)
print("Sprzedaż per miasto i kategoria:")
print(sprzedaz_miasto_kat.unstack(fill_value=0))
```

> "Grupowanie po dwóch kolumnach daje nam dwupoziomowy indeks. `.unstack()` rozkłada drugi poziom do kolumn — dostajemy tabelę krzyżową. To jest właśnie to, co zaraz zrobimy elegancko z pivot_table."

**[Live coding — Cell 11: groupby z transformacją]**

```python
# transform — wartość grupowa z powrotem w każdym wierszu
kompletne['sprzedaz_segmentu'] = kompletne.groupby('segment')['wartosc'].transform('sum')
kompletne['udzial_w_segmencie'] = (kompletne['wartosc'] / kompletne['sprzedaz_segmentu'] * 100).round(1)

print("5 największych zamówień z udziałem w segmencie:")
print(kompletne[['imie', 'segment', 'nazwa', 'wartosc', 'sprzedaz_segmentu', 'udzial_w_segmencie']]
      .sort_values('wartosc', ascending=False).head(5))
```

> "`.transform()` różni się od `.agg()` — wynik ma tę samą długość co oryginalny DataFrame. Każdy wiersz dostaje wartość swojej grupy. Świetne do liczenia udziałów procentowych."

---

### 1:15-1:25 — MATERIAŁ 4: pivot_table i crosstab (10 min)

**[Live coding — Cell 12: pivot_table]**

> "pivot_table to bardziej deklaratywny sposób na to samo co groupby + unstack. Jeśli znacie tabele przestawne z Excela — to jest dokładnie to samo."

```python
# Tabela przestawna: segment × kategoria
pivot = pd.pivot_table(
    kompletne,
    values='wartosc',     # co agregujemy
    index='segment',      # wiersze
    columns='kategoria',  # kolumny
    aggfunc='sum',        # funkcja agregująca
    fill_value=0,         # zamiast NaN
    margins=True          # sumy brzegowe
)
print("Sprzedaż: Segment × Kategoria [PLN]")
print(pivot.round(2))
```

> "Wynik to gotowa tabela raportowa. Margins=True dodaje wiersz i kolumnę 'All' z sumami. To jest format, który możemy wyeksportować do Excela i pokazać szefowi."

**[Live coding — Cell 13: crosstab]**

```python
# crosstab — liczy wystąpienia (liczebności, nie wartości)
ct = pd.crosstab(
    kompletne['segment'],
    kompletne['miasto'],
    margins=True
)
print("Liczba zamówień: Segment × Miasto")
print(ct)

# crosstab z normalizacją — procenty
ct_pct = pd.crosstab(
    kompletne['segment'],
    kompletne['miasto'],
    normalize='index'    # procenty per wiersz
)
print("\nUdziały procentowe per segment:")
print((ct_pct * 100).round(1))
```

> "crosstab to specjalizowany odpowiednik pivot_table do liczenia częstości. Normalize='index' zamienia liczby na procenty — każdy wiersz sumuje się do 1. Możemy zobaczyć: klienci VIP zamawiają głównie z Warszawy i Krakowa."

---

### 1:25-1:35 — AKTYWNOŚĆ: Tworzenie raportu biznesowego (10 min)

> "Czas żebyście sami spróbowali. Macie dostęp do naszej kompletnej tabeli. Proszę żebyście w ciągu 7 minut odpowiedzieli na 3 pytania biznesowe."

**[Wyświetl na projektorze, studenci piszą samodzielnie]**

```
ZADANIE — raport dla zarządu TechShop:

1. Które 3 produkty wygenerowały największy przychód? (groupby po nazwie)
2. Jaki jest średni koszyk (średnia wartość zamówienia) per miasto? (groupby)
3. Zbuduj tabelę przestawną: miesiąc (rows) × kategoria (columns), wartość = suma sprzedaży
   Wskazówka: kompletne['miesiac'] = kompletne['data'].dt.month
```

> "Za 7 minut omówimy wspólnie — kto chce pokazać swoje rozwiązanie?"

**[Po 7 minutach — live coding rozwiązania razem ze studentami]**

```python
# Rozwiązanie 1: Top 3 produkty
top3 = kompletne.groupby('nazwa')['wartosc'].sum().nlargest(3)
print("Top 3 produkty wg przychodu:")
print(top3)

# Rozwiązanie 2: Średni koszyk per miasto
koszyk = kompletne.groupby('miasto')['wartosc'].mean().round(2).sort_values(ascending=False)
print("\nŚredni koszyk per miasto:")
print(koszyk)

# Rozwiązanie 3: Tabela miesięczna
kompletne['miesiac'] = kompletne['data'].dt.month
pivot_czas = pd.pivot_table(
    kompletne, values='wartosc',
    index='miesiac', columns='kategoria',
    aggfunc='sum', fill_value=0, margins=True
)
print("\nSprzedaż miesięczna per kategoria:")
print(pivot_czas.round(2))
```

---

### 1:35-1:45 — PODSUMOWANIE

> "Co dzisiaj zrobiliśmy?"

> "Po pierwsze: merge — łączyliśmy tabele po kluczu relacyjnym. Cztery typy: inner (wspólne), left (wszystkie z lewej + dopasowania), right (wszystkie z prawej), outer (wszystkie). To jest SQL JOIN w Pandas."

> "Po drugie: concat — sklejaliśmy tabele pionowo, gdy mają te same kolumny. Dane z różnych okresów, różnych plików Excel — concat z ignore_index."

> "Po trzecie: groupby — split-apply-combine. Grupujemy po jednej lub wielu kolumnach, agregujemy sum/mean/count. Nazwana agregacja — zawsze w kodzie produkcyjnym."

> "Po czwarte: pivot_table i crosstab — gotowe raporty tabelaryczne z sumami brzegowymi i normalizacją."

> "Za tydzień — Matplotlib. Te dane, które teraz agregatujemy, będziemy wizualizować. Słupki sprzedaży per miasto, trend miesięczny, udziały kategorii na kołowym. To, co zrobiliście dziś na papierze, za tydzień zamienicie w wykresy."

> "Zadanie domowe: w notebooku z laboratorium jest Ćwiczenie 4 — pivot_table i crosstab. Zróbcie to przed następnymi zajęciami i zcommitujcie na GitHub."

> "Pytania?"

---

## Notatki i wskazówki dla prowadzącego

### Typowe błędy studentów (i jak reagować)
| Błąd | Komunikat | Odpowiedź |
|------|-----------|-----------|
| Merge po złym kluczu | KeyError lub zbyt mało wierszy | "Sprawdź left_on i right_on — muszą wskazywać na te same dane, ale w różnych tabelach" |
| Duplikowane kolumny po merge | Kolumny `id_x`, `id_y` | "To normalne — dwie tabele mają kolumnę `id`. Użyj suffixes lub rename" |
| groupby daje Series zamiast DataFrame | Nie ma .reset_index() | "groupby zwraca Series — żeby dostać DataFrame, dodaj .reset_index()" |
| pivot_table z NaN zamiast 0 | Puste komórki | "Dodaj fill_value=0" |

### Pytania kontrolne (można zadawać w trakcie)
- "Jaką różnicę zobaczylibyśmy między inner a outer w naszych danych, gdyby jeden klient nie miał zamówień?"
- "Dlaczego nie używamy concat gdy chcemy dodać dane o klientach do tabeli zamówień?"
- "Co się stanie jeśli w groupby nie podamy żadnej funkcji agregującej?"

### Obserwacje z dydaktyki
- Diagram Venna dla typów merge bardzo pomaga — narysuj kredą lub pokaż cell z komentarzem
- Przejście groupby → pivot_table studentom wychodzi dobrze gdy pokazać że to "to samo, ale wygodniej"
- Aktywność (1:25-1:35) — daj naprawdę 7 minut, nie skracaj. Cisza jest OK — studenci pracują
