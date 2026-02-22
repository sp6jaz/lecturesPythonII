# W09 Laboratorium — Ćwiczenia

## Matplotlib: podstawy wizualizacji danych

**Czas:** 90 minut
**Notebook:** utwórz nowy plik `W09_lab.ipynb` w VS Code
**Dataset:** tips (wbudowany w seaborn) + dane biznesowe TechShop
**Commit:** na końcu zajęć wykonaj `git commit -m "W09: matplotlib, wykresy, subplots"`

---

## Przydatne materiały

| Temat | Link |
|-------|------|
| Matplotlib — Pyplot tutorial | https://matplotlib.org/stable/tutorials/pyplot.html |
| Matplotlib — `plot()` | https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html |
| Matplotlib — `bar()` / `barh()` | https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html |
| Matplotlib — `scatter()` | https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html |
| Matplotlib — `hist()` | https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html |
| Matplotlib — `subplots()` | https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html |
| Matplotlib — Galeria przykładów | https://matplotlib.org/stable/gallery/index.html |
| Matplotlib — Lista kolorów | https://matplotlib.org/stable/gallery/color/named_colors.html |
| Matplotlib — Style sheets | https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html |

### Kluczowe pojęcia

- **Figure** — cały "obraz" (okno wykresu). Tworzy się przez `plt.figure()` lub `plt.subplots()`.
- **Axes** — pojedynczy wykres na figurze. Figure może mieć wiele Axes (subplots).
- **`plt.plot()` vs `ax.plot()`** — `plt.plot()` rysuje na aktualnym Axes. `ax.plot()` rysuje na konkretnym Axes. Preferuj `ax.plot()` — daje większą kontrolę.
- **`tight_layout()`** — automatycznie dopasowuje marginesy żeby etykiety się nie nakładały.

---

## Dane startowe — wklej jako pierwszą komórkę notebooka

```python
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Dataset tips
tips = sns.load_dataset('tips')

# Dane sprzedaży TechShop (z W08)
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze']
sprzedaz_2024 = [45230, 38920, 52100, 48700, 55200, 62300]
sprzedaz_2023 = [41000, 35000, 48000, 44000, 50000, 58000]

kategorie = ['Komputery', 'Akcesoria', 'Audio', 'Storage']
sprzedaz_kat = [15899.94, 2939.83, 1199.97, 349.93]

print(f"Tips dataset: {tips.shape}")
print(tips.head(3))
```

---

## Ćwiczenie 1: Podstawowe typy wykresów — linia, słupki, scatter (20 min)

**Cel:** Stworzyć trzy podstawowe typy wykresów i zapisać jako PNG.

### Zadanie 1.1 — Wykres liniowy: trend sprzedaży

Narysuj wykres liniowy trendu sprzedaży miesięcznej za 2024 rok.

```python
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(miesiace, sprzedaz_2024,
        color=???,           # 'steelblue'
        linewidth=???,       # 2
        marker=???,          # 'o'
        markersize=8)

ax.set_title(???)            # 'Trend sprzedaży Q1-Q2 2024'
ax.set_xlabel(???)           # 'Miesiąc'
ax.set_ylabel(???)           # 'Sprzedaż [PLN]'
ax.set_ylim(0, 70000)
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('trend_2024.png', dpi=100)
plt.close()
print("Zapisano: trend_2024.png")
```

**Sprawdzenie 1.1** ✅
Wykres liniowy z 6 punktami (kółkami) połączonymi niebieską linią. Oś Y od 0 do 70 000. Tytuł i etykiety osi widoczne. Wzrost widoczny szczególnie od kwietnia do czerwca.

---

### Zadanie 1.2 — Wykres słupkowy: sprzedaż per kategoria

Narysuj wykres słupkowy (pionowy) sprzedaży per kategoria produktów.

```python
fig, ax = plt.subplots(figsize=(9, 5))

slupki = ax.bar(???,          # kategorie
                ???,          # sprzedaz_kat
                color='steelblue',
                edgecolor='navy',
                linewidth=0.8)

# Dodaj wartości nad słupkami
for slupek, wartosc in zip(slupki, sprzedaz_kat):
    ax.text(
        slupek.get_x() + slupek.get_width() / 2,
        slupek.get_height() + 100,
        f'{wartosc:,.0f} zł',
        ha='center', va='bottom', fontsize=9
    )

ax.set_title(???)             # 'Sprzedaż per kategoria — TechShop 2024'
ax.set_xlabel('Kategoria')
ax.set_ylabel('Sprzedaż [PLN]')
ax.set_ylim(0, 18000)

plt.tight_layout()
plt.savefig('sprzedaz_kategorie.png', dpi=100)
plt.close()
print("Zapisano: sprzedaz_kategorie.png")
```

