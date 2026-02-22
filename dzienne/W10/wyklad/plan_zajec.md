# W10 Wykład — Plan zajęć dla prowadzącego

## Temat: Matplotlib + Seaborn — wizualizacja zaawansowana

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z seaborn/matplotlib/pandas
- **Przed wykładem:** otwórz `seaborn_dashboard_demo.ipynb`
- **Dataset:** seaborn tips (wbudowany — `sns.load_dataset('tips')`)

### Efekty uczenia się (Bloom poziom 3-4)
Po tym wykładzie osoba studiująca:
1. **Tworzy** wykresy kategoryczne (`barplot`, `boxplot`, `violinplot`) i macierzowe (`heatmap`) z Seaborn, dobierając typ wykresu do charakteru danych (Bloom 3)
2. **Konstruuje** siatkę wykresów używając `plt.subplots()`, `fig.add_subplot()` i `GridSpec` z kontrolą współdzielonych osi (Bloom 3)
3. **Projektuje** wielopanelowy dashboard łączący 4–6 wykresów na jednej figurze (Bloom 4)
4. **Analizuje** dane biznesowe (restauracja, sprzedaż) i wybiera odpowiednie typy wizualizacji do opowiadania historii danymi (Bloom 4)
5. **Eksportuje** gotowe wizualizacje do pliku PNG/PDF z kontrolą jakości (`savefig`, `dpi`, `bbox_inches`) (Bloom 3)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W09 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | Zeszły tydzień: podstawy. Teraz: Seaborn + dashboardy | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Seaborn — barplot, boxplot, violinplot, heatmap, pairplot | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | Zaawansowany Matplotlib — subplots, GridSpec, shared axes | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | Dashboard — 4–6 wykresów na jednej figurze | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Stylizacja, eksport (savefig), wskazówki praktyczne | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Budujemy 4-panelowy dashboard z datasetu tips | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Zapowiedź W11: statystyka i scipy | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W09)

> "Pięć pytań z zeszłego tygodnia — 3 minuty, kartka lub Mentimeter."

**[Użyj quiz_w10.md — pytania 1 i 2 z W09]**

> "Odpowiedzi omówimy razem. Kto miał 5/5? Brawo. Kto miał 4? Dobra robota. Poniżej 4 — przejrzyj notatki z W09, bo dziś budujemy na tamtym fundamencie."

---

### 0:05-0:10 — WPROWADZENIE

> "Zeszły tydzień: podstawy Matplotlib. `plt.plot()`, `plt.bar()`, `plt.scatter()`. Umieliście narysować jeden wykres. Dzisiaj przechodzimy na wyższy poziom — i robimy to w dwóch wymiarach."

> "Wymiar pierwszy: **Seaborn**. To biblioteka zbudowana na wierzchu Matplotlib, która w 3 liniach kodu daje wam wykresy, które wyglądają jak z profesjonalnej publikacji. Barplot ze słupkami błędów, violinplot pokazujący rozkład, heatmapa korelacji. Seaborn jest standardem w data science — każdy raport w Jupyter Notebooku, każda prezentacja wyników — to jest Seaborn."

> "Wymiar drugi: **dashboardy**. Jeden wykres to jeden punkt widzenia. Dashboard — 4, 6, 8 wykresów na jednej figurze — to pełna historia. Wyobraźcie sobie raport dla zarządu restauracji: przychody per dzień tygodnia, rozkład napiwków, korelacja między wielkością stolika a rachunkiem, porównanie lunch vs kolacja. Cztery wykresy, jeden rzut oka, pełna analiza."

> "Cały dzień pracujemy na jednym datasecie — **tips**. To dane z prawdziwej restauracji: 244 rachunki, 7 kolumn. Mamy rachunki, napiwki, dzień tygodnia, porę dnia, płeć, palenie/niepalenie, liczbę osób przy stoliku. Mały, czysty, bogaty w zależności — idealny do nauki wizualizacji."

**[Wyświetl na projektorze]**

```
Dataset tips — 7 kolumn:
total_bill  | float  | łączny rachunek (USD)
tip         | float  | napiwek (USD)
sex         | cat    | płeć płacącego (Male/Female)
smoker      | cat    | sekcja dla palących (Yes/No)
day         | cat    | dzień tygodnia (Thur/Fri/Sat/Sun)
time        | cat    | pora dnia (Lunch/Dinner)
size        | int    | liczba osób przy stoliku
```

> "Otwieramy notebook. Zaczynamy od Seaborn."

---

