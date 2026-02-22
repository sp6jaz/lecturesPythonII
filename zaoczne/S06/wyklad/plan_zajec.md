# S06 Wykład — Plan zajęć dla prowadzącego (zaoczne)

## Temat: Statystyka opisowa — miary, korelacja, rozkłady, outliery

### Informacje organizacyjne
- **Czas:** 90 min (blok wykładowy)
- **Forma:** wykład konwersatoryjny z live coding
- **Tryb:** zaoczne — po wykładzie od razu lab (180 min razem)
- **Potrzebne:** komputer z projektorem, VS Code, venv z scipy/numpy/pandas/matplotlib/seaborn
- **Dataset:** generowany w notebooku — 200 pracowników HR (wynagrodzenia, staż, dział)
- **Poprzednie zajęcia:** S05 — Matplotlib + Seaborn, studenci znają Pandas i wizualizację

### Efekty uczenia się (Bloom poziom 2-4)
Po tym wykładzie osoba studiująca:
1. **Oblicza** miary tendencji centralnej (mean, median, mode) i rozproszenia (std, var, IQR, quantile) oraz interpretuje je w kontekście biznesowym (Bloom 2)
2. **Interpretuje** wynik `df.describe()` i `scipy.stats.describe()` — szybka diagnoza datasetu (Bloom 2)
3. **Analizuje** korelację Pearsona i Spearmana (`df.corr()`, `scipy.stats.pearsonr`), interpretuje siłę i kierunek związku, odróżnia korelację od przyczynowości (Bloom 3)
4. **Stosuje** skośność (`skew()`) i kurtozę (`kurtosis()`) do oceny kształtu rozkładu danych (Bloom 3)
5. **Wykrywa** wartości odstające metodą IQR i z-score, ocenia ich wpływ na miary statystyczne (Bloom 3)
6. **Stosuje** `scipy.stats.norm` do modelowania rozkładu normalnego i weryfikuje normalność testem Shapiro-Wilka (Bloom 3)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **WPROWADZENIE** | "Umiemy ładować, czyścić, wizualizować. Teraz: co te liczby ZNACZĄ?" | Rozmowa |
| 0:05-0:25 | **MATERIAŁ 1** | Statystyki opisowe: mean, median, std, describe() — z interpretacją biznesową | Live coding |
| 0:25-0:40 | **MATERIAŁ 2** | Korelacja: df.corr(), Pearson, Spearman, scatter + regresja, interpretacja r | Live coding |
| 0:40-0:50 | **PRZERWA** | 10 minut | — |
| 0:50-1:05 | **MATERIAŁ 3** | Skośność, kurtoza, wykrywanie outlierów (IQR, z-score) | Live coding |
| 1:05-1:20 | **MATERIAŁ 4** | Rozkład normalny: histogram + krzywa, scipy.stats.norm, test Shapiro-Wilka | Live coding |
| 1:20-1:30 | **PODSUMOWANIE** | Kluczowe zasady + zapowiedź laboratorium | Rozmowa |

---

## STENOGRAM — co mowic i robic

### 0:00-0:05 — WPROWADZENIE

> "Przez ostatnie spotkania nauczylismy sie ladowac dane z CSV, czyscic je w Pandas, rysowac wykresy w Matplotlib i Seaborn. Mamy dane na wykresie. Ladnie wyglada."

> "Ale co to ZNACZY? Czy wynagrodzenia w firmie sa wysokie? Czy sa fair? Czy pracownicy z dluzszym stazem zarabiaja proporcjonalnie wiecej? Czy sa osoby, ktore zarabiaja tak duzo lub tak malo, ze to anomalia?"

> "To sa pytania ze swiata biznesu — i odpowiada na nie **statystyka opisowa**. Nie machine learning, nie deep learning — zwykle liczby: srednia, mediana, odchylenie standardowe, korelacja. Te liczby mowia menedzerowi wiecej niz sto wykresow."

