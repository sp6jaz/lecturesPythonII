# S06 Lab — Cwiczenia: Statystyka opisowa w Pythonie (zaoczne)

**Programowanie w Pythonie II** | Laboratorium S06
**Czas:** 90 min
**Notebook:** `s06_statystyka.ipynb`
**Dataset:** generowany w notebooku — dane sprzedazowe 300 transakcji

---

## Setup — uruchom jako pierwsza komorkę

```python
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Seed zapewnia identyczne dane u kazdego studenta
np.random.seed(2026)
n = 300

# Dataset sprzedazowy — transakcje e-commerce
kategorie = np.random.choice(
    ['Elektronika', 'Odziez', 'Dom i ogrod', 'Sport', 'Ksiazki'],
    n, p=[0.25, 0.30, 0.20, 0.15, 0.10]
)

# Kwota transakcji zalezy od kategorii
baza_kwot = {
    'Elektronika': 450, 'Odziez': 180, 'Dom i ogrod': 250,
    'Sport': 300, 'Ksiazki': 60
}
kwota = np.array([
    baza_kwot[k] + np.random.exponential(scale=baza_kwot[k] * 0.5)
    for k in kategorie
]).round(2)

# Wiek klienta
wiek_klienta = np.random.normal(loc=35, scale=10, size=n).clip(18, 70).round().astype(int)

# Ocena satysfakcji (1-5)
satysfakcja = np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.10, 0.30, 0.40, 0.15])

# Liczba produktow w koszyku
liczba_produktow = np.random.poisson(lam=3, size=n).clip(1, 15)

# Czas dostawy (dni)
czas_dostawy = np.random.gamma(shape=2, scale=2, size=n).clip(1, 20).round(1)

# Wstawiamy 8 outlierow (bledne dane / zamowienia hurtowe)
outlier_idx = np.random.choice(n, 8, replace=False)
kwota[outlier_idx[:4]] = np.array([5500, 7200, 8100, 9500])  # hurtowe
kwota[outlier_idx[4:]] = np.array([0.01, 0.50, 0.99, 1.00])  # bledne

df = pd.DataFrame({
    'kategoria': kategorie,
    'kwota': kwota,
    'wiek_klienta': wiek_klienta,
    'satysfakcja': satysfakcja,
    'liczba_produktow': liczba_produktow,
    'czas_dostawy': czas_dostawy
})

print(f"Dataset sprzedazowy: {df.shape[0]} transakcji, {df.shape[1]} kolumn")
print(df.head(10))
print(f"\nTypy kolumn:\n{df.dtypes}")
```

---

## Cwiczenie 1: Statystyki opisowe na datasecie sprzedazowym (20 min)

**Kontekst biznesowy:** Jestes analitykiem w dziale e-commerce. Dyrektor sprzedazy pyta: "Jak wygladaja nasze transakcje? Jaka jest typowa kwota zamowienia? Ktora kategoria sprzedaje najwiecej?" Przygotuj raport statystyczny.

### 1a. df.describe() — pelny przeglad

Uruchom `df.describe()` i zinterpretuj wynik.

```python
# Krok 1: Pelny describe
print("=== df.describe() ===")
print(df.describe().round(2))

# Krok 2: Odpowiedz w komentarzu:
# - Ile transakcji jest w datasecie?
# - Jaka jest srednia kwota transakcji?
# - Czy srednia kwota > mediana (50%)? Co to mowi o rozkladzie?
# - Jaki jest rozstep kwot (max - min)?
```

### 1b. Miary centralne i rozproszenia dla kwoty

Oblicz recznie srednia, mediane, dominante, std, IQR i rozstep.