**Sprawdzenie 1.2** ✅
Cztery słupki (Komputery dominuje: ~15 900 zł). Nad każdym słupkiem wartość PLN. Komputery wyraźnie wyróżniają się wysokością — zdecydowany lider.

---

### Zadanie 1.3 — Scatter: rachunek vs napiwek (tips dataset)

Narysuj wykres punktowy zależności napiwku od wartości rachunku.

```python
fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(
    ???,              # tips['total_bill'] — oś X
    ???,              # tips['tip'] — oś Y
    alpha=???,        # 0.6 — przezroczystość
    color='steelblue',
    s=50,             # rozmiar punktu
    edgecolors='gray',
    linewidth=0.5
)

ax.set_title('Korelacja: wartość rachunku vs napiwek')
ax.set_xlabel('Wartość rachunku [$]')
ax.set_ylabel(???)    # 'Napiwek [$]'

plt.tight_layout()
plt.savefig('scatter_tips.png', dpi=100)
plt.close()
print("Zapisano: scatter_tips.png")
```

**Sprawdzenie 1.3** ✅
244 punkty rozmieszczone na wykresie. Widoczna dodatnia korelacja — wyższy rachunek → wyższy napiwek. Zagęszczenie punktów w rejonie 10-20 $ rachunku i 2-4 $ napiwku.

---

### Wyzwanie dodatkowe (jeśli skończyłeś wcześniej)
Dodaj do scatter z 1.3 kolorowanie według liczby gości (`tips['size']`) używając parametru `c=tips['size'], cmap='Blues'`. Dodaj colorbar: `plt.colorbar(scatter, ax=ax).set_label('Liczba gości')`.

---

## Ćwiczenie 2: Dostosowywanie — etykiety, kolory, legendy (20 min)

**Cel:** Opanować formatowanie wykresów: wiele serii, legenda, styl, kolory.

### Zadanie 2.1 — Porównanie dwóch lat (legenda)

Narysuj wykres liniowy porównujący sprzedaż 2023 i 2024 na jednym wykresie z legendą.

```python
fig, ax = plt.subplots(figsize=(10, 5))

# Seria 2023 — linia przerywana
ax.plot(miesiace, sprzedaz_2023,
        label=???,            # '2023'
        color='lightsteelblue',
        linewidth=2,
        marker='s',           # kwadraty
        linestyle='--')       # przerywana

# Seria 2024 — linia ciągła
ax.plot(miesiace, sprzedaz_2024,
        label=???,            # '2024'
        color='steelblue',
        linewidth=2,
        marker='o')

ax.set_title('Sprzedaż Q1-Q2: porównanie rok do roku')
ax.set_xlabel('Miesiąc')
ax.set_ylabel('Sprzedaż [PLN]')
ax.legend(title=???, loc='upper left')  # title='Rok'
ax.grid(axis='y', alpha=???)            # 0.4

plt.tight_layout()
plt.savefig('porownanie_lat.png', dpi=100)
plt.close()
print("Zapisano: porownanie_lat.png")
```

**Sprawdzenie 2.1** ✅
Dwie linie: ciągła (2024) i przerywana (2023). Legenda z tytułem "Rok" w lewym górnym rogu. Linie 2024 wyraźnie wyżej niż 2023 — wzrost rok do roku widoczny w każdym miesiącu.

---

### Zadanie 2.2 — Słupki poziome z kolorami (barh)

Narysuj słupki poziome sprzedaży per kategoria. Każdy słupek innym kolorem.

```python
kolory_kat = ['#2196F3', '#66BB6A', '#FFA726', '#AB47BC']

fig, ax = plt.subplots(figsize=(9, 5))

# barh = horizontal bar
ax.barh(???,              # kategorie
        ???,              # sprzedaz_kat
        color=kolory_kat)

# Etykiety wartości przy słupkach
for i, (kat, wartosc) in enumerate(zip(kategorie, sprzedaz_kat)):
    ax.text(wartosc + 100, i,
            f'{wartosc:,.0f} zł',
            va='center', fontsize=9)

ax.set_title('Sprzedaż per kategoria — układ poziomy')
ax.set_xlabel('Sprzedaż [PLN]')
ax.set_xlim(0, 18000)

plt.tight_layout()
plt.savefig('kategorie_poziome.png', dpi=100)
plt.close()
print("Zapisano: kategorie_poziome.png")
```