### 0:10-0:30 — MATERIAŁ 1: Seaborn — piękne wykresy w 3 liniach (20 min)

**[Otwórz notebook — komórka 1: setup]**

```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Wczytaj dataset tips — wbudowany w seaborn
tips = sns.load_dataset('tips')

# Ustaw motyw — whitegrid to klasyczny wybór do prezentacji
sns.set_theme(style='whitegrid', palette='muted')

print(f"Dataset tips: {tips.shape[0]} wierszy, {tips.shape[1]} kolumn")
print(tips.head())
```

> "Trzy linijki konfiguracji: `%matplotlib inline` — wykresy w notebooku, `sns.set_theme(style='whitegrid', palette='muted')` — profesjonalny motyw. Od teraz wszystkie nasze wykresy wyglądają jak z raportu McKinsey, nie jak z lat 90."

> "Dostępne style: `white`, `dark`, `whitegrid`, `darkgrid`, `ticks`. Palety: `muted`, `bright`, `deep`, `pastel`, `colorblind`. Ja używam `whitegrid` i `muted` — czytelne, profesjonalne."

**[Komórka 2 — barplot]**

```python
# barplot — średnia + 95% przedział ufności
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Lewy: średni rachunek per dzień
sns.barplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='sex',
    ax=axes[0],
    palette='muted'
)
axes[0].set_title('Średni rachunek wg dnia i płci', fontsize=12)
axes[0].set_xlabel('Dzień tygodnia')
axes[0].set_ylabel('Rachunek (USD)')

# Prawy: średni napiwek per dzień
sns.barplot(
    data=tips,
    x='day',
    y='tip',
    hue='time',
    ax=axes[1],
    palette='Set2'
)
axes[1].set_title('Średni napiwek wg dnia i pory', fontsize=12)
axes[1].set_xlabel('Dzień tygodnia')
axes[1].set_ylabel('Napiwek (USD)')

plt.tight_layout()
plt.show()
plt.close()
```

> "Zwróćcie uwagę na wąsy na słupkach — to 95% przedział ufności. Seaborn liczy to automatycznie, bez żadnego dodatkowego kodu. W Matplotlib musielibyście to policzyć ręcznie i narysować ręcznie. To jest właśnie siła Seaborn."

> "Parametr `hue` — podział na grupy kolorem. Dodajecie jedną linię i słupki są rozbite na dwie grupy. Przykład biznesowy: klient chce wiedzieć czy mężczyźni i kobiety zostawiają różne napiwki. Jeden parametr — gotowe."

**[Komórka 3 — boxplot]**

```python
# boxplot — rozkład: Q1, Q2 (mediana), Q3, IQR, outliery
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Lewy: rachunki per dzień
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='time',
    ax=axes[0],
    palette='pastel'
)
axes[0].set_title('Rozkład rachunków wg dnia', fontsize=12)
axes[0].set_xlabel('Dzień tygodnia')
axes[0].set_ylabel('Rachunek (USD)')

# Prawy: napiwki per dzień
sns.boxplot(
    data=tips,
    x='day',
    y='tip',
    ax=axes[1],
    palette='Set3'
)
axes[1].set_title('Rozkład napiwków wg dnia', fontsize=12)
axes[1].set_xlabel('Dzień tygodnia')
axes[1].set_ylabel('Napiwek (USD)')

plt.tight_layout()
plt.show()
plt.close()
```

> "Boxplot — skrzynka z wąsami. Skrzynka to IQR — od 25. do 75. percentyla. Linia w środku — mediana. Wąsy — 1.5 x IQR. Kropki poza wąsami — wartości odstające, outliery. To jest więcej informacji niż średnia i odchylenie standardowe razem wzięte."

> "Przykład: patrzcie na sobotę. Mediana rachunku wysoka, wąs górny też długi — duże zróżnicowanie. Niedziela — mediana podobna, ale rozrzut mniejszy. Restauracja: sobotnie stoliki bardziej zróżnicowane w wydatkach niż niedzielne. To informacja dla menedżera."

**[Komórka 4 — violinplot]**

```python
# violinplot — rozkład jako gęstość + boxplot
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Lewy: rachunki lunch vs kolacja
sns.violinplot(
    data=tips,
    x='time',
    y='total_bill',
    hue='sex',
    split=True,
    ax=axes[0],
    palette='muted'
)
axes[0].set_title('Rachunki: Lunch vs Kolacja (wg płci)', fontsize=12)
axes[0].set_xlabel('Pora dnia')
axes[0].set_ylabel('Rachunek (USD)')

# Prawy: napiwki wg dnia
sns.violinplot(
    data=tips,
    x='day',
    y='tip',
    ax=axes[1],
    palette='Set2',
    inner='box'
)
axes[1].set_title('Rozkład napiwków wg dnia', fontsize=12)
axes[1].set_xlabel('Dzień tygodnia')
axes[1].set_ylabel('Napiwek (USD)')

plt.tight_layout()
plt.show()
plt.close()
```

