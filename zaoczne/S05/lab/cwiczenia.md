# S05 Laboratorium — Cwiczenia

## Matplotlib + Seaborn: wizualizacja danych i dashboardy

**Czas:** 90 minut
**Notebook:** utworz nowy plik `S05_lab.ipynb` w VS Code
**Dataset:** tips (wbudowany w seaborn)
**Commit:** na koncu zajec wykonaj `git commit -m "S05: matplotlib, seaborn, dashboard"`

---

## Przydatne materiały

| Temat | Link |
|-------|------|
| Matplotlib — Pyplot tutorial | https://matplotlib.org/stable/tutorials/pyplot.html |
| Matplotlib — Gallery | https://matplotlib.org/stable/gallery/index.html |
| Seaborn — Tutorial | https://seaborn.pydata.org/tutorial.html |
| Seaborn — API Reference | https://seaborn.pydata.org/api.html |
| Matplotlib — Cheat Sheets | https://matplotlib.org/cheatsheets/ |

---

## Dane startowe — wklej jako pierwsza komorke notebooka

```python
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
import seaborn as sns

# Ustaw motyw Seaborn globalnie
sns.set_theme(style='whitegrid', palette='muted')

# Dataset tips
tips = sns.load_dataset('tips')

# Dane sprzedazy TechShop
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze']
sprzedaz_2024 = [45230, 38920, 52100, 48700, 55200, 62300]
sprzedaz_2023 = [41000, 35000, 48000, 44000, 50000, 58000]

print(f"Tips dataset: {tips.shape[0]} wierszy, {tips.shape[1]} kolumn")
print(tips.head(3))
```

---

## Cwiczenie 1: Matplotlib — linia, slupki, scatter (20 min)

**Cel:** Stworzyc trzy podstawowe typy wykresow z datasetu tips i danych biznesowych.

### Zadanie 1.1 — Wykres liniowy: trend sprzedazy

Narysuj wykres liniowy trendu sprzedazy miesiecznej za 2024 rok.

```python
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(miesiace, sprzedaz_2024,
        color=???,           # 'steelblue'
        linewidth=???,       # 2
        marker=???,          # 'o'
        markersize=8)

ax.set_title(???)            # 'Trend sprzedazy Q1-Q2 2024'
ax.set_xlabel(???)           # 'Miesiac'
ax.set_ylabel(???)           # 'Sprzedaz [PLN]'
ax.set_ylim(0, 70000)
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('trend_2024.png', dpi=100)
plt.close()
print("Zapisano: trend_2024.png")
```

### Zadanie 1.2 — Wykres slupkowy: sredni rachunek per dzien (tips)

Oblicz sredni rachunek per dzien tygodnia i narysuj wykres slupkowy.

```python
sredni_rachunek = tips.groupby('day')['total_bill'].mean().round(2)
print(sredni_rachunek)

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(???,                  # sredni_rachunek.index
       ???,                  # sredni_rachunek.values
       color='steelblue',
       edgecolor='navy',
       linewidth=0.8)

ax.set_title(???)            # 'Sredni rachunek per dzien tygodnia'
ax.set_xlabel('Dzien')
ax.set_ylabel(???)           # 'Sredni rachunek [$]'
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('rachunek_dzien.png', dpi=100)
plt.close()
print("Zapisano: rachunek_dzien.png")
```

### Zadanie 1.3 — Scatter: rachunek vs napiwek (tips)

Narysuj wykres punktowy zaleznosci napiwku od wartosci rachunku.

```python
fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(
    ???,              # tips['total_bill'] — os X
    ???,              # tips['tip'] — os Y
    alpha=???,        # 0.6
    color='steelblue',
    s=50,
    edgecolors='gray',
    linewidth=0.5
)

ax.set_title('Korelacja: wartosc rachunku vs napiwek')
ax.set_xlabel(???)   # 'Wartosc rachunku [$]'
ax.set_ylabel(???)   # 'Napiwek [$]'

plt.tight_layout()
plt.savefig('scatter_tips.png', dpi=100)
plt.close()
print("Zapisano: scatter_tips.png")
```

### Sprawdzenie 1 ✅

