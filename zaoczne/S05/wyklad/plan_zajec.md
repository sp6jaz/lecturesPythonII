# S05 Wykład — Plan zajęć dla prowadzącego

## Temat: Matplotlib + Seaborn — wizualizacja danych i dashboardy

### Informacje organizacyjne
- **Czas:** 90 min (wykład, pierwsza połowa spotkania)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z matplotlib/seaborn/pandas
- **Dataset:** `sns.load_dataset('tips')` — 244 rachunki z restauracji
- **Kontekst:** studenci zaoczni, po S03-S04 (Pandas: DataFrame, selekcja, czyszczenie, merge, groupby)
- **Po wykładzie:** od razu laboratorium (90 min), prowadzi ta sama osoba

### Efekty uczenia sie (Bloom poziom 2-4)
Po tym wykladzie osoba studiujaca:
1. **Stosuje** konwencje `import matplotlib.pyplot as plt` i rozroznia obiekt Figure od Axes (Bloom 2)
2. **Tworzy** podstawowe typy wykresow: liniowy, slupkowy, punktowy i histogram za pomoca Matplotlib (Bloom 3)
3. **Dostosowuje** wyglad wykresow: tytuly, etykiety osi, legendy, siatka, adnotacje (Bloom 3)
4. **Konstruuje** uklad wielu wykresow za pomoca `plt.subplots(rows, cols)` (Bloom 3)
5. **Tworzy** wykresy statystyczne (barplot, boxplot, heatmap, pairplot) za pomoca Seaborn z parametrem `hue` (Bloom 3)
6. **Projektuje** wielopanelowy dashboard laczacy 4+ wykresow na jednej figurze i eksportuje go do PNG (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **WPROWADZENIE** | "Przez 4 spotkania analizowalismy dane — czas je POKAZAC" | Rozmowa |
| 0:05-0:25 | **MATERIAL 1** | Matplotlib: Figure/Axes, plot, bar, barh, scatter, hist | Live coding |
| 0:25-0:40 | **MATERIAL 2** | Formatowanie: title, xlabel, legend, grid, annotate, subplots | Live coding |
| 0:40-0:50 | **PRZERWA** | 10 minut | --- |
| 0:50-1:05 | **MATERIAL 3** | Pandas .plot() + Seaborn: barplot, boxplot, heatmap, pairplot, hue | Live coding |
| 1:05-1:20 | **MATERIAL 4** | Dashboard: wiele wykresow na jednej figurze + eksport savefig | Live coding |
| 1:20-1:30 | **PODSUMOWANIE** | Kluczowe wzorce, zapowiedz laboratorium | Rozmowa |

---

## STENOGRAM — co mowic i robic

### 0:00-0:05 — WPROWADZENIE

> "Cztery spotkania za nami. Na S01 ustawilismy warsztat pracy, na S02 NumPy, na S03 i S04 Pandas — wczytywanie, selekcja, czyszczenie, laczenie, agregacja. Za kazdym razem konczylismy na liczbach w terminalu."

> "Dzisiaj zmieniamy perspektywe. Ludzie przetwarzaja obrazy 60 000 razy szybciej niz tekst — to nie estetyka, to neurobiologia. Wykres slupkowy z piecioma kategoriami mowi wiecej niz tabela z piecioma wierszami. Dlatego wizualizacja to nie dodatek do analizy — to jej serce."

> "Plan na dzisiaj: dwie biblioteki, jedna historia. Matplotlib — fundament, szczegolowy, elastyczny. Seaborn — nadbudowka, piekne wykresy w trzech liniach. Na koniec: dashboard — wiele wykresow na jednej figurze, gotowy do prezentacji."

> "Caly dzien pracujemy na datasecie tips — dane z restauracji: 244 rachunki, napiwki, dzien tygodnia, pora dnia, plec, palenie, liczba osob. Maly, czysty, bogaty w zaleznosci."

**[Otworz VS Code z nowym notebookiem lub przygotowanym plikiem demo]**

---

### 0:05-0:25 — MATERIAL 1: Matplotlib — architektura i podstawowe wykresy (20 min)

**[Live coding — architektura Figure/Axes]**

> "Zaczynam od konwencji. W calym kursie uzywamy tej samej linii:"

```python
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

tips = sns.load_dataset('tips')
print(f"Tips: {tips.shape[0]} wierszy, {tips.shape[1]} kolumn")
```

> "Zawsze `import matplotlib.pyplot as plt`. To standard — tak samo jak `import pandas as pd`. Jesli zobaczysz gdzies inny alias — ktos nie stosuje konwencji branzowych."

> "Zanim narysujemy cokolwiek, musimy rozumiec hierarchie obiektow. Figure to cale okno — kontener. Axes to jeden uklad wspolrzednych z osiami X i Y — na nim rysujemy. Figure moze zawierac wiele Axes."

> "Sa dwa style pracy:"

```python
# Styl 1: imperatywny (pyplot) — szybki, do prostych wykresow
plt.figure(figsize=(8, 4))
plt.plot([1, 2, 3, 4], [10, 20, 15, 30])
plt.title("Najprostszy wykres")
plt.savefig("temp.png")
plt.close()

# Styl 2: obiektowy (Figure/Axes) — elastyczny, ZALECANY
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([1, 2, 3, 4], [10, 20, 15, 30])
ax.set_title("Wykres obiektowy")
plt.savefig("temp.png")
plt.close()
```

> "Ktory styl stosowac? Styl 2 — obiektowy. Na poczatku nieco bardziej rozbudowany, ale gdy zaczniecie tworzyc wiele wykresow naraz — imperatywny sie gubi. Ja pokazuje oba, zebyscie umieli czytac cudzy kod."

**[Live coding — wykres liniowy]**

> "Pierwszy powazny przyklad — trend sprzedazy miesiecznej."

```python
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze']
sprzedaz = [45230, 38920, 52100, 48700, 55200, 62300]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(miesiace, sprzedaz,
        color='steelblue',
        linewidth=2,
        marker='o',
        markersize=8)

ax.set_title('Trend sprzedazy Q1-Q2 2024', fontsize=14, fontweight='bold')
ax.set_xlabel('Miesiac')
ax.set_ylabel('Sprzedaz [PLN]')
ax.set_ylim(0, 70000)
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('trend_sprzedazy.png', dpi=100)
plt.close()
```

> "Kilka rzeczy: `figsize=(10, 5)` — szerokosc na wysokosc w calach. `marker='o'` — kolka na punktach danych, widac gdzie sa dane. `tight_layout()` — poprawia marginesy. `plt.close()` — zamyka figure, bez tego nastepny wykres sie nalazy."

**[Live coding — wykres slupkowy]**

> "Wykres slupkowy — klasyczny raport per kategoria."

```python
produkty = ['Laptop ProX', 'Monitor 27"', 'Klawiatura', 'Sluchawki BT', 'Mysz']
przychod = [11999.97, 3899.97, 1499.94, 1199.97, 449.95]

fig, ax = plt.subplots(figsize=(10, 5))

slupki = ax.bar(produkty, przychod,
                color='steelblue',
                edgecolor='navy',
                linewidth=0.8)

# Wartosci nad slupkami
for slupek, wartosc in zip(slupki, przychod):
    ax.text(slupek.get_x() + slupek.get_width() / 2,
            slupek.get_height() + 100,
            f'{wartosc:,.0f} zl',
            ha='center', va='bottom', fontsize=9)

ax.set_title('Top 5 produktow — przychod 2024', fontsize=14, fontweight='bold')
ax.set_xlabel('Produkt')
ax.set_ylabel('Przychod [PLN]')

plt.tight_layout()
plt.savefig('sprzedaz_produkty.png', dpi=100)
plt.close()
```

> "Podpisy wartosci nad slupkami — to nie dekoracja, to informacja. Bez nich widac proporcje, ale nie dokladne wartosci."

**[Live coding — barh (slupki poziome)]**

> "Gdy etykiety sa dlugie — slupki poziome. `barh()` zamiast `bar()`."

```python
kategorie = ['Komputery', 'Akcesoria', 'Audio', 'Storage']
sprzedaz_kat = [15899, 2940, 1200, 350]

fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(kategorie, sprzedaz_kat, color=['#2196F3', '#66BB6A', '#FFA726', '#AB47BC'])
ax.set_title('Sprzedaz per kategoria [PLN]')
ax.set_xlabel('PLN')

plt.tight_layout()
plt.savefig('kategorie.png', dpi=100)
plt.close()
```

**[Live coding — scatter]**

> "Scatter plot — korelacja miedzy dwiema zmiennymi. Czy rachunek wplywa na napiwek?"

```python
fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(tips['total_bill'], tips['tip'],
           alpha=0.6, color='steelblue', s=50,
           edgecolors='gray', linewidth=0.5)

ax.set_title('Korelacja: rachunek vs napiwek', fontsize=13, fontweight='bold')
ax.set_xlabel('Wartosc rachunku [$]')
ax.set_ylabel('Napiwek [$]')

plt.tight_layout()
plt.savefig('scatter_tips.png', dpi=100)
plt.close()
```

> "`alpha=0.6` — przezroczystosc. Bez niej punkty sie zaslaniaja. Z nia — widzisz zageszczenie."

**[Live coding — histogram]**

> "Histogram — rozklad jednej zmiennej. Ile obserwacji wpada w kazdy przedzial."

```python
fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(tips['total_bill'], bins=20,
        color='steelblue', edgecolor='white', linewidth=0.8)

ax.set_title('Rozklad wartosci rachunkow')
ax.set_xlabel('Wartosc rachunku [$]')
ax.set_ylabel('Liczba obserwacji')

plt.tight_layout()
plt.savefig('histogram.png', dpi=100)
plt.close()
```

> "Co widzimy: prawosskosny rozklad, wiekszosc miedzy 10-20 dolarow, sporadycznie wysokie. To wiedza uzyskana w 2 sekundy — bez liczenia srednich."

---

### 0:25-0:40 — MATERIAL 2: Formatowanie, subplots, Pandas .plot() (15 min)

**[Live coding — wiele serii + legenda]**

> "W biznesie prawie zawsze porownujemy wiele rzeczy: rok do roku, plan do wykonania."

```python
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze']
sprzedaz_2023 = [41000, 35000, 48000, 44000, 50000, 58000]
sprzedaz_2024 = [45230, 38920, 52100, 48700, 55200, 62300]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(miesiace, sprzedaz_2023,
        label='2023', color='lightsteelblue',
        linewidth=2, marker='s', linestyle='--')
ax.plot(miesiace, sprzedaz_2024,
        label='2024', color='steelblue',
        linewidth=2, marker='o')

ax.set_title('Sprzedaz Q1-Q2: porownanie rok do roku')
ax.set_xlabel('Miesiac')
ax.set_ylabel('Sprzedaz [PLN]')
ax.legend(title='Rok', loc='upper left')
ax.grid(axis='y', alpha=0.4)

plt.tight_layout()
plt.savefig('porownanie_lat.png', dpi=100)
plt.close()
```

> "Legenda: `label=` w `plot()`, potem `ax.legend()`. `linestyle='--'` — przerywana dla starszego roku. Roznicujcie markery i style, nie tylko kolory — ktos moze drukowac czarno-bialo lub miec daltonizm."

**[Live coding — annotate]**

> "Adnotacje — strzalka z tekstem pokazujaca wazny punkt."

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(miesiace, sprzedaz_2024, marker='o', color='steelblue', linewidth=2)
ax.annotate(
    'Szczyt sprzedazy!',
    xy=(5, 62300),           # punkt strzalki
    xytext=(3, 65000),       # pozycja tekstu
    arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
    fontsize=11, color='red', fontweight='bold'
)
ax.set_title('Trend z adnotacja')
ax.set_ylabel('PLN')
plt.tight_layout()
plt.savefig('annotate_demo.png', dpi=100)
plt.close()
```

> "`annotate()` — uzyteczne w raportach do zwrocenia uwagi na anomalie, szczyty, progi."

**[Live coding — subplots 2x2]**

> "Subplots — wiele wykresow na jednej figurze."

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# [0,0] Trend sprzedazy — liniowy
axes[0, 0].plot(miesiace, sprzedaz_2024, marker='o', color='steelblue', linewidth=2)
axes[0, 0].set_title('Trend sprzedazy Q1-Q2')
axes[0, 0].set_ylabel('PLN')
axes[0, 0].grid(axis='y', alpha=0.4)

# [0,1] Slupki per kategoria
kategorie = ['Komputery', 'Akcesoria', 'Audio', 'Storage']
wartosci = [15899, 2940, 1200, 350]
axes[0, 1].barh(kategorie, wartosci, color='steelblue')
axes[0, 1].set_title('Sprzedaz per kategoria')
axes[0, 1].set_xlabel('PLN')

# [1,0] Scatter: rachunek vs napiwek
axes[1, 0].scatter(tips['total_bill'], tips['tip'],
                   alpha=0.5, color='steelblue', s=30)
axes[1, 0].set_title('Rachunek vs Napiwek')
axes[1, 0].set_xlabel('Rachunek [$]')
axes[1, 0].set_ylabel('Napiwek [$]')

# [1,1] Histogram rachunkow
axes[1, 1].hist(tips['total_bill'], bins=20, color='steelblue', edgecolor='white')
axes[1, 1].set_title('Rozklad rachunkow')
axes[1, 1].set_xlabel('Rachunek [$]')
axes[1, 1].set_ylabel('Liczba')

plt.suptitle('Dashboard analityczny — 4 wykresy', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('dashboard_mpl.png', dpi=100)
plt.close()
```

> "`plt.subplots(2, 2)` — dwa wiersze, dwie kolumny. `axes[wiersz, kolumna]` — indeksowanie jak w NumPy. `plt.suptitle()` — tytul calej Figure, ponad wszystkimi wykresami."

**[Live coding — Pandas .plot()]**

> "Pandas ma wlasna metode `.plot()` ktora wewnatrz uzywa Matplotlib, ale wymaga znacznie mniej kodu."

```python
sprzedaz_df = pd.DataFrame({
    'miesiac': ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze'],
    'plan': [44000, 40000, 50000, 47000, 53000, 60000],
    'wykonanie': [45230, 38920, 52100, 48700, 55200, 62300]
}).set_index('miesiac')

ax = sprzedaz_df.plot(
    kind='line', figsize=(10, 5), marker='o',
    title='Plan vs wykonanie sprzedazy Q1-Q2 2024',
    ylabel='PLN'
)
ax.grid(axis='y', alpha=0.4)
plt.tight_layout()
plt.savefig('plan_vs_wykonanie.png', dpi=100)
plt.close()
```

> "Magiczne zdanie: `.plot(kind='line')`. Pandas automatycznie bierze indeks jako os X, a kolumny jako serie. Legenda tworzy sie samoczynnie. `kind` moze byc: `'line'`, `'bar'`, `'barh'`, `'hist'`, `'scatter'`, `'pie'`, `'box'`."

> "Najsilniejsza kombinacja: `groupby` + `.plot()`. Pelny pipeline w pieciu linijkach."

```python
ax = tips.groupby('day', observed=True)['total_bill'].mean().plot(
    kind='bar', figsize=(8, 5), color='steelblue',
    title='Sredni rachunek per dzien tygodnia',
    ylabel='Sredni rachunek [$]', rot=0
)
ax.grid(axis='y', alpha=0.4)
plt.tight_layout()
plt.savefig('rachunek_dzien.png', dpi=100)
plt.close()
```

---

### 0:40-0:50 — PRZERWA (10 min)

---

### 0:50-1:05 — MATERIAL 3: Seaborn — piekne wykresy w 3 liniach (15 min)

> "Wracamy po przerwie. Matplotlib jest potezny, ale gadatliwy. Seaborn to biblioteka zbudowana na Matplotlib, specjalizujaca sie w wizualizacji statystycznej."

**[Live coding — setup Seaborn + barplot]**

```python
# Ustaw motyw — raz, na poczatku
sns.set_theme(style='whitegrid', palette='muted')
```

> "Jedna linia — i wszystkie wykresy wygladaja profesjonalnie. Dostepne style: `white`, `dark`, `whitegrid`, `darkgrid`, `ticks`. Palety: `muted`, `bright`, `deep`, `pastel`, `colorblind`."

```python
fig, ax = plt.subplots(figsize=(9, 5))

sns.barplot(
    data=tips, x='day', y='total_bill',
    hue='sex',           # podzial na grupy kolorem
    palette='muted',
    ax=ax
)
ax.set_title('Sredni rachunek wg dnia i plci', fontsize=12)
ax.set_xlabel('Dzien tygodnia')
ax.set_ylabel('Rachunek (USD)')

plt.tight_layout()
plt.savefig('barplot_seaborn.png', dpi=100)
plt.close()
```

> "Zwroccie uwage na wasy na slupkach — to 95% przedzial ufnosci. Seaborn liczy to automatycznie. W Matplotlib musielibyscie to policzyc recznie."

> "Parametr `hue` — podzial na grupy kolorem. Dodajecie jeden parametr i slupki rozbite na dwie grupy. To jest sila Seaborn."

**[Live coding — boxplot]**

```python
fig, ax = plt.subplots(figsize=(9, 5))

sns.boxplot(
    data=tips, x='day', y='tip',
    hue='time',
    palette='pastel',
    ax=ax
)
ax.set_title('Rozklad napiwkow wg dnia i pory dnia', fontsize=12)
ax.set_xlabel('Dzien tygodnia')
ax.set_ylabel('Napiwek (USD)')

plt.tight_layout()
plt.savefig('boxplot_seaborn.png', dpi=100)
plt.close()
```

> "Boxplot — skrzynka z wasami. Skrzynka to IQR — od 25. do 75. percentyla. Linia w srodku — mediana. Wasy — 1.5 x IQR. Kropki poza wasami — outliery. Wiecej informacji niz srednia i odchylenie standardowe razem wziete."

**[Live coding — heatmap]**

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Lewa: korelacja zmiennych numerycznych
corr = tips.select_dtypes('number').corr()
sns.heatmap(
    corr, annot=True, fmt='.2f',
    cmap='coolwarm', center=0,
    ax=axes[0], square=True
)
axes[0].set_title('Korelacja zmiennych')

# Prawa: pivot heatmap — sredni rachunek per dzien i pora
pivot = tips.pivot_table(values='total_bill', index='day', columns='time', aggfunc='mean')
sns.heatmap(
    pivot, annot=True, fmt='.1f',
    cmap='YlOrRd', ax=axes[1]
)
axes[1].set_title('Sredni rachunek (dzien x pora)')

plt.tight_layout()
plt.savefig('heatmap_seaborn.png', dpi=100)
plt.close()
```

> "Heatmapa — macierz kolorow. Najczestsze zastosowania: korelacja i pivot. `annot=True` — liczby wewnatrz komorek. `cmap='coolwarm'` — niebieski negatywna, czerwony pozytywna korelacja."

> "Patrzcie: total_bill i tip — 0.68. Silna pozytywna. total_bill i size — 0.60. Wiekszy stolik = wyzszy rachunek."

**[Live coding — pairplot]**

```python
g = sns.pairplot(
    tips[['total_bill', 'tip', 'size', 'sex']],
    hue='sex',
    diag_kind='kde',
    plot_kws={'alpha': 0.6}
)
g.fig.suptitle('Pairplot — zmienne numeryczne vs plec', y=1.02, fontsize=14)
plt.savefig('pairplot.png', dpi=100, bbox_inches='tight')
plt.close()
```

> "Pairplot — automatyczna macierz wykresow. Kazda zmienna vs kazda inna. Na przekatnej — rozklad. Jedna linijka kodu dla 9 wykresow. Uwaga: pairplot tworzy wlasna figure — nie przyjmuje parametru `ax=`."

---

### 1:05-1:20 — MATERIAL 4: Dashboard + eksport (15 min)

> "Teraz laczymy wszystko. Dashboard — wiele wykresow na jednej figurze, opowiadajace spojna historie."

> "Scenariusz: jestescie analitykami restauracji. Wlasciciel pyta: jak idzie biznes? Kiedy zarabiamy najwiecej? Kto zostawia najwieksze napiwki? Macie 2 minuty na prezentacje. Odpowiedz: dashboard."

**[Live coding — pelny dashboard]**

```python
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(16, 11))
fig.patch.set_facecolor('#f8f9fa')
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)