```python
kwota_col = df['kwota']

# Uzupelnij:
srednia   = ___   # .mean()
mediana   = ___   # .median()
dominanta = ___   # .mode()[0]

odch_std  = ___   # .std()
q1        = ___   # .quantile(0.25)
q3        = ___   # .quantile(0.75)
iqr       = ___   # q3 - q1
rozstep   = ___   # .max() - .min()

print("=== KWOTA TRANSAKCJI ===")
print(f"Srednia:   {srednia:>10,.2f} PLN")
print(f"Mediana:   {mediana:>10,.2f} PLN")
print(f"Dominanta: {dominanta:>10,.2f} PLN")
print(f"Std:       {odch_std:>10,.2f} PLN")
print(f"Q1 (P25):  {q1:>10,.2f} PLN")
print(f"Q3 (P75):  {q3:>10,.2f} PLN")
print(f"IQR:       {iqr:>10,.2f} PLN")
print(f"Rozstep:   {rozstep:>10,.2f} PLN")
```

### 1c. Statystyki per kategoria (groupby + describe)

```python
# Statystyki per kategoria — srednia, mediana, std, count
kat_stats = df.groupby('kategoria', observed=True)['kwota'].agg([
    'count', 'mean', 'median', 'std'
]).round(2).sort_values('median', ascending=False)
kat_stats.columns = ['Liczba', 'Srednia', 'Mediana', 'Std']
print("=== KWOTA PER KATEGORIA ===")
print(kat_stats)
```

### 1d. Histogram z miarami centralnymi

```python
fig, ax = plt.subplots(figsize=(10, 5))

# Uzupelnij: histogram kwot (bins=40, color='steelblue', edgecolor='white', alpha=0.8)
ax.hist(___, bins=___, color=___, edgecolor=___, alpha=___)

# Dodaj linie: srednia (red, --), mediana (green, -)
ax.axvline(srednia, color='red', lw=2, linestyle='--', label=f'Srednia: {srednia:,.0f}')
ax.axvline(mediana, color='green', lw=2, linestyle='-', label=f'Mediana: {mediana:,.0f}')

ax.set_title('Rozklad kwot transakcji')
ax.set_xlabel('Kwota (PLN)')
ax.set_ylabel('Liczba transakcji')
ax.legend()
plt.tight_layout()
plt.show()
plt.close()
```

### Sprawdzenie 1 ✅

- [ ] `df.describe()` — count = 300 dla kazdej kolumny numerycznej
- [ ] Srednia kwoty jest znacznie wieksza od mediany (rozklad prawostronnie skosny przez outliery hurtowe)
- [ ] Mediana kwoty: okolo **240–280 PLN** (typowa transakcja)
- [ ] Rozstep kwot: okolo **9 500 PLN** (od 0.01 do 9 500 — outliery!)
- [ ] Kategoria Elektronika: najwyzsza mediana (okolo 500–700 PLN)
- [ ] Kategoria Ksiazki: najnizsza mediana (okolo 60–90 PLN)
- [ ] Histogram: czerwona linia (srednia) wyraznie na prawo od zielonej (mediany)

---

## Cwiczenie 2: Korelacja — macierz korelacji + heatmapa (20 min)

**Kontekst biznesowy:** Dyrektor marketingu pyta: "Czy wieksi klienci wydaja wiecej? Czy czas dostawy wplywa na satysfakcje? Czy klienci kupujacy wiecej produktow wydaja wiecej pieniedzy?" Twoja analiza korelacji pomoze zrozumiec zaleznosci.

### 2a. Macierz korelacji Pearsona

```python
# Krok 1: Wybierz kolumny numeryczne i oblicz macierz korelacji
zmienne = ['kwota', 'wiek_klienta', 'satysfakcja', 'liczba_produktow', 'czas_dostawy']
corr = df[zmienne].corr()
print("=== MACIERZ KORELACJI PEARSONA ===")
print(corr.round(3))
```

### 2b. Heatmapa korelacji

```python
# Krok 2: Wizualizacja — heatmapa
fig, ax = plt.subplots(figsize=(8, 7))

im = ax.imshow(corr.values, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(im, ax=ax, shrink=0.8)

ax.set_xticks(range(len(zmienne)))
ax.set_yticks(range(len(zmienne)))
ax.set_xticklabels(zmienne, rotation=45, ha='right')
ax.set_yticklabels(zmienne)

# Wpisz wartosci w komorki
for i in range(len(zmienne)):
    for j in range(len(zmienne)):
        val = corr.values[i, j]
        ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                fontsize=10, color='black' if abs(val) < 0.6 else 'white')

ax.set_title('Macierz korelacji — transakcje e-commerce')
plt.tight_layout()
plt.show()
plt.close()
```

