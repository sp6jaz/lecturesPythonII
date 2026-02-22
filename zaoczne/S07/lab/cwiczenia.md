# S07 — Ćwiczenia: Testy hipotez, A/B testing, chi-kwadrat

**Programowanie w Pythonie II** | Laboratorium S07 (zaoczne)
**Notebook:** `lab_s07_testy_hipotez.ipynb`
**Dataset:** generowany w kodzie (`np.random.seed(42)`)
**Czas:** 90 min

---

## Przydatne materiały

| Temat | Link |
|-------|------|
| SciPy — ttest_ind() | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html |
| SciPy — ttest_rel() | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html |
| SciPy — shapiro() | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html |
| Wikipedia — Test t-Studenta | https://pl.wikipedia.org/wiki/Test_t-Studenta |
| Wikipedia — Wartość p | https://pl.wikipedia.org/wiki/Warto%C5%9B%C4%87_p |

---

## Setup — uruchom jako pierwszą komórkę

```python
%matplotlib inline
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(42)
sns.set_theme(style='whitegrid', palette='muted')

print("scipy:", __import__('scipy').__version__)
print("numpy:", np.__version__)
print("Środowisko gotowe.")
```

---

## Ćwiczenie 1: T-test jednorodkowy — czy średnia pensja = 5000 PLN? (15 min)

**Kontekst biznesowy:** Pracujesz w dziale HR firmy produkcyjnej. Dyrekcja deklaruje, że średnia pensja na stanowiskach operacyjnych wynosi 5000 PLN brutto. Związki zawodowe kwestionują tę deklarację. Twoje zadanie: zebrać próbkę i statystycznie zweryfikować tę wartość.

### Krok 1: Załaduj dane i obejrzyj je

```python
np.random.seed(42)
pensje = np.random.normal(loc=5400, scale=700, size=50)

# Podstawowe statystyki
print("=== Próbka pensji (n=50) ===")
print(f"Średnia:   {pensje.mean():.2f} PLN")
print(f"Mediana:   {np.median(pensje):.2f} PLN")
print(f"Std:       {pensje.std():.2f} PLN")
print(f"Min-Max:   {pensje.min():.0f} – {pensje.max():.0f} PLN")
```

### Krok 2: Sformułuj hipotezy

```python
# Zapisz w zmiennych — przyda się do raportu
h0 = "Średnia pensja = 5000 PLN (deklaracja dyrekcji)"
h1 = "Średnia pensja ≠ 5000 PLN (jest inna niż deklarowana)"
wartosc_oczekiwana = 5000

print(f"H₀: {h0}")
print(f"H₁: {h1}")
```

### Krok 3: Przeprowadź test

```python
# ZADANIE: Uzupełnij wywołanie jednorodkowego t-testu
# Wskazówka: stats.ttest_1samp(dane, popmean=wartość)
t_stat, p_val = _______________________________________________

print(f"t-statystyka = {t_stat:.4f}")
print(f"p-wartość     = {p_val:.4f}")
print(f"Poziom istotności α = 0.05")
print()

if p_val < 0.05:
    print("WYNIK: p < 0.05 → Odrzucamy H₀")
    print(f"WNIOSEK: Średnia pensja ({pensje.mean():.0f} PLN) ISTOTNIE "
          f"różni się od deklarowanych {wartosc_oczekiwana} PLN.")
else:
    print("WYNIK: p ≥ 0.05 → Brak podstaw do odrzucenia H₀")
    print("WNIOSEK: Brak dowodów na różnicę od deklarowanej wartości.")
```

### Krok 4: Przedział ufności

```python
# ZADANIE: Oblicz 95% przedział ufności dla średniej pensji
# Wskazówka: stats.t.interval(0.95, df=n-1, loc=mean, scale=stats.sem(dane))
ci = stats.t.interval(0.95, df=len(pensje)-1,
                      loc=pensje.mean(),
                      scale=stats.sem(pensje))
print(f"95% CI: [{ci[0]:.2f}, {ci[1]:.2f}] PLN")
print(f"Deklarowana wartość 5000 w CI: {'TAK' if ci[0] <= 5000 <= ci[1] else 'NIE'}")
```