> "Violinplot to boxplot plus KDE — kernel density estimation. Kształt skrzypiec pokazuje gdzie jest zagęszczenie danych. Tam gdzie skrzypce są szerokie — dużo obserwacji. Wąskie — mało. Parametr `split=True` z `hue` — dwie połówki skrzypiec, jedno obok drugiego. Czytelnie, elegancko."

> "Kiedy używać violinplota zamiast boxplota? Gdy rozkład jest wielomodalny — np. dwa skupiska. Boxplot by to ukrył, violinplot pokaże wyraźnie dwa wybrzuszenia."

**[Komórka 5 — heatmap]**

```python
# heatmap — macierz korelacji lub pivotowa
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Lewy: korelacja zmiennych numerycznych
corr = tips.select_dtypes('number').corr()
sns.heatmap(
    corr,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    ax=axes[0],
    square=True
)
axes[0].set_title('Korelacja zmiennych', fontsize=12)

# Prawy: pivot heatmap — średni rachunek per dzień i pora
pivot = tips.pivot_table(
    values='total_bill',
    index='day',
    columns='time',
    aggfunc='mean'
)
sns.heatmap(
    pivot,
    annot=True,
    fmt='.1f',
    cmap='YlOrRd',
    ax=axes[1]
)
axes[1].set_title('Średni rachunek (dzień × pora)', fontsize=12)

plt.tight_layout()
plt.show()
plt.close()
```

> "Heatmapa — macierz kolorów. Najczęstsze zastosowania: korelacja (czy zmienne idą razem?) i pivot (przekrojowy raport). Parametr `annot=True` dodaje liczby wewnątrz komórek. `cmap='coolwarm'` — niebieski negatywna, czerwony pozytywna korelacja. `center=0` — 0 korelacja = biały."

> "Patrzcie na korelację: total_bill i tip — 0.68. Silna pozytywna. total_bill i size — 0.60. Większy stolik = wyższy rachunek. tip i size — 0.49. Silny związek. Natomiast tip i total_bill to oczywiście związek — restauracja z wyższymi rachunkami dostaje wyższe napiwki bezwzględnie, choć procentowo mogą być niższe."

**[Komórka 6 — pairplot]**

```python
# pairplot — macierz wykresów: wszystkie vs wszystkie
# UWAGA: pairplot tworzy własną figurę (nie używa ax=)
g = sns.pairplot(
    tips[['total_bill', 'tip', 'size', 'sex']],
    hue='sex',
    diag_kind='kde',
    plot_kws={'alpha': 0.6}
)
g.fig.suptitle('Pairplot — zmienne numeryczne vs płeć', y=1.02, fontsize=14)
plt.show()
plt.close()
```

> "Pairplot — automatyczna macierz wykresów. Każda zmienna numeryczna vs każda inna. Na przekątnej — rozkład (KDE lub histogram). Off-diagonal — scatter. Parametr `hue` — koloruje punkty wg kategorii. Jedyna linijka kodu dla 9 wykresów naraz."

> "Ważna uwaga techniczna: pairplot zwraca `PairGrid`, nie standardową figurę. Dlatego tytuł ustawiamy przez `g.fig.suptitle()`, nie przez `plt.title()`. I po wywołaniu `plt.show()` koniecznie `plt.close()` — żeby nie psuć kolejnych wykresów."

---

### 0:30-0:45 — MATERIAŁ 2: Zaawansowany Matplotlib — siatka subplotów (15 min)

> "Teraz druga warstwa: jak Matplotlib organizuje wiele wykresów na jednej figurze. Znamy już `plt.subplots(rows, cols)` — prosta siatka. Dzisiaj idziemy dalej: nieregularne siatki z GridSpec, wspólne osie."

**[Komórka 7 — subplots revisited]**