**Sprawdzenie 2.2** ✅
Cztery poziome słupki z różnymi kolorami. Każdy słupek ma wartość PLN po prawej stronie. Komputery zdecydowanie najdłuższy — niebieski słupek dominuje. Format poziomy — etykiety kategorii czytelne bez obrotu.

---

### Zadanie 2.3 — Styl wykresów

Zastosuj styl `seaborn-v0_8-whitegrid` i narysuj wykres liniowy trendu.

```python
# Zastosuj styl
plt.style.use('seaborn-v0_8-whitegrid')

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(miesiace, sprzedaz_2024,
        color='#1565C0',
        linewidth=2.5,
        marker='o',
        markersize=10,
        label='Sprzedaż 2024')

ax.fill_between(miesiace, sprzedaz_2024,
                alpha=0.15,
                color='#1565C0')   # wypełnienie pod linią

ax.set_title('Trend sprzedaży 2024 — styl seaborn', fontsize=13)
ax.set_xlabel('Miesiąc')
ax.set_ylabel('Sprzedaż [PLN]')
ax.legend()

plt.tight_layout()
plt.savefig('trend_styl.png', dpi=100)
plt.close()

# Przywróć domyślny styl
plt.style.use('default')
print("Zapisano: trend_styl.png")
```

**Sprawdzenie 2.3** ✅
Wykres z białym tłem i szarą siatką (styl seaborn). Pod linią trendu widoczne jasne niebieskie wypełnienie (`fill_between`). Wygląda profesjonalnie — gotowy do prezentacji.

---

### Wyzwanie dodatkowe
Pobaw się parametrami `plt.style.use()`. Dostępne style: `'ggplot'`, `'bmh'`, `'dark_background'`, `'fivethirtyeight'`. Narysuj ten sam wykres w każdym stylu i porównaj.

---

## Ćwiczenie 3: Pełna wizualizacja z datasetu tips (30 min) — samodzielne

**Cel:** Przeprowadzić samodzielnie analizę wizualną datasetu tips i odpowiedzieć na pytania biznesowe.

To jest ćwiczenie **samodzielne** — spróbuj przez 10 minut sam zanim poprosisz o pomoc.

Restauracja "Pod Widelcem" chce wiedzieć:

---

### Zadanie 3.1 — Kiedy klienci zostawiają najwyższe napiwki?

Oblicz **średni napiwek per dzień tygodnia** i narysuj wykres słupkowy.

```python
# Twój kod:
sredni_napiwek = ???  # groupby('day')['tip'].mean().round(2)

# Wykres:
ax = sredni_napiwek.plot(
    kind=???,          # 'bar'
    figsize=(8, 5),
    color='steelblue',
    title=???,         # 'Średni napiwek per dzień tygodnia'
    ylabel='Napiwek [$]',
    rot=0
)
ax.grid(axis='y', alpha=0.4)
plt.tight_layout()
plt.savefig(???)       # 'napiwek_dzien.png'
plt.close()
```

**Sprawdzenie 3.1** ✅
Wyniki (przybliżone):
- Sun: ~3.26 $ (najwyższy)
- Sat: ~2.99 $
- Thur: ~2.77 $
- Fri: ~2.73 $

Obserwacja: **Niedziela** przynosi najwyższe napiwki — klienci są hojniejsi w weekend.

---

### Zadanie 3.2 — Czy palacze dają wyższe napiwki?

Narysuj scatter: `total_bill` vs `tip`, z kolorowaniem według kolumny `smoker` (Tak/Nie).

```python
fig, ax = plt.subplots(figsize=(9, 6))

# Podziel na dwie grupy i narysuj osobno
palacze = tips[tips['smoker'] == 'Yes']
niepalacze = tips[tips['smoker'] == 'No']

ax.scatter(???,   # palacze['total_bill']
           ???,   # palacze['tip']
           alpha=0.6, color='tomato', label='Palacz', s=50)

ax.scatter(???,   # niepalacze['total_bill']
           ???,   # niepalacze['tip']
           alpha=0.6, color='steelblue', label='Niepalacz', s=50)

ax.set_title('Rachunek vs napiwek: palacze vs niepalacze')
ax.set_xlabel('Wartość rachunku [$]')
ax.set_ylabel('Napiwek [$]')
ax.legend(title='Palacz')

plt.tight_layout()
plt.savefig('scatter_palacze.png', dpi=100)
plt.close()
print("Zapisano: scatter_palacze.png")
```

**Sprawdzenie 3.2** ✅
Dwa kolory punktów: czerwony = palacze, niebieski = niepalacze. Punkty mieszają się — nie widać wyraźnej różnicy. Obserwacja: palenie nie ma prostego związku z wysokością napiwku.

---

