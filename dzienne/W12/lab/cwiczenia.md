# L12 — Ćwiczenia: Statystyka — rozkłady i testy hipotez

**Programowanie w Pythonie II** | Laboratorium 12
**Notebook:** `lab12_hypothesis_testing.ipynb`
**Dataset:** generowany w kodzie (`np.random.seed(42)`)

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

## Przydatne materiały

| Temat | Link |
|-------|------|
| SciPy — `ttest_1samp()` | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html |
| SciPy — `ttest_ind()` (niezależny) | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html |
| SciPy — `ttest_rel()` (sparowany) | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html |
| SciPy — `shapiro()` (test normalności) | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html |
| SciPy — `chi2_contingency()` | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html |
| SciPy — `norm` (rozkład normalny) | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html |
| Wikipedia — Test t-Studenta | https://pl.wikipedia.org/wiki/Test_t-Studenta |
| Wikipedia — Wartość p | https://pl.wikipedia.org/wiki/Warto%C5%9B%C4%87_p |

### Kluczowe pojęcia

- **H₀ (hipoteza zerowa)** — "nie ma różnicy" / "nie ma efektu". To hipoteza którą testujemy.
- **H₁ (hipoteza alternatywna)** — "jest różnica" / "jest efekt". To co chcemy wykazać.
- **p-wartość** — prawdopodobieństwo uzyskania takiego wyniku (lub bardziej ekstremalnego) JEŚLI H₀ jest prawdą.
  - p < 0.05 → odrzucamy H₀ (wynik istotny statystycznie)
  - p ≥ 0.05 → nie ma podstaw do odrzucenia H₀
- **t-test jednorodkowy** — czy średnia próby różni się od znanej wartości? Np. "Czy średni czas dostawy ≠ 24h?"
- **t-test niezależny** — czy dwie NIEZALEŻNE grupy mają różne średnie? Np. "Czy grupa A ≠ grupa B?"
- **t-test sparowany** — czy ta sama grupa ma różne wyniki PRZED i PO? Np. "Czy szkolenie pomogło?"
- **Welch's t-test** — wersja `equal_var=False`. Bezpieczniejsza — nie zakłada równości wariancji. ZAWSZE używaj tej wersji.
- **Chi-kwadrat** — test dla danych kategorycznych. "Czy preferencje zależą od grupy wiekowej?"

---

## Ćwiczenie 1: Rozkład normalny i testy normalności (20 min)

**Kontekst biznesowy:** Pracujesz w dziale analityki firmy logistycznej. Analizujesz czasy dostawy paczek. Chcesz sprawdzić czy dane są normalne (żebyś wiedział jakich testów możesz potem używać), a także odpowiedzieć na pytania zarządu dotyczące prawdopodobieństwa opóźnień.

### 1a. Obliczenia na rozkładzie normalnym

Firma deklaruje że czas dostawy wynosi średnio **48 godzin** (μ) z odchyleniem standardowym **6 godzin** (σ).

```python
mu_dostawa = 48   # godziny
sigma_dostawa = 6

# ZADANIE 1: Jakie jest prawdopodobieństwo, że dostawa trwa DŁUŻEJ niż 60 godzin?
# Wskazówka: P(X > 60) = 1 - CDF(60)
p_opoznienie = _______________________________________________
print(f"P(dostawa > 60h): {p_opoznienie*100:.2f}%")

# ZADANIE 2: Jaki jest 95. percentyl czasu dostawy?
# (95% dostaw realizowanych szybciej niż ta wartość — dla SLA)
percentyl_95 = _______________________________________________
print(f"95. percentyl SLA: {percentyl_95:.1f} godzin")

# ZADANIE 3: Jaki % dostaw mieści się w oknie 42-54 godzin (±1σ od średniej)?
# Wskazówka: CDF(54) - CDF(42)
p_okno = _______________________________________________
print(f"P(42h ≤ dostawa ≤ 54h): {p_okno*100:.2f}%")
```

**Oczekiwane wyniki:**
- P(dostawa > 60h) ≈ 2.28%
- 95. percentyl ≈ 57.9 godzin
- P(42h ≤ X ≤ 54h) ≈ 68.27%

### 1b. Generowanie danych i wizualizacja

