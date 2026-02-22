# W11 Wykład — Plan zajęć dla prowadzącego

## Temat: Statystyka opisowa w Pythonie

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z scipy/numpy/pandas/matplotlib
- **Przed wykładem:** otwórz `stats_demo.ipynb`
- **Dataset:** `employees.csv` (generowany w notebooku) — dane HR: wynagrodzenia, staż, dział

### Efekty uczenia się (Bloom poziom 2-3)
Po tym wykładzie osoba studiująca:
1. **Opisuje** miary tendencji centralnej (średnia, mediana, dominanta) i rozproszenia (odchylenie standardowe, wariancja, IQR, rozstęp) oraz interpretuje je w kontekście biznesowym (Bloom 2)
2. **Oblicza** korelację Pearsona i Spearmana za pomocą `np.corrcoef()` i `scipy.stats.spearmanr()`, interpretuje siłę i kierunek związku (Bloom 2)
3. **Stosuje** `scipy.stats.describe()` do szybkiej analizy rozkładu — skośność, kurtoza, percentyle (Bloom 3)
4. **Wykrywa** wartości odstające metodą IQR i z-score, ocenia ich wpływ na analizę biznesową (Bloom 3)
5. **Analizuje** dane kadrowe (wynagrodzenia, staż) łącząc miary statystyczne z interpretacją biznesową (Bloom 3)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań: 2 z W10, 3 nowe | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | "Wiemy jak ładować, czyścić, łączyć, wizualizować. Teraz: co te liczby ZNACZĄ?" | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Miary tendencji centralnej i rozproszenia — z interpretacją biznesową | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | Korelacja Pearsona i Spearmana — interpretacja, corrcoef, scatter z trendem | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | scipy.stats — describe, skewność, kurtoza, percentyle | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Wykrywanie wartości odstających — IQR, z-score, wpływ na biznes | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Analiza statystyczna datasetu HR/wynagrodzenia | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Zapowiedź W12: testy hipotez, testy A/B | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W10)

> "Pięć pytań — 3 minuty, kartka lub Mentimeter. Dwa pytania z zeszłego tygodnia, trzy z dzisiejszego tematu — żebyście zobaczyli, czego się dziś nauczycie."

**[Użyj quiz_w11.md — pytania 1 i 2 z W10]**

> "Odpowiedzi omówimy razem. Pytania 3, 4 i 5 — z nowego materiału. Nie znacie ich jeszcze, ale pod koniec zajęć będziecie wiedzieć, dlaczego odpowiedź jest taka, a nie inna."

---

### 0:05-0:10 — WPROWADZENIE

> "Przez ostatnie tygodnie nauczyliśmy się ładować dane z CSV i baz danych, czyścić je, łączyć tabele joinami, wizualizować w Matplotlib i Seaborn. Mamy dane na wykresie. Ładnie wygląda."

> "Ale co to ZNACZY? Czy wynagrodzenia są wysokie? Czy są fair? Czy pracownicy z dłuższym stażem zarabiają proporcjonalnie więcej? Czy są osoby, które zarabiają tak dużo lub tak mało, że to anomalia?"

> "To są pytania ze świata biznesu — i odpowiada na nie **statystyka opisowa**. Nie machine learning, nie deep learning — zwykłe liczby: średnia, mediana, odchylenie standardowe, korelacja. Te liczby mówią menedżerowi więcej niż sto wykresów."

> "Dziś przejdziemy przez cały zestaw narzędzi. Wszystko z Pythonem — pandas, numpy i `scipy.stats`. Pod koniec wykładu będziecie umieli wziąć dowolny dataset biznesowy i opisać go statystycznie w 10 minut."

**[Wyświetl na projektorze]**
```
Mapa dnia:
1. Miary centralne i rozproszenia  → co jest typowe?
2. Korelacja                        → co zależy od czego?
3. scipy.stats — rozkład           → jak wyglądają dane?
4. Wartości odstające               → kto jest anomalią?
```

> "Cały dzień pracujemy na danych HR — wynagrodzenia, staż pracy, dział. Dane wygenerujemy sami w notebooku, ale wzorowane na realnych strukturach firm. Zaczynamy."

---