```python
# plt.subplots — standardowa siatka
# sharey=True — wszystkie wykresy mają tę samą oś Y (łatwiejsze porównanie)
fig, axes = plt.subplots(
    2, 3,
    figsize=(14, 8),
    sharey=False,
    constrained_layout=True
)

# Dostęp do konkretnego wykresu: axes[wiersz, kolumna]
axes[0, 0].set_title('axes[0,0]')
axes[0, 1].set_title('axes[0,1]')
axes[0, 2].set_title('axes[0,2]')
axes[1, 0].set_title('axes[1,0]')
axes[1, 1].set_title('axes[1,1]')
axes[1, 2].set_title('axes[1,2]')

# Rysujemy na każdym
sns.barplot(data=tips, x='day', y='total_bill', ax=axes[0, 0])
sns.boxplot(data=tips, x='day', y='tip', ax=axes[0, 1])
sns.violinplot(data=tips, x='time', y='total_bill', ax=axes[0, 2])
corr = tips.select_dtypes('number').corr()
sns.heatmap(corr, annot=True, fmt='.2f', ax=axes[1, 0], cbar=False)
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', ax=axes[1, 1])
sns.countplot(data=tips, x='day', hue='smoker', ax=axes[1, 2])

fig.suptitle('Siatka 2x3 — subplots(2,3)', fontsize=16)
plt.show()
plt.close()
```

> "Siatka 2x3 — 6 wykresów. Dostęp do każdego przez `axes[wiersz, kolumna]`. `constrained_layout=True` — nowsze, lepsze `tight_layout()`. Automatycznie dopasowuje odstępy."

> "Parametr `sharey=True` — wszystkie wykresy w kolumnie mają tę samą oś Y. Użyteczne gdy porównujecie te same miary. `sharex=True` — wspólna oś X — przydatne przy wykresach szeregów czasowych jeden pod drugim."

**[Komórka 8 — GridSpec — nieregularne siatki]**

```python
import matplotlib.gridspec as gridspec

# GridSpec — elastyczna siatka z komórkami różnej wielkości
fig = plt.figure(figsize=(14, 9), constrained_layout=True)
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3)

# Górny panel — rozciągnięty na 2 kolumny (duży, ważny)
ax_top = fig.add_subplot(gs[0, :2])
sns.barplot(
    data=tips, x='day', y='total_bill',
    hue='sex', ax=ax_top, palette='muted'
)
ax_top.set_title('Średni rachunek wg dnia i płci (główny panel)', fontsize=11)

# Górny prawy — mały
ax_tr = fig.add_subplot(gs[0, 2])
tips['day'].value_counts().plot(kind='pie', ax=ax_tr, autopct='%1.0f%%')
ax_tr.set_title('Udział dni', fontsize=11)
ax_tr.set_ylabel('')

# Środkowy rząd — trzy równe
ax_m1 = fig.add_subplot(gs[1, 0])
ax_m2 = fig.add_subplot(gs[1, 1])
ax_m3 = fig.add_subplot(gs[1, 2])
sns.boxplot(data=tips, x='time', y='tip', ax=ax_m1, palette='pastel')
ax_m1.set_title('Napiwki: lunch/kolacja', fontsize=10)
corr = tips.select_dtypes('number').corr()
sns.heatmap(corr, annot=True, fmt='.2f', ax=ax_m2, cbar=False, cmap='coolwarm')
ax_m2.set_title('Korelacja', fontsize=10)
sns.scatterplot(
    data=tips, x='total_bill', y='tip',
    hue='smoker', ax=ax_m3, alpha=0.7
)
ax_m3.set_title('Rachunek vs napiwek', fontsize=10)

# Dolny — pełna szerokość
ax_bot = fig.add_subplot(gs[2, :])
tips_sum = tips.groupby('day', observed=True)['total_bill'].sum().reset_index()
ax_bot.bar(
    tips_sum['day'].astype(str),
    tips_sum['total_bill'],
    color=sns.color_palette('muted')[:4]
)
ax_bot.set_title('Suma rachunków wg dnia tygodnia', fontsize=11)
ax_bot.set_xlabel('Dzień')
ax_bot.set_ylabel('Suma rachunków (USD)')

fig.suptitle('Dashboard RestaurantAnalytics — GridSpec 3x3', fontsize=14)
plt.show()
plt.close()
```

> "GridSpec — to jest właśnie narzędzie do prawdziwych dashboardów. Definiujemy siatkę 3x3, ale każdy subplot może zajmować wiele komórek. `gs[0, :2]` — pierwszy wiersz, pierwsze dwie kolumny. `gs[2, :]` — trzeci wiersz, pełna szerokość. Slice notation jak w NumPy."

> "Kiedy używać GridSpec zamiast `subplots()`? Gdy chcecie nierówne panele — np. jeden duży wykres na górze i trzy małe na dole. To jest właśnie układ profesjonalnych raportów."