### Krok 5: Wizualizacja

```python
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Histogram z zaznaczoną deklarowaną wartością
axes[0].hist(pensje, bins=15, alpha=0.7, color='steelblue',
             edgecolor='white', density=True)
axes[0].axvline(5000, color='red', ls='--', lw=2, label='H₀: μ=5000')
axes[0].axvline(pensje.mean(), color='green', ls='-', lw=2,
                label=f'x̄={pensje.mean():.0f}')
axes[0].set_title(f'Rozkład pensji (n=50)\np={p_val:.4f}')
axes[0].set_xlabel('Pensja brutto (PLN)')
axes[0].set_ylabel('Gęstość')
axes[0].legend()

# Przedział ufności
axes[1].errorbar(['Średnia pensja'], [pensje.mean()],
    yerr=[[pensje.mean()-ci[0]], [ci[1]-pensje.mean()]],
    fmt='o', color='steelblue', ms=10, capsize=12, lw=2.5,
    label=f'95% CI: [{ci[0]:.0f}, {ci[1]:.0f}]')
axes[1].axhline(5000, color='red', ls='--', lw=1.5,
                label='Deklaracja: 5000 PLN')
axes[1].set_title('Przedział ufności vs deklaracja')
axes[1].set_ylabel('PLN')
axes[1].legend()
axes[1].grid(True, axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
plt.close()
```

### Krok 6: Raport dla dyrekcji (komórka Markdown)

```markdown
## Raport: Weryfikacja średniej pensji

**Pytanie:** Czy średnia pensja na stanowiskach operacyjnych wynosi 5000 PLN?

**Wyniki:**
- Średnia z próbki: XXXX PLN (n=50)
- p-wartość: X.XXXX
- 95% przedział ufności: [XXXX, XXXX] PLN
- Deklarowana wartość 5000 PLN [mieści / nie mieści] się w przedziale ufności

**Wniosek:** [Uzupełnij — 2 zdania w języku zrozumiałym dla dyrekcji]
```

### Sprawdzenie 1 ✅

- [ ] `ttest_1samp(pensje, popmean=5000)` wywołane poprawnie
- [ ] t ≈ 2.62, p ≈ 0.012 — wynik istotny (odrzucamy H₀)
- [ ] 95% CI ≈ [5056, 5428] — wartość 5000 NIE mieści się w CI
- [ ] Histogram z dwiema pionowymi liniami (H₀ i średnia próbkowa)
- [ ] Raport Markdown z wnioskiem w języku biznesowym

---

## Ćwiczenie 2: T-test niezależny — dział A vs dział B (20 min)

**Kontekst biznesowy:** W firmie są dwa główne działy operacyjne: dział A (produkcja) i dział B (logistyka). Związki zawodowe twierdzą, że dział B zarabia więcej. HR prosi cię o analizę — czy różnica pensji jest statystycznie istotna, czy to może być przypadek wynikający z małej próby?

### Krok 1: Załaduj dane

```python
np.random.seed(42)
dzial_A = np.random.normal(loc=5200, scale=800, size=40)
dzial_B = np.random.normal(loc=5800, scale=850, size=35)

print("=== Porównanie działów A i B ===")
print(f"Dział A (produkcja):  n={len(dzial_A)}, x̄={dzial_A.mean():.2f}, "
      f"s={dzial_A.std():.2f}")
print(f"Dział B (logistyka):  n={len(dzial_B)}, x̄={dzial_B.mean():.2f}, "
      f"s={dzial_B.std():.2f}")
print(f"Różnica średnich: {dzial_B.mean()-dzial_A.mean():.2f} PLN")
```