# === PANEL 1: Glowny — przychody per dzien ===
ax1 = fig.add_subplot(gs[0, :2])
tips_day = tips.groupby('day', observed=True).agg(
    total=('total_bill', 'sum'),
    count=('total_bill', 'count')
).reset_index()
bars = ax1.bar(
    tips_day['day'].astype(str), tips_day['total'],
    color=sns.color_palette('muted')[:4],
    edgecolor='white', linewidth=1.2
)
for bar, val in zip(bars, tips_day['total']):
    ax1.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 20,
             f'${val:.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax1.set_title('Laczne przychody wg dnia tygodnia', fontsize=12, fontweight='bold')
ax1.set_ylabel('Suma rachunkow (USD)')

# === PANEL 2: Kolowy — proporcja dni ===
ax2 = fig.add_subplot(gs[0, 2])
day_counts = tips['day'].value_counts()
ax2.pie(day_counts.values, labels=day_counts.index,
        autopct='%1.0f%%', colors=sns.color_palette('muted')[:len(day_counts)])
ax2.set_title('Udzial wizyt wg dnia', fontsize=11, fontweight='bold')

# === PANEL 3: Boxplot napiwkow ===
ax3 = fig.add_subplot(gs[1, 0])
sns.boxplot(data=tips, x='day', y='tip', palette='pastel', ax=ax3)
ax3.set_title('Rozklad napiwkow wg dnia', fontsize=11, fontweight='bold')
ax3.set_xlabel('Dzien')
ax3.set_ylabel('Napiwek (USD)')

