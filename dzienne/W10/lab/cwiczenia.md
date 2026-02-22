# L10 — Ćwiczenia: Matplotlib + Seaborn zaawansowane

**Programowanie w Pythonie II** | Laboratorium 10
**Notebook:** `lab10_seaborn_dashboard.ipynb`
**Dataset:** `sns.load_dataset('tips')` — 244 rachunki z restauracji

---

## Setup — uruchom jako pierwszą komórkę

```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np

# Ustaw motyw globalnie — wszystkie wykresy w tym stylu
sns.set_theme(style='whitegrid', palette='muted')

# Wczytaj dataset
tips = sns.load_dataset('tips')

print(f"Dataset tips: {tips.shape[0]} wierszy, {tips.shape[1]} kolumn")
print("\nKolumny i typy:")
print(tips.dtypes)
print("\nPierwsze 5 wierszy:")
tips.head()
```

---

## Ćwiczenie 1: Wykresy Seaborn — barplot, boxplot, heatmap (20 min)

**Kontekst biznesowy:** Jesteś analitykiem restauracji. Właściciel chce zobaczyć podstawowe statystyki — średnie rachunki, rozkłady napiwków i zależności między zmiennymi.

### 1a. Barplot z podziałem na grupy

Stwórz wykres słupkowy pokazujący **średni rachunek (`total_bill`) per dzień tygodnia (`day`)**, z podziałem kolorystycznym według płci płacącego (`sex`).

```python
fig, ax = plt.subplots(figsize=(9, 5))

# Uzupełnij: sns.barplot(...)
# Parametry: data=tips, x='day', y='total_bill', hue='sex', palette='muted', ax=ax

ax.set_title('Średni rachunek wg dnia tygodnia i płci')
ax.set_xlabel('Dzień tygodnia')
ax.set_ylabel('Średni rachunek (USD)')

plt.tight_layout()
plt.show()
plt.close()
```

**Pytanie:** W który dzień tygodnia mężczyźni płacą średnio najwięcej? Czy w każdy dzień mężczyźni płacą więcej niż kobiety?

### 1b. Boxplot — rozkład napiwków

Stwórz boxplot pokazujący **rozkład napiwków (`tip`) per dzień tygodnia**, z dodatkowym parametrem `hue='time'` (Lunch / Dinner).

```python
fig, ax = plt.subplots(figsize=(9, 5))

# Uzupełnij: sns.boxplot(...)
# Parametry: data=tips, x='day', y='tip', hue='time', palette='pastel', ax=ax

ax.set_title('Rozkład napiwków wg dnia i pory dnia')
ax.set_xlabel('Dzień tygodnia')
ax.set_ylabel('Napiwek (USD)')

plt.tight_layout()
plt.show()
plt.close()
```

**Pytanie:** W którym dniu mediana napiwku jest najwyższa? Czy kolacje generują wyższe napiwki niż lunche?

### 1c. Heatmapa korelacji

Stwórz heatmapę korelacji zmiennych numerycznych datasetu tips.

```python
fig, ax = plt.subplots(figsize=(6, 5))

# Wylicz korelację — tylko kolumny numeryczne
corr = tips.select_dtypes('number').corr()

# Uzupełnij: sns.heatmap(...)
# Parametry: corr, annot=True, fmt='.2f', cmap='coolwarm', center=0,
#            square=True, ax=ax

ax.set_title('Macierz korelacji — dataset tips')

plt.tight_layout()
plt.show()
plt.close()
```

**Pytanie:** Które dwie zmienne mają najsilniejszą korelację? Ile wynosi ta wartość?

### 1d. Violinplot (bonus)

Stwórz violinplot porównujący rozkład `total_bill` dla Lunch vs Dinner, z podziałem na płeć (`split=True`).

```python
fig, ax = plt.subplots(figsize=(8, 5))

# Uzupełnij: sns.violinplot(...)
# Parametry: data=tips, x='time', y='total_bill', hue='sex',
#            split=True, palette='muted', inner='box', ax=ax

ax.set_title('Rozkład rachunków: Lunch vs Kolacja wg płci')
ax.set_xlabel('Pora dnia')
ax.set_ylabel('Rachunek (USD)')

plt.tight_layout()
plt.show()
plt.close()
```

### Sprawdzenie 1 ✅

- [ ] Barplot wyświetla 4 dni z dwoma kolorami (Male/Female)
- [ ] Słupki barplota mają wąsy (przedziały ufności 95%)
- [ ] Boxplot pokazuje medianę, IQR i outliery
- [ ] Heatmapa ma liczby w każdej komórce, skala coolwarm (czerwony = pozytywna, niebieski = negatywna)
- [ ] Korelacja total_bill–tip: sprawdź czy wynosi ~0.67–0.68

---

## Ćwiczenie 2: Subplots i układ wykresów (20 min)