### Zadanie 3.3 — Rozkład napiwków (histogram + obserwacja)

Narysuj histogram kolumny `tip`. Dobierz liczbę binów tak, żeby wykres był informatywny (spróbuj bins=10, 20, 30 i wybierz najlepszy).

```python
fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(???,           # tips['tip']
        bins=???,      # zaproponuj: 20
        color='salmon',
        edgecolor='white',
        linewidth=0.8)

ax.set_title(???)
ax.set_xlabel('Napiwek [$]')
ax.set_ylabel('Liczba obserwacji')

# Dodaj pionową linię — średnia
ax.axvline(tips['tip'].mean(),
           color='darkred',
           linewidth=2,
           linestyle='--',
           label=f"Średnia: {tips['tip'].mean():.2f} $")
ax.legend()

plt.tight_layout()
plt.savefig('histogram_napiwki.png', dpi=100)
plt.close()
print("Zapisano: histogram_napiwki.png")
```

**Sprawdzenie 3.3** ✅
Histogram z wyraźną skośnością prawostronną — większość napiwków 1.5-3 $, ale są outlierzy do 10 $. Czerwona przerywana linia = średnia (~2.99 $). `axvline` — linia pionowa na konkretnej wartości X — przydatne do zaznaczenia średniej/mediany/progu.

---

### Zadanie 3.4 — Słupkowy: liczba zamówień per pora dnia

Oblicz liczbę zamówień per `time` (Lunch/Dinner) i per `sex`. Narysuj wykres słupkowy grupowany.

```python
# Zlicz zamówienia per pora dnia i płeć
count_df = tips.groupby(['time', 'sex'], observed=True)['total_bill'].count().unstack()
print(count_df)

# Wykres słupkowy grupowany
ax = count_df.plot(
    kind='bar',
    figsize=(8, 5),
    color=['steelblue', 'salmon'],
    title='Liczba zamówień: pora dnia × płeć',
    ylabel='Liczba zamówień',
    rot=0
)
ax.legend(title='Płeć')
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('zamowienia_pora.png', dpi=100)
plt.close()
print("Zapisano: zamowienia_pora.png")
```

**Sprawdzenie 3.4** ✅
Dwa grupy słupków (Lunch/Dinner), każda podzielona na Male/Female. Dinner zdecydowanie dominuje pod względem liczby zamówień. Mężczyźni zamawiają częściej niż kobiety w obu porach dnia.

---

### Własna obserwacja (obowiązkowe)
Dodaj komórkę Markdown w notebooku i napisz (2-3 zdania): co wynika z Twoich 4 wykresów? Jaką radę dałbyś menedżerowi restauracji?

---

## Ćwiczenie 4: Wiele wykresów (subplots) + zapis + commit (15 min)

**Cel:** Zbudować dashboard analityczny 2×2, zapisać PNG i wykonać commit.

### Zadanie 4.1 — Dashboard tips 2×2

Stwórz Figure z 4 wykresami w układzie 2×2:

```python
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# [0, 0] — Średni napiwek per dzień (słupkowy)
sredni_napiwek_dzien = tips.groupby('day', observed=True)['tip'].mean()
axes[0, 0].bar(sredni_napiwek_dzien.index,
               sredni_napiwek_dzien.values,
               color='steelblue')
axes[0, 0].set_title('Średni napiwek per dzień')
axes[0, 0].set_ylabel('Napiwek [$]')
axes[0, 0].grid(axis='y', alpha=0.4)

# [0, 1] — Scatter: rachunek vs napiwek
axes[0, 1].scatter(tips['total_bill'], tips['tip'],
                   alpha=???,          # 0.5
                   color='steelblue',
                   s=30)
axes[0, 1].set_title(???)              # 'Rachunek vs Napiwek'
axes[0, 1].set_xlabel('Rachunek [$]')
axes[0, 1].set_ylabel('Napiwek [$]')

# [1, 0] — Histogram napiwków
axes[1, 0].hist(tips['tip'],
                bins=???,              # 20
                color='salmon',
                edgecolor='white')
axes[1, 0].set_title('Rozkład napiwków')
axes[1, 0].set_xlabel('Napiwek [$]')
axes[1, 0].set_ylabel('Liczba obserwacji')

# [1, 1] — Liczba zamówień per dzień (bar)
zamowienia_dzien = tips.groupby('day', observed=True)['total_bill'].count()
axes[1, 1].bar(zamowienia_dzien.index,
               zamowienia_dzien.values,
               color='lightsteelblue',
               edgecolor='steelblue')
axes[1, 1].set_title('Liczba zamówień per dzień')
axes[1, 1].set_ylabel('Liczba zamówień')
axes[1, 1].grid(axis='y', alpha=0.4)

plt.suptitle('Dashboard Restauracji "Pod Widelcem"',
             fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('dashboard_tips.png', dpi=100)
plt.close()
print("Zapisano: dashboard_tips.png")
```