```python
np.random.seed(42)

# Generujemy 200 faktycznych czasów dostawy
czasy_dostawy = np.random.normal(loc=48, scale=6, size=200)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Panel lewy: histogram z krzywą normalną
# Uzupełnij: narysuj histogram (density=True, alpha=0.7, color='steelblue')
# i nałóż krzywą: stats.norm.pdf(x_range, loc=..., scale=...)
axes[0].set_title('Histogram czasów dostawy vs krzywa normalna')
axes[0].set_xlabel('Czas dostawy (h)')
axes[0].set_ylabel('Gęstość')

# Panel prawy: QQ-plot
# Uzupełnij: stats.probplot(czasy_dostawy, dist='norm', plot=axes[1])
axes[1].set_title('QQ-plot — czy dane są normalne?')

plt.tight_layout()
plt.show()
plt.close()
```

**Pytanie:** Patrząc na QQ-plot — czy punkty leżą blisko linii prostej? Co to oznacza?

### 1c. Formalny test normalności

```python
np.random.seed(42)

# Zbiór 1: czasy dostawy (normalne z definicji — wygenerowane z normal())
czasy_normalne = np.random.normal(48, 6, 100)

# Zbiór 2: kwoty reklamacji (asymetryczne — małe wartości częste, duże rzadkie)
kwoty_reklamacji = np.random.exponential(scale=150, size=100) + 50

# Dla każdego zbioru:
# a) Przeprowadź test Shapiro-Wilka (stats.shapiro)
# b) Wypisz: W, p-wartość, wniosek (normalny / nie-normalny przy α=0.05)

for nazwa, dane in [('Czasy dostawy', czasy_normalne), ('Kwoty reklamacji', kwoty_reklamacji)]:
    # Uzupełnij: stat, p = stats.shapiro(dane)
    stat, p = _______________________________________________
    wniosek = "NORMALNY" if p > 0.05 else "NIE-NORMALNY"
    print(f"{nazwa:25s} | W={stat:.4f} | p={p:.4f} | {wniosek}")
```

**Pytanie:** Dlaczego kwoty reklamacji raczej nie będą normalne? Jaką to ma konsekwencję dla wyboru testu statystycznego?

### Sprawdzenie 1 ✅

- [ ] `stats.norm.cdf()` i `stats.norm.ppf()` użyte poprawnie — wyniki jak w oczekiwanych
- [ ] Histogram pokazuje słupki danych z nałożoną krzywą normalną
- [ ] QQ-plot narysowany z `stats.probplot(..., plot=axes[1])` — punkty blisko linii
- [ ] Test Shapiro-Wilka: czasy dostawy p > 0.05 (normalny), reklamacje p < 0.05 (nie-normalny)
- [ ] Każdy wykres ma tytuł i etykiety osi

---

## Ćwiczenie 2: T-testy — porównywanie grup (20 min)

**Kontekst biznesowy:** Jesteś analitykiem w firmie e-commerce. Masz trzy różne scenariusze analityczne — każdy wymaga innego rodzaju t-testu.

### 2a. T-test jednorodkowy — czy spełniamy standard?

Dział sprzedaży twierdzi że średni czas realizacji zamówienia wynosi **24 godziny**. Zebrałeś 60 faktycznych czasów realizacji. Czy deklaracja jest zgodna z rzeczywistością?

```python
np.random.seed(42)
czasy_realizacji = np.random.normal(loc=25.8, scale=4.5, size=60)

print(f"Dane: n={len(czasy_realizacji)}, x̄={czasy_realizacji.mean():.2f}h, s={czasy_realizacji.std():.2f}h")
print()

# ZADANIE: Przeprowadź jednorodkowy t-test, testując czy μ = 24
# t_stat, p_val = stats.ttest_1samp(dane, popmean=wartosc_oczekiwana)
t_stat, p_val = _______________________________________________

print(f"H₀: μ = 24h")
print(f"t = {t_stat:.4f}, p = {p_val:.4f}")
print()

# Sformułuj wniosek — uzupełnij:
if p_val < 0.05:
    print("WYNIK: _______________________________________________")
    print("WNIOSEK (dla managera): _______________________________________________")
else:
    print("WYNIK: _______________________________________________")
    print("WNIOSEK (dla managera): _______________________________________________")
```

**Oczekiwany wynik:** p < 0.05 — rzeczywisty czas realizacji istotnie różni się od deklarowanych 24h (jest wyższy).

### 2b. T-test niezależnych grup — A/B test produktu

Testujecie dwa różne warianty opisu produktu (A i B). Mierzycie czas spędzony na stronie (sekundy) przez użytkowników.