# === PANEL 4: Heatmapa korelacji ===
ax4 = fig.add_subplot(gs[1, 1])
corr = tips.select_dtypes('number').corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, ax=ax4, cbar=False, square=True)
ax4.set_title('Korelacja zmiennych', fontsize=11, fontweight='bold')

# === PANEL 5: Scatter rachunek vs napiwek ===
ax5 = fig.add_subplot(gs[1, 2])
sns.scatterplot(data=tips, x='total_bill', y='tip',
                hue='smoker', alpha=0.7, ax=ax5,
                palette={'Yes': '#e74c3c', 'No': '#2ecc71'})
ax5.set_title('Rachunek vs napiwek', fontsize=11, fontweight='bold')
ax5.set_xlabel('Rachunek (USD)')
ax5.set_ylabel('Napiwek (USD)')
ax5.legend(fontsize=8, title_fontsize=8)

# === PANEL 6: Violinplot — dolny, pelna szerokosc ===
ax6 = fig.add_subplot(gs[2, :])
sns.violinplot(data=tips, x='day', y='total_bill', hue='time',
               split=True, palette={'Lunch': '#3498db', 'Dinner': '#e74c3c'},
               ax=ax6, inner='box')
ax6.set_title('Rozklad rachunkow: Lunch vs Dinner', fontsize=12, fontweight='bold')
ax6.set_xlabel('Dzien tygodnia')
ax6.set_ylabel('Rachunek (USD)')