**Sprawdzenie 4.1** ✅
4 wykresy w układzie 2×2: górny lewy = słupkowy napiwki per dzień, górny prawy = scatter, dolny lewy = histogram, dolny prawy = słupkowy liczba zamówień. Tytuł główny ponad wszystkimi. Wszystkie wykresy czytelne — bez uciętych etykiet (`tight_layout`).

---

### Zadanie 4.2 — Commit na GitHub

Zapisz notebook i wykonaj commit zawierający notebook i PNG.

```bash
# W terminalu VS Code (Ctrl+`)
git add W09_lab.ipynb dashboard_tips.png
git add trend_2024.png sprzedaz_kategorie.png scatter_tips.png
git commit -m "W09: matplotlib — wykresy, subplots, dashboard"
git push
```

Sprawdź na GitHub czy commit jest widoczny. Pokaż prowadzącemu link do swojego commita.

**Sprawdzenie 4.2** ✅
Na GitHub w Twoim repozytorium widać: `W09_lab.ipynb` + przynajmniej `dashboard_tips.png`. Komunikat commita zawiera "W09".

---

## Podsumowanie — co dziś zrobiłeś

```
import matplotlib.pyplot as plt    → zawsze ten alias
%matplotlib inline                 → w Jupyter, jako pierwsza linia

fig, ax = plt.subplots()          → punkt startowy każdego wykresu

ax.plot()     → trend w czasie (liniowy)
ax.bar()      → porównanie kategorii (pionowy)
ax.barh()     → porównanie kategorii (poziomy, przy długich etykietach)
ax.scatter()  → korelacja dwóch zmiennych
ax.hist()     → rozkład jednej zmiennej

ax.set_title()    → tytuł wykresu
ax.set_xlabel()   → etykieta osi X
ax.set_ylabel()   → etykieta osi Y
ax.legend()       → legenda (potrzebuje label= w plot/scatter)
ax.grid()         → siatka (axis='y', alpha=0.4)
ax.axvline()      → pionowa linia na wartości X

plt.tight_layout()    → poprawia marginesy
plt.savefig('f.png')  → zapisz plik PNG
plt.close()           → zamknij Figure (zawsze po savefig!)

plt.subplots(2, 2)    → układ 2×2, axes[wiersz, kolumna]
plt.suptitle()        → tytuł całej Figure (ponad subplots)

df.plot(kind='bar')   → wykres wprost z DataFrame (Pandas)
```

### Wymagania do zaliczenia laboratorium W09
- [ ] Ćwiczenie 1: 3 podstawowe typy wykresów (linia, słupki, scatter) zapisane jako PNG
- [ ] Ćwiczenie 2: wykres z dwiema seriami i legendą + barh z kolorami
- [ ] Ćwiczenie 3: samodzielna analiza tips — 4 wykresy + komórka Markdown z obserwacją
- [ ] Ćwiczenie 4: dashboard 2×2 zapisany jako dashboard_tips.png
- [ ] Commit na GitHub z komunikatem zawierającym "W09"

---

## Jeśli utkniesz

| Problem | Rozwiązanie |
|---------|-------------|
| Wykres nie wyświetla się | Dodaj `%matplotlib inline` na początku notebooka. W VS Code: sprawdź czy masz Jupyter extension |
| Etykiety osi się nakładają | Użyj `plt.tight_layout()` lub `fig.autofmt_xdate()` dla dat. Albo: `plt.xticks(rotation=45)` |
| Legenda zasłania wykres | `plt.legend(loc='upper left')` lub `plt.legend(bbox_to_anchor=(1.05, 1))` (poza wykresem) |
| Kolory — nie wiem jakie są dostępne | Podstawowe: `'red'`, `'blue'`, `'green'`, `'orange'`. Pełna lista: matplotlib.org/stable/gallery/color/named_colors.html |
| `subplots()` — nie wiem jak adresować panele | `fig, axes = plt.subplots(2, 2)` → `axes[0, 0]` (lewy górny), `axes[1, 1]` (prawy dolny) |
| Wykres się nie zapisuje | `plt.savefig('wykres.png', dpi=150, bbox_inches='tight')` — PRZED `plt.show()`! |
| `alpha=0.6` — co to? | Przezroczystość: 0 = niewidoczny, 1 = pełny kolor. 0.6 = lekko prześwitujący |