**[Komórka 9 — shared axes]**

```python
# sharex i sharey — wspólne osie dla porównania
fig, axes = plt.subplots(
    2, 2,
    figsize=(12, 8),
    sharex='col',    # kolumny dzielą oś X
    sharey='row',    # wiersze dzielą oś Y
    constrained_layout=True
)

# Kolumna 0: napiwki (wspólna X = day, wspólna Y = tip)
sns.stripplot(data=tips, x='day', y='tip', ax=axes[0, 0], jitter=True, alpha=0.5)
axes[0, 0].set_title('Strip plot napiwków')

sns.boxplot(data=tips, x='day', y='tip', ax=axes[1, 0], palette='pastel')
axes[1, 0].set_title('Box plot napiwków')

# Kolumna 1: rachunki (wspólna X = day, wspólna Y = total_bill)
sns.stripplot(data=tips, x='day', y='total_bill', ax=axes[0, 1], jitter=True, alpha=0.5)
axes[0, 1].set_title('Strip plot rachunków')

sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[1, 1], palette='muted')
axes[1, 1].set_title('Box plot rachunków')

fig.suptitle('Shared axes — porównanie strip vs box plot', fontsize=14)
plt.show()
plt.close()
```

> "`sharex='col'` — wszystkie wykresy w tej samej kolumnie mają tę samą skalę osi X. Możecie bezpośrednio porównać strip plot z boxplotem — patrzą na te same dane, ta sama skala. To jest esencja dobrego dashboardu — ułatwione porównanie."

> "Opcje: `sharex=True` — wszystkie wykresy, `sharex='col'` — per kolumna, `sharex='row'` — per wiersz, `sharex=False` (domyślnie) — każdy sam."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: Dashboard — cała analiza na jednej figurze (20 min)

> "Po przerwie budujemy dashboard. To jest praktyczny cel wszystkiego, czego się dziś uczyliście. Dashboard = wiele wykresów na jednej figurze, opowiadające spójną historię."

> "Nasz scenariusz: jesteście analitykami restauracji. Właściciel pyta: 'Jak idzie biznes? Kiedy zarabiamy najwięcej? Kto zostawia największe napiwki?' Macie 2 minuty na prezentację. Odpowiedź: dashboard."

**[Komórka 10 — pełny dashboard restauracji]**

```python
# Kompletny dashboard restauracji — 6 paneli
fig = plt.figure(figsize=(16, 11))
fig.patch.set_facecolor('#f8f9fa')  # jasnoszare tło figury

# Definiujemy siatkę
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)

# === PANEL 1: Główny — przychody per dzień ===
ax1 = fig.add_subplot(gs[0, :2])
tips_day = tips.groupby('day', observed=True).agg(
    total=('total_bill', 'sum'),
    avg=('total_bill', 'mean'),
    count=('total_bill', 'count')
).reset_index()
bars = ax1.bar(
    tips_day['day'].astype(str),
    tips_day['total'],
    color=sns.color_palette('muted')[:4],
    edgecolor='white', linewidth=1.2
)
# Dodaj etykiety na słupkach
for bar, val in zip(bars, tips_day['total']):
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 20,
        f'${val:.0f}',
        ha='center', va='bottom', fontsize=9, fontweight='bold'
    )
ax1.set_title('Łączne przychody wg dnia tygodnia', fontsize=12, fontweight='bold')
ax1.set_xlabel('Dzień')
ax1.set_ylabel('Suma rachunków (USD)')
ax1.set_facecolor('#ffffff')

# === PANEL 2: Kołowy — proporcja dni ===
ax2 = fig.add_subplot(gs[0, 2])
day_counts = tips['day'].value_counts()
ax2.pie(
    day_counts.values,
    labels=day_counts.index,
    autopct='%1.0f%%',
    colors=sns.color_palette('muted')[:len(day_counts)],
    startangle=90
)
ax2.set_title('Udział wizyt wg dnia', fontsize=11, fontweight='bold')

# === PANEL 3: Boxplot napiwków ===
ax3 = fig.add_subplot(gs[1, 0])
sns.boxplot(
    data=tips, x='day', y='tip',
    palette='pastel', ax=ax3, linewidth=1.2
)
ax3.set_title('Rozkład napiwków wg dnia', fontsize=11, fontweight='bold')
ax3.set_xlabel('Dzień')
ax3.set_ylabel('Napiwek (USD)')
ax3.set_facecolor('#ffffff')

# === PANEL 4: Heatmapa korelacji ===
ax4 = fig.add_subplot(gs[1, 1])
corr = tips.select_dtypes('number').corr()
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True  # ukryj górny trójkąt
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    ax=ax4,
    cbar=False,
    square=True
)
ax4.set_title('Korelacja zmiennych', fontsize=11, fontweight='bold')

# === PANEL 5: Scatter rachunek vs napiwek ===
ax5 = fig.add_subplot(gs[1, 2])
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='smoker',
    style='time',
    alpha=0.7,
    ax=ax5,
    palette={'Yes': '#e74c3c', 'No': '#2ecc71'}
)
ax5.set_title('Rachunek vs napiwek', fontsize=11, fontweight='bold')
ax5.set_xlabel('Rachunek (USD)')
ax5.set_ylabel('Napiwek (USD)')
ax5.set_facecolor('#ffffff')
ax5.legend(fontsize=8, title_fontsize=8)

# === PANEL 6: Violinplot — rozkład rachunków ===
ax6 = fig.add_subplot(gs[2, :])
sns.violinplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='time',
    split=True,
    palette={'Lunch': '#3498db', 'Dinner': '#e74c3c'},
    ax=ax6,
    inner='box'
)
ax6.set_title(
    'Rozkład rachunków wg dnia i pory dnia (Lunch vs Dinner)',
    fontsize=12, fontweight='bold'
)
ax6.set_xlabel('Dzień tygodnia')
ax6.set_ylabel('Rachunek (USD)')
ax6.set_facecolor('#ffffff')

# Tytuł główny
fig.suptitle(
    'Restaurant Analytics Dashboard — Dataset Tips (244 rachunki)',
    fontsize=15, fontweight='bold', y=1.01
)

plt.show()
plt.close()
```

