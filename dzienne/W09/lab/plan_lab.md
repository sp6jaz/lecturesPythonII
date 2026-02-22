# W09 Laboratorium — Plan zajęć dla prowadzącego (doktoranta)

## Temat: Matplotlib — podstawy wizualizacji danych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** samodzielna praca przy komputerze, para programming dozwolony
- **Sala:** laboratorium komputerowe z VS Code
- **Wymagane:** Python + venv z matplotlib/pandas/numpy/seaborn, dostęp do GitHub
- **Plik dla studentów:** `cwiczenia.md` — udostępnij przez Moodle lub Teams przed zajęciami

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przygotowanie przed zajęciami (15 min przed)
1. Sprawdź środowisko: `python -c "import matplotlib; print(matplotlib.__version__)"`
2. Upewnij się, że studenci mają dostęp do `cwiczenia.md`
3. Miej gotowe rozwiązania wszystkich ćwiczeń (poniżej + w cwiczenia.md)
4. Sprawdź, czy dataset `tips` jest dostępny: `python -c "import seaborn as sns; print(sns.load_dataset('tips').shape)"`
5. Przygotuj folder roboczy — studenci powinni zapisywać PNG pliki w katalogu `W09_lab/`

### Struktura laboratorium

| Czas | Etap | Treść |
|------|------|-------|
| 0:00-0:05 | **Wstęp** | Organizacja, cel, przypomnienie z wykładu |
| 0:05-0:25 | **Ćwiczenie 1** | Podstawowe typy wykresów: linia, słupki, scatter (20 min) |
| 0:25-0:45 | **Ćwiczenie 2** | Dostosowywanie: etykiety, kolory, legendy (20 min) |
| 0:45-1:15 | **Ćwiczenie 3** | Pełna wizualizacja z datasetu tips/biznesowego (30 min) — samodzielne |
| 1:15-1:30 | **Ćwiczenie 4** | Wiele wykresów (subplots), zapis PNG, commit (15 min) |

### Jak prowadzić zajęcia

**Zasada pierwsza: daj czas**
- Ćwiczenie 3 jest samodzielne — nie pomagaj przez pierwsze 10 minut
- Jeśli student skończył wcześniej — ma pytania dodatkowe w każdym ćwiczeniu
- Lepiej przerobić 3 ćwiczenia solidnie niż 4 powierzchownie

**Zasada druga: scaffolding**
- Każde ćwiczenie ma kod startowy z `???` do uzupełnienia
- Po każdym punkcie: sekcja "Sprawdzenie" — studentowi musi się wyświetlić konkretny wykres
- Jeśli wielu studentów utknęło w tym samym miejscu — daj wskazówkę całej grupie

**Zasada trzecia: commit na koniec**
- Ćwiczenie 4 kończy się commitem PNG + notebook
- Bez commita = bez zaliczenia ćwiczenia

---

## Ścieżka prowadzenia — co mówić

### 0:00-0:05 — Wstęp

> "Na wykładzie poznaliśmy Matplotlib: Figure i Axes, podstawowe typy wykresów, formatowanie i Pandas .plot(). Dzisiaj ćwiczymy na danych — tips dataset i dane biznesowe."

> "Otwórzcie VS Code, nowy notebook `W09_lab.ipynb`. Pierwsza komórka zawsze: `%matplotlib inline` i importy."

> "Pracujecie samodzielnie lub w parach. Po każdym ćwiczeniu: Sprawdzenie — porównajcie swój wykres z opisem. Jeśli wykres wygląda inaczej niż powinien — jest błąd do znalezienia."

> "Wykresy zapisujecie przez `plt.savefig()` — każdy PNG to plik, który zobaczymy w Git na końcu."

---

### 0:05-0:25 — Ćwiczenie 1 (obserwuj, pomagaj gdy ≥3 osoby mają ten sam problem)

**Najczęstszy problem:** brak `plt.close()` — wykresy się nakładają.

**Po 20 minutach:**
> "Wszyscy widzą wykres liniowy z markerami, słupkowy i scatter? Kto ma pustą komórkę — sprawdź czy masz `%matplotlib inline` na początku notebooka."

---

### 0:25-0:45 — Ćwiczenie 2 (formatowanie — tu studenci eksperymentują)

**Obserwuj:** czy studenci zmieniają kolory, dodają legendę, stosują `tight_layout()`

> "Jeśli etykiety osi X się nakładają — albo obróćcie (`rotation=45`) albo użyjcie `barh` zamiast `bar`."

---

### 0:45-1:15 — Ćwiczenie 3 (samodzielne — nie pomagaj za wcześnie)

> "Ćwiczenie 3 jest samodzielne — stosujecie wszystko z ćwiczeń 1 i 2. Przez pierwsze 10 minut próbujecie sami. Mam do was prośbę: zanim mnie zapytacie — najpierw przeczytajcie komunikat błędu."

**Po 15 minutach:** Możesz napisać na tablicy schemat kroków:
```
1. sns.load_dataset('tips') → DataFrame
2. groupby('...') → Series
3. .plot() lub ax.scatter() → wykres
4. set_title / set_xlabel / set_ylabel
5. savefig + close
```

---