**Kontekst biznesowy:** Tworzysz stronę raportu dla zarządu — 4 wykresy, jeden obok drugiego i jeden pod jednym. Musisz kontrolować układ.

### 2a. Regularna siatka 2x2

Stwórz siatkę 2x2 z czterema różnymi wykresami z datasetu tips. Każdy wykres musi mieć tytuł i etykiety osi.

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)

# Panel [0,0]: barplot — średni rachunek per dzień
sns.barplot(data=tips, x='day', y='total_bill', ax=axes[0, 0], palette='muted')
axes[0, 0].set_title('Średni rachunek wg dnia')
axes[0, 0].set_xlabel('Dzień')
axes[0, 0].set_ylabel('Rachunek (USD)')

# Panel [0,1]: boxplot — rozkład napiwków per dzień
# Uzupełnij: sns.boxplot(...)
axes[0, 1].set_title('Rozkład napiwków wg dnia')
axes[0, 1].set_xlabel('Dzień')
axes[0, 1].set_ylabel('Napiwek (USD)')

# Panel [1,0]: scatterplot — total_bill vs tip, hue='smoker'
# Uzupełnij: sns.scatterplot(...)
axes[1, 0].set_title('Rachunek vs Napiwek (palacze vs niepalacze)')
axes[1, 0].set_xlabel('Rachunek (USD)')
axes[1, 0].set_ylabel('Napiwek (USD)')

# Panel [1,1]: countplot — liczba wizyt per dzień, hue='time'
# Uzupełnij: sns.countplot(...)
axes[1, 1].set_title('Liczba wizyt wg dnia i pory')
axes[1, 1].set_xlabel('Dzień')
axes[1, 1].set_ylabel('Liczba wizyt')

fig.suptitle('Analiza restauracji — siatka 2x2', fontsize=15, fontweight='bold')
plt.show()
plt.close()
```

### 2b. Nieregularna siatka GridSpec

Stwórz layout: górny panel zajmuje pełną szerokość (barplot sumy rachunków), dolny rząd ma dwa równe panele (boxplot i heatmap).

```python
fig = plt.figure(figsize=(14, 9))
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.3)

# Górny panel — pełna szerokość (wiersz 0, wszystkie kolumny)
ax_top = fig.add_subplot(gs[0, :])

tips_sum = tips.groupby('day', observed=True)['total_bill'].sum().reset_index()
ax_top.bar(
    tips_sum['day'].astype(str),
    tips_sum['total_bill'],
    color=sns.color_palette('muted')[:4]
)
ax_top.set_title('Łączne przychody wg dnia tygodnia', fontsize=12, fontweight='bold')
ax_top.set_xlabel('Dzień')
ax_top.set_ylabel('Suma rachunków (USD)')

# Dolny lewy — boxplot (wiersz 1, kolumna 0)
ax_bl = fig.add_subplot(gs[1, 0])
# Uzupełnij: sns.boxplot(data=tips, x='time', y='tip', ax=ax_bl, palette='pastel')
ax_bl.set_title('Napiwki: Lunch vs Kolacja')
ax_bl.set_xlabel('Pora dnia')
ax_bl.set_ylabel('Napiwek (USD)')

# Dolny prawy — heatmapa pivot (wiersz 1, kolumna 1)
ax_br = fig.add_subplot(gs[1, 1])
pivot = tips.pivot_table(
    values='tip',
    index='day',
    columns='time',
    aggfunc='mean',
    observed=True
)
# Uzupełnij: sns.heatmap(pivot, annot=True, fmt='.2f', cmap='YlOrRd', ax=ax_br)
ax_br.set_title('Średni napiwek (dzień × pora)')

fig.suptitle('Dashboard GridSpec — górny panel + 2 dolne', fontsize=14, fontweight='bold')
plt.show()
plt.close()
```

### 2c. Shared axes

Stwórz 2 wykresy jeden pod drugim ze **wspólną osią X** (`day`). Górny: stripplot napiwków. Dolny: boxplot napiwków. Oś Y niezależna.

```python
fig, axes = plt.subplots(
    2, 1,
    figsize=(8, 8),
    sharex=True,          # wspólna oś X
    constrained_layout=True
)

# Górny: stripplot
sns.stripplot(
    data=tips, x='day', y='tip',
    jitter=True, alpha=0.5, ax=axes[0], palette='muted'
)
axes[0].set_title('Strip plot napiwków (każdy punkt = jeden stolik)')
axes[0].set_xlabel('')    # brak etykiety — dzielona z dolnym
axes[0].set_ylabel('Napiwek (USD)')

# Dolny: boxplot
# Uzupełnij: sns.boxplot(...)
axes[1].set_title('Box plot napiwków')
axes[1].set_xlabel('Dzień tygodnia')
axes[1].set_ylabel('Napiwek (USD)')