> "Dzis przejdziemy przez caly zestaw narzedzi statystycznych. Zaczniemy od podstaw — describe i miary centralne — przez korelacje, skosnos, outliery, az do rozkładu normalnego i testu Shapiro-Wilka. Wszystko z Pythonem — pandas, numpy, scipy.stats."

**[Wyswietl na projektorze]**
```
Mapa dnia:
1. Statystyki opisowe (describe)  → co jest typowe?
2. Korelacja                       → co zalezy od czego?
3. Skosnos, kurtoza, outliery      → jak wygladaja dane?
4. Rozklad normalny + Shapiro      → czy dane sa "normalne"?
```

> "Caly dzien pracujemy na danych HR — wynagrodzenia, staz pracy, dzial. Dane wygenerujemy sami w notebooku. Zaczynamy."

---

### 0:05-0:25 — MATERIAL 1: Statystyki opisowe i describe() (20 min)

**[Otworz notebook — komórka 1: setup i generowanie danych]**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

%matplotlib inline

np.random.seed(42)
n = 200

dzialy = np.random.choice(['IT', 'Sprzedaz', 'HR', 'Marketing', 'Finanse'], n,
                           p=[0.30, 0.25, 0.15, 0.20, 0.10])
staz = np.random.gamma(shape=3, scale=2, size=n).clip(0.5, 20).round(1)

baza = {'IT': 9000, 'Sprzedaz': 7000, 'HR': 6500, 'Marketing': 7500, 'Finanse': 8500}
wynagrodzenie = np.array([
    baza[d] + staz[i] * 300 + np.random.normal(0, 1200)
    for i, d in enumerate(dzialy)
]).clip(4000, 25000).round(-2)

# 5 celowych outlierow
wynagrodzenie[np.random.choice(n, 5, replace=False)] = np.random.choice(
    [2000, 2500, 35000, 40000, 38000], 5, replace=False
)

df = pd.DataFrame({
    'dzial': dzialy,
    'staz_lat': staz,
    'wynagrodzenie': wynagrodzenie,
    'wiek': (25 + staz + np.random.normal(0, 3, n)).clip(22, 65).round().astype(int),
    'ocena_roczna': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.10, 0.40, 0.35, 0.10])
})

print(f"Dataset HR: {df.shape[0]} pracownikow, {df.shape[1]} kolumn")
print(df.head())
```

> "Wygenerowalismy 200 pracownikow z realistyczna struktura: wynagrodzenie zalezy od dzialu i stazu, z losowym szumem. Dodalismy 5 outlierow — to sa te osoby z pensja 2000 albo 40 000, ktore zaburzaja statystyki. W praktyce takie dane to bledy w danych albo specjalne kontrakty."

**[Komórka 2 — df.describe()]**

```python
# df.describe() — jeden wiersz kodu, pelny przeglad
print("=== df.describe() ===")
print(df.describe().round(0))
```

> "`df.describe()` — to jest pierwsza rzecz, ktora odpalamy na kazdym nowym datasecie. Jedna linia kodu, a dostajemy: count, mean, std, min, kwartyle (25%, 50%, 75%), max. Dla kazdej kolumny numerycznej."

> "Co nam to mowi? Count = 200 wszedzie — brak brakow danych. Srednia wynagrodzenia okolo 9 900 PLN. Mediana (50%) — 9 450 PLN. Srednia wieksza od mediany? To znaczy, ze rozklad jest prawostronnie skosny — kilka osob z bardzo wysokimi pensjami ciagnie srednia w gore."

**[Komórka 3 — miary centralne i rozproszenia]**

```python
placa = df['wynagrodzenie']

srednia = placa.mean()
mediana = placa.median()
dominanta = placa.mode()[0]

odch_std = placa.std()
q1 = placa.quantile(0.25)
q3 = placa.quantile(0.75)
iqr = q3 - q1
rozstep = placa.max() - placa.min()