### Krok 2: Przeprowadź Welch's t-test

```python
# ZADANIE: Uzupełnij wywołanie niezależnego t-testu (Welch)
# Wskazówka: stats.ttest_ind(grupa1, grupa2, equal_var=False)
t_stat, p_val = _______________________________________________

print(f"H₀: μ_A = μ_B (działy płacą tak samo)")
print(f"H₁: μ_A ≠ μ_B (działy płacą inaczej)")
print(f"\nt = {t_stat:.4f}")
print(f"p = {p_val:.4f}")
print()

if p_val < 0.05:
    print(f"WYNIK: Odrzucamy H₀ — różnica jest ISTOTNA STATYSTYCZNIE.")
    print(f"Dział B zarabia więcej o ~{dzial_B.mean()-dzial_A.mean():.0f} PLN/mies.")
else:
    print("WYNIK: Brak podstaw do odrzucenia H₀.")
```

### Krok 3: Przedział ufności dla różnicy

```python
# ZADANIE: Oblicz 95% CI dla różnicy średnich (B - A)
diff = dzial_B.mean() - dzial_A.mean()
se_diff = np.sqrt(dzial_A.var()/len(dzial_A) + dzial_B.var()/len(dzial_B))
df = len(dzial_A) + len(dzial_B) - 2
t_krit = stats.t.ppf(0.975, df)
ci_low = diff - t_krit * se_diff
ci_high = diff + t_krit * se_diff

print(f"Różnica (B-A): {diff:.2f} PLN")
print(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}] PLN")
print(f"Zero w CI: {'TAK' if ci_low <= 0 <= ci_high else 'NIE'}")
```

### Krok 4: Wizualizacja

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)

# Panel 1: Histogramy
axes[0].hist(dzial_A, bins=15, alpha=0.6, color='steelblue', density=True,
             label=f'Dział A (x̄={dzial_A.mean():.0f})')
axes[0].hist(dzial_B, bins=15, alpha=0.6, color='tomato', density=True,
             label=f'Dział B (x̄={dzial_B.mean():.0f})')
axes[0].axvline(dzial_A.mean(), color='steelblue', ls='--', lw=2)
axes[0].axvline(dzial_B.mean(), color='tomato', ls='--', lw=2)
axes[0].set_title(f'Rozkład pensji\n(p={p_val:.4f})')
axes[0].set_xlabel('Pensja (PLN)')
axes[0].legend(fontsize=9)

# Panel 2: Boxplot
bp = axes[1].boxplot([dzial_A, dzial_B],
                      labels=['Dział A\n(produkcja)', 'Dział B\n(logistyka)'],
                      patch_artist=True,
                      medianprops=dict(color='red', linewidth=2))
bp['boxes'][0].set_facecolor('lightblue')
bp['boxes'][1].set_facecolor('lightsalmon')
axes[1].set_title('Boxplot — porównanie działów')
axes[1].set_ylabel('Pensja (PLN)')
axes[1].grid(True, axis='y', alpha=0.3)

# Panel 3: CI dla różnicy
axes[2].errorbar(['Różnica B−A'], [diff],
    yerr=[[diff-ci_low], [ci_high-diff]],
    fmt='o', color='darkgreen', ms=10, capsize=12, lw=2.5,
    label=f'Różnica = {diff:.0f} PLN')
axes[2].axhline(0, color='red', ls='--', lw=1.5, label='H₀: różnica = 0')
axes[2].set_title('95% CI dla różnicy pensji')
axes[2].set_ylabel('PLN')
axes[2].legend(fontsize=9)
axes[2].grid(True, axis='y', alpha=0.3)