### 2c. Scatter plot z linia regresji — najsilniejsza korelacja

```python
# Krok 3: Znajdz najsilniejsza korelacje (poza przekatna)
# Uzupelnij: wybierz pare zmiennych z najwyzszym |r|
# Narysuj scatter plot z linia trendu

# Przyklad: kwota vs liczba_produktow
r_val, p_val = stats.pearsonr(df['kwota'], df['liczba_produktow'])

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df['liczba_produktow'], df['kwota'], alpha=0.4, color='steelblue', s=30)

# Linia trendu
z = np.polyfit(df['liczba_produktow'], df['kwota'], 1)
p_fit = np.poly1d(z)
x_line = np.linspace(df['liczba_produktow'].min(), df['liczba_produktow'].max(), 100)
ax.plot(x_line, p_fit(x_line), 'r--', lw=2, label=f'Trend (r={r_val:.3f})')

ax.set_xlabel('Liczba produktow w koszyku')
ax.set_ylabel('Kwota transakcji (PLN)')
ax.set_title('Liczba produktow vs Kwota')
ax.legend()
plt.tight_layout()
plt.show()
plt.close()

print(f"Pearson r = {r_val:.4f}, p = {p_val:.4f}")
print(f"Interpretacja: {'istotna' if p_val < 0.05 else 'nieistotna'} statystycznie")
```

### 2d. Interpretacja — odpowiedz na pytania biznesowe

```python
# Krok 4: Oblicz korelacje dla pytan biznesowych i zinterpretuj
pary = [
    ('wiek_klienta', 'kwota', 'Wiek vs Kwota'),
    ('czas_dostawy', 'satysfakcja', 'Czas dostawy vs Satysfakcja'),
    ('liczba_produktow', 'kwota', 'Liczba produktow vs Kwota'),
]

print("=== ODPOWIEDZI DLA DYREKTORA MARKETINGU ===")
for x, y, nazwa in pary:
    r, p = stats.pearsonr(df[x], df[y])
    sila = 'silna' if abs(r) > 0.5 else ('umiarkowana' if abs(r) > 0.3 else 'slaba')
    kier = 'dodatnia' if r > 0 else 'ujemna'
    ist = 'TAK' if p < 0.05 else 'NIE'
    print(f"\n{nazwa}:")
    print(f"  r = {r:.4f} ({sila}, {kier}), p = {p:.4f}, istotna: {ist}")

# W komentarzu napisz wnioski biznesowe:
# - Czy starsi klienci wydaja wiecej?
# - Czy dluzszy czas dostawy obniza satysfakcje?
# - Czy wiecej produktow = wyzsza kwota?
```

### Sprawdzenie 2 ✅

- [ ] Macierz korelacji: 5x5, wartosci na przekatnej = 1.000
- [ ] Korelacja czas_dostawy–satysfakcja: **slaba ujemna** (r okolo -0.05 do -0.15) — dluzsza dostawa troche obniza satysfakcje
- [ ] Korelacja liczba_produktow–kwota: **slaba** (r okolo 0.0–0.15) — outliery zaburzaja zwiazek
- [ ] Korelacja wiek–kwota: **bliska zeru** — wiek nie decyduje o kwocie zakupu
- [ ] Heatmapa: wiekszos komórek w kolorach neutralnych (brak silnych korelacji — realistyczne!)
- [ ] Scatter plot: widoczne punkty z linia trendu, r i p wyswietlone

---

## Cwiczenie 3: Wykrywanie outlierow (25 min)

**Kontekst biznesowy:** Przed przygotowaniem raportu kwartalnego musisz oczyscic dane. Zauwazyles podejrzane transakcje: zamowienia za 0.01 PLN i za ponad 5 000 PLN. Czy to bledy? Zamowienia hurtowe? Przetestuj dwie metody wykrywania i podejmij decyzje.

### 3a. Metoda IQR