> "To jest dashboard. Sześć wykresów, jedna historia. Zaczynamy od góry: łączne przychody — sobota zarabia najwięcej. Proporcja dni — sobota i niedziela to 60% wizyt. Boxplot napiwków — w niedzielę mediana napiwku wyższa, ale outlierów więcej w sobotę. Korelacja — rachunek i napiwek idą razem (0.68). Scatter — palacze i niepalacze mają podobny pattern napiwków. Violin — kolacyjni goście mają wyższe i bardziej rozrzucone rachunki."

> "Właściciel restauracji w 2 minuty wie wszystko co ważne. To jest wartość dashboardu."

**[Komórka 11 — tipsy i triki]**

```python
# Profesjonalne detale, które robią różnicę

# 1. Dodawanie tekstu do wykresu — annotations
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=tips, x='day', y='total_bill', ax=ax, palette='muted')
# Adnotacja
ax.annotate(
    'Szczyt sprzedaży',
    xy=(2, 20.4),        # punkt strzałki (Sat)
    xytext=(3.2, 23),    # tekst
    arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
    fontsize=10, color='red'
)
ax.set_title('Adnotacja na wykresie')
plt.tight_layout()
plt.show()
plt.close()

# 2. Legenda poza wykresem
fig, ax = plt.subplots(figsize=(8, 4))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', ax=ax)
ax.legend(
    title='Dzień',
    bbox_to_anchor=(1.05, 1),  # przesuń legendę poza wykres
    loc='upper left',
    borderaxespad=0.
)
ax.set_title('Legenda poza wykresem')
plt.tight_layout()
plt.show()
plt.close()
```

> "Dwa triki które warto zapamiętać. Po pierwsze: `ax.annotate()` — strzałka z tekstem pokazująca ważny punkt. Używacie w raportach żeby zwrócić uwagę na anomalię lub szczyt."

> "Po drugie: legenda poza wykresem — `bbox_to_anchor=(1.05, 1)`. Gdy macie dużo kategorii, legenda zasłania dane. Przesunięcie poza wykres rozwiązuje problem. `plt.tight_layout()` po tym — dopasowuje marginesy."

---

### 1:15-1:25 — MATERIAŁ 4: Stylizacja i eksport (10 min)

**[Komórka 12 — stylizacja zaawansowana]**

```python
# Dostępne style Seaborn i Matplotlib
print("Style Seaborn:", ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks'])
print("Style Matplotlib:", ['bmh', 'ggplot', 'seaborn-v0_8', 'classic', 'fivethirtyeight'])

# Porównanie stylów
styles = ['whitegrid', 'darkgrid', 'white', 'ticks']
fig, axes = plt.subplots(1, 4, figsize=(16, 3), constrained_layout=True)

for ax, style in zip(axes, styles):
    with sns.axes_style(style):
        sns.barplot(data=tips, x='day', y='total_bill', ax=ax, palette='muted')
        ax.set_title(f"style='{style}'", fontsize=10)
        ax.set_xlabel('')

fig.suptitle('Porównanie stylów Seaborn', fontsize=12)
plt.show()
plt.close()
```