fig.suptitle('Analiza pensji: Dział A vs Dział B', fontsize=13, fontweight='bold')
plt.show()
plt.close()
```

### Krok 5: Pytania do odpowiedzi (Markdown)

1. Dlaczego użyliśmy `equal_var=False` (Welch) zamiast klasycznego t-testu Studenta?
2. Co by się stało, gdybyśmy użyli `ttest_rel` (sparowany) zamiast `ttest_ind`? Czy byłoby to poprawne?
3. Różnica ~778 PLN jest istotna statystycznie. Ale czy jest istotna BIZNESOWO? Jakie dodatkowe informacje potrzebujesz?

### Sprawdzenie 2 ✅

- [ ] `ttest_ind(dzial_A, dzial_B, equal_var=False)` wywołane poprawnie
- [ ] t ≈ -4.24, p ≈ 0.0001 — wynik istotny (odrzucamy H₀)
- [ ] 95% CI ≈ [417, 1139] PLN — zero NIE mieści się w CI
- [ ] 3 panele wizualizacji: histogramy, boxplot, CI
- [ ] Odpowiedzi na 3 pytania w komórce Markdown

---

## Ćwiczenie 3: A/B test kampanii e-mailowej (30 min)

**Kontekst biznesowy:** Jesteś analitykiem w firmie e-commerce. Dział marketingu przetestował dwie wersje maila do bazy klientów:
- **Wersja A** (stary email): klasyczny newsletter ze zniżkami
- **Wersja B** (nowy email): personalizowany mail z rekomendacjami produktów

Metryka: **wartość zakupu po kliknięciu w email** (PLN). Każdy klient kliknął dokładnie raz.

Twoje zadanie: przeprowadzić pełną analizę A/B i przygotować rekomendację.

### Dane

```python
np.random.seed(42)
n_old, n_new = 180, 180

# Stary email — standardowy newsletter
email_stary = np.random.normal(loc=42, scale=12, size=n_old)

# Nowy email — personalizowane rekomendacje
email_nowy = np.random.normal(loc=47, scale=13, size=n_new)
```

### KROK 1: Statystyki opisowe

```python
# ZADANIE: Oblicz dla obu grup: n, średnia, mediana, std, min, max
# Wskazówka: użyj pd.Series().describe() lub np.mean/median/std

print("=== Statystyki opisowe ===")
print(f"Stary email: n={n_old}, x̄={email_stary.mean():.2f}, "
      f"mediana={np.median(email_stary):.2f}, s={email_stary.std():.2f}")
print(f"Nowy email:  n={n_new}, x̄={email_nowy.mean():.2f}, "
      f"mediana={np.median(email_nowy):.2f}, s={email_nowy.std():.2f}")
print(f"\nRóżnica średnich: {email_nowy.mean()-email_stary.mean():.2f} PLN "
      f"({(email_nowy.mean()/email_stary.mean()-1)*100:.1f}%)")
```

### KROK 2: Test normalności

```python
# ZADANIE: Sprawdź normalność obu grup testem Shapiro-Wilka
# Użyj podpróby 50 obserwacji (n=180 to dużo dla Shapiro)
np.random.seed(42)
idx = np.random.choice(n_old, 50, replace=False)

stat_old, p_old = stats.shapiro(email_stary[idx])
stat_new, p_new = stats.shapiro(email_nowy[idx])

print("=== Test normalności (Shapiro-Wilk) ===")
print(f"Stary: W={stat_old:.4f}, p={p_old:.4f} "
      f"{'(normalny)' if p_old > 0.05 else '(nie-normalny)'}")
print(f"Nowy:  W={stat_new:.4f}, p={p_new:.4f} "
      f"{'(normalny)' if p_new > 0.05 else '(nie-normalny)'}")
```

### KROK 3: Test właściwy (Welch's t-test)

```python
# ZADANIE: Przeprowadź Welch's t-test
t_stat, p_val = _______________________________________________

print("=== Welch's t-test ===")
print(f"H₀: μ_stary = μ_nowy (email nie ma znaczenia)")
print(f"H₁: μ_stary ≠ μ_nowy (personalizacja zmienia wartość zakupu)")
print(f"\nt = {t_stat:.4f}")
print(f"p = {p_val:.4f}")
print()