```python
# Krok 1: Oblicz granice IQR
q1 = df['kwota'].quantile(0.25)
q3 = df['kwota'].quantile(0.75)
iqr = q3 - q1
dolna = q1 - 1.5 * iqr
gorna = q3 + 1.5 * iqr

print(f"Q1 = {q1:,.2f}, Q3 = {q3:,.2f}, IQR = {iqr:,.2f}")
print(f"Granice IQR: [{dolna:,.2f}, {gorna:,.2f}]")

# Krok 2: Wykryj outliery
maska_iqr = (df['kwota'] < dolna) | (df['kwota'] > gorna)
outliery_iqr = df[maska_iqr]
print(f"\nLiczba outlierow (IQR): {maska_iqr.sum()} z {len(df)}")
print("\nOutliery:")
print(outliery_iqr[['kategoria', 'kwota', 'liczba_produktow']].sort_values('kwota').to_string())
```

### 3b. Boxplot — wizualizacja outlierow

```python
# Krok 3: Boxplot — ogolny i per kategoria
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Lewy: ogolny boxplot kwot
axes[0].boxplot(df['kwota'], vert=True)
axes[0].set_title('Boxplot kwot transakcji')
axes[0].set_ylabel('Kwota (PLN)')

# Prawy: boxplot per kategoria
kategorie_unikalne = sorted(df['kategoria'].unique())
dane_per_kat = [df[df['kategoria'] == k]['kwota'].values for k in kategorie_unikalne]
bp = axes[1].boxplot(dane_per_kat, labels=kategorie_unikalne, vert=True)
axes[1].set_title('Boxplot kwot per kategoria')
axes[1].set_ylabel('Kwota (PLN)')
axes[1].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.show()
plt.close()
```

### 3c. Metoda z-score

```python
# Krok 4: Z-score
z_scores = np.abs(stats.zscore(df['kwota']))
maska_z = z_scores > 3.0
print(f"Outlierzy z-score (|z| > 3.0): {maska_z.sum()} z {len(df)}")
print(df[maska_z][['kategoria', 'kwota']].sort_values('kwota').to_string())

# Krok 5: Porownanie metod
print(f"\n=== POROWNANIE METOD ===")
print(f"IQR:     {maska_iqr.sum()} outlierow")
print(f"Z-score: {maska_z.sum()} outlierow")
print(f"Wspolne: {(maska_iqr & maska_z).sum()} outlierow")
```

### 3d. Decyzja biznesowa — co zrobic z outlierami?

```python
# Krok 6: Podziel outliery na kategorie decyzyjne
outliery = df[maska_iqr].copy()

# Kwoty < 1 PLN — prawdopodobnie bledy (testowe transakcje)
bledy = outliery[outliery['kwota'] < 1.0]
print(f"Bledy danych (kwota < 1 PLN): {len(bledy)} transakcji")
print(bledy[['kategoria', 'kwota']].to_string())

# Kwoty > 5000 PLN — prawdopodobnie zamowienia hurtowe
hurtowe = outliery[outliery['kwota'] > 5000]
print(f"\nZamowienia hurtowe (kwota > 5000 PLN): {len(hurtowe)} transakcji")
print(hurtowe[['kategoria', 'kwota', 'liczba_produktow']].to_string())

# Krok 7: Stworz oczyszczony dataset
# Usun bledy, zostaw hurtowe (ale oznacz)
df_clean = df[df['kwota'] >= 1.0].copy()  # usuwamy transakcje testowe
df_clean['typ'] = np.where(df_clean['kwota'] > 5000, 'hurtowa', 'detaliczna')
print(f"\nDataset po oczyszczeniu: {len(df_clean)} transakcji")
print(f"Hurtowe: {(df_clean['typ'] == 'hurtowa').sum()}")
print(f"Detaliczne: {(df_clean['typ'] == 'detaliczna').sum()}")

# Krok 8: Porownanie statystyk
print(f"\n=== WPLYW OCZYSZCZENIA ===")
print(f"{'Miara':<15} {'Przed':>12} {'Po':>12}")
print("-" * 41)
for nazwa, przed, po in [
    ('Srednia', df['kwota'].mean(), df_clean['kwota'].mean()),
    ('Mediana', df['kwota'].median(), df_clean['kwota'].median()),
    ('Std', df['kwota'].std(), df_clean['kwota'].std()),
]:
    print(f"{nazwa:<15} {przed:>12,.2f} {po:>12,.2f}")
```