### 0:10-0:30 — MATERIAŁ 1: Miary tendencji centralnej i rozproszenia (20 min)

**[Otwórz notebook — komórka 1: setup i generowanie danych]**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats

%matplotlib inline

np.random.seed(42)

# Generujemy realistyczny dataset HR
n = 200

dzialy = np.random.choice(['IT', 'Sprzedaż', 'HR', 'Marketing', 'Finanse'], n,
                           p=[0.30, 0.25, 0.15, 0.20, 0.10])
staz = np.random.gamma(shape=3, scale=2, size=n).clip(0.5, 20).round(1)

# Wynagrodzenie zależy od działu i stażu + szum
baza = {'IT': 9000, 'Sprzedaż': 7000, 'HR': 6500, 'Marketing': 7500, 'Finanse': 8500}
wynagrodzenie = np.array([
    baza[d] + staz[i] * 300 + np.random.normal(0, 1200)
    for i, d in enumerate(dzialy)
]).clip(4000, 25000).round(-2)

# Dodajemy 5 outlierów
wynagrodzenie[np.random.choice(n, 5, replace=False)] = np.random.choice(
    [2000, 2500, 35000, 40000, 38000], 5, replace=False
)

df = pd.DataFrame({
    'dział': dzialy,
    'staż_lat': staz,
    'wynagrodzenie': wynagrodzenie,
    'wiek': (25 + staz + np.random.normal(0, 3, n)).clip(22, 65).round().astype(int),
    'ocena_roczna': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.10, 0.40, 0.35, 0.10])
})

print(f"Dataset HR: {df.shape[0]} pracowników, {df.shape[1]} kolumn")
print(df.head())
```

> "Wygenerowaliśmy 200 pracowników z realną strukturą: wynagrodzenie zależy od działu — IT płaci najlepiej, HR najgorzej — i od stażu, z losowym szumem. Dodaliśmy 5 outlierów, żeby widzieć jak statystyki reagują na anomalie. W praktyce te anomalie to błędy w danych albo wyjątkowe kontrakty — będziemy je wykrywać w Materiale 4."

**[Komórka 2 — miary centralne]**

```python
# --- Miary tendencji centralnej ---
placa = df['wynagrodzenie']

srednia = placa.mean()
mediana = placa.median()
dominanta = placa.mode()[0]

print("=== MIARY TENDENCJI CENTRALNEJ ===")
print(f"Średnia wynagrodzenie:   {srednia:,.0f} PLN")
print(f"Mediana wynagrodzenie:   {mediana:,.0f} PLN")
print(f"Dominanta wynagrodzenie: {dominanta:,.0f} PLN")
```

> "Trzy liczby, trzy różne pytania. **Średnia** pyta: jaka jest suma podzielona przez liczbę? Ale jest wrażliwa na outliers. Jeden prezes z pensją 200 tys. podnosi średnią dla całej firmy."

> "**Mediana** pyta: co jest w środku? 50% pracowników zarabia mniej, 50% więcej. Jest odporna na outliers — dlatego GUS podaje mediany wynagrodzeń, nie średnie."

> "**Dominanta** pyta: jakie wynagrodzenie jest najpopularniejsze? W naszych danych zaokrąglaliśmy do 100 PLN, więc dominanta jest konkretna. W danych ciągłych mniej użyteczna — tam lepiej jest histogram."

> "Jeżeli mediana < średnia — rozkład jest prawostronnie skośny. Kilka osób z bardzo wysokimi pensjami ciągnie średnią w górę. To jest typowe dla danych o wynagrodzeniach na rynku."

**[Komórka 3 — wizualizacja: average vs median]**

```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(placa, bins=30, color='steelblue', edgecolor='white', alpha=0.8)
ax.axvline(srednia, color='red', lw=2, linestyle='--', label=f'Średnia: {srednia:,.0f}')
ax.axvline(mediana, color='green', lw=2, linestyle='-', label=f'Mediana: {mediana:,.0f}')
ax.axvline(dominanta, color='orange', lw=2, linestyle=':', label=f'Dominanta: {dominanta:,.0f}')
ax.set_title('Rozkład wynagrodzeń — średnia, mediana, dominanta')
ax.set_xlabel('Wynagrodzenie (PLN)')
ax.set_ylabel('Liczba pracowników')
ax.legend()
plt.tight_layout()
plt.show()
plt.close()
```

> "Patrzcie na histogram. Główna masa pracowników jest tu — i tu jest mediana, zielona linia. Czerwona — średnia — jest pociągnięta w prawo przez te kilka outlierów z pensją powyżej 35 tys. To jest efekt, który widzicie w każdym raporcie o wynagrodzeniach — dlatego media piszą: 'mediana wynagrodzenia to X', a nie 'średnia to Y'."

**[Komórka 4 — miary rozproszenia]**

```python
# --- Miary rozproszenia ---
odch_std = placa.std()
wariancja = placa.var()
q1 = placa.quantile(0.25)
q3 = placa.quantile(0.75)
iqr = q3 - q1
rozstep = placa.max() - placa.min()