if p_val < 0.05:
    print(">>> Odrzucamy H₀ — personalizacja ISTOTNIE zwiększa wartość zakupu.")
else:
    print(">>> Brak podstaw do odrzucenia H₀.")
```

### KROK 4: Przedział ufności i effect size

```python
# ZADANIE: Oblicz 95% CI dla różnicy oraz Cohen's d
diff = email_nowy.mean() - email_stary.mean()
se_diff = np.sqrt(email_stary.var()/n_old + email_nowy.var()/n_new)
df = n_old + n_new - 2
t_krit = stats.t.ppf(0.975, df)

ci_low = diff - t_krit * se_diff
ci_high = diff + t_krit * se_diff

# Cohen's d = różnica / pooled std
pooled_std = np.sqrt((email_stary.std()**2 + email_nowy.std()**2) / 2)
cohens_d = diff / pooled_std

print(f"Różnica (nowy - stary): {diff:.2f} PLN")
print(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}] PLN")
print(f"Cohen's d: {cohens_d:.3f}", end="")
if abs(cohens_d) < 0.2:
    print(" (mały efekt)")
elif abs(cohens_d) < 0.5:
    print(" (średni efekt)")
elif abs(cohens_d) < 0.8:
    print(" (średni-duży efekt)")
else:
    print(" (duży efekt)")
```

### KROK 5: Wizualizacja (4 panele)

```python
fig, axes = plt.subplots(2, 2, figsize=(13, 9), constrained_layout=True)

# Panel 1: Histogramy
axes[0,0].hist(email_stary, bins=20, alpha=0.6, color='steelblue', density=True,
               label=f'Stary (x̄={email_stary.mean():.1f})')
axes[0,0].hist(email_nowy, bins=20, alpha=0.6, color='tomato', density=True,
               label=f'Nowy (x̄={email_nowy.mean():.1f})')
axes[0,0].axvline(email_stary.mean(), color='steelblue', ls='--', lw=2)
axes[0,0].axvline(email_nowy.mean(), color='tomato', ls='--', lw=2)
axes[0,0].set_title(f'Rozkład wartości zakupu\n(p={p_val:.4f})')
axes[0,0].set_xlabel('Wartość zakupu (PLN)')
axes[0,0].legend(fontsize=9)

# Panel 2: Boxplot
bp = axes[0,1].boxplot([email_stary, email_nowy],
    labels=['Stary email', 'Nowy email'],
    patch_artist=True,
    medianprops=dict(color='red', linewidth=2))
bp['boxes'][0].set_facecolor('lightblue')
bp['boxes'][1].set_facecolor('lightsalmon')
axes[0,1].set_title('Boxplot — porównanie wersji')
axes[0,1].set_ylabel('Wartość zakupu (PLN)')
axes[0,1].grid(True, axis='y', alpha=0.3)

# Panel 3: Przedział ufności
axes[1,0].errorbar(['Różnica\n(nowy − stary)'], [diff],
    yerr=[[diff-ci_low], [ci_high-diff]],
    fmt='o', color='darkgreen', ms=10, capsize=12, lw=2.5,
    label=f'Różnica = {diff:.1f} PLN')
axes[1,0].axhline(0, color='red', ls='--', lw=1.5, label='H₀: różnica = 0')
axes[1,0].set_title(f'95% CI dla różnicy\n[{ci_low:.1f}, {ci_high:.1f}] PLN')
axes[1,0].set_ylabel('PLN')
axes[1,0].legend(fontsize=9)
axes[1,0].grid(True, axis='y', alpha=0.3)

# Panel 4: Projekcja biznesowa
baza_klientow = np.array([5000, 10000, 20000, 50000])
dodatkowy_przychod = baza_klientow * diff
axes[1,1].bar(range(len(baza_klientow)),
              dodatkowy_przychod / 1000,
              color='mediumseagreen', edgecolor='white')