print("=== MIARY TENDENCJI CENTRALNEJ ===")
print(f"Srednia:   {srednia:>10,.0f} PLN")
print(f"Mediana:   {mediana:>10,.0f} PLN")
print(f"Dominanta: {dominanta:>10,.0f} PLN")
print()
print("=== MIARY ROZPROSZENIA ===")
print(f"Odchylenie std: {odch_std:>10,.0f} PLN")
print(f"Q1 (P25):       {q1:>10,.0f} PLN")
print(f"Q3 (P75):       {q3:>10,.0f} PLN")
print(f"IQR:            {iqr:>10,.0f} PLN")
print(f"Rozstep:        {rozstep:>10,.0f} PLN")
```

> "Trzy miary centralne, trzy rozne pytania. **Srednia** — suma podzielona przez liczbe, ale wrazliwa na outliery. Jeden prezes z pensja 200 tys. podnosi srednia calej firmy. **Mediana** — wartosc srodkowa. 50% pracownikow zarabia mniej, 50% wiecej. Odporna na outliery — dlatego GUS podaje mediany wynagrodzen, nie srednie. **Dominanta** — najczestsza wartosc."

> "Jezeli mediana < srednia — rozklad jest prawostronnie skosny. To typowe dla danych o wynagrodzeniach."

> "Miary rozproszenia: **Odchylenie standardowe** — przecietne odchylenie od sredniej, w tych samych jednostkach. STD 4000 PLN = typowy pracownik zarabia plus/minus 4000 od sredniej. **IQR** — rozstep miedzykwartylowy, od Q1 do Q3. 50% srodkowych obserwacji. Odporny na outliery. **Rozstep** — max minus min. U nas ogromny, bo mamy outliery z pensja 2000 i 40000."

**[Komórka 4 — wizualizacja: histogram z miarami centralnymi]**

```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(placa, bins=30, color='steelblue', edgecolor='white', alpha=0.8)
ax.axvline(srednia, color='red', lw=2, linestyle='--', label=f'Srednia: {srednia:,.0f}')
ax.axvline(mediana, color='green', lw=2, linestyle='-', label=f'Mediana: {mediana:,.0f}')
ax.set_title('Rozklad wynagrodzen — srednia vs mediana')
ax.set_xlabel('Wynagrodzenie (PLN)')
ax.set_ylabel('Liczba pracownikow')
ax.legend()
plt.tight_layout()
plt.show()
plt.close()
```

> "Patrzcie na histogram. Glowna masa pracownikow jest tutaj — i tu jest mediana, zielona linia. Czerwona — srednia — jest pociagnieta w prawo przez outliery. To jest dowod na to, ze mediana jest bezpieczniejsza miara dla danych skosnych."

**[Komórka 5 — statystyki per dzial]**

```python
# Porownanie dzialow: groupby + describe
dzialy_stats = df.groupby('dzial', observed=True)['wynagrodzenie'].agg([
    'mean', 'median', 'std', 'min', 'max',
    lambda x: x.quantile(0.75) - x.quantile(0.25)
]).round(0)
dzialy_stats.columns = ['Srednia', 'Mediana', 'Std', 'Min', 'Max', 'IQR']
print("=== WYNAGRODZENIA PER DZIAL ===")
print(dzialy_stats.sort_values('Mediana', ascending=False))
```

> "IT ma najwyzsza mediane i najwyzsze STD — duze zroznicowanie, bo jest i junior i senior. HR i Sprzedaz — najnizsze mediany, mniejsze zroznicowanie. To sa realne wzorce z rynku pracy."

**[Komórka 6 — percentyle]**

```python
# Percentyle — narzedzie HR i benchmarking
percentyle = [10, 25, 50, 75, 90, 95, 99]
print("=== PERCENTYLE WYNAGRODZEN ===")
for p in percentyle:
    val = np.percentile(df['wynagrodzenie'], p)
    print(f"P{p:3d}: {val:>10,.0f} PLN")