```python
np.random.seed(42)
czas_strona_A = np.random.normal(loc=65, scale=20, size=90)   # wersja A
czas_strona_B = np.random.normal(loc=72, scale=22, size=90)   # wersja B

print(f"Wersja A: n={len(czas_strona_A)}, x̄={czas_strona_A.mean():.1f}s, s={czas_strona_A.std():.1f}s")
print(f"Wersja B: n={len(czas_strona_B)}, x̄={czas_strona_B.mean():.1f}s, s={czas_strona_B.std():.1f}s")
print(f"Różnica: {czas_strona_B.mean()-czas_strona_A.mean():.1f}s")
print()

# ZADANIE: Welch's t-test (equal_var=False)
# t_stat, p_val = stats.ttest_ind(grupa1, grupa2, equal_var=False)
t_stat, p_val = _______________________________________________

print(f"H₀: μ_A = μ_B (obie wersje zatrzymują użytkownika tak samo długo)")
print(f"t = {t_stat:.4f}, p = {p_val:.4f}")
print()

# Wizualizacja: boxplot porównawczy
fig, ax = plt.subplots(figsize=(7, 5))
ax.boxplot([czas_strona_A, czas_strona_B],
           labels=['Wersja A', 'Wersja B'],
           patch_artist=True,
           boxprops=dict(facecolor='lightblue'),
           medianprops=dict(color='red', linewidth=2))
ax.set_title(f'Czas na stronie: A vs B\n(t={t_stat:.2f}, p={p_val:.4f})')
ax.set_ylabel('Czas (sekundy)')
ax.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
plt.close()
```

**Pytanie:** Dlaczego używamy `equal_var=False` zamiast `equal_var=True`? Co różni te dwa warianty?

### 2c. Sparowany t-test — efekt kampanii lojalnościowej

Mierzysz wydatki 40 klientów w miesiącu **przed** i **po** wprowadzeniu programu lojalnościowego. To ci sami klienci — dane są powiązane.

```python
np.random.seed(42)
wydatki_przed = np.random.normal(loc=380, scale=80, size=40)
# Program lojalnościowy: wzrost o ~10% z losowością
wydatki_po = wydatki_przed * np.random.normal(1.10, 0.06, size=40)

print(f"Przed: x̄={wydatki_przed.mean():.1f} PLN, s={wydatki_przed.std():.1f}")
print(f"Po:    x̄={wydatki_po.mean():.1f} PLN, s={wydatki_po.std():.1f}")
roznice = wydatki_po - wydatki_przed
print(f"Średnia zmiana: +{roznice.mean():.1f} PLN (+{roznice.mean()/wydatki_przed.mean()*100:.1f}%)")
print()

# ZADANIE: Sparowany t-test
# t_stat, p_val = stats.ttest_rel(przed, po)
t_stat, p_val = _______________________________________________

print(f"t = {t_stat:.4f}, p = {p_val:.6f}")

# Sformułuj wniosek i oblicz roczny efekt:
if p_val < 0.05:
    roczny_efekt = roznice.mean() * 12 * 40
    print(f"\nWNIOSEK: Program lojalnościowy ISTOTNIE zwiększa wydatki klientów.")
    print(f"Roczny efekt (40 klientów): +{roczny_efekt:,.0f} PLN")
```

**Pytanie:** Dlaczego użyliśmy `ttest_rel` zamiast `ttest_ind`? Co byłoby błędem gdybyśmy użyli `ttest_ind` na tych samych danych?

### Sprawdzenie 2 ✅

- [ ] 2a: `ttest_1samp` z `popmean=24` — t > 0, p < 0.05, wniosek: istotna różnica od normy
- [ ] 2b: `ttest_ind(..., equal_var=False)` — boxplot narysowany, tytuł z t i p
- [ ] 2c: `ttest_rel(przed, po)` — p bardzo małe (< 0.001), roczny efekt obliczony
- [ ] Każde zadanie zawiera sformułowanie wniosku w języku managera (nie tylko liczby)

---

## Ćwiczenie 3: Pełna analiza A/B testu (30 min) — samodzielna praca

**Kontekst biznesowy:** Jesteś analitykiem danych w firmie SaaS (oprogramowanie subskrypcyjne). Dział marketingu uruchomił dwie wersje onboardingu nowych użytkowników:
- **Wersja A:** standardowy onboarding — tekst + zrzuty ekranu
- **Wersja B:** interaktywny onboarding — krok po kroku z animacjami

Metryka: **liczba funkcji aktywowanych przez użytkownika w pierwszych 7 dniach** (im więcej, tym lepiej — koreluje z retencją).