> "Cztery style Seaborn. Ja polecam `whitegrid` do prezentacji (czytelna siatka), `white` do publikacji (minimalistyczny), `ticks` do raportów technicznych. Możecie tymczasowo zmienić styl dla jednego wykresu — `with sns.axes_style(style):` — context manager. Po bloku wraca do ustawień globalnych."

**[Komórka 13 — palety kolorów]**

```python
# Palety — wybór profesjonalny
fig, axes = plt.subplots(2, 3, figsize=(14, 6), constrained_layout=True)
palettes = ['muted', 'bright', 'pastel', 'deep', 'Set2', 'colorblind']

for ax, palette in zip(axes.flat, palettes):
    sns.barplot(data=tips, x='day', y='total_bill', ax=ax, palette=palette)
    ax.set_title(f"palette='{palette}'", fontsize=10)
    ax.set_xlabel('')
    ax.set_ylabel('')

fig.suptitle('Palety kolorów Seaborn', fontsize=13)
plt.show()
plt.close()
```

> "Palety. `colorblind` — dostępna dla osób z zaburzeniami widzenia kolorów. Zawsze używajcie jej w oficjalnych materiałach i artykułach. `pastel` — jasne, do tła. `deep` / `muted` — standardowe, profesjonalne. `bright` — tylko gdy dane muszą krzyczeć."

**[Komórka 14 — savefig, eksport]**

```python
# savefig — eksport do pliku
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=tips, x='day', y='total_bill',
    hue='sex', palette='muted', ax=ax
)
ax.set_title('Średni rachunek wg dnia i płci', fontsize=13)
ax.set_xlabel('Dzień tygodnia')
ax.set_ylabel('Rachunek (USD)')
sns.despine()  # usuń górną i prawą krawędź osi

# Eksport do PNG
plt.savefig(
    '/tmp/restauracja_analiza.png',
    dpi=150,            # jakość: 72 (web), 150 (standard), 300 (druk)
    bbox_inches='tight', # nie obcinaj elementów
    facecolor='white',   # białe tło (nie przezroczyste)
    format='png'
)
print("PNG zapisany")

# Eksport do PDF (wektorowy — skaluje się bez utraty jakości)
plt.savefig(
    '/tmp/restauracja_analiza.pdf',
    dpi=300,
    bbox_inches='tight',
    format='pdf'
)
print("PDF zapisany")

plt.show()
plt.close()
```

> "Trzy kluczowe parametry `savefig`: `dpi` — dots per inch. 72 do web, 150 do ekranu, 300 do druku. `bbox_inches='tight'` — nie obcinaj tytułu, legendy, etykiet. Prawie zawsze chcecie `'tight'`. `facecolor='white'` — białe tło. Domyślnie może być przezroczyste — nieładne na szarym tle prezentacji."

> "Format: PNG — rastrowy (nie skaluje się), dobry do internetu. PDF — wektorowy (skaluje się nieskończenie), dobry do druku i LaTeXa. SVG — wektorowy, dobry do HTML/stron www."

> "`sns.despine()` — usuwa górną i prawą ramkę osi. Minimalistyczny wygląd. Popularne w akademickich publikacjach."

**[Komórka 15 — wskazówki praktyczne]**

```python
# Checklist profesjonalnego wykresu

"""
CHECKLIST — zanim wyeksportujesz wykres:

1. TYTUŁ — czy mówi co wykres pokazuje? (nie 'Wykres 1', ale 'Średni rachunek wg dnia')
2. ETYKIETY OSI — zawsze! X i Y z jednostkami jeśli mają.
3. LEGENDA — czy jest czytelna? Poza wykresem jeśli zasłania dane.
4. SKALA — czy oś Y zaczyna od 0? (dla barplotów tak, dla boxplotów niekoniecznie)
5. ADNOTACJE — wyróżnij najważniejszy punkt.
6. ROZMIAR — fig. figsize dobrane do miejsca użycia (artykuł vs prezentacja vs dashboard).
7. DPI — 150 minimum dla wszystkiego co wychodzi poza notebook.
8. DOSTĘPNOŚĆ — palette='colorblind' dla publicznych materiałów.
"""

# Szybki workflow dla notebooka
def zbuduj_wykres(data, x, y, title, xlabel, ylabel, filepath=None):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=data, x=x, y=y, ax=ax, palette='muted')
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    sns.despine()
    plt.tight_layout()
    if filepath:
        plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"Zapisano: {filepath}")
    plt.show()
    plt.close()

# Przykład użycia
zbuduj_wykres(
    tips, 'day', 'total_bill',
    'Średni rachunek wg dnia tygodnia',
    'Dzień', 'Rachunek (USD)',
    '/tmp/quick_chart.png'
)
```