```

> "Firmy uzywaja percentyli do benchmarkingu wynagrodzen. 'Chcemy placic na poziomie P75 rynku' — czyli w gornych 25%. P95 i P99 — tu ukrywaja sie outliery albo specjalne kontrakty."

---

### 0:25-0:40 — MATERIAL 2: Korelacja (15 min)

**[Komórka 7 — macierz korelacji]**

```python
# Macierz korelacji Pearsona
corr = df[['staz_lat', 'wynagrodzenie', 'wiek', 'ocena_roczna']].corr()
print("Macierz korelacji Pearsona:")
print(corr.round(3))
```

> "Korelacja Pearsona — r — mierzy sile liniowego zwiazku miedzy dwoma zmiennymi. Skala od -1 do +1. r = +1: idealna zależnosc dodatnia. r = 0: brak zwiazku. r = -1: idealna zależnosc ujemna."

> "W praktyce: r > 0.7 — silna, r = 0.4–0.7 — umiarkowana, r < 0.4 — slaba. Ale pamietajcie: **korelacja nie jest przyczynowoscia**. Sprzedaz lodow koreluje z utonięciami — bo lato jest przyczyna obydwu."

**[Komórka 8 — scatter + linia regresji]**

```python
r_staz, p_staz = stats.pearsonr(df['staz_lat'], df['wynagrodzenie'])

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Lewy: staz vs wynagrodzenie
axes[0].scatter(df['staz_lat'], df['wynagrodzenie'], alpha=0.5, color='steelblue', s=40)
z = np.polyfit(df['staz_lat'], df['wynagrodzenie'], 1)
p_line = np.poly1d(z)
x_line = np.linspace(df['staz_lat'].min(), df['staz_lat'].max(), 100)
axes[0].plot(x_line, p_line(x_line), 'r--', lw=2, label=f'Trend (r={r_staz:.2f})')
axes[0].set_title('Staz vs Wynagrodzenie')
axes[0].set_xlabel('Staz pracy (lata)')
axes[0].set_ylabel('Wynagrodzenie (PLN)')
axes[0].legend()

# Prawy: ocena roczna vs wynagrodzenie
r_ocena, _ = stats.pearsonr(df['ocena_roczna'], df['wynagrodzenie'])
axes[1].scatter(df['ocena_roczna'], df['wynagrodzenie'], alpha=0.5, color='coral', s=40)
z2 = np.polyfit(df['ocena_roczna'], df['wynagrodzenie'], 1)
p2 = np.poly1d(z2)
x2 = np.linspace(df['ocena_roczna'].min(), df['ocena_roczna'].max(), 100)
axes[1].plot(x2, p2(x2), 'b--', lw=2, label=f'Trend (r={r_ocena:.2f})')
axes[1].set_title('Ocena roczna vs Wynagrodzenie')
axes[1].set_xlabel('Ocena roczna (1-5)')
axes[1].set_ylabel('Wynagrodzenie (PLN)')
axes[1].legend()

plt.tight_layout()
plt.show()
plt.close()

print(f"\nPearson staz–wynagrodzenie: r = {r_staz:.4f}, p = {p_staz:.4f}")
print(f"Pearson ocena–wynagrodzenie: r = {r_ocena:.4f}")
```

> "Dwa scatter ploty, dwa rozne wyniki. Staz vs wynagrodzenie — widoczna zaleznosc, linia trendu idzie w gore. Ocena roczna vs wynagrodzenie — chaos. To jest wartosc scatter plota — pokazuje cos, czego sama liczba r nie pokaze: ksztalt zaleznosci."

> "Interpretacja r: staz koreluje z wynagrodzeniem umiarkowanie — bo w firmie nie tylko staz decyduje o pensji. Ocena roczna praktycznie nie koreluje — bo ocena to subiektywna decyzja managera."

**[Komórka 9 — heatmapa korelacji]**

```python
# Heatmapa korelacji (bez seaborn — czysty matplotlib)
fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(corr.values, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(im, ax=ax)
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha='right')
ax.set_yticklabels(corr.columns)

