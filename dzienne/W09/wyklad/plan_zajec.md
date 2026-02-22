# W09 Wykład — Plan zajęć dla prowadzącego

## Temat: Matplotlib — podstawy wizualizacji danych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z matplotlib/pandas/numpy
- **Przed wykładem:** otwórz `matplotlib_demo.ipynb`

### Efekty uczenia się (Bloom poziom 2-3)
Po tym wykładzie osoba studiująca:
1. **Stosuje** konwencję `import matplotlib.pyplot as plt` i rozróżnia obiekt Figure od Axes (Bloom 2)
2. **Tworzy** podstawowe typy wykresów: liniowy, słupkowy, kołowy i punktowy za pomocą `plt.plot()`, `plt.bar()`, `plt.scatter()` (Bloom 3)
3. **Dostosowuje** wygląd wykresów: tytuły, etykiety osi, legendy, kolory, style (Bloom 3)
4. **Konstruuje** układ wielu wykresów za pomocą `plt.subplots()` i wyświetla histogram rozkładu (Bloom 3)
5. **Stosuje** metodę `.plot()` DataFrame Pandas do szybkiego tworzenia wykresów z danych tabelarycznych (Bloom 3)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W08 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | "Przez 4 tygodnie analizowaliśmy dane — czas je POKAZAĆ" | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Figure, Axes, plt.plot(), plt.bar() — podstawowe typy wykresów | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | Etykiety, tytuły, legendy, kolory, style | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | scatter, histogram, plt.subplots() — wiele wykresów | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Pandas `.plot()` — wykresy wprost z DataFrame | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Stwórz 3 wykresy z datasetu tips | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Zapowiedź W10 (Seaborn, dashboardy) | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W08)

> "Pięć pytań z zeszłego tygodnia — 3 minuty, bez zaglądania do notatek."

**[Użyj quiz_w08.md]**

---

### 0:05-0:10 — WPROWADZENIE

> "Przez cztery tygodnie robiliśmy jedno i to samo: ładowaliśmy dane, czyściliśmy je, łączyliśmy tabele, agregowaliśmy, tworzyliśmy pivot table. I za każdym razem kończyliśmy na liczbach w terminalu."

> "Ktoś mi powie: i co z tych liczb? Że Warszawa ma 9589 zł sprzedaży, a Premium 1999 zł średniej wartości zamówienia. Super. Ale gdybym wam pokazał wykres słupkowy z pięcioma miastami — w ciągu dwóch sekund wiedzielibyście, które miasto lideruje, jak duże są różnice i czy są jakieś anomalie. Ludzie przetwarzają obrazy 60 000 razy szybciej niż tekst. To nie jest estetyka — to neurobiologia."

> "Dzisiaj zaczynamy wizualizację. Matplotlib to fundament — starsza biblioteka, nieco gadatliwa, ale niezbędna. Wszystkie inne biblioteki wizualizacyjne w Pythonie — Seaborn, Plotly, Pandas .plot() — siedzą na wierzchu Matplotlib. Jak opanujemy fundamenty, reszta przyjdzie naturalnie."

> "Plan na dzisiaj: Figure i Axes — architektura wykresu, podstawowe typy wykresów — linia, słupki, kółka, punkty, formatowanie — kolory, etykiety, legendy, wiele wykresów naraz, i szybkie wykresy wprost z Pandas."

**[Otwórz notebook matplotlib_demo.ipynb]**

---

### 0:10-0:30 — MATERIAŁ 1: Figure, Axes, plt.plot(), plt.bar() (20 min)

**[Live coding — Cell 1: Import i pierwsze spojrzenie]**