print("=== MIARY ROZPROSZENIA ===")
print(f"Odchylenie std:     {odch_std:,.0f} PLN")
print(f"Wariancja:          {wariancja:,.0f} PLN²")
print(f"Q1 (25 percentyl):  {q1:,.0f} PLN")
print(f"Q3 (75 percentyl):  {q3:,.0f} PLN")
print(f"IQR (Q3 - Q1):      {iqr:,.0f} PLN")
print(f"Rozstęp (max-min):  {rozstep:,.0f} PLN")
```

> "Miary rozproszenia mówią: jak bardzo dane się różnią od siebie?"

> "**Odchylenie standardowe** — to jest 'przeciętne odchylenie od średniej', w tych samych jednostkach co dane. Jeśli STD wynagrodzeń to 2000 PLN — typowy pracownik zarabia ±2000 od średniej."

> "**Wariancja** — to STD do kwadratu. Jest w PLN² — trudno interpretować intuicyjnie. Używamy jej w obliczeniach matematycznych, ale do raportu zawsze podajemy STD."

> "**IQR — rozstęp międzykwartylowy** — to jest odległość między Q1 a Q3. 50% środkowych obserwacji mieści się w tym przedziale. IQR jest odporny na outliers — bo nie patrzy na wartości krańcowe."

> "**Rozstęp** — max minus min. Bardzo wrażliwy na outliers. U nas — przez te pensjże 2000 i 40000 — rozstęp jest ogromny i mało informuje o typowych pracownikach."

**[Komórka 5 — porównanie działów]**

```python
# Statystyki per dział
statystyki_dzial = df.groupby('dział', observed=True)['wynagrodzenie'].agg([
    'mean', 'median', 'std', 'min', 'max',
    lambda x: x.quantile(0.75) - x.quantile(0.25)
]).round(0)
statystyki_dzial.columns = ['Średnia', 'Mediana', 'Std', 'Min', 'Max', 'IQR']
print(statystyki_dzial.sort_values('Mediana', ascending=False))
```

> "Patrzcie — IT ma najwyższą medianę, ale też wysokie odchylenie standardowe. W IT wynagrodzenia bardzo się różnią — senior vs junior. HR ma niską medianę i niskie STD — mniejsze zróżnicowanie. To są realne wzorce z rynku pracy."

---

### 0:30-0:45 — MATERIAŁ 2: Korelacja (15 min)

**[Komórka 6 — korelacja Pearsona]**

```python
# --- Korelacja Pearsona ---
corr_matrix = df[['staż_lat', 'wynagrodzenie', 'wiek', 'ocena_roczna']].corr()
print("Macierz korelacji Pearsona:")
print(corr_matrix.round(3))