for i in range(len(corr)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f'{corr.values[i, j]:.2f}',
                ha='center', va='center', fontsize=11,
                color='black' if abs(corr.values[i, j]) < 0.7 else 'white')

ax.set_title('Macierz korelacji — dataset HR')
plt.tight_layout()
plt.show()
plt.close()
```

> "Heatmapa korelacji — jeden rzut oka i widzicie ktore zmienne sa powiazane. Staz–wiek: najsilniejsza korelacja, okolo 0.76 — logiczne, im starszy pracownik, tym dluzszy staz. Staz–wynagrodzenie: umiarkowana. Ocena–cokolwiek: praktycznie zero."

> "Korelacja Spearmana — uzywamy gdy dane nie sa normalne, mamy outliery, albo zaleznosc jest monotoniczny ale nieliniowa. Liczy korelacje na rangach, nie na wartosciach. Jest odporniejsza."

```python
rho, p_rho = stats.spearmanr(df['staz_lat'], df['wynagrodzenie'])
print(f"Pearson r  = {r_staz:.4f}")
print(f"Spearman rho = {rho:.4f}")
print(f"Roznica: {abs(rho - r_staz):.3f}")
```

> "Spearman jest wyzszy od Pearsona — bo outliery zaburzaja Pearsona. To jest sygnal, ze w danych sa wartosci odstajace."

---

### 0:40-0:50 — PRZERWA (10 min)

> "10 minut przerwy. Zanim wrocicie — pomyslcie: mediana czy srednia do raportu o wynagrodzeniach? I dlaczego?"

---

### 0:50-1:05 — MATERIAL 3: Skosnos, kurtoza, outliery (15 min)

**[Komórka 10 — skew() i kurtosis()]**

```python
# Skosnos i kurtoza — Pandas
print("=== SKOSNOS I KURTOZA ===")
print(f"Skosnos (skew):     {df['wynagrodzenie'].skew():.3f}")
print(f"Kurtoza (kurtosis): {df['wynagrodzenie'].kurtosis():.3f}")
print()

# scipy.stats.describe — pelny snapshot
opis = stats.describe(df['wynagrodzenie'])
print("=== scipy.stats.describe ===")
print(f"Liczba obserwacji:  {opis.nobs}")
print(f"Min, Max:           {opis.minmax[0]:,.0f} — {opis.minmax[1]:,.0f}")
print(f"Srednia:            {opis.mean:,.0f}")
print(f"Wariancja:          {opis.variance:,.0f}")
print(f"Skosnos:            {opis.skewness:.3f}")
print(f"Kurtoza:            {opis.kurtosis:.3f}")
```

> "**Skosnos (skewness)** mowi o asymetrii rozkladu. Zero: symetria idealna. Wartosc dodatnia: ogon po prawej — kilka bardzo wysokich wartosci ciagnie rozklad w prawo. Tak jak nasze wynagrodzenia. Regula: |skewness| < 0.5 — prawie symetryczny, 0.5–1.0 — umiarkowanie skosny, > 1.0 — silnie skosny."

> "**Kurtoza (kurtosis)** mowi o 'spiczastosci' rozkladu i grubosci ogonow. Zero = rozklad normalny. Dodatnia: ostry szczyt i grube ogony — wiele wartosci skupionych blisko centrum, ale tez wiecej ekstremalnych. Nasze dane maja bardzo wysoka kurtoze — to przez 5 outlierow."

> "`scipy.stats.describe()` — jedna funkcja, szesc liczb. Szybki snapshot kazdego datasetu."

**[Komórka 11 — wykrywanie outlierow: IQR]**

```python
# Metoda IQR
def wykryj_outliery_iqr(seria, mnoznik=1.5):
    q1 = seria.quantile(0.25)
    q3 = seria.quantile(0.75)
    iqr = q3 - q1
    dolna = q1 - mnoznik * iqr
    gorna = q3 + mnoznik * iqr
    maska = (seria < dolna) | (seria > gorna)
    return maska, dolna, gorna