> "Zaczynam od konwencji. W całym kursie używamy tej samej linii:"

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print(f"Matplotlib: {plt.matplotlib.__version__}")
```

> "Zawsze `import matplotlib.pyplot as plt`. To jest standard — tak samo jak `import pandas as pd`. Jeśli zobaczycie gdzieś inny alias — to ktoś nie stosuje standardów branżowych."

**[Live coding — Cell 2: Architektura — Figure i Axes]**

> "Zanim narysujemy cokolwiek, musimy rozumieć jak Matplotlib buduje wykres. Jest hierarchia obiektów."

> "Figure to całe okno lub całość strony — kontener. Axes to jeden układ współrzędnych z osiami X i Y — to na nim rysujemy. Figure może zawierać wiele Axes."

> "Są dwa style pracy z Matplotlib:"

```python
# Styl 1: imperatywny (pyplot API) — szybki, dobry do prostych wykresów
plt.figure(figsize=(8, 4))
plt.plot([1, 2, 3, 4], [10, 20, 15, 30])
plt.title("Najprostszy wykres")
plt.savefig("temp.png")
plt.close()

# Styl 2: obiektowy (Figure/Axes API) — elastyczny, zalecany dla złożonych
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([1, 2, 3, 4], [10, 20, 15, 30])
ax.set_title("Wykres obiektowy")
plt.savefig("temp.png")
plt.close()
```

> "W notatnikach Jupyter dodajemy `%matplotlib inline` na początku — wykresy renderują się wewnątrz notebooka, nie w osobnym oknie. Bez tego — puste okno albo brak wykresu."

> "Który styl stosować? Styl 2 — obiektowy. Na początku jest nieco bardziej rozbudowany, ale gdy zaczniecie tworzyć wiele wykresów naraz — zobaczycie, że imperatywny się gubi. Ja pokażę oba, żebyście umieli czytać cudzy kod."

**[Live coding — Cell 3: Wykres liniowy — trend sprzedaży]**

> "Pierwszy poważny przykład — trend sprzedaży miesięcznej. To klasyczny przypadek biznesowy."

```python
# Dane sprzedaży miesięcznej (Q1-Q2 2024)
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze']
sprzedaz = [45230, 38920, 52100, 48700, 55200, 62300]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(miesiace, sprzedaz,
        color='steelblue',
        linewidth=2,
        marker='o',
        markersize=8)

ax.set_title('Trend sprzedaży Q1-Q2 2024', fontsize=14, fontweight='bold')
ax.set_xlabel('Miesiąc')
ax.set_ylabel('Sprzedaż [PLN]')
ax.set_ylim(0, 70000)

plt.tight_layout()
plt.savefig('trend_sprzedazy.png', dpi=100)
plt.close()
print("Zapisano: trend_sprzedazy.png")
```

> "Kilka rzeczy do zapamiętania: `figsize=(10, 5)` — szerokość na wysokość w calach, 10x5 to typowy format poziomy dla prezentacji. `marker='o'` — kółka na punktach danych — zawsze dodawaj, bo widać gdzie są dane. `linewidth=2` — domyślna linia jest trochę za cienka do prezentacji. `plt.tight_layout()` — automatycznie poprawia marginesy, żeby etykiety się nie ucinały."

> "`plt.savefig()` zamiast `plt.show()` — w skrypcie używamy `savefig`, bo `show()` blokuje wykonanie i otwiera okno GUI. W Jupyter z `%matplotlib inline` możemy używać też `plt.show()`, ale `savefig` jest bezpieczniejszy i daje nam plik."

**[Live coding — Cell 4: Wykres słupkowy — sprzedaż per produkt]**

> "Wykres słupkowy — klasyczny raport sprzedaży per produkt lub per kategoria."

```python
# Top 5 produktów — przychód
produkty = ['Laptop ProX', 'Monitor 27"', 'Klawiatura', 'Słuchawki BT', 'Mysz']
przychod = [11999.97, 3899.97, 1499.94, 1199.97, 449.95]

fig, ax = plt.subplots(figsize=(10, 5))

slupki = ax.bar(produkty, przychod,
                color='steelblue',
                edgecolor='navy',
                linewidth=0.8)

# Wartości nad słupkami
for slupek, wartosc in zip(slupki, przychod):
    ax.text(slupek.get_x() + slupek.get_width() / 2,
            slupek.get_height() + 100,
            f'{wartosc:,.0f} zł',
            ha='center', va='bottom', fontsize=9)

ax.set_title('Top 5 produktów — przychód 2024', fontsize=14, fontweight='bold')
ax.set_xlabel('Produkt')
ax.set_ylabel('Przychód [PLN]')
ax.set_ylim(0, 14000)