axes[1,1].set_xticks(range(len(baza_klientow)))
axes[1,1].set_xticklabels([f'{x//1000}k' for x in baza_klientow])
axes[1,1].set_title('Szacowany dodatkowy przychód')
axes[1,1].set_xlabel('Baza klientów')
axes[1,1].set_ylabel('Dodatkowy przychód (tys. PLN)')
axes[1,1].grid(True, axis='y', alpha=0.3)

fig.suptitle('A/B Test — Kampania e-mailowa: Pełna analiza',
             fontsize=13, fontweight='bold')
plt.show()
plt.close()
```

### KROK 6: Wniosek biznesowy (komórka Markdown)

```markdown
## Wyniki A/B testu — Kampania e-mailowa

**Pytanie:** Czy personalizowany email (nowa wersja) zwiększa wartość zakupu?

**Wyniki:**
- Stary email: x̄ = XX.XX PLN (n=180)
- Nowy email: x̄ = XX.XX PLN (n=180)
- Różnica: +X.XX PLN (X.X%)
- p-wartość: X.XXXX
- 95% CI dla różnicy: [X.XX, X.XX] PLN
- Cohen's d: X.XXX (wielkość efektu: ______)

**Wniosek:**
[Czy personalizacja działa? Opisz wynik w języku zrozumiałym
dla dyrektora marketingu. Odnieś się do przedziału ufności
i projekcji przychodów.]

**Rekomendacja:**
[Wdrożyć / nie wdrażać / potrzeba więcej danych — z uzasadnieniem.
Jeśli wdrażać — oszacuj dodatkowy przychód przy bazie 20 000 klientów.]
```

### Sprawdzenie 3 ✅

- [ ] KROK 1: statystyki opisowe dla obu grup wypisane czytelnie
- [ ] KROK 2: Shapiro-Wilk na podpróbie 50 obs. — oba p > 0.05
- [ ] KROK 3: `ttest_ind(..., equal_var=False)`, t ≈ -4.46, p < 0.001
- [ ] KROK 4: CI ≈ [3.14, 8.06] PLN, Cohen's d ≈ 0.47 (średni efekt)
- [ ] KROK 5: 4 panele — histogramy, boxplot, CI, projekcja biznesowa
- [ ] KROK 6: komórka Markdown z wnioskiem po polsku, zrozumiała dla dyrektora marketingu
- [ ] Cały kod wykonuje się bez błędów

---

## Ćwiczenie 4: Chi-kwadrat — segment klienta a kanał pozyskania (25 min)

**Kontekst biznesowy:** Firma e-commerce analizuje swoją bazę klientów. Chce wiedzieć, czy kanał pozyskania klienta (organiczny / płatne reklamy / polecenia) wpływa na to, do jakiego segmentu klient trafia (Basic / Standard / Premium). Jeśli tak — marketing może lepiej alokować budżet.

### Krok 1: Przygotuj tabelę kontyngencji

```python
# Tabela kontyngencji: Kanał pozyskania × Segment klienta
# Wiersze: kanały pozyskania
# Kolumny: segmenty klientów
dane = np.array([
    [60, 30, 10],   # Organiczny — głównie Basic
    [25, 45, 30],   # Paid Ads — dużo Standard
    [15, 25, 60],   # Polecenia — głównie Premium
])

kanaly = ['Organiczny', 'Paid Ads', 'Polecenia']
segmenty = ['Basic', 'Standard', 'Premium']

df_tab = pd.DataFrame(dane, index=kanaly, columns=segmenty)
df_tab['SUMA'] = df_tab.sum(axis=1)
df_tab.loc['SUMA'] = df_tab.sum()