Twoje zadanie: przeprowadzić pełną analizę i przygotować raport dla Product Managera.

### Dane

```python
np.random.seed(42)
n_A = 200  # użytkownicy wersji A
n_B = 200  # użytkownicy wersji B

# Wersja A — standardowy onboarding
onboarding_A = np.random.normal(loc=4.2, scale=1.8, size=n_A).clip(0, 10).round(1)

# Wersja B — interaktywny onboarding
onboarding_B = np.random.normal(loc=5.1, scale=1.9, size=n_B).clip(0, 10).round(1)
```

### KROK 1: Statystyki opisowe

Oblicz i wypisz dla obu grup: liczebność, średnią, medianę, odchylenie standardowe, minimum, maksimum.

```python
# Uzupełnij: statystyki dla onboarding_A i onboarding_B
# Użyj: np.mean(), np.median(), np.std(), np.min(), np.max()
# lub pd.Series().describe()

# Twój kod tutaj:
```

### KROK 2: Test normalności

```python
# Sprawdź normalność obu grup testem Shapiro-Wilka
# Podpróba 50 obserwacji (n=200 to za dużo dla Shapiro)
np.random.seed(42)
idx_check = np.random.choice(n_A, 50, replace=False)

# Twój kod tutaj:
# stat_A, p_A = stats.shapiro(onboarding_A[idx_check])
# stat_B, p_B = stats.shapiro(onboarding_B[idx_check])
# Wypisz wyniki i wniosek
```

### KROK 3: Test właściwy

```python
# Przeprowadź Welch's t-test
# Wypisz: t-statystykę, p-wartość, wniosek przy α=0.05

# Twój kod tutaj:
```

### KROK 4: Przedział ufności dla różnicy

```python
# Oblicz 95% CI dla różnicy średnich (B - A)
# Wzór:
#   diff = mean_B - mean_A
#   se_diff = sqrt(var_A/n_A + var_B/n_B)
#   df = n_A + n_B - 2
#   ci = diff ± t_krit(0.975, df) * se_diff

# Twój kod tutaj:
# Wypisz: diff, ci_low, ci_high
```

### KROK 5: Wizualizacja

Stwórz figurę z **3 panelami** (użyj `plt.subplots(1, 3, figsize=(15, 5))`):

1. **Panel lewy:** histogramy obu grup na jednym wykresie (różne kolory, alpha=0.6, density=True)
2. **Panel środkowy:** boxplot porównawczy (A vs B)
3. **Panel prawy:** przedział ufności dla różnicy (errorbar — punkt + wąs, plus linia H₀ na 0)

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)

# Panel 1: Histogramy
# Twój kod tutaj

# Panel 2: Boxplot
# Twój kod tutaj

# Panel 3: Przedział ufności
# Twój kod tutaj

fig.suptitle('A/B Test Onboarding — Raport analityczny', fontsize=13, fontweight='bold')
plt.show()
plt.close()
```

### KROK 6: Wniosek biznesowy (komórka Markdown)

Dodaj do notebooka komórkę Markdown z wnioskiem w następującym formacie:

```markdown
## Wyniki A/B testu — Onboarding [Twoje imię]

**Pytanie:** Czy interaktywny onboarding (wersja B) zwiększa aktywację funkcji?

**Wyniki:**
- Średnia aktywacja A: X.XX funkcji
- Średnia aktywacja B: X.XX funkcji
- Różnica: +X.XX funkcji (X.X%)
- p-wartość: X.XXXX
- 95% CI dla różnicy: [X.XX, X.XX]

**Wniosek:** [Jeden akapit w języku zrozumiałym dla Product Managera — bez wzorów statystycznych]

**Rekomendacja:** [Wdrożyć / nie wdrażać / potrzeba więcej danych — z uzasadnieniem]
```

### Rozszerzenie (dla szybkich)

```python
# 1. Oblicz effect size — Cohen's d
# d = (mean_B - mean_A) / pooled_std
# pooled_std = sqrt((std_A**2 + std_B**2) / 2)
# Interpretacja: d < 0.2 = mały, 0.2-0.5 = średni, > 0.8 = duży efekt

# 2. Symulacja: ile użytkowników potrzeba żeby wykryć ten efekt?
# (power analysis — scipy.stats.power, lub ręczne obliczenie)