# Bezpośrednio
r, p_value = stats.pearsonr(df['staż_lat'], df['wynagrodzenie'])
print(f"\nKorelacja staż–wynagrodzenie: r = {r:.3f}, p = {p_value:.4f}")
```

> "Korelacja Pearsona — r — mierzy siłę liniowego związku między dwiema zmiennymi numerycznymi. Skala od -1 do +1."

> "r = +1: idealna zależność dodatnia — im więcej stażu, tym wyższe wynagrodzenie, zawsze. r = 0: brak związku liniowego. r = -1: idealna zależność ujemna."

> "W praktyce: r > 0.7 — silna, r = 0.4–0.7 — umiarkowana, r < 0.4 — słaba. Ale pamiętajcie: **korelacja nie jest przyczyną**. Jeśli sprzedaż lodów koreluje z utonięciami — to lato jest przyczyną obydwu, nie lody."

> "p-value mówi: czy ta korelacja mogła wyniknąć przez przypadek? p < 0.05 = statystycznie istotna. Będziemy o tym mówić szczegółowo w W12 przy testach hipotez."

**[Komórka 7 — scatter plot z trendem]**

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Lewy: staż vs wynagrodzenie
axes[0].scatter(df['staż_lat'], df['wynagrodzenie'],
                alpha=0.5, color='steelblue', s=40)

# Linia trendu
z = np.polyfit(df['staż_lat'], df['wynagrodzenie'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['staż_lat'].min(), df['staż_lat'].max(), 100)
axes[0].plot(x_line, p(x_line), 'r--', lw=2, label=f'Trend (r={r:.2f})')
axes[0].set_title('Staż vs Wynagrodzenie')
axes[0].set_xlabel('Staż pracy (lata)')
axes[0].set_ylabel('Wynagrodzenie (PLN)')
axes[0].legend()

# Prawy: ocena roczna vs wynagrodzenie
r2, _ = stats.pearsonr(df['ocena_roczna'], df['wynagrodzenie'])
axes[1].scatter(df['ocena_roczna'], df['wynagrodzenie'],
                alpha=0.5, color='coral', s=40)
z2 = np.polyfit(df['ocena_roczna'], df['wynagrodzenie'], 1)
p2 = np.poly1d(z2)
x_line2 = np.linspace(df['ocena_roczna'].min(), df['ocena_roczna'].max(), 100)
axes[1].plot(x_line2, p2(x_line2), 'b--', lw=2, label=f'Trend (r={r2:.2f})')
axes[1].set_title('Ocena roczna vs Wynagrodzenie')
axes[1].set_xlabel('Ocena roczna (1-5)')
axes[1].set_ylabel('Wynagrodzenie (PLN)')
axes[1].legend()

plt.tight_layout()
plt.show()
plt.close()
```

> "Dwa scatter ploty, dwa różne wyniki. Po lewej: staż vs wynagrodzenie — widoczna zależność, linia trendu idzie w górę. Po prawej: ocena roczna vs wynagrodzenie — chaos. Dlaczego? Bo ocena to decyzja managera, a nie automatyczna zależność od pensji."

> "To jest wartość scatter plota — pokazuje coś, czego sama liczba r nie pokaże: kształt zależności i outlierów."

**[Komórka 8 — korelacja Spearmana]**

```python
# --- Korelacja Spearmana ---
rho, p_spearman = stats.spearmanr(df['staż_lat'], df['wynagrodzenie'])
print(f"Korelacja Spearmana (rho): rho = {rho:.3f}, p = {p_spearman:.4f}")
print(f"Korelacja Pearsona   (r):  r   = {r:.3f}")
print(f"\nRóżnica: {abs(rho - r):.3f}")
```

> "Kiedy używać Spearmana zamiast Pearsona? Gdy dane nie są normalnie rozłożone, gdy mamy outliery, albo gdy zależność nie jest liniowa — ale monotonicz: im więcej X, tym więcej Y, niekoniecznie proporcjonalnie."

> "Spearman liczy korelację nie na wartościach, ale na **rangach** — na miejscach w rankingu. Jest odporniejszy na outlierów. Jeśli r i rho są bardzo różne — to znak, że mamy outlierów lub zależność nieliniową. Wyobraźcie sobie dane sprzedaży: gdy reklama jest mała, sprzedaż powoli rośnie. Gdy reklama jest duża, sprzedaż eksploduje — to jest monotoniczne, ale nieliniowe. Spearman sobie z tym poradzi."

---

### 0:45-0:55 — PRZERWA (10 min)

> "10 minut. Zanim wrócicie — w głowie: mediana czy średnia dla danych o wynagrodzeniach? I dlaczego?"

---

### 0:55-1:15 — MATERIAŁ 3: scipy.stats — describe, skośność, kurtoza, percentyle (20 min)

**[Komórka 9 — scipy.stats.describe]**