fig.suptitle('Strip + Box plot — te same dane, różna prezentacja', fontsize=13)
plt.show()
plt.close()
```

### Sprawdzenie 2 ✅

- [ ] Siatka 2x2 — wszystkie 4 panele mają tytuły i etykiety osi
- [ ] GridSpec: górny panel wizualnie szerszy (pełna szerokość)
- [ ] Shared axes: oś X (day) synchroniczna — zmiana zakresu jednego zmienia drugi
- [ ] `constrained_layout=True` lub `plt.tight_layout()` — brak nakładania się etykiet

---

## Ćwiczenie 3: Pełny dashboard z datasetu tips (30 min) — samodzielna praca

**Kontekst biznesowy:** Właściciel restauracji pyta: *"Jak idzie biznes? Kiedy zarabiamy najwięcej? Kto zostawia największe napiwki? Czy wielkość stolika ma znaczenie?"* Twoim zadaniem jest zbudowanie kompletnego dashboardu analitycznego.

### Wymagania

Zbuduj figurę z **minimum 4 panelami** (polecane 6), używając GridSpec lub `subplots()`. Dashboard musi zawierać:

**Obowiązkowe (minimum):**
- Panel z barplotem lub wykresem słupkowym przychodów / napiwków per dzień
- Panel z boxplotem lub violinplotem rozkładu
- Panel z heatmapą (korelacja lub pivot)
- Panel ze scatterplotem zależności liczbowych

**Polecane (dla lepszej oceny):**
- Etykiety z wartościami na słupkach (patrz przykład z wykładu)
- Tytuł główny figury (`fig.suptitle()`)
- Spójne kolorowanie — np. ten sam kolor dla tego samego dnia we wszystkich panelach
- Wniosek biznesowy pod każdym panelem (w tytule lub adnotacji)

### Szablon startowy

```python
# Dashboard Tips — Ćwiczenie 3
fig = plt.figure(figsize=(16, 11))
fig.patch.set_facecolor('#f8f9fa')

gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)

# === PANEL 1: Twój wybór ===
ax1 = fig.add_subplot(gs[0, :2])   # górny, 2/3 szerokości
# ...

# === PANEL 2: Twój wybór ===
ax2 = fig.add_subplot(gs[0, 2])    # górny prawy, 1/3 szerokości
# ...

# === PANEL 3: Twój wybór ===
ax3 = fig.add_subplot(gs[1, 0])
# ...

# === PANEL 4: Twój wybór ===
ax4 = fig.add_subplot(gs[1, 1])
# ...

# === PANEL 5: Twój wybór ===
ax5 = fig.add_subplot(gs[1, 2])
# ...

# === PANEL 6: Dolny — pełna szerokość ===
ax6 = fig.add_subplot(gs[2, :])
# ...

fig.suptitle('Restaurant Analytics Dashboard — Twoje imię', fontsize=15, fontweight='bold', y=1.01)
plt.show()
plt.close()
```

### Wskazówki

- Paletę ustawiamy raz: `kolory = sns.color_palette('muted')[:4]` — używamy `kolory[0]`, `kolory[1]` itd.
- Pivot table: `tips.pivot_table(values='tip', index='day', columns='time', aggfunc='mean', observed=True)`
- Suma per dzień: `tips.groupby('day', observed=True)['total_bill'].sum().reset_index()`
- Etykiety na słupkach: patrz komórka 10 w notebooku demo wykładu

### Rozszerzenie (dla szybkich)

Odpowiedz na poniższe pytania danymi z dashboardu:
1. Który dzień tygodnia jest najbardziej dochodowy (suma rachunków)?
2. Czy palacze zostawiają wyższe napiwki procentowo od rachunku?
3. Jak liczba osób przy stoliku wpływa na rachunek?

```python
# Pytanie 1: suma per dzień
print(tips.groupby('day', observed=True)['total_bill'].sum().sort_values(ascending=False))

# Pytanie 2: procent napiwku
tips['tip_pct'] = tips['tip'] / tips['total_bill'] * 100
print(tips.groupby('smoker', observed=True)['tip_pct'].mean())

# Pytanie 3: korelacja size vs total_bill
print(f"Korelacja liczba osób–rachunek: {tips['size'].corr(tips['total_bill']):.3f}")
```

### Sprawdzenie 3 ✅

- [ ] Figura zawiera minimum 4 panele
- [ ] Każdy panel ma tytuł
- [ ] Każdy panel ma etykiety osi (x i y)
- [ ] Figura ma tytuł główny (`fig.suptitle`)
- [ ] Kod wykonuje się bez błędów (żadnego `Error` / `Exception`)
- [ ] `plt.show()` na końcu, `plt.close()` po show

---

## Ćwiczenie 4: Szlif, eksport i commit (15 min)

### 4a. Eksport dashboardu do PNG

Wróć do kodu dashboardu z Ćwiczenia 3 i dodaj `plt.savefig()` przed `plt.show()`.

```python
# W kodzie dashboardu z Ćwiczenia 3, PRZED plt.show() dodaj:

plt.savefig(
    'dashboard_tips.png',
    dpi=150,              # jakość: 150 = dobry ekran, 300 = druk
    bbox_inches='tight',  # nie obcinaj tytułu / etykiet
    facecolor='white',    # białe tło (ważne!)
    format='png'
)
print("Dashboard zapisany jako dashboard_tips.png")

plt.show()
plt.close()
```

### 4b. Jeden wykres z adnotacją

Stwórz barplot sumy rachunków per dzień i dodaj adnotację strzałką na najwyższym słupku.

```python
fig, ax = plt.subplots(figsize=(8, 5))

tips_sum = tips.groupby('day', observed=True)['total_bill'].sum().reset_index()
sns.barplot(data=tips_sum, x='day', y='total_bill', palette='muted', ax=ax)

# Znajdź maksimum
max_idx = tips_sum['total_bill'].idxmax()
max_day = tips_sum.loc[max_idx, 'day']
max_val = tips_sum.loc[max_idx, 'total_bill']

# Dodaj adnotację
ax.annotate(
    f'Szczyt: ${max_val:.0f}',
    xy=(max_idx, max_val),
    xytext=(max_idx + 0.5, max_val + 150),
    arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
    fontsize=10, color='red', fontweight='bold'
)

ax.set_title('Łączne przychody wg dnia tygodnia — z adnotacją szczytu')
ax.set_xlabel('Dzień tygodnia')
ax.set_ylabel('Suma rachunków (USD)')
sns.despine()

plt.tight_layout()
plt.savefig('szczyt_przychodow.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
plt.close()
```

### 4c. Commit do repozytorium Git

```bash
# W terminalu (poza notebookiem):
cd ~/python2_projekt

# Sprawdź status
git status

# Dodaj pliki
git add lab10_seaborn_dashboard.ipynb
git add dashboard_tips.png
git add szczyt_przychodow.png

# Commit
git commit -m "L10: Dashboard Seaborn z datasetu tips — barplot, boxplot, heatmap, scatter"

# Wypchnij (jeśli masz remote)
git push
```

### 4d. Pytania refleksyjne (zapisz odpowiedzi w komórce Markdown w notebooku)

1. Kiedy używasz `barplot`, a kiedy `boxplot`? Podaj przykład biznesowy dla każdego.
2. Dlaczego `pairplot` nie przyjmuje parametru `ax=`? Co to oznacza przy budowaniu dashboardu?
3. Jaka jest różnica między `dpi=72` a `dpi=300` w `savefig()`? Kiedy każde stosować?

### Sprawdzenie 4 ✅

- [ ] Plik `dashboard_tips.png` istnieje w katalogu projektu
- [ ] Plik `szczyt_przychodow.png` istnieje z adnotacją strzałką
- [ ] `git log` — widoczny commit z plikiem `lab10_seaborn_dashboard.ipynb`
- [ ] Notebook ma komórkę Markdown z odpowiedziami na 3 pytania refleksyjne
- [ ] Wykres z adnotacją ma strzałkę wskazującą na szczyt słupka

---

## Podsumowanie kluczowych komend

```python
# Seaborn — typy wykresów
sns.barplot(data=df, x='kat', y='num', hue='grupa', ax=ax)      # słupki + CI
sns.boxplot(data=df, x='kat', y='num', hue='grupa', ax=ax)      # skrzynka z wąsami
sns.violinplot(data=df, x='kat', y='num', split=True, ax=ax)    # rozkład jako KDE
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax) # mapa cieplna
sns.scatterplot(data=df, x='num1', y='num2', hue='kat', ax=ax)  # rozrzut
sns.countplot(data=df, x='kat', hue='kat2', ax=ax)              # zliczenie
g = sns.pairplot(df[cols], hue='kat')                            # macierz wszystkich

# Subplots — regularna siatka
fig, axes = plt.subplots(2, 3, figsize=(14, 8), constrained_layout=True)
axes[0, 0]  # dostęp do panelu [wiersz, kolumna]

# GridSpec — nieregularna siatka
gs = gridspec.GridSpec(3, 3, figure=fig)
ax = fig.add_subplot(gs[0, :])   # pełna szerokość
ax = fig.add_subplot(gs[1, 0])   # konkretna komórka

# Styl i eksport
sns.set_theme(style='whitegrid', palette='muted')  # ustaw raz na początku
fig.suptitle('Tytuł', fontsize=14)
plt.tight_layout()  # lub constrained_layout=True
plt.savefig('plik.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
plt.close()          # zawsze na końcu!
```