print("=== Tabela kontyngencji ===")
print(df_tab)
print(f"\nŁączna liczba klientów: {dane.sum()}")
```

### Krok 2: Przeprowadź test chi-kwadrat

```python
# ZADANIE: Uzupełnij wywołanie testu chi-kwadrat
# Wskazówka: stats.chi2_contingency(tabela_numpy)
# UWAGA: użyj oryginalnej tablicy `dane` (bez wiersza/kolumny SUMA!)
chi2_stat, p_val, dof, expected = _______________________________________________

print("=== Test chi-kwadrat ===")
print(f"H₀: Kanał pozyskania i segment klienta są NIEZALEŻNE")
print(f"H₁: Kanał pozyskania WPŁYWA na segment klienta")
print(f"\nχ² = {chi2_stat:.4f}")
print(f"df = {dof}")
print(f"p  = {p_val:.2e}")
print()

print("Wartości oczekiwane (gdyby kanał NIE wpływał na segment):")
print(pd.DataFrame(expected.round(1), index=kanaly, columns=segmenty))
print()

if p_val < 0.05:
    print(">>> Odrzucamy H₀ — kanał pozyskania WPŁYWA na segment klienta!")
else:
    print(">>> Brak dowodów na zależność.")
```

### Krok 3: Analiza residuów — gdzie leży zależność?

```python
# Residua standaryzowane: (obserwowane - oczekiwane) / sqrt(oczekiwane)
# |residuum| > 2 → silne odchylenie od niezależności
residua = (dane - expected) / np.sqrt(expected)

print("=== Residua standaryzowane ===")
print("(wartość > 2: znacząco WIĘCEJ niż oczekiwano)")
print("(wartość < -2: znacząco MNIEJ niż oczekiwano)")
print()
df_res = pd.DataFrame(residua.round(2), index=kanaly, columns=segmenty)
print(df_res)
print()

# Interpretacja
print("Kluczowe obserwacje:")
for i, kanal in enumerate(kanaly):
    for j, segment in enumerate(segmenty):
        if abs(residua[i, j]) > 2:
            kierunek = "WIĘCEJ" if residua[i, j] > 0 else "MNIEJ"
            print(f"  {kanal} → {segment}: {kierunek} niż oczekiwano "
                  f"(residuum = {residua[i,j]:.2f})")
```

### Krok 4: Wizualizacja (3 panele)

```python
fig, axes = plt.subplots(1, 3, figsize=(16, 5), constrained_layout=True)

# Panel 1: Stacked bar chart
colors = ['#3498db', '#2ecc71', '#e74c3c']
bottom = np.zeros(3)
for i, (seg, kolor) in enumerate(zip(segmenty, colors)):
    axes[0].bar(kanaly, dane[:, i], bottom=bottom, label=seg,
                color=kolor, alpha=0.85, edgecolor='white')
    bottom += dane[:, i]
axes[0].set_title('Liczba klientów\nwg kanału i segmentu')
axes[0].set_ylabel('Liczba klientów')
axes[0].legend(title='Segment')

# Panel 2: Procentowy stacked bar chart (100%)
dane_pct = dane / dane.sum(axis=1, keepdims=True) * 100
bottom_pct = np.zeros(3)
for i, (seg, kolor) in enumerate(zip(segmenty, colors)):
    axes[1].bar(kanaly, dane_pct[:, i], bottom=bottom_pct,
                label=seg, color=kolor, alpha=0.85, edgecolor='white')
    # Etykiety procentowe
    for j in range(3):
        if dane_pct[j, i] > 8:
            axes[1].text(j, bottom_pct[j] + dane_pct[j, i]/2,
                        f'{dane_pct[j, i]:.0f}%', ha='center', va='center',
                        fontsize=9, fontweight='bold', color='white')
    bottom_pct += dane_pct[:, i]
axes[1].set_title('Struktura procentowa\nwg kanału')
axes[1].set_ylabel('Udział (%)')
axes[1].legend(title='Segment')