plt.tight_layout()
plt.savefig('sprzedaz_produkty.png', dpi=100)
plt.close()
print("Zapisano: sprzedaz_produkty.png")
```

> "Zwróćcie uwagę na dwie rzeczy: podpisy wartości nad słupkami — to nie jest dekoracja, to informacja. Bez nich widać proporcje, ale nie dokładne wartości. Formatowanie `{wartosc:,.0f}` — przecinek jako separator tysięcy, zero miejsc po przecinku."

> "`edgecolor='navy'` — ciemna ramka wokół słupków. Subtelna rzecz, ale sprawia, że wykres wygląda profesjonalnie, szczególnie w druku."

---

### 0:30-0:45 — MATERIAŁ 2: Etykiety, tytuły, legendy, kolory, style (15 min)

**[Live coding — Cell 5: Wiele serii — porównanie lat]**

> "W biznesie prawie zawsze porównujemy wiele rzeczy jednocześnie. Rok do roku, plan do wykonania, produkt A do produktu B. Do tego potrzebujemy wielu serii na jednym wykresie i legendy."

```python
# Porównanie sprzedaży rok do roku
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze']
sprzedaz_2023 = [41000, 35000, 48000, 44000, 50000, 58000]
sprzedaz_2024 = [45230, 38920, 52100, 48700, 55200, 62300]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(miesiace, sprzedaz_2023,
        label='2023',
        color='lightsteelblue',
        linewidth=2,
        marker='s',
        linestyle='--')

ax.plot(miesiace, sprzedaz_2024,
        label='2024',
        color='steelblue',
        linewidth=2,
        marker='o')