# 3. Sprawdź asymetrię (skewness) i kurtozę obu grup
# scipy.stats.skew(), scipy.stats.kurtosis()
```

### Sprawdzenie 3 ✅

- [ ] KROK 1: statystyki opisowe dla obu grup wypisane i czytelne
- [ ] KROK 2: test Shapiro na podpróbie 50 obs. — wynik z wnioskiem
- [ ] KROK 3: `ttest_ind(..., equal_var=False)` — t i p wypisane, wniosek przy α=0.05
- [ ] KROK 4: CI obliczone, diff i granice wypisane
- [ ] KROK 5: 3 panele wizualizacji — histogramy, boxplot, errorbar z CI; tytuł główny
- [ ] KROK 6: komórka Markdown z wnioskiem — po polsku, bez wzorów, zrozumiała dla PM
- [ ] Cały kod wykonuje się bez błędów

---

## Ćwiczenie 4: Chi-kwadrat, przedziały ufności i commit (15 min)

### 4a. Test chi-kwadrat — analiza segmentów klientów

Firma zebrała dane o tym, jaki rodzaj supportu wybierają klienci różnych planów. Czy typ planu wpływa na preferencję kanału wsparcia?

```python
# Tabela kontyngencji: Plan subskrypcji × Kanał wsparcia
# Wiersze: Basic, Pro, Enterprise
# Kolumny: Chat, Email, Telefon

dane_support = np.array([
    [80, 50, 20],    # Basic: preferują chat
    [45, 60, 35],    # Pro: mieszane
    [15, 40, 60],    # Enterprise: preferują telefon
])

plany = ['Basic', 'Pro', 'Enterprise']
kanaly = ['Chat', 'Email', 'Telefon']

# ZADANIE: Przeprowadź test chi-kwadrat
# chi2_stat, p_val, dof, expected = stats.chi2_contingency(tabela)
chi2_stat, p_val, dof, expected = _______________________________________________

print("=== Test chi-kwadrat: Plan × Kanał wsparcia ===")
print(f"\nObserwowane:")
print(pd.DataFrame(dane_support, index=plany, columns=kanaly))
print(f"\nchi² = {chi2_stat:.4f}, df = {dof}, p = {p_val:.6f}")
print()
if p_val < 0.05:
    print("WYNIK: Preferencje kanału wsparcia ZALEŻĄ od planu subskrypcji.")
    print("AKCJA: Dedykowany routing supportu — Basic → Chat, Enterprise → Telefon.")
else:
    print("WYNIK: Brak zależności między planem a preferencją kanału.")

# Wizualizacja: stacked bar chart
fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(plany))
bottom = np.zeros(len(plany))
colors = ['#3498db', '#2ecc71', '#e74c3c']
for i, (kanal, kolor) in enumerate(zip(kanaly, colors)):
    ax.bar(x, dane_support[:, i], bottom=bottom, label=kanal, color=kolor, alpha=0.85, edgecolor='white')
    bottom += dane_support[:, i]