# Panel 3: Heatmapa residuów
im = axes[2].imshow(residua, cmap='RdBu_r', aspect='auto', vmin=-5, vmax=5)
axes[2].set_xticks(range(len(segmenty)))
axes[2].set_yticks(range(len(kanaly)))
axes[2].set_xticklabels(segmenty)
axes[2].set_yticklabels(kanaly)
for i in range(len(kanaly)):
    for j in range(len(segmenty)):
        axes[2].text(j, i, f'{residua[i,j]:.1f}', ha='center', va='center',
                     fontsize=12, fontweight='bold',
                     color='white' if abs(residua[i,j]) > 2 else 'black')
plt.colorbar(im, ax=axes[2], label='Residuum standaryzowane')
axes[2].set_title(f'Heatmapa residuów\n(χ²={chi2_stat:.1f}, p<0.001)')

fig.suptitle('Analiza chi-kwadrat: Kanał pozyskania × Segment klienta',
             fontsize=13, fontweight='bold')
plt.show()
plt.close()
```

### Krok 5: Wniosek i rekomendacja (Markdown)

```markdown
## Analiza: Kanał pozyskania a segment klienta

**Wyniki testu chi-kwadrat:**
- χ² = XX.XX, df = X, p = X.XXe-XX
- Wniosek: kanał pozyskania [jest / nie jest] istotnie powiązany z segmentem

**Kluczowe zależności (z residuów):**
- Organiczny → głównie klienci _______ (residuum = ____)
- Paid Ads → głównie klienci _______ (residuum = ____)
- Polecenia → głównie klienci _______ (residuum = ____)

**Rekomendacja dla marketingu:**
[3-4 zdania — jak alokować budżet, jeśli firma chce zwiększyć
liczbę klientów Premium? A jeśli chce zwiększyć wolumen (Basic)?]
```

### Krok 6: Commit do repozytorium Git

```bash
# W terminalu:
cd ~/python2_projekt

git status
git add lab_s07_testy_hipotez.ipynb
git commit -m "S07: Testy hipotez — t-test, A/B test, chi-kwadrat — scipy.stats"
git push
```

### Sprawdzenie 4 ✅

- [ ] `chi2_contingency(dane)` wywołane poprawnie
- [ ] chi2 = 78.00, df = 4, p < 0.001 — wynik istotny
- [ ] Residua obliczone i zinterpretowane: Organik→Basic (+4.6), Polecenia→Premium (+4.6)
- [ ] 3 panele: stacked bar, procentowy stacked bar, heatmapa residuów
- [ ] Wniosek Markdown z konkretnymi rekomendacjami budżetowymi
- [ ] `git log` — widoczny commit z plikiem notebooka

---

## Podsumowanie kluczowych komend

```python
# === T-TESTY ===
# Jednorodkowy — jedna próba vs oczekiwana wartość
t, p = stats.ttest_1samp(dane, popmean=mu0)

# Niezależny (Welch) — dwie różne grupy
t, p = stats.ttest_ind(grupa_A, grupa_B, equal_var=False)

# Sparowany — te same osoby, dwa pomiary
t, p = stats.ttest_rel(przed, po)

# === CHI-KWADRAT ===
# Zależność zmiennych kategorycznych (tabela kontyngencji)
chi2, p, dof, expected = stats.chi2_contingency(tabela_2d)

# === PRZEDZIAŁY UFNOŚCI ===
se = stats.sem(dane)                                      # błąd standardowy
ci = stats.t.interval(0.95, df=n-1, loc=mean, scale=se)   # 95% CI

# === WZORZEC A/B TESTU (5 kroków) ===
# 1. Statystyki opisowe (mean, median, std)
# 2. Test normalności (stats.shapiro, podpróba 50 obs.)
# 3. Test właściwy (ttest_ind, equal_var=False)
# 4. Przedział ufności + effect size (Cohen's d)
# 5. Wniosek biznesowy — w języku managera, z projekcją $$$
```