```python
# --- scipy.stats.describe ---
from scipy import stats

opis = stats.describe(df['wynagrodzenie'])
print("=== scipy.stats.describe ===")
print(f"Liczba obserwacji:  {opis.nobs}")
print(f"Min, Max:           {opis.minmax[0]:,.0f} — {opis.minmax[1]:,.0f}")
print(f"Średnia:            {opis.mean:,.0f}")
print(f"Wariancja:          {opis.variance:,.0f}")
print(f"Skośność:           {opis.skewness:.3f}")
print(f"Kurtoza:            {opis.kurtosis:.3f}")
```

> "`scipy.stats.describe()` — jedna funkcja, sześć liczb. To jest szybki snapshot każdego datasetu. Ale te ostatnie dwie — skośność i kurtoza — wymagają wyjaśnienia."

> "**Skośność (skewness)** mówi o asymetrii rozkładu. Zero: symetria idealna, jak rozkład normalny. Wartość dodatnia: ogon po prawej — tak jak nasze wynagrodzenia, kilka bardzo wysokich wartości ciągnie rozkład w prawo. Wartość ujemna: ogon po lewej — rzadziej, ale spotykana np. w czasach reakcji: większość szybko, nieliczni bardzo wolno."

> "Praktyczna reguła: |skewness| < 0.5 — rozkład prawie symetryczny. 0.5–1.0 — umiarkowanie skośny. > 1.0 — silnie skośny. Przy silnej skośności: preferujemy medianę nad średnią."

> "**Kurtoza (kurtosis)** mówi o 'spiczastości' rozkładu i grubości ogonów. Zero: rozkład normalny (to jest nadmiarowa kurtoza — scipy liczy właśnie nadmiarową). Dodatnia: ostry szczyt i grube ogony — wiele wartości skupionych blisko centrum, ale też więcej ekstremalnych. Ujemna: płaski rozkład, wartości równomiernie rozłożone."

> "W biznesie wysoka kurtoza wynagrodzeń oznacza: większość zarabia podobnie, ale są też ekstrema na obu końcach. Dla ryzyka finansowego — wysoka kurtoza to niebezpieczna sytuacja."

**[Komórka 10 — percentyle]**

```python
# --- Percentyle ---
percentyle = [10, 25, 50, 75, 90, 95, 99]
print("=== PERCENTYLE WYNAGRODZEŃ ===")
for p in percentyle:
    val = np.percentile(df['wynagrodzenie'], p)
    print(f"P{p:3d}: {val:>10,.0f} PLN")

# Lub pandas
print("\nPandas quantile:")
print(df['wynagrodzenie'].quantile([0.10, 0.25, 0.50, 0.75, 0.90]).round(0))
```

> "Percentyle to bardzo praktyczne narzędzie HR i biznesowe. P50 = mediana. P25 to dolny kwartyl — 25% pracowników zarabia mniej. P75 = górny kwartyl."

> "Firmy używają percentyli do benchmarkingu wynagrodzeń. 'Chcemy płacić na poziomie P75 rynku' — to znaczy: chcemy być w górnych 25%. 'Nasz pracownik zarabia poniżej P25 rynku' — czas na podwyżkę."

> "P95 i P99 — to są te osoby, które zarabiają eksplodująco dużo. Często właśnie tutaj ukrywają się outlierzy albo specjalne kontrakty."

**[Komórka 11 — wizualizacja skośności]**

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Lewy: histogram z percentylami
axes[0].hist(df['wynagrodzenie'], bins=30, color='steelblue',
             edgecolor='white', alpha=0.8)
for p_val, color, label in [(25, 'green', 'Q1'), (50, 'orange', 'Mediana'), (75, 'red', 'Q3')]:
    val = np.percentile(df['wynagrodzenie'], p_val)
    axes[0].axvline(val, color=color, lw=2, linestyle='--', label=f'{label}: {val:,.0f}')
axes[0].set_title('Rozkład wynagrodzeń z percentylami')
axes[0].set_xlabel('Wynagrodzenie (PLN)')
axes[0].set_ylabel('Liczba')
axes[0].legend(fontsize=9)