maska_iqr, dolna, gorna = wykryj_outliery_iqr(df['wynagrodzenie'])
print(f"Metoda IQR — granice: [{dolna:,.0f} PLN, {gorna:,.0f} PLN]")
print(f"Liczba outlierow: {maska_iqr.sum()} z {len(df)}")
print("\nOutliery:")
print(df[maska_iqr][['dzial', 'staz_lat', 'wynagrodzenie']].to_string())
```

> "Metoda IQR: kazda obserwacja poza [Q1 - 1.5*IQR, Q3 + 1.5*IQR] to outlier. To ta sama regula, ktora boxplot uzywa do rysowania wasow."

**[Komórka 12 — wykrywanie outlierow: z-score]**

```python
# Metoda z-score
z_scores = np.abs(stats.zscore(df['wynagrodzenie']))
maska_z = z_scores > 3.0
print(f"Metoda z-score (|z| > 3.0): {maska_z.sum()} outlierow z {len(df)}")
print(df[maska_z][['dzial', 'staz_lat', 'wynagrodzenie']].to_string())
```

> "Z-score: ile odchylen standardowych od sredniej? |z| > 3 = outlier. Reguła: 99.7% obserwacji z rozkladu normalnego miesci sie w plus/minus 3 STD."

> "Problem: z-score zaklada rozklad normalny i jest wrazliwy na same outliery — bo oblicza srednia i STD, ktore sa juz zaburzone. Dlatego IQR jest zwykle lepszy jako pierwsza metoda."

**[Komórka 13 — wplyw outlierow na statystyki]**

```python
# Porownanie: z outlierami vs bez
bez = df[~maska_iqr]['wynagrodzenie']
print("=== WPLYW OUTLIEROW ===")
print(f"{'Miara':<20} {'Z outlierami':>15} {'Bez':>15} {'Zmiana':>10}")
print("-" * 62)
for nazwa, z_val, bez_val in [
    ('Srednia', placa.mean(), bez.mean()),
    ('Mediana', placa.median(), bez.median()),
    ('Std', placa.std(), bez.std()),
]:
    print(f"{nazwa:<20} {z_val:>15,.0f} {bez_val:>15,.0f} {z_val - bez_val:>+10,.0f}")
```

> "Patrzcie: mediana prawie sie nie zmienila — bo jest odporna na outliery. Srednia i STD zmienily sie znaczaco. To jest dowod, ze mediana i IQR sa bezpieczniejszymi miarami."

> "Jak reagowac na outliery w biznesie? **Nie kasowac automatycznie.** Najpierw weryfikacja: czy to blad danych? Poprawiamy. Czy to realny przypadek — specjalny kontrakt? Zostawiamy, ale analizujemy osobno."

---

### 1:05-1:20 — MATERIAL 4: Rozklad normalny i test Shapiro-Wilka (15 min)

**[Komórka 14 — rozklad normalny: krzywa + histogram]**

```python
# Rozklad normalny — fundament statystyki
from scipy.stats import norm

# Generujemy dane normalne do demonstracji
np.random.seed(99)
dane_normalne = np.random.normal(loc=10000, scale=2000, size=500)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Lewy: histogram danych normalnych + krzywa
axes[0].hist(dane_normalne, bins=30, density=True, color='steelblue',
             edgecolor='white', alpha=0.7, label='Histogram (dane)')
x = np.linspace(dane_normalne.min(), dane_normalne.max(), 200)
axes[0].plot(x, norm.pdf(x, loc=dane_normalne.mean(), scale=dane_normalne.std()),
             'r-', lw=2, label='Krzywa normalna')
axes[0].set_title('Dane normalne (symulacja)')
axes[0].set_xlabel('Wartosc')
axes[0].set_ylabel('Gestosc')
axes[0].legend()

# Prawy: histogram naszych wynagrodzen + proba dopasowania
axes[1].hist(df['wynagrodzenie'], bins=30, density=True, color='coral',
             edgecolor='white', alpha=0.7, label='Histogram (wynagrodzenia)')