### Sprawdzenie 3 ✅

- [ ] IQR wykrywa **wiecej** outlierow niz z-score (IQR jest bardziej czuly)
- [ ] Z-score (|z| > 3) wykrywa tylko **najekstremniejsze** wartosci (kilka najwyzszych kwot)
- [ ] Outliery dolne: 4 transakcje z kwota < 1 PLN (0.01, 0.50, 0.99, 1.00)
- [ ] Outliery gorne: 4 transakcje hurtowe (5500, 7200, 8100, 9500 PLN)
- [ ] Boxplot ogolny: wyrazne punkty ponizej i powyzej wasow
- [ ] Boxplot per kategoria: Elektronika ma najwyzsze wasy (drozsza kategoria)
- [ ] Po usunieciu bledow (kwota < 1 PLN): srednia spada, mediana prawie bez zmiany
- [ ] Decyzja: bledy kasujemy, hurtowe oznaczamy — nie kasujemy automatycznie!

---

## Cwiczenie 4: Rozklad normalny — histogram, Shapiro, QQ plot (25 min)

**Kontekst biznesowy:** Zespol data science planuje zastosowac testy parametryczne (t-test) do porownania srednich kwot miedzy kategoriami. Zanim to zrobisz, musisz sprawdzic, czy dane maja rozklad normalny. Jesli nie — trzeba uzyc testow nieparametrycznych.

### 4a. Histogram z krzywa normalna

```python
from scipy.stats import norm

# Krok 1: Histogram kwot (oczyszczonych) + dopasowana krzywa normalna
kwota_clean = df_clean[df_clean['typ'] == 'detaliczna']['kwota']

fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(kwota_clean, bins=35, density=True, color='steelblue',
        edgecolor='white', alpha=0.7, label='Histogram')

# Dopasuj krzywa normalna
mu = kwota_clean.mean()
sigma = kwota_clean.std()
x = np.linspace(kwota_clean.min(), kwota_clean.max(), 200)
ax.plot(x, norm.pdf(x, loc=mu, scale=sigma), 'r-', lw=2,
        label=f'Krzywa normalna (mu={mu:.0f}, sigma={sigma:.0f})')

ax.set_title('Kwoty detaliczne — histogram vs rozklad normalny')
ax.set_xlabel('Kwota (PLN)')
ax.set_ylabel('Gestosc')
ax.legend()
plt.tight_layout()
plt.show()
plt.close()

print(f"Srednia: {mu:.2f} PLN, Std: {sigma:.2f} PLN")
print(f"Skosnos: {kwota_clean.skew():.3f}")
print(f"Kurtoza: {kwota_clean.kurtosis():.3f}")
```

### 4b. Test Shapiro-Wilka

```python
# Krok 2: Test Shapiro-Wilka
# H0: dane pochodza z rozkladu normalnego
# H1: dane NIE pochodza z rozkladu normalnego

stat_w, p_shapiro = stats.shapiro(kwota_clean)
print("=== TEST SHAPIRO-WILKA ===")
print(f"W = {stat_w:.4f}")
print(f"p = {p_shapiro:.6f}")
print(f"Wniosek: {'Brak podstaw do odrzucenia H0 (dane moga byc normalne)' if p_shapiro >= 0.05 else 'Odrzucamy H0 — dane NIE sa normalnie rozlozone'}")
print()

# Krok 3: Shapiro per kategoria
print("=== SHAPIRO PER KATEGORIA ===")
for kat in sorted(df_clean['kategoria'].unique()):
    podzb = df_clean[df_clean['kategoria'] == kat]['kwota']
    w, p = stats.shapiro(podzb)
    wynik = 'normalne' if p >= 0.05 else 'NIE normalne'
    print(f"  {kat:<15}: W={w:.4f}, p={p:.4f} -> {wynik}")
```

### 4c. QQ plot — wizualna ocena normalnosci