# Prawy: boxplot per dział
df.boxplot(column='wynagrodzenie', by='dział', ax=axes[1], figsize=(6, 5))
axes[1].set_title('Wynagrodzenie per dział')
axes[1].set_xlabel('Dział')
axes[1].set_ylabel('Wynagrodzenie (PLN)')
plt.suptitle('')  # usuń automatyczny tytuł z boxplot

plt.tight_layout()
plt.show()
plt.close()
```

> "Boxplot to wizualizacja kwartylów. Pudełko to IQR: od Q1 do Q3. Linia w środku — mediana. Wąsy — typowy zakres (1.5 × IQR). Punkty poza wąsami — to są właśnie kandydaci na outlierów. Zobaczcie — IT i Finanse mają kilka punktów powyżej górnego wąsa."

---

### 1:15-1:25 — MATERIAŁ 4: Wykrywanie wartości odstających (10 min)

**[Komórka 12 — metoda IQR]**

```python
# --- Wykrywanie outlierów: metoda IQR ---
def wykryj_outliery_iqr(seria, mnoznik=1.5):
    q1 = seria.quantile(0.25)
    q3 = seria.quantile(0.75)
    iqr = q3 - q1
    dolna_granica = q1 - mnoznik * iqr
    gorna_granica = q3 + mnoznik * iqr
    maski = (seria < dolna_granica) | (seria > gorna_granica)
    return maski, dolna_granica, gorna_granica

maska_iqr, dolna, gorna = wykryj_outliery_iqr(df['wynagrodzenie'])
outliery_iqr = df[maska_iqr]
print(f"Metoda IQR — granice: [{dolna:,.0f} PLN, {gorna:,.0f} PLN]")
print(f"Liczba outlierów: {maska_iqr.sum()} z {len(df)}")
print("\nOutliery:")
print(outliery_iqr[['dział', 'staż_lat', 'wynagrodzenie']].to_string())
```

> "Metoda IQR: każda obserwacja poza przedziałem [Q1 − 1.5×IQR, Q3 + 1.5×IQR] jest traktowana jako outlier. To jest ta sama reguła, której używa boxplot do rysowania wąsów."

> "Mnożnik 1.5 jest standardem (Tukey). Czasem używa się 3.0 dla 'ekstremalnych outlierów'. Wybór mnożnika zależy od kontekstu — w danych medycznych będziemy bardzo restrykcyjni, w danych sprzedażowych — bardziej liberalni."

**[Komórka 13 — metoda z-score]**

```python
# --- Wykrywanie outlierów: z-score ---
z_scores = np.abs(stats.zscore(df['wynagrodzenie']))
prog = 3.0
maska_z = z_scores > prog
outliery_z = df[maska_z]
print(f"Metoda z-score — próg: |z| > {prog}")
print(f"Liczba outlierów: {maska_z.sum()} z {len(df)}")
print("\nOutliery (z-score):")
print(outliery_z[['dział', 'staż_lat', 'wynagrodzenie']].to_string())
```

> "Z-score mówi: ile odchyleń standardowych ta wartość jest od średniej? |z| > 3 — standardowy próg outliera. Reguła: 99.7% obserwacji z rozkładu normalnego mieści się w ±3 STD."

> "Problem: z-score zakłada rozkład normalny i jest wrażliwy na same outlierów — bo oblicza średnią i STD, które same są zaburzone przez outlierów. Mamy błędne koło. Dlatego IQR jest zazwyczaj lepszy jako pierwsza metoda."

> "Jak reagować na outlierów w biznesie? **Nie kasować automatycznie.** Najpierw weryfikacja: czy to błąd danych? Wpisano 200 000 zamiast 20 000? Kasujemy lub poprawiamy. Czy to realny przypadek — prezes, specjalny kontrakt? Zostawiamy, ale analizujemy osobno. Outlierzy często są najciekawszymi przypadkami w danych."

**[Komórka 14 — porównanie statystyk z/bez outlierów]**

```python
# Wpływ outlierów na statystyki
bez_outlierow = df[~maska_iqr]['wynagrodzenie']