- [ ] Wykres liniowy: 6 punktow (kolek) polaczonych niebieska linia, os Y od 0 do 70 000
- [ ] Wykres slupkowy: 4 slupki (Thur/Fri/Sat/Sun), wartosci przyblizne: Thur ~17.7, Fri ~17.2, Sat ~20.4, Sun ~21.4
- [ ] Scatter: 244 punkty, widoczna dodatnia korelacja — wyzszy rachunek = wyzszy napiwek
- [ ] Kazdy wykres ma tytul i etykiety osi
- [ ] Trzy pliki PNG w katalogu projektu

---

## Cwiczenie 2: Formatowanie — tytuly, etykiety, legenda, style (15 min)

**Cel:** Opanowac formatowanie: wiele serii, legenda, kolory, styl, adnotacja.

### Zadanie 2.1 — Porownanie dwoch lat (legenda)

Narysuj wykres liniowy porownujacy sprzedaz 2023 i 2024 na jednym wykresie z legenda.

```python
fig, ax = plt.subplots(figsize=(10, 5))

# Seria 2023 — linia przerywana
ax.plot(miesiace, sprzedaz_2023,
        label=???,            # '2023'
        color='lightsteelblue',
        linewidth=2,
        marker='s',
        linestyle='--')

# Seria 2024 — linia ciagla
ax.plot(miesiace, sprzedaz_2024,
        label=???,            # '2024'
        color='steelblue',
        linewidth=2,
        marker='o')

ax.set_title('Sprzedaz Q1-Q2: porownanie rok do roku')
ax.set_xlabel('Miesiac')
ax.set_ylabel('Sprzedaz [PLN]')
ax.legend(title=???, loc='upper left')   # title='Rok'
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('porownanie_lat.png', dpi=100)
plt.close()
print("Zapisano: porownanie_lat.png")
```

### Zadanie 2.2 — Styl i adnotacja

Zastosuj styl `seaborn-v0_8-whitegrid` i dodaj adnotacje strzalka na szczycie trendu.

```python
plt.style.use('seaborn-v0_8-whitegrid')

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(miesiace, sprzedaz_2024,
        color='#1565C0', linewidth=2.5,
        marker='o', markersize=10, label='Sprzedaz 2024')

ax.fill_between(miesiace, sprzedaz_2024,
                alpha=0.15, color='#1565C0')

# Adnotacja na szczycie
ax.annotate(
    'Szczyt: 62 300 PLN',
    xy=(5, 62300),
    xytext=(3, 66000),
    arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
    fontsize=10, color='red', fontweight='bold'
)

ax.set_title('Trend sprzedazy 2024 — styl seaborn + adnotacja', fontsize=13)
ax.set_xlabel('Miesiac')
ax.set_ylabel('Sprzedaz [PLN]')
ax.legend()

plt.tight_layout()
plt.savefig('trend_styl.png', dpi=100)
plt.close()

plt.style.use('default')   # przywroc domyslny styl
print("Zapisano: trend_styl.png")
```

### Sprawdzenie 2 ✅

- [ ] Wykres porownawczy: dwie linie (ciagla 2024, przerywana 2023), legenda z tytulem "Rok"
- [ ] Linia 2024 wyraznie wyzej — wzrost rok do roku widoczny
- [ ] Wykres ze stylem: biale tlo z siatka, niebieskie wypelnienie pod linia, strzalka na szczycie
- [ ] `fill_between` widoczne jako jasnoniebieski obszar pod linia

---

## Cwiczenie 3: Subplots 2x2 z roznymi typami wykresow (15 min)

**Cel:** Zbudowac uklad 4 wykresow na jednej figurze, kazdy innego typu.

### Zadanie 3.1 — Dashboard Matplotlib 2x2

Stworz Figure z 4 wykresami w ukladzie 2x2 uzywajac datasetu tips:

```python
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# [0, 0] — Sredni napiwek per dzien (slupkowy)
sredni_napiwek_dzien = tips.groupby('day')['tip'].mean()
axes[0, 0].bar(
    sredni_napiwek_dzien.index,
    sredni_napiwek_dzien.values,
    color='steelblue')
axes[0, 0].set_title(???)           # 'Sredni napiwek per dzien'
axes[0, 0].set_ylabel('Napiwek [$]')
axes[0, 0].grid(axis='y', alpha=0.4)

# [0, 1] — Scatter: rachunek vs napiwek
axes[0, 1].scatter(
    tips['total_bill'], tips['tip'],
    alpha=???,                       # 0.5
    color='steelblue', s=30)
axes[0, 1].set_title(???)           # 'Rachunek vs Napiwek'
axes[0, 1].set_xlabel('Rachunek [$]')
axes[0, 1].set_ylabel('Napiwek [$]')

# [1, 0] — Histogram napiwkow
axes[1, 0].hist(
    tips['tip'],
    bins=???,                        # 20
    color='salmon',
    edgecolor='white')
axes[1, 0].set_title('Rozklad napiwkow')
axes[1, 0].set_xlabel('Napiwek [$]')
axes[1, 0].set_ylabel('Liczba obserwacji')

# [1, 1] — Liczba zamowien per dzien
zamowienia_dzien = tips.groupby('day')['total_bill'].count()
axes[1, 1].bar(
    zamowienia_dzien.index,
    zamowienia_dzien.values,
    color='lightsteelblue',
    edgecolor='steelblue')
axes[1, 1].set_title('Liczba zamowien per dzien')
axes[1, 1].set_ylabel('Liczba zamowien')
axes[1, 1].grid(axis='y', alpha=0.4)

plt.suptitle(???,                    # 'Dashboard restauracji — 4 wykresy'
             fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('dashboard_4panel.png', dpi=100)
plt.close()
print("Zapisano: dashboard_4panel.png")
```

### Sprawdzenie 3 ✅

- [ ] 4 wykresy w ukladzie 2x2
- [ ] Gorny lewy: slupkowy (sredni napiwek: Sun ~3.26, Sat ~2.99, Thur ~2.77, Fri ~2.73)
- [ ] Gorny prawy: scatter z 244 punktami
- [ ] Dolny lewy: histogram napiwkow (prawoskosny rozklad)
- [ ] Dolny prawy: slupkowy (liczba zamowien: Sat ~87, Sun ~76, Thur ~62, Fri ~19)
- [ ] Tytul glowny ponad wszystkimi wykresami (`suptitle`)
- [ ] Brak ucietych etykiet (`tight_layout`)

---

## Cwiczenie 4: Seaborn — barplot, boxplot, heatmap korelacji (20 min)

**Cel:** Tworzyc wykresy statystyczne Seaborn z parametrem `hue` i odpowiadac na pytania biznesowe.

### Zadanie 4.1 — Barplot z podzialem na grupy

Sredni rachunek per dzien tygodnia, z podzialem na plec platacego.

```python
fig, ax = plt.subplots(figsize=(9, 5))

sns.barplot(
    data=???,            # tips
    x=???,               # 'day'
    y=???,               # 'total_bill'
    hue=???,             # 'sex'
    palette='muted',
    ax=ax
)

ax.set_title('Sredni rachunek wg dnia tygodnia i plci')
ax.set_xlabel('Dzien tygodnia')
ax.set_ylabel('Sredni rachunek (USD)')

plt.tight_layout()
plt.savefig('barplot_hue.png', dpi=100)
plt.close()
print("Zapisano: barplot_hue.png")
```

**Pytanie:** W ktory dzien mezczyzni placa srednio najwiecej?

### Zadanie 4.2 — Boxplot: rozklad napiwkow

Rozklad napiwkow per dzien tygodnia, z podzialem na pore dnia (Lunch/Dinner).

```python
fig, ax = plt.subplots(figsize=(9, 5))

sns.boxplot(
    data=tips,
    x=???,               # 'day'
    y=???,               # 'tip'
    hue=???,             # 'time'
    palette='pastel',
    ax=ax
)

ax.set_title('Rozklad napiwkow wg dnia i pory dnia')
ax.set_xlabel('Dzien tygodnia')
ax.set_ylabel('Napiwek (USD)')

plt.tight_layout()
plt.savefig('boxplot_hue.png', dpi=100)
plt.close()
print("Zapisano: boxplot_hue.png")
```

**Pytanie:** W ktorym dniu mediana napiwku jest najwyzsza? Czy kolacje generuja wyzsze napiwki?

### Zadanie 4.3 — Heatmapa korelacji

Stworz heatmape korelacji zmiennych numerycznych datasetu tips.