```python
# Krok 4: QQ plot (quantile-quantile)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Lewy: QQ plot kwot detalicznych
stats.probplot(kwota_clean, dist='norm', plot=axes[0])
axes[0].set_title('QQ plot — kwoty detaliczne')
axes[0].get_lines()[0].set_color('steelblue')
axes[0].get_lines()[0].set_markersize(4)

# Prawy: QQ plot dla danych naprawde normalnych (porownanie)
np.random.seed(99)
dane_normalne = np.random.normal(loc=mu, scale=sigma, size=len(kwota_clean))
stats.probplot(dane_normalne, dist='norm', plot=axes[1])
axes[1].set_title('QQ plot — dane wygenerowane (normalne)')
axes[1].get_lines()[0].set_color('coral')
axes[1].get_lines()[0].set_markersize(4)

plt.tight_layout()
plt.show()
plt.close()

print("Interpretacja QQ plot:")
print("- Jesli punkty leza na linii prostej — dane sa normalne")
print("- Odchylenia na koncach — grube ogony (outliery)")
print("- Zakrzywienie — skosnos rozkladu")
```

### 4d. Wnioski i decyzja o tescie statystycznym

```python
# Krok 5: Podsumowanie — czy mozemy uzywac testow parametrycznych?
print("=== PODSUMOWANIE — NORMALNOSC DANYCH ===")
print()
print("Metoda 1 — Histogram:")
print(f"  Skosnos = {kwota_clean.skew():.3f} (> 1.0 = silnie skosny)")
print(f"  Kurtoza = {kwota_clean.kurtosis():.3f}")
print()
print("Metoda 2 — Shapiro-Wilk:")
print(f"  p = {p_shapiro:.6f} ({'< 0.05 — NIE normalne' if p_shapiro < 0.05 else '>= 0.05 — brak podstaw do odrzucenia'})")
print()
print("Metoda 3 — QQ plot:")
print("  Wizualnie: czy punkty leza na prostej?")
print()
print("DECYZJA:")
if p_shapiro < 0.05:
    print("  Dane NIE sa normalne -> stosujemy testy nieparametryczne")
    print("  (np. Mann-Whitney zamiast t-testu)")
else:
    print("  Brak podstaw do odrzucenia normalnosci -> mozemy uzyc t-testu")
```

### Sprawdzenie 4 ✅

- [ ] Histogram: krzywa normalna NIE dopasowuje sie dobrze do danych (dane sa prawostronnie skosne)
- [ ] Skosnos kwot detalicznych: **wartość dodatnia > 1.0** (silnie prawoskosny)
- [ ] Shapiro-Wilk p < 0.05 — **odrzucamy normalnosc** (kwoty transakcji nie maja rozkladu normalnego)
- [ ] Shapiro per kategoria: wiekszos kategorii **nie przechodzi** testu normalnosci
- [ ] QQ plot lewy (dane realne): punkty **odchylaja sie od prostej** na prawym koncu (prawy ogon)
- [ ] QQ plot prawy (dane normalne): punkty **leza na prostej** — to jest wzorzec
- [ ] Wniosek: dane sprzedazowe nie sa normalne — nalezy uzywac testow nieparametrycznych
- [ ] Kontekst: dane sprzedazowe z natury maja rozklad prawostronnie skosny (duzo malych transakcji, malo duzych)

---

## Podsumowanie

Po ukonczeniu wszystkich cwiczen osoba studiujaca potrafi:
- Stosowac `df.describe()` i `groupby().agg()` do szybkiej analizy statystycznej datasetu
- Obliczac i interpretowac macierz korelacji oraz prezentowac ja jako heatmape
- Wykrywac wartosci odstajace dwoma metodami (IQR, z-score) i podejmowac decyzje biznesowe
- Weryfikowac normalnosc rozkladu za pomoca histogramu, testu Shapiro-Wilka i QQ plota
- Laczyc analize statystyczna z wizualizacja w spojnym raporcie

**Commit na koniec zajec:**
```bash
git add s06_statystyka.ipynb
git commit -m "S06: statystyka opisowa — describe, korelacja, outliery, normalnosc"
```