> "Enkapsulacja wykresu w funkcję — praktyczny wzorzec. Parametryzujecie dane, etykiety, opcjonalny zapis do pliku. Używacie tej samej funkcji 10 razy z różnymi kolumnami. Spójny styl w całym projekcie. To jest DRY — Don't Repeat Yourself."

---

### 1:25-1:35 — AKTYWNOŚĆ: Budujemy 4-panelowy dashboard (10 min)

> "Wasza kolej. 10 minut. Cel: zbudować 4-panelowy dashboard z datasetu tips. Macie wszystkie narzędzia — subplots, seaborn, GridSpec. Podane są specyfikacje każdego panelu."

**[Wyświetl na projektorze]**

```python
# ZADANIE — Zbuduj dashboard z 4 paneli
# Użyj plt.subplots(2, 2, figsize=(12, 8))
# lub GridSpec — do wyboru

tips = sns.load_dataset('tips')
fig, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)

# PANEL 1 (axes[0,0]):
# barplot — średni napiwek per dzień, z podziałem hue='smoker'
# Tytuł: 'Napiwki: palacze vs niepalacze'

# PANEL 2 (axes[0,1]):
# boxplot — rozkład total_bill per size (liczba osób)
# Tips: x='size', y='total_bill'
# Tytuł: 'Rachunek wg liczby osób'

# PANEL 3 (axes[1,0]):
# heatmap — pivot_table: wiersze=day, kolumny=time, wartości=mean(tip)
# Tytuł: 'Średni napiwek (dzień × pora)'

# PANEL 4 (axes[1,1]):
# scatterplot — total_bill vs tip, hue='day', size='size'
# Tytuł: 'Rachunek vs napiwek (wg dnia i liczby osób)'

fig.suptitle('Dashboard Tips — wersja studencka', fontsize=14)
plt.show()
plt.close()
```

**Oczekiwany wynik:** 4 wykresy, spójny styl, tytuł główny, czytelne podpisy osi.

> "Kto skończy wcześniej — dodajcie eksport do PNG przez `plt.savefig()`."

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy dzisiejszy wykład."

> "**Seaborn** — biblioteka nad Matplotlib. Jej siła: typy wykresów których nie ma w Matplotlib (violinplot, pairplot), automatyczne statystyki (przedziały ufności w barplot), piękny domyślny styl. API: `sns.barplot()`, `sns.boxplot()`, `sns.violinplot()`, `sns.heatmap()`, `sns.pairplot()`. Wszystkie przyjmują `data=`, `x=`, `y=`, `hue=`, `ax=`."

> "**Subplots i GridSpec** — dwa sposoby na wiele wykresów. `plt.subplots(rows, cols)` — regularna siatka. `GridSpec` — nieregularna, gdy chcecie różne rozmiary. Dostęp: `axes[i, j]` lub `fig.add_subplot(gs[i, j])`. `constrained_layout=True` — automatyczne marginesy."

> "**Dashboard** — spójna historia z wielu wykresów. Zaczynajcie od pytania biznesowego, dobierajcie typy wykresów do danych i pytania. Tytuł, etykiety, legenda — obowiązkowe. Eksport z `dpi=150`, `bbox_inches='tight'`."

> "**Praktyczny wzorzec**: `sns.set_theme()` raz na początku, `plt.tight_layout()` lub `constrained_layout=True` przed każdym `plt.show()`, `plt.close()` po każdej figurze. Te trzy nawyki eliminują 90% problemów z wyglądem i pamięcią."

> "Następny tydzień: **W11 — Statystyka z SciPy**. Histogramy rozkładów, testy hipotez (t-test, chi-kwadrat), przedziały ufności. Będziecie potrzebować wizualizacji z dzisiaj — statystyki i wykresy są nierozłączne."

**Zadanie domowe (nieoceniane):**
> "Znajdźcie publiczny dataset CSV (Kaggle, data.gov, dane.gov.pl). Wczytajcie go Pandą. Zbudujcie dashboard z minimum 4 wykresami w Seaborn. Opisz w 3 zdaniach co wykresy mówią o danych. Notebook na GitHub."