```python
fig, ax = plt.subplots(figsize=(6, 5))

# Oblicz korelacje
corr = tips.select_dtypes('number').corr()

sns.heatmap(
    ???,                 # corr
    annot=???,           # True — liczby w komorkach
    fmt=???,             # '.2f' — dwa miejsca po przecinku
    cmap=???,            # 'coolwarm'
    center=0,
    square=True,
    ax=ax
)

ax.set_title('Macierz korelacji — dataset tips')

plt.tight_layout()
plt.savefig('heatmap_corr.png', dpi=100)
plt.close()
print("Zapisano: heatmap_corr.png")
```

**Pytanie:** Ktore dwie zmienne maja najsilniejsza korelacje? Ile wynosi?

### Zadanie 4.4 (bonus) — Violinplot

Porownaj rozklad rachunkow Lunch vs Dinner z podzialem na plec.

```python
fig, ax = plt.subplots(figsize=(8, 5))

sns.violinplot(
    data=tips,
    x='time',
    y='total_bill',
    hue='sex',
    split=True,
    palette='muted',
    inner='box',
    ax=ax
)

ax.set_title('Rozklad rachunkow: Lunch vs Kolacja wg plci')
ax.set_xlabel('Pora dnia')
ax.set_ylabel('Rachunek (USD)')

plt.tight_layout()
plt.savefig('violin_bonus.png', dpi=100)
plt.close()
print("Zapisano: violin_bonus.png")
```

### Sprawdzenie 4 ✅

- [ ] Barplot: 4 dni, kazdy z dwoma slupkami (Male/Female), wasy bledow widoczne (95% CI)
- [ ] Boxplot: skrzynki z mediana, IQR, wasami i outlierami
- [ ] Heatmap: liczby w kazdej komorce, skala coolwarm, korelacja total_bill-tip ~0.68
- [ ] Parametr `hue` uzyty poprawnie w barplot i boxplot (podwojne kolory)
- [ ] Odpowiedzi na pytania biznesowe (w komentarzu lub komorce Markdown)

---

## Cwiczenie 5: Dashboard — 4 wykresy na jednym rysunku + eksport PNG (20 min)

**Cel:** Zbudowac kompletny dashboard analityczny Seaborn, wyeksportowac do PNG i wykonac commit.

### Kontekst biznesowy

Wlasciciel restauracji "Pod Widelcem" chce jednoobrazkowy raport: przychody, napiwki, korelacje, porownania. Twoj dashboard ma odpowiedziec na pytania:
- Ktory dzien przynosi najwiecej przychodu?
- Jak rozkladaja sie napiwki?
- Czy jest zwiazek miedzy rachunkiem a napiwkiem?
- Jakie sa korelacje miedzy zmiennymi?

### Zadanie 5.1 — Dashboard Seaborn 2x2

Stworz figure z 4 panelami Seaborn:

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10), constrained_layout=True)