print("=== WPŁYW OUTLIERÓW NA STATYSTYKI ===")
print(f"{'Miara':<20} {'Z outlierami':>15} {'Bez outlierów':>15}")
print("-" * 52)
print(f"{'Średnia':<20} {df['wynagrodzenie'].mean():>15,.0f} {bez_outlierow.mean():>15,.0f}")
print(f"{'Mediana':<20} {df['wynagrodzenie'].median():>15,.0f} {bez_outlierow.median():>15,.0f}")
print(f"{'Std':<20} {df['wynagrodzenie'].std():>15,.0f} {bez_outlierow.std():>15,.0f}")
print(f"{'IQR':<20} {(df['wynagrodzenie'].quantile(0.75) - df['wynagrodzenie'].quantile(0.25)):>15,.0f} {(bez_outlierow.quantile(0.75) - bez_outlierow.quantile(0.25)):>15,.0f}")
```

> "Patrzcie na tę tabelę. Mediana prawie się nie zmieniła — bo jest odporna na outlierów. Średnia i STD — zmieniły się znacząco. IQR — stabilny. To jest dowód na to, że mediana i IQR są bezpieczniejszymi miarami, gdy mamy outlierów w danych."

---

### 1:25-1:35 — AKTYWNOŚĆ: Analiza statystyczna datasetu HR (10 min)

> "Teraz wasza kolej. Macie 8 minut. Otwórzcie nowy notebook lub nową komórkę."

**[Wyświetl na projektorze zadania]**

```
ZADANIA (samodzielnie):

1. Oblicz i wyświetl: średnią, medianę, std dla kolumny 'staż_lat'
   Pytanie: czy rozkład stażu jest skośny? Jak to sprawdzić?

2. Oblicz korelację Pearsona: wiek vs wynagrodzenie
   Porównaj z korelacją staż vs wynagrodzenie (obliczoną wcześniej)
   Pytanie: co koreluje silniej z wynagrodzeniem — wiek czy staż?

3. Użyj scipy.stats.describe() na kolumnie 'staż_lat'
   Odczytaj skośność. Zinterpretuj słownie.

4. Wykryj outliery w kolumnie 'staż_lat' metodą IQR
   Ilu pracowników ma "anomalny" staż?
```

> "Po 8 minutach — omówimy razem. Kto chce pokazać swój kod na projektorze?"

**[Po 8 minutach — omówienie]**

> "Korelacja wiek–wynagrodzenie powinna być umiarkowana — bo wiek i staż są powiązane, ale wiek też zawiera lata nauki, urlopy, zmiany branży. Staż bezpośrednio odzwierciedla doświadczenie w pracy — dlatego koreluje silniej z wynagrodzeniem."

---

### 1:35-1:45 — PODSUMOWANIE i zapowiedź W12

> "Zrobiliśmy dziś pełny zestaw statystyki opisowej: miary centralne, miary rozproszenia, korelacja, scipy.stats, wykrywanie outlierów."

> "Co zapamiętajcie:"

**[Wyświetl na projektorze]**
```
KLUCZOWE ZASADY:

✓ Dane skośne → mediana bezpieczniejsza niż średnia
✓ Outliery → IQR + z-score, ale najpierw weryfikacja
✓ Korelacja ≠ przyczynowość (zawsze!)
✓ Spearman → gdy dane niespełniają normalności lub mamy outliery
✓ Percentyle → benchmark, nie tylko kwartyle
```

> "Na kolejnym wykładzie — W12 — przechodzimy do testowania hipotez. Będziemy odpowiadać na pytania: 'Czy IT zarabia STATYSTYCZNIE istotnie więcej niż HR?' Nie tylko 'więcej w danych', ale 'więcej w populacji'. To jest t-test, chi-kwadrat, Mann-Whitney. Będziemy też robić testy A/B — fundament optymalizacji w e-commerce i marketingu."

> "Na laboratoriach — ćwiczenia na tym samym datasecie HR. Będziecie pisać samodzielnie, więc dobrze jeśli rozumiecie co dziś pokazałem."

> "Pytania? Dziękuję za uwagę."

---

## Materiały dodatkowe (dla ciekawych)

- `stats_demo.ipynb` — pełny notebook z kodem z wykładu
- `quiz_w11.md` — quiz na kolejne zajęcia
- Scipy docs: `scipy.stats` — pełna dokumentacja funkcji statystycznych
- Pandas docs: `DataFrame.describe()`, `DataFrame.corr()`