ax.set_title('Sprzedaż Q1-Q2: porównanie rok do roku', fontsize=14, fontweight='bold')
ax.set_xlabel('Miesiąc')
ax.set_ylabel('Sprzedaż [PLN]')
ax.legend(title='Rok', loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('porownanie_lat.png', dpi=100)
plt.close()
print("Zapisano: porownanie_lat.png")
```

> "Legenda: `ax.legend(title='Rok', loc='upper left')`. Parametr `label` w `ax.plot()` to tekst legendy — musi być podany, bo bez niego legenda nie wie co wyświetlić. `loc` — umieszczenie: 'upper left', 'upper right', 'lower right', 'best'. `best` automatycznie znajdzie miejsce z najmniejszym zachodzeniem na dane."

> "`linestyle='--'` — przerywana linia dla starszego roku — wizualny sygnał, że to dane historyczne. `marker='s'` — kwadraty zamiast kółek. Różnicujcie markery i style linii, nie tylko kolory — bo ktoś może drukować w czerni i bieli lub ma daltonizm."

> "`grid(axis='y', alpha=0.4)` — linie siatki tylko poziome, z przezroczystością. Siatka pomaga czytać wartości, ale nie może dominować nad danymi."

**[Live coding — Cell 6: Kolory i style]**

> "Kilka słów o kolorach — bo tu studenci często popełniają błędy."

```python
# Palety kolorów i style
print("Kolory nazwane (przykłady):")
print("  steelblue, navy, cornflowerblue")
print("  salmon, tomato, firebrick")
print("  forestgreen, mediumseagreen, limegreen")
print("  gold, darkorange, chocolate")

print("\nFormat hex:")
print("  #2196F3 — niebieski Material Design")
print("  #4CAF50 — zielony Material Design")

print("\nStyle wykresów dostępne:")
for styl in ['seaborn-v0_8-whitegrid', 'ggplot', 'bmh', 'default']:
    print(f"  {styl}")
```

> "Zasada kolorów w wizualizacji biznesowej: jeden kolor wiodący (np. firmowy niebieski), drugi jako akcent. Unikajcie paletek tęczowych — każdy kolor musi coś znaczyć. Czerwony = problem/strata, zielony = dobrze/zysk, szary = tło/reference."

> "Matplotlib ma wbudowane style — `plt.style.use('seaborn-v0_8-whitegrid')` zamienia domyślny szary styl na biały ze siatką, profesjonalnie wygląda w prezentacjach. Na laboratoriach możecie eksperymentować."

```python
# Przykład z użyciem stylu
plt.style.use('seaborn-v0_8-whitegrid')

fig, ax = plt.subplots(figsize=(8, 4))
kategorie = ['Komputery', 'Akcesoria', 'Audio', 'Storage']
sprzedaz_kat = [15899, 2940, 1200, 350]
kolory = ['#2196F3', '#66BB6A', '#FFA726', '#AB47BC']

ax.barh(kategorie, sprzedaz_kat, color=kolory)
ax.set_title('Sprzedaż per kategoria [PLN]')
ax.set_xlabel('PLN')

plt.tight_layout()
plt.savefig('kategorie.png', dpi=100)
plt.close()

plt.style.use('default')  # reset stylu
print("Zapisano: kategorie.png")
```

> "`barh()` zamiast `bar()` — słupki poziome. Kiedy mamy długie etykiety — zawsze słupki poziome. Tutaj 'Klawiatura mechaniczna' nie zmieściłaby się pod pionowym słupkiem."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: scatter, histogram, plt.subplots() (20 min)

**[Live coding — Cell 7: Wykres punktowy — korelacja]**

> "Wracamy po przerwie. Dwa nowe typy wykresów — scatter i histogram."

> "Scatter plot — wykres punktowy — służy do pokazywania korelacji między dwiema zmiennymi. Klasyczne pytanie: czy wartość zamówienia rośnie z wielkością zamówienia? Czy długość rachunku w restauracji zależy od liczby gości?"

```python
# Dataset tips — wbudowany w seaborn, przygotujemy go ręcznie
import seaborn as sns
tips = sns.load_dataset('tips')

fig, ax = plt.subplots(figsize=(8, 6))

scatter = ax.scatter(
    tips['total_bill'],
    tips['tip'],
    c=tips['size'],          # kolor = liczba gości
    cmap='Blues',            # paleta kolorów
    alpha=0.7,               # przezroczystość
    s=60,                    # rozmiar punktu
    edgecolors='gray',
    linewidth=0.5
)

# Colorbar — legenda dla koloru
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Liczba gości', rotation=270, labelpad=15)

ax.set_title('Korelacja: rachunek vs napiwek', fontsize=13, fontweight='bold')
ax.set_xlabel('Wartość rachunku [$]')
ax.set_ylabel('Napiwek [$]')

plt.tight_layout()
plt.savefig('scatter_tips.png', dpi=100)
plt.close()
print("Zapisano: scatter_tips.png")
```

> "Trzy informacje w jednym wykresie: X-oś rachunek, Y-oś napiwek, kolor = liczba gości. Widzimy: im wyższy rachunek, tym wyższy napiwek — to logiczne. Ale czy duże grupy (ciemny kolor) dają proporcjonalnie więcej? Sprawdzimy na laboratoriach."

> "`alpha=0.7` — przezroczystość punktów. Bez niej, gdy punkty się nakładają, widzimy tylko jeden kolor. Z przezroczystością — zaciemnione miejsca = zagęszczenie danych."

**[Live coding — Cell 8: Histogram — rozkład danych]**

> "Histogram pokazuje rozkład jednej zmiennej — ile obserwacji wpada w każdy przedział wartości. To jest najszybszy sposób żeby zobaczyć: czy dane są normalnie rozłożone, skośne, czy mają wiele grup?"

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram rachunków
axes[0].hist(tips['total_bill'],
             bins=20,
             color='steelblue',
             edgecolor='white',
             linewidth=0.8)
axes[0].set_title('Rozkład wartości rachunków')
axes[0].set_xlabel('Wartość rachunku [$]')
axes[0].set_ylabel('Liczba obserwacji')

# Histogram napiwków
axes[1].hist(tips['tip'],
             bins=15,
             color='salmon',
             edgecolor='white',
             linewidth=0.8)
axes[1].set_title('Rozkład napiwków')
axes[1].set_xlabel('Napiwek [$]')
axes[1].set_ylabel('Liczba obserwacji')

plt.suptitle('Dataset Tips — rozkłady zmiennych', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('histogramy.png', dpi=100)
plt.close()
print("Zapisano: histogramy.png")
```

> "Tu po raz pierwszy użyłem `plt.subplots(1, 2)` — jeden wiersz, dwie kolumny. Wynik: `axes` to tablica dwóch obiektów Axes. `axes[0]` — lewy, `axes[1]` — prawy."

> "`plt.suptitle()` — tytuł całej Figure, nie pojedynczego Axes. Siada powyżej wszystkich wykresów."

> "Co widzimy z histogramów: rachunki — prawoskośny rozkład, większość między 10-20 dolarów, sporadycznie wysokie. Napiwki — moda około 2 dolary, ale są outlierzy do 10 dolarów. To jest wiedza, którą uzyskujemy w 2 sekundy — bez liczenia średnich."

**[Live coding — Cell 9: plt.subplots — układ 2×2]**

> "Teraz pokażę jak budować bardziej złożone układy — dashboard w jednym oknie."

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# [0,0] Trend sprzedaży — liniowy
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze']
sprzedaz = [45230, 38920, 52100, 48700, 55200, 62300]
axes[0, 0].plot(miesiace, sprzedaz, marker='o', color='steelblue', linewidth=2)
axes[0, 0].set_title('Trend sprzedaży Q1-Q2')
axes[0, 0].set_ylabel('PLN')
axes[0, 0].grid(axis='y', alpha=0.4)

# [0,1] Sprzedaż per kategoria — słupkowy poziomy
kategorie = ['Komputery', 'Akcesoria', 'Audio', 'Storage']
wartosci = [15899, 2940, 1200, 350]
axes[0, 1].barh(kategorie, wartosci, color='steelblue')
axes[0, 1].set_title('Sprzedaż per kategoria')
axes[0, 1].set_xlabel('PLN')

# [1,0] Scatter: rachunek vs napiwek
axes[1, 0].scatter(tips['total_bill'], tips['tip'],
                   alpha=0.5, color='steelblue', s=30)
axes[1, 0].set_title('Rachunek vs Napiwek')
axes[1, 0].set_xlabel('Rachunek [$]')
axes[1, 0].set_ylabel('Napiwek [$]')

# [1,1] Histogram rachunków
axes[1, 1].hist(tips['total_bill'], bins=20, color='steelblue', edgecolor='white')
axes[1, 1].set_title('Rozkład rachunków')
axes[1, 1].set_xlabel('Rachunek [$]')
axes[1, 1].set_ylabel('Liczba')

plt.suptitle('Dashboard analityczny — przegląd danych', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('dashboard.png', dpi=100)
plt.close()
print("Zapisano: dashboard.png")
```

> "Układ 2×2. `axes[wiersz, kolumna]` — indeksowanie jak w numpy. axes[0,0] lewy górny, axes[1,1] prawy dolny."

> "Jeden styl wizualny — steelblue we wszystkich — spójność wizualna to podstawa profesjonalnego raportu. Nie dlatego że nie mamy inwencji, ale dlatego że mózg łatwo przetwarza spójne rzeczy."

---

### 1:15-1:25 — MATERIAŁ 4: Pandas .plot() — wykresy z DataFrame (10 min)

**[Live coding — Cell 10: Pandas .plot()]**

> "Ostatni blok dzisiaj — dobra wiadomość. Pandas ma własną metodę `.plot()` która wewnątrz używa Matplotlib, ale wymaga znacznie mniej kodu."

```python
# Sprzedaż miesięczna jako DataFrame
sprzedaz_df = pd.DataFrame({
    'miesiac': ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze'],
    'plan': [44000, 40000, 50000, 47000, 53000, 60000],
    'wykonanie': [45230, 38920, 52100, 48700, 55200, 62300]
}).set_index('miesiac')

print(sprzedaz_df)

# Wykres liniowy — jedna linia kodu
ax = sprzedaz_df.plot(
    kind='line',
    figsize=(10, 5),
    marker='o',
    title='Plan vs wykonanie sprzedaży Q1-Q2 2024',
    ylabel='PLN',
    color={'plan': 'lightsteelblue', 'wykonanie': 'steelblue'}
)
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('plan_vs_wykonanie.png', dpi=100)
plt.close()
print("Zapisano: plan_vs_wykonanie.png")
```

> "Magiczne zdanie: `.plot(kind='line')`. Pandas automatycznie bierze indeks jako oś X, a wszystkie kolumny rysuje jako oddzielne serie. Legenda tworzy się samoczynnie z nazw kolumn."

> "`kind` może być: `'line'`, `'bar'`, `'barh'`, `'hist'`, `'scatter'`, `'pie'`, `'box'`. Sprawdźcie dokumentację — większość typów dostępna z jednym parametrem."

**[Live coding — Cell 11: groupby + .plot() — workflow]**

> "Najsilniejsza kombinacja: groupby do agregacji, potem .plot() do wizualizacji. Pełny pipeline w pięciu linijkach."

```python
# Sprzedaż per dzień tygodnia w datasecie tips
sprzedaz_dzien = tips.groupby('day', observed=True)['total_bill'].mean().round(2)
print("Średni rachunek per dzień:")
print(sprzedaz_dzien)

# Bezpośrednio do wykresu
ax = sprzedaz_dzien.plot(
    kind='bar',
    figsize=(8, 5),
    color='steelblue',
    title='Średni rachunek per dzień tygodnia',
    ylabel='Średni rachunek [$]',
    rot=0          # etykiety osi X bez obrotu
)
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('rachunek_dzien.png', dpi=100)
plt.close()
print("Zapisano: rachunek_dzien.png")
```

> "Widzicie: `groupby('day')['total_bill'].mean()` zwraca Series z indeksem day. `.plot(kind='bar')` bierze ten indeks jako oś X. Jeden pipeline: ładujesz dane → czyścisz → łączysz → agregatujesz → wizualizujesz. To jest właśnie praca analityka danych."

> "Kluczowa różnica Pandas .plot() vs bezpośrednie Matplotlib: Pandas jest szybszy do prototypowania, Matplotlib daje pełną kontrolę. W pracy: zacznij od Pandas .plot(), jeśli potrzebujesz czegoś specyficznego — przejdź na Matplotlib."

---

### 1:25-1:35 — AKTYWNOŚĆ: Trzy wykresy z datasetu tips (10 min)

> "Czas żebyście sami spróbowali. 8 minut, trzy wykresy — dataset tips, który już znamy."

**[Wyświetl na projektorze, studenci piszą samodzielnie]**

```
ZADANIE — 3 wykresy z datasetu tips:

1. Wykres słupkowy: ile zamówień (count) per dzień tygodnia?
   tips.groupby('day', observed=True)['total_bill'].count().plot(kind='bar', ...)

2. Scatter: total_bill na osi X, tip na osi Y.
   Kolor = dzień (możesz użyć prostego koloru, niekoniecznie mapowania)
   ax.scatter(tips['total_bill'], tips['tip'], ...)

3. Histogram: rozkład napiwków (kolumna 'tip').
   Ile binów? Dobierz sam. Opis osi — koniecznie.

Każdy wykres: tytuł + etykiety osi + plt.savefig() + plt.close()
```

> "Za 8 minut omówimy wspólnie — pokaż kod i wykres."

**[Po 8 minutach — krótki live coding rozwiązania z komentarzem]**

```python
# Rozwiązanie 1: liczba zamówień per dzień
zamowienia_dzien = tips.groupby('day', observed=True)['total_bill'].count()
ax = zamowienia_dzien.plot(
    kind='bar', figsize=(7, 4), color='steelblue',
    title='Liczba zamówień per dzień', ylabel='Liczba zamówień', rot=0
)
plt.tight_layout()
plt.savefig('zam_dzien.png', dpi=100)
plt.close()

# Rozwiązanie 2: scatter tip vs total_bill
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(tips['total_bill'], tips['tip'], alpha=0.6, color='steelblue', s=40)
ax.set_title('Rachunek vs Napiwek')
ax.set_xlabel('Rachunek [$]')
ax.set_ylabel('Napiwek [$]')
plt.tight_layout()
plt.savefig('scatter_aktywnosc.png', dpi=100)
plt.close()

# Rozwiązanie 3: histogram tip
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(tips['tip'], bins=20, color='salmon', edgecolor='white')
ax.set_title('Rozkład napiwków')
ax.set_xlabel('Napiwek [$]')
ax.set_ylabel('Liczba obserwacji')
plt.tight_layout()
plt.savefig('hist_tip.png', dpi=100)
plt.close()
print("Trzy wykresy zapisane.")
```

---

### 1:35-1:45 — PODSUMOWANIE

> "Co dzisiaj zrobiliśmy?"

> "Po pierwsze: architektura Matplotlib — Figure to kontener, Axes to jeden układ współrzędnych. `fig, ax = plt.subplots()` — zapamiętajcie tę linię. To jest punkt startowy 90% wykresów które napiszecie."

> "Po drugie: podstawowe typy wykresów — `plot()` dla trendów w czasie, `bar()` i `barh()` dla porównań kategorii, `scatter()` dla korelacji, `hist()` dla rozkładów. Cztery typy, cztery pytania analityczne."

> "Po trzecie: formatowanie — title, xlabel, ylabel, legend, grid, kolory. Każdy wykres bez etykiet osi i tytułu to wykres, który nie powinien trafić do raportu."

> "Po czwarte: Pandas `.plot()` — szybki prototyp, jedna linia. Połączone z groupby — kompletny pipeline od danych do wizualizacji."

> "Za tydzień — Seaborn. Matplotlib jest potężny, ale gadatliwy. Seaborn to biblioteka zbudowana na Matplotlib, specjalizująca się w wizualizacji statystycznej. Box plots, violin plots, heatmapy, FacetGrid. I wykresy, które wyglądają profesjonalnie domyślnie — bez dziesiątek linii konfiguracji."

> "Zadanie domowe: w notebooku laboratoryjnym jest Ćwiczenie 4 — subplots 2×2 + zapis PNG + commit. Zróbcie to przed następnymi zajęciami."

> "Pytania?"

---

## Notatki i wskazówki dla prowadzącego

### Typowe błędy studentów (i jak reagować)
| Błąd | Komunikat | Odpowiedź |
|------|-----------|-----------|
| Brak `plt.close()` | Wykresy nakładają się lub dublują | "Po każdym `savefig` dodaj `plt.close()` — bez tego matplotlib trzyma poprzedni wykres w pamięci" |
| Brak `%matplotlib inline` w Jupyter | Wykres się nie wyświetla | "Pierwsza komórka notebooka: `%matplotlib inline` — bez tego Jupyter nie wie gdzie renderować" |
| `ax.title` zamiast `ax.set_title()` | AttributeError | "Metody na Axes mają prefiks `set_`: `set_title()`, `set_xlabel()`, `set_ylabel()`. Bez `set_` — błąd" |
| Zbyt mała figura | Etykiety ucięte | "Zwiększ figsize: `(10, 6)` to bezpieczny rozmiar. `plt.tight_layout()` też pomaga" |
| `plt.show()` zamiast `plt.savefig()` | Puste okno lub brak wykresu w HTML | "W skryptach i nbconvert: `savefig`. W Jupyter z inline: `show` jest OK, ale `savefig` jest bezpieczniejszy" |

### Pytania kontrolne (można zadawać w trakcie)
- "Jaka jest różnica między Figure a Axes?"
- "Dlaczego `ax.plot()` a nie `plt.plot()` — kiedy którego?"
- "Co się stanie jeśli nie dodacie `plt.tight_layout()`?"

### Obserwacje z dydaktyki
- Aktywność (1:25-1:35): 8 minut to prawidłowy czas — daj naprawdę te 8 minut
- Studenci zazwyczaj robią scatter jako pierwszy, bo to najprostszy — sprawdź czy robią wszystkie trzy
- Scatter plot: często zapominają `alpha` — pokaż bez i z alpha, różnica jest natychmiastowo widoczna
- `tight_layout()` — studentom wylatuje; możesz zrobić stałą zasadę: każdy wykres kończy się `tight_layout() → savefig() → close()`