fig.suptitle('Restaurant Analytics Dashboard — Dataset Tips',
             fontsize=15, fontweight='bold', y=1.01)
plt.savefig('dashboard_tips.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Dashboard zapisany: dashboard_tips.png")
```

> "Szesc wykresow, jedna historia. Przychody, proporcje, rozklady, korelacje, porownania. Wlasciciel w 2 minuty wie wszystko co wazne."

**[Live coding — eksport]**

> "Trzy kluczowe parametry `savefig`:"

```python
plt.savefig(
    'wykres.png',
    dpi=150,              # 72 web, 150 ekran, 300 druk
    bbox_inches='tight',  # nie obcinaj elementow
    facecolor='white'     # biale tlo
)
```

> "`dpi` — dots per inch: 150 to minimum dla czegokolwiek poza Jupyter. `bbox_inches='tight'` — prawie zawsze chcecie. `facecolor='white'` — domyslnie moze byc przezroczyste."

> "Formaty: PNG — rastrowy, do internetu. PDF — wektorowy, do druku. SVG — wektorowy, do stron www."

> "`sns.despine()` — usuwa gorna i prawa ramke osi. Minimalistyczny wyglad, popularny w publikacjach."

---

### 1:17-1:20 — AKTYWNOŚĆ — Mini-quiz (3 min)

> **Prowadzący mówi:** "Zanim podsumujemy — szybki quiz. Odpowiedzcie na kartce lub w parach."

1. Czym rozni sie `fig, ax = plt.subplots()` od `plt.plot()`? Ktory styl jest zalecany i dlaczego?
2. Co robi parametr `hue` w Seaborn? Podaj przyklad uzycia z `sns.barplot()`.
3. Jakie trzy parametry `savefig()` powinniscie ZAWSZE ustawiac przy eksporcie wykresu?

> **[Po 2 min]** "Kto chce odpowiedzieć? [Omów odpowiedzi: 1) Obiektowy (fig, ax) daje pelna kontrole nad wieloma wykresami, imperatywny (plt.plot) jest szybszy ale sie gubi przy subplots; 2) hue dzieli dane na grupy kolorem, np. hue='sex' w barplot — oddzielne slupki dla kazdej plci; 3) dpi=150, bbox_inches='tight', facecolor='white']"

---

### 1:20-1:30 — PODSUMOWANIE

> "Co dzisiaj zrobilismy?"

> "Po pierwsze: **Matplotlib — architektura**. Figure to kontener, Axes to uklad wspolrzednych. `fig, ax = plt.subplots()` — punkt startowy 90% wykresow."

> "Po drugie: **5 typow wykresow** — `plot()` dla trendow, `bar()` i `barh()` dla kategorii, `scatter()` dla korelacji, `hist()` dla rozkladow. Cztery typy, cztery pytania analityczne."

> "Po trzecie: **formatowanie** — title, xlabel, ylabel, legend, grid, annotate. Kazdy wykres bez etykiet osi to wykres ktory nie powinien trafic do raportu."

> "Po czwarte: **Seaborn** — nadbudowka nad Matplotlib. Barplot ze slupkami bledow, boxplot z IQR, heatmapa korelacji, pairplot macierzowy. Parametr `hue` — podzial na grupy w jednym parametrze."

> "Po piate: **dashboard** — wiele wykresow, jedna historia. `plt.subplots(rows, cols)` lub GridSpec dla nieregularnych siatek. Eksport: `savefig('plik.png', dpi=150, bbox_inches='tight')`."

> "Teraz przechodzimy do laboratorium — bedziecie sami tworzyc wykresy i budowac wlasny dashboard. Wszystko co pokazalem — uzywacie w cwiczeniach."

---

## Notatki i wskazowki dla prowadzacego

### Typowe bledy studentow
| Blad | Komunikat/Objaw | Odpowiedz |
|------|-----------------|-----------|
| Brak `plt.close()` | Wykresy nakladaja sie | "Po kazdym `savefig` dodaj `plt.close()`" |
| Brak `%matplotlib inline` | Wykres sie nie wyswietla w Jupyter | "Pierwsza komorka: `%matplotlib inline`" |
| `ax.title` zamiast `ax.set_title()` | AttributeError | "Metody na Axes maja prefiks `set_`" |
| Za mala figura | Etykiety uciete | "Zwieksz figsize lub dodaj `plt.tight_layout()`" |
| `plt.show()` w skrypcie | Puste okno lub brak wykresu | "W skryptach: `savefig`. W Jupyter z inline: `show` jest OK" |
| Brak `hue=` w legendzie Seaborn | Chce kolorowac ale nie wie jak | "Dodaj `hue='kolumna'` — Seaborn sam tworzy legende" |
| pairplot z `ax=` | AttributeError | "pairplot tworzy wlasna figure — nie przyjmuje `ax=`" |

### Tempo zaoczne vs dzienne
- Wyklad zaoczny laczy W09 + W10 dzienne — tempo szybsze, mniej zadan w trakcie
- Skupic sie na fundamentach: Figure/Axes, 5 typow, formatowanie, Seaborn barplot/boxplot/heatmap, dashboard, eksport
- GridSpec pokazac, ale nie wymuszac — studenci na labach moga uzyc `subplots(2, 2)`
- violinplot i pairplot — szybki pokaz, na labach jako bonus