x2 = np.linspace(df['wynagrodzenie'].min(), df['wynagrodzenie'].max(), 200)
axes[1].plot(x2, norm.pdf(x2, loc=placa.mean(), scale=placa.std()),
             'r-', lw=2, label='Krzywa normalna')
axes[1].set_title('Wynagrodzenia — czy normalne?')
axes[1].set_xlabel('Wynagrodzenie (PLN)')
axes[1].set_ylabel('Gestosc')
axes[1].legend()

plt.tight_layout()
plt.show()
plt.close()
```

> "Po lewej — dane, ktore wygenerowalismy z rozkladu normalnego. Histogram ladnie dopasowuje sie do krzywej dzwonowej. Po prawej — nasze wynagrodzenia. Widzicie? Krzywa nie pasuje — ogon po prawej, outliery. Te dane NIE sa normalnie rozlozone."

> "`scipy.stats.norm` — obiekt reprezentujacy rozklad normalny. `norm.pdf()` — gestosc prawdopodobienstwa, `norm.cdf()` — dystrybuanta (jakie prawdopodobienstwo, ze wartosc jest mniejsza od X). Uzywamy go do modelowania i porownywania z danymi."

**[Komórka 15 — scipy.stats.norm: obliczenia]**

```python
# Rozklad normalny — operacje
mu, sigma = 10000, 2000  # srednia, odchylenie std

# Jakie prawdopodobienstwo, ze pracownik zarabia mniej niz 7000?
p_lt_7000 = norm.cdf(7000, loc=mu, scale=sigma)
print(f"P(X < 7000) = {p_lt_7000:.4f} ({p_lt_7000*100:.1f}%)")

# Jakie prawdopodobienstwo, ze zarabia wiecej niz 14000?
p_gt_14000 = 1 - norm.cdf(14000, loc=mu, scale=sigma)
print(f"P(X > 14000) = {p_gt_14000:.4f} ({p_gt_14000*100:.1f}%)")

# Jaki prog wynagrodzenia = top 10%?
top_10 = norm.ppf(0.90, loc=mu, scale=sigma)
print(f"Top 10% zarabia powyzej: {top_10:,.0f} PLN")
```

> "Trzy typowe pytania biznesowe, trzy funkcje: `cdf()` — prawdopodobienstwo ponizej progu. `1 - cdf()` — prawdopodobienstwo powyzej progu. `ppf()` — odwrotnosc, podajesz prawdopodobienstwo, dostajesz prog. Jesli wynagrodzenia sa normalne, te obliczenia daja sensowne wyniki."

**[Komórka 16 — test Shapiro-Wilka]**

```python
# Test Shapiro-Wilka: czy dane sa normalnie rozlozone?
# H0: dane pochodza z rozkladu normalnego
# H1: dane NIE pochodza z rozkladu normalnego

stat_norm, p_norm = stats.shapiro(dane_normalne[:50])  # max 50 dla demonstracji
print("=== TEST SHAPIRO-WILKA ===")
print(f"\nDane symulowane (normalne):")
print(f"  W = {stat_norm:.4f}, p = {p_norm:.4f}")
print(f"  Wniosek: {'Brak podstaw do odrzucenia H0 — dane moga byc normalne' if p_norm >= 0.05 else 'Odrzucamy H0 — dane NIE sa normalne'}")

stat_wyn, p_wyn = stats.shapiro(df['wynagrodzenie'])
print(f"\nWynagrodzenia HR:")
print(f"  W = {stat_wyn:.4f}, p = {p_wyn:.4f}")
print(f"  Wniosek: {'Brak podstaw do odrzucenia H0' if p_wyn >= 0.05 else 'Odrzucamy H0 — dane NIE sa normalne'}")