# === PANEL [0, 0]: Barplot — sredni rachunek per dzien, hue='sex' ===
sns.barplot(
    data=tips, x='day', y='total_bill',
    hue='sex', palette='muted', ax=axes[0, 0]
)
axes[0, 0].set_title('Sredni rachunek wg dnia i plci', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Dzien tygodnia')
axes[0, 0].set_ylabel('Rachunek (USD)')

# === PANEL [0, 1]: Boxplot — rozklad napiwkow per dzien ===
sns.boxplot(
    data=???,            # tips
    x=???,               # 'day'
    y=???,               # 'tip'
    palette='pastel',
    ax=axes[0, 1]
)
axes[0, 1].set_title('Rozklad napiwkow wg dnia', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Dzien tygodnia')
axes[0, 1].set_ylabel('Napiwek (USD)')

# === PANEL [1, 0]: Heatmapa korelacji ===
corr = tips.select_dtypes('number').corr()
sns.heatmap(
    corr,
    annot=True, fmt='.2f',
    cmap='coolwarm', center=0,
    square=True,
    ax=axes[1, 0],
    cbar=False
)
axes[1, 0].set_title('Korelacja zmiennych', fontsize=12, fontweight='bold')

# === PANEL [1, 1]: Scatterplot — rachunek vs napiwek, hue='smoker' ===
sns.scatterplot(
    data=tips,
    x=???,               # 'total_bill'
    y=???,               # 'tip'
    hue=???,             # 'smoker'
    alpha=0.7,
    ax=axes[1, 1],
    palette={'Yes': '#e74c3c', 'No': '#2ecc71'}
)
axes[1, 1].set_title('Rachunek vs napiwek (palacze)', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Rachunek (USD)')
axes[1, 1].set_ylabel('Napiwek (USD)')

fig.suptitle(
    'Restaurant Analytics Dashboard — Dataset Tips (244 rachunki)',
    fontsize=15, fontweight='bold'
)

# === EKSPORT ===
plt.savefig(
    'dashboard_seaborn.png',
    dpi=150,
    bbox_inches='tight',
    facecolor='white'
)
plt.close()
print("Dashboard zapisany: dashboard_seaborn.png")
```

### Zadanie 5.2 — Wnioski biznesowe

Dodaj komorke Markdown w notebooku i odpowiedz (2-3 zdania na kazde pytanie):

1. **Ktory dzien jest najbardziej dochodowy?** (uzyj danych z dashboardu)
2. **Czy palacze zostawiaja wyzsze napiwki?** (patrz scatter)
3. **Jaka jest najsilniejsza korelacja w danych?** (patrz heatmap)

### Zadanie 5.3 — Commit do repozytorium Git

```bash
# W terminalu VS Code (Ctrl+`)
git add S05_lab.ipynb dashboard_seaborn.png
git commit -m "S05: matplotlib, seaborn, dashboard restauracji"
git push
```

### Sprawdzenie 5 ✅

- [ ] Dashboard ma 4 panele: barplot, boxplot, heatmap, scatterplot
- [ ] Kazdy panel ma tytul i etykiety osi
- [ ] Tytul glowny figury widoczny (`suptitle`)
- [ ] Plik `dashboard_seaborn.png` istnieje w katalogu — rozmiar > 50 KB
- [ ] `dpi=150` i `bbox_inches='tight'` w `savefig`
- [ ] Komorka Markdown z wnioskami biznesowymi (minimum 3 odpowiedzi)
- [ ] Commit na GitHub z komunikatem zawierajacym "S05"
- [ ] Kod wykonuje sie bez bledow (zaden `Error` / `Exception`)

---

## Podsumowanie — kluczowe komendy

```python
# === MATPLOTLIB — podstawy ===
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 5))     # punkt startowy

ax.plot(x, y, marker='o', color='steelblue')   # liniowy (trend)
ax.bar(x, y, color='steelblue')                # slupkowy pionowy
ax.barh(x, y, color='steelblue')               # slupkowy poziomy
ax.scatter(x, y, alpha=0.6)                     # punktowy (korelacja)
ax.hist(data, bins=20)                           # histogram (rozklad)

# === FORMATOWANIE ===
ax.set_title('Tytul', fontsize=14)
ax.set_xlabel('Os X')
ax.set_ylabel('Os Y')
ax.legend(title='Legenda')
ax.grid(axis='y', alpha=0.4)
ax.annotate('Tekst', xy=(x, y), xytext=(tx, ty),
            arrowprops=dict(arrowstyle='->'))

# === SUBPLOTS ===
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0]   # dostep: [wiersz, kolumna]
plt.suptitle('Tytul glowny')

# === PANDAS .plot() ===
df.plot(kind='bar', figsize=(8, 5), title='Tytul')
tips.groupby('day')['tip'].mean().plot(kind='bar')

# === SEABORN ===
import seaborn as sns
sns.set_theme(style='whitegrid', palette='muted')

sns.barplot(data=df, x='kat', y='num', hue='grupa', ax=ax)
sns.boxplot(data=df, x='kat', y='num', hue='grupa', ax=ax)
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
sns.scatterplot(data=df, x='x', y='y', hue='grupa', ax=ax)
g = sns.pairplot(df, hue='kat')   # nie przyjmuje ax=

# === EKSPORT ===
plt.savefig('plik.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()   # ZAWSZE po savefig!
```

### Wymagania do zaliczenia S05

- [ ] Cw 1: trzy podstawowe typy wykresow (linia, slupki, scatter) zapisane jako PNG
- [ ] Cw 2: wykres z dwiema seriami i legenda + styl z adnotacja
- [ ] Cw 3: dashboard 2x2 w Matplotlib (`subplots` + `suptitle`)
- [ ] Cw 4: wykresy Seaborn z parametrem `hue` (barplot, boxplot, heatmap)
- [ ] Cw 5: dashboard Seaborn 4-panelowy wyeksportowany jako PNG + wnioski + commit