### 1:15-1:30 — Ćwiczenie 4 + commit

> "Ćwiczenie 4 to układ 2×2 z czterema różnymi wykresami. Zwróćcie uwagę na indeksowanie axes[wiersz, kolumna]."

> "Na koniec: commit! Kto nie ma commita, proszę zrobić teraz. Commit powinien zawierać: notebook W09_lab.ipynb + przynajmniej jeden PNG."

---

## Tabela troubleshooting

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| Wykres się nie wyświetla w Jupyter | Brak `%matplotlib inline` | Dodaj `%matplotlib inline` jako pierwszą linię w pierwszej komórce |
| Wykresy się nakładają | Brak `plt.close()` po `savefig` | Po każdym `plt.savefig()` dodaj `plt.close()` |
| `AttributeError: Axes has no 'title'` | `ax.title` zamiast `ax.set_title()` | Metody Axes mają prefiks `set_`: `set_title()`, `set_xlabel()`, `set_ylabel()` |
| Etykiety osi X się nakładają | Za długie teksty w pionowych słupkach | `plt.xticks(rotation=45)` lub użyj `barh` (słupki poziome) |
| PNG zapisany jako pusty plik | `plt.close()` przed `plt.savefig()` | Kolejność: najpierw `savefig()`, potem `close()` |
| `FileNotFoundError` przy `sns.load_dataset` | Brak internetu lub cache | `tips = pd.read_csv(...)` — skorzystaj z danych wbudowanych w ćwiczeniu (kod startowy) |
| Kolormap nie działa w scatter | Brak wartości numerycznych dla `c=` | Sprawdź typ kolumny: `tips['size'].dtype` — musi być numeryczny |
| `tight_layout()` nie usuwa problemu | Figsize za mała | Zwiększ `figsize=(12, 9)` dla układów 2×2 |
| `UserWarning: Matplotlib is currently using agg` | Brak display w środowisku | Normalne w trybie headless — `savefig` działa, `show()` nie |
| Git: `.png` nie jest w repozytorium | Plik poza katalogiem repo | Upewnij się, że `savefig` zapisuje do katalogu z `.git` |

---

## Weryfikacja odpowiedzi — opisy wykresów kontrolnych

### Ćwiczenie 1
- Wykres liniowy: niebieska linia z markerami `o`, 6 punktów (miesiące Q1-Q2), oś Y od 0 do ~70 000
- Wykres słupkowy: 4-5 pionowych słupków z wartościami nad nimi, tytuł i etykiety osi
- Scatter: co najmniej 200 punktów (tips dataset), widoczne zagęszczenie w lewym dolnym rogu

### Ćwiczenie 2
- Wykres z legendą: dwie serie z różnymi kolorami/markerami, legenda w rogu
- Styl: widoczna siatka (`grid`), `tight_layout` — bez uciętych etykiet
- Słupkowy z kolorami per słupek: każdy słupek inny kolor lub barwa z palety

### Ćwiczenie 3
- Przynajmniej 3 wykresy z datasetu tips zapisane jako PNG
- Każdy ma: tytuł, etykiety obu osi, odpowiedni typ (bar/scatter/hist/line)
- Widoczna analityczna obserwacja w opisie markdown (co wynika z wykresu)

### Ćwiczenie 4
- Układ 2×2 (4 wykresy na jednej Figure), `suptitle` nad wszystkimi
- Wszystkie 4 pliki PNG committed w Git
- Komunikat commita zawiera "W09"

---

## Zadanie domowe (dla chętnych)

> "Wróćcie do danych ze sklepu TechShop z W08 (zamówienia, klienci, produkty). Stwórzcie dashboard 2×2 z: trendem sprzedaży miesięcznej, sprzedażą per miasto (barh), sprzedażą per kategoria (bar), i scatter'em wartość zamówienia vs ilość. Zapisz jako `dashboard_techshop.png` i commituj."

Rozwiązanie-szkielet:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Dane TechShop z W08 (skopiuj z poprzedniego notebooka)
# kompletne — DataFrame po triple merge

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# [0,0] Trend miesięczny
kompletne['miesiac'] = kompletne['data'].dt.month
trend = kompletne.groupby('miesiac')['wartosc'].sum()
axes[0, 0].plot(trend.index, trend.values, marker='o', color='steelblue')
axes[0, 0].set_title('Trend sprzedaży miesięcznej')

# [0,1] Per miasto
miasto = kompletne.groupby('miasto')['wartosc'].sum().sort_values()
axes[0, 1].barh(miasto.index, miasto.values, color='steelblue')
axes[0, 1].set_title('Sprzedaż per miasto')

# [1,0] Per kategoria
kat = kompletne.groupby('kategoria')['wartosc'].sum().sort_values(ascending=False)
axes[1, 0].bar(kat.index, kat.values, color='steelblue')
axes[1, 0].set_title('Sprzedaż per kategoria')

# [1,1] Scatter
axes[1, 1].scatter(kompletne['ilosc'], kompletne['wartosc'], alpha=0.6, color='steelblue')
axes[1, 1].set_title('Ilość vs wartość zamówienia')

plt.suptitle('Dashboard TechShop', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('dashboard_techshop.png', dpi=100)
plt.close()
```