ax.set_xticks(x)
ax.set_xticklabels(plany)
ax.set_title(f'Preferencja kanału wsparcia wg planu\n(χ²={chi2_stat:.1f}, p={p_val:.4f})')
ax.set_xlabel('Plan subskrypcji')
ax.set_ylabel('Liczba zgłoszeń')
ax.legend(title='Kanał', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
plt.close()
```

### 4b. Przedział ufności dla wskaźnika konwersji

```python
np.random.seed(42)

# SCENARIUSZ: Badamy konwersję landing page. 500 odwiedzin, 43 zakupy.
n_odwiedzin = 500
n_zakupow = 43

# Konwersja punktowa
konwersja = n_zakupow / n_odwiedzin
print(f"Konwersja (punkt): {konwersja*100:.2f}%")

# ZADANIE: Oblicz 95% przedział ufności dla konwersji
# Użyj: stats.t.interval(0.95, df=n-1, loc=mean, scale=stats.sem(data))
# LUB dla proporcji: Wald CI
# Wskazówka dla proporcji:
#   se_prop = sqrt(p*(1-p)/n)
#   ci = (p - 1.96*se_prop, p + 1.96*se_prop)

se_prop = np.sqrt(konwersja * (1 - konwersja) / n_odwiedzin)
z_95 = stats.norm.ppf(0.975)
ci_low = konwersja - z_95 * se_prop
ci_high = konwersja + z_95 * se_prop

print(f"95% CI dla konwersji: [{ci_low*100:.2f}%, {ci_high*100:.2f}%]")
print()

# ZADANIE DODATKOWE: Jaka minimalna liczba odwiedzin potrzebna żeby
# szerokość CI < 1 punkt procentowy (0.01)?
# Wzór: n = z² * p*(1-p) / (E/2)² gdzie E = 0.01
# Twój kod tutaj:
```

### 4c. Commit do repozytorium Git

```bash
# W terminalu (poza notebookiem):
cd ~/python2_projekt

# Sprawdź status
git status

# Dodaj plik notebooka
git add lab12_hypothesis_testing.ipynb

# Commit
git commit -m "L12: Testy hipotez — t-test, A/B test, chi-kwadrat, CI — scipy.stats"

# Wypchnij (jeśli masz remote)
git push
```

### 4d. Pytania refleksyjne (zapisz w komórce Markdown w notebooku)

1. Kiedy używasz t-testu, a kiedy chi-kwadrat? Podaj jeden przykład biznesowy dla każdego.
2. Co to jest błąd I rodzaju (false positive) i jak się ma do progu α=0.05? Podaj przykład szkodliwego FP w biznesie.
3. Dlaczego przedział ufności jest bardziej użyteczny od samej p-wartości w raportowaniu wyników A/B testu dla managera?

### Sprawdzenie 4 ✅

- [ ] `chi2_contingency` wywołane poprawnie, chi², df, p wypisane z wnioskiem
- [ ] Stacked bar chart narysowany z legendą i tytułem zawierającym chi² i p
- [ ] Przedział ufności dla konwersji obliczony — dwie liczby w nawiasach `[X.XX%, Y.YY%]`
- [ ] `git log` — widoczny commit z plikiem `lab12_hypothesis_testing.ipynb`
- [ ] Notebook ma komórkę Markdown z odpowiedziami na 3 pytania refleksyjne

---

## Podsumowanie kluczowych komend

```python
# Rozkład normalny
stats.norm.pdf(x, loc=mu, scale=sigma)    # gęstość prawdopodobieństwa
stats.norm.cdf(x, loc=mu, scale=sigma)    # P(X <= x)
stats.norm.ppf(p, loc=mu, scale=sigma)    # kwantyl (odwrotność CDF)

# Testy normalności
stat, p = stats.shapiro(dane)             # Shapiro-Wilk (n < 5000)
stats.probplot(dane, dist='norm', plot=ax) # QQ-plot wizualny

# T-testy
t, p = stats.ttest_1samp(dane, popmean=mu0)           # vs wartość oczekiwana
t, p = stats.ttest_ind(grA, grB, equal_var=False)      # 2 niezależne grupy (Welch)
t, p = stats.ttest_rel(przed, po)                      # 2 powiązane pomiary (sparowany)

# Test chi-kwadrat
chi2, p, dof, expected = stats.chi2_contingency(tabela) # tabela = np.array 2D

# Przedziały ufności
se = stats.sem(dane)                                    # błąd standardowy
ci = stats.t.interval(0.95, df=n-1, loc=mean, scale=se) # 95% CI dla średniej

# Wzorzec pełnej analizy
np.random.seed(42)                        # zawsze!
stat, p = stats.shapiro(dane[:200])       # normalność (podpróba)
t, p = stats.ttest_ind(A, B, equal_var=False)  # test
# interpretuj → wniosek biznesowy
```

---

## Jeśli utkniesz

| Problem | Rozwiązanie |
|---------|-------------|
| Nie wiem którego t-testu użyć | Te same osoby przed/po? → `ttest_rel`. Dwie różne grupy? → `ttest_ind`. Porównanie ze stałą? → `ttest_1samp` |
| `ttest_ind` daje inny wynik niż kolega | Sprawdź `equal_var=False` (Welch). Domyślnie `True` (Student) — to inny test! |
| p-wartość = 0.000... | Wyświetl w notacji naukowej: `f"p = {p:.2e}"`. Np. p = 3.45e-08 |
| Shapiro-Wilk: "p-value may be poorly conditioned" | Dla n > 5000 użyj podpróby: `stats.shapiro(dane[:500])` |
| QQ-plot nie rysuje na axes | Użyj `plot=ax`: `stats.probplot(dane, dist='norm', plot=ax)` (nie `plot=plt`!) |
| `chi2_contingency` — zero w tabeli | Połącz rzadkie kategorie lub sprawdź dane |
| Przedział ufności — `stats.t.interval()` | `stats.t.interval(0.95, df=n-1, loc=mean, scale=se)` — pierwszy arg to confidence level |