# Bez outlierow?
bez_out = df[~maska_iqr]['wynagrodzenie']
stat_bez, p_bez = stats.shapiro(bez_out)
print(f"\nWynagrodzenia bez outlierow:")
print(f"  W = {stat_bez:.4f}, p = {p_bez:.4f}")
print(f"  Wniosek: {'Brak podstaw do odrzucenia H0' if p_bez >= 0.05 else 'Odrzucamy H0 — dane NIE sa normalne'}")
```

> "Test Shapiro-Wilka — formalny test normalnosci. Hipoteza zerowa: dane pochodza z rozkladu normalnego. Jesli p < 0.05 — odrzucamy H0, dane nie sa normalne."

> "Dane symulowane: p > 0.05, nie odrzucamy — logiczne, bo je sami wygenerowalismy z rozkladu normalnego. Wynagrodzenia: p bliskie zera — silne odrzucenie, dane nie sa normalne. Ale uwaga: nawet bez outlierow wynagrodzenia czesto nie sa normalne — bo maja naturalna dolna granice (minimalne wynagrodzenie) i prawostronny ogon."

> "Dlaczego to wazne? Wiele testow statystycznych — t-test, ANOVA — zaklada normalnosc. Jesli dane nie sa normalne, musimy uzywac testow nieparametrycznych (Mann-Whitney, Kruskal-Wallis). O tym porozmawiamy szerzej na kolejnych zajeciach."

---

### 1:17-1:20 — AKTYWNOŚĆ — Mini-quiz (3 min)

> **Prowadzący mówi:** "Zanim podsumujemy — szybki quiz. Odpowiedzcie na kartce lub w parach."

1. Mediana wynagrodzen = 9 450 PLN, srednia = 9 900 PLN. Co to mowi o ksztalcie rozkladu?
2. Korelacja Pearsona r = 0.85 miedzy liczba reklam a sprzedaza. Czy reklamy POWODUJA wieksza sprzedaz? Dlaczego?
3. Metoda IQR wykryla 5 outlierow w wynagrodzeniach. Czy od razu je usuwasz? Co robisz najpierw?

> **[Po 2 min]** "Kto chce odpowiedzieć? [Omów odpowiedzi: 1) Rozklad prawostronnie skosny — kilka wysokich pensji ciagnie srednia w gore, mediana jest odporniejsza; 2) NIE — korelacja nie jest przyczynowoscia. Moze byc trzeci czynnik (np. sezon, wielkosc firmy); 3) Nie usuwasz automatycznie. Najpierw weryfikacja: blad danych? Popraw. Realny przypadek (specjalny kontrakt)? Analizuj osobno.]"

---

### 1:20-1:30 — PODSUMOWANIE

> "Podsumujmy. Dzis przeszlismy pelny zestaw statystyki opisowej."

**[Wyswietl na projektorze]**

```
KLUCZOWE ZASADY:

1. df.describe() — pierwsza rzecz na kazdym nowym datasecie
2. Dane skosne → mediana bezpieczniejsza niz srednia
3. Korelacja =/= przyczynowos — zawsze!
4. Outliery → IQR + z-score, ale najpierw weryfikacja (nie kasowac slepol!)
5. Rozklad normalny → scipy.stats.norm (pdf, cdf, ppf)
6. Shapiro-Wilk → sprawdz normalnosc ZANIM zastosujesz testy parametryczne
```

> "Za chwile przechodzimy do czesci laboratoryjnej. Bedziecie robic to samo na tych samych danych — ale sami. Statystyki opisowe, macierz korelacji, heatmapa, wykrywanie outlierow, histogram z krzywa normalna i test Shapiro. Wszystko krok po kroku."

> "Pytania przed laboratorium?"

---

## Materialy dodatkowe (dla ciekawych)

- Pandas docs: `DataFrame.describe()`, `DataFrame.corr()`, `Series.skew()`, `Series.kurtosis()`
- Scipy docs: `scipy.stats.describe()`, `scipy.stats.norm`, `scipy.stats.shapiro`
- VanderPlas — *Python Data Science Handbook*, rozdzial "Aggregation and Grouping"
