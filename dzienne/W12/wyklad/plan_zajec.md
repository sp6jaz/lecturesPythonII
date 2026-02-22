# W12 Wykład — Plan zajęć dla prowadzącego

## Temat: Statystyka — rozkłady i testy hipotez

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z scipy/numpy/matplotlib/seaborn
- **Przed wykładem:** otwórz `hypothesis_demo.ipynb`
- **Kluczowe hasło:** "Statystyka to narzędzie decyzyjne — nie matematyka dla matematyki"

### Efekty uczenia się (Bloom poziom 3-4)
Po tym wykładzie osoba studiująca:
1. **Stosuje** `scipy.stats.norm` do obliczania prawdopodobieństw i kwantyli rozkładu normalnego oraz interpretuje PDF i CDF w kontekście biznesowym (Bloom 3)
2. **Analizuje** dane pod kątem normalności używając wykresu QQ-plot i testu Shapiro-Wilka, interpretując wynik w kategoriach praktycznych (Bloom 4)
3. **Stosuje** jednorodkowy t-test, niezależny t-test dwóch grup i sparowany t-test do testowania hipotez, interpretując p-wartość w kontekście decyzji biznesowej (Bloom 3)
4. **Projektuje** pełną analizę A/B testu kampanii marketingowej: od sformułowania hipotez przez wykonanie testu po sformułowanie wniosku dla decydenta (Bloom 4)
5. **Interpretuje** wyniki testu chi-kwadrat dla danych kategorycznych i oblicza przedziały ufności, podając wnioski w języku zrozumiałym dla niestatystyka (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W11 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | Przejście od statystyki opisowej do wnioskowania: "czy możemy to UDOWODNIĆ?" | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Rozkład normalny — scipy.stats.norm, PDF, CDF, QQ-plot, Shapiro-Wilk | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | T-test — jednorodkowy, niezależny, sparowany; interpretacja p-wartości | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | A/B testing w biznesie — praktyczny przykład kampanii marketingowej | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Test chi-kwadrat dla danych kategorycznych, przedziały ufności | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | A/B test na danych marketingowych — studenci sami przeprowadzają | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Zapowiedź W13: scikit-learn, Plotly | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W11)

> "Pięć pytań z zeszłego tygodnia — 3 minuty, kartka lub Mentimeter."

**[Użyj quiz_w12.md — pytania 1 i 2 z W11]**

> "Odpowiedzi omówimy razem. Kto miał 5/5? Brawo. Kto miał 4? Dobra robota. Poniżej 4 — przejrzyj notatki z W11, bo dziś budujemy na tamtym fundamencie."

---

### 0:05-0:10 — WPROWADZENIE

> "Zeszły tydzień: statystyka opisowa. Średnia, mediana, odchylenie standardowe. Narysowaliście histogramy, boxploty. Umiecie opisać dane — powiedzieć 'jak jest'. Ale to nie wystarczy w biznesie."

> "W biznesie zawsze pada pytanie: *czy to jest prawdziwa różnica, czy przypadek?* Przykład: wdrożyliście nową stronę sklepu internetowego. Konwersja z wersji A wyniosła 3.2%, z wersji B — 3.8%. Czy wersja B jest NAPRAWDĘ lepsza, czy to tylko szum statystyczny? Odpowiedź na to pytanie kosztuje Waszą firmę pieniądze."

> "Albo: mierzycie satysfakcję klientów przed i po szkoleniu obsługi. Średnia wzrosła z 7.2 do 7.9. Czy szkolenie NAPRAWDĘ pomogło, czy to efekt sezonowości? Inwestycja 50 000 zł w szkolenie — czy była warta?"

> "Testy hipotez to narzędzie, które mówi Wam: *tak, ta różnica jest statystycznie istotna* — lub *nie, to mógł być przypadek*. Nie magia, nie trudna matematyka. W Pythonie: trzy linijki kodu i odpowiedź."

> "Dzisiaj nauczycie się tych trzech linijek. I co ważniejsze — nauczycie się interpretować wynik. Bo liczba p=0.032 nic Wam nie powie, jeśli nie wiecie co z nią zrobić."

**[Wyświetl na projektorze — kluczowe pojęcia]**

```
H₀ (hipoteza zerowa)  — "nie ma różnicy", "efekt nie istnieje"
H₁ (hipoteza robocza) — "jest różnica", "wersja B jest lepsza"
p-wartość             — prawdopodobieństwo, że H₀ jest prawdą
α = 0.05              — próg decyzyjny (5%)

Jeśli p < 0.05 → odrzucamy H₀ → różnica jest statystycznie istotna
Jeśli p ≥ 0.05 → brak podstaw do odrzucenia H₀ → brak dowodów na różnicę
```

> "Otwieramy notebook. Zaczynamy od rozkładu normalnego — fundamentu całej statystyki."

---

### 0:10-0:30 — MATERIAŁ 1: Rozkład normalny i testy normalności (20 min)

**[Otwórz notebook — komórka 1: setup]**

```python
%matplotlib inline
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(42)
sns.set_theme(style='whitegrid', palette='muted')
print("Środowisko gotowe.")
```

> "Importujemy `scipy.stats` — to jest nasza biblioteka statystyczna. Zawiera ponad 100 rozkładów i dziesiątki testów. Dzisiaj użyjemy kilku najważniejszych."

> "`np.random.seed(42)` — zawsze ustawiamy ziarno losowości. Dzięki temu Wasze wyniki będą identyczne z moimi. Ważne podczas nauki i debugowania."

**[Komórka 2 — rozkład normalny: PDF i CDF]**

```python
# Rozkład normalny — scipy.stats.norm
# Parametry: loc=średnia, scale=odchylenie standardowe

mu = 170      # średni wzrost dorosłego Polaka (cm)
sigma = 8     # odchylenie standardowe

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 300)

# PDF — funkcja gęstości prawdopodobieństwa
pdf = stats.norm.pdf(x, loc=mu, scale=sigma)

# CDF — dystrybuanta (skumulowana)
cdf = stats.norm.cdf(x, loc=mu, scale=sigma)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# PDF
axes[0].plot(x, pdf, 'b-', linewidth=2.5, label='PDF')
axes[0].axvline(mu, color='red', linestyle='--', linewidth=1.5, label=f'μ = {mu}')
axes[0].fill_between(
    x,
    pdf,
    where=(x >= mu - sigma) & (x <= mu + sigma),
    alpha=0.3, color='blue', label='68% (±1σ)'
)
axes[0].fill_between(
    x,
    pdf,
    where=(x >= mu - 2*sigma) & (x <= mu + 2*sigma),
    alpha=0.15, color='green', label='95% (±2σ)'
)
axes[0].set_title('PDF — funkcja gęstości prawdopodobieństwa\n(wzrost dorosłych Polaków)', fontsize=11)
axes[0].set_xlabel('Wzrost (cm)')
axes[0].set_ylabel('Gęstość prawdopodobieństwa')
axes[0].legend(fontsize=9)

# CDF
axes[1].plot(x, cdf, 'g-', linewidth=2.5)
axes[1].axhline(0.5, color='red', linestyle='--', linewidth=1.2, label='50. percentyl (mediana)')
axes[1].axhline(0.95, color='orange', linestyle=':', linewidth=1.2, label='95. percentyl')
axes[1].set_title('CDF — dystrybuanta\n(wzrost dorosłych Polaków)', fontsize=11)
axes[1].set_xlabel('Wzrost (cm)')
axes[1].set_ylabel('Skumulowane prawdopodobieństwo')
axes[1].legend(fontsize=9)

plt.tight_layout()
plt.show()
plt.close()
```

> "Dwa wykresy, dwa punkty widzenia na ten sam rozkład."

> "PDF — funkcja gęstości. Pozioma oś: wzrost. Pionowa: nie jest to bezpośrednio prawdopodobieństwo, ale gęstość. Pole pod krzywą między dwoma wartościami = prawdopodobieństwo. Zaznaczone obszary: niebieskie ±1σ — 68% populacji mieści się w tym zakresie. Zielone ±2σ — 95% populacji. Reguła 68-95-99.7 — zapamiętajcie ją."

> "CDF — dystrybuanta. Dla danej wartości X mówi: jaki % populacji ma wartość MNIEJSZĄ lub równą X. Czerwona linia: 50% ma wzrost mniejszy niż 170 cm. Pomarańczowa: 95% ma wzrost mniejszy niż ~183 cm. Pytacie managera: 'ile osób w Polsce nosi koszule powyżej L?' Odpowiedź pochodzi z CDF."

**[Komórka 3 — praktyczne obliczenia]**

```python
# Praktyczne pytania biznesowe — scipy.stats.norm

mu, sigma = 170, 8   # wzrost

# PYTANIE 1: jakie % populacji ma wzrost > 185 cm?
prob_above_185 = 1 - stats.norm.cdf(185, loc=mu, scale=sigma)
print(f"Wzrost > 185 cm: {prob_above_185*100:.1f}% populacji")

# PYTANIE 2: jaka jest granica górnych 10%? (np. dla produkcji ubrań XL/XXL)
percentyl_90 = stats.norm.ppf(0.90, loc=mu, scale=sigma)
print(f"Górne 10% populacji ma wzrost > {percentyl_90:.1f} cm")

# PYTANIE 3: ile % populacji mieści się między 160 a 180 cm?
prob_160_180 = stats.norm.cdf(180, loc=mu, scale=sigma) - stats.norm.cdf(160, loc=mu, scale=sigma)
print(f"Wzrost 160–180 cm: {prob_160_180*100:.1f}% populacji")

# PYTANIE 4 — e-commerce: czas ładowania strony ~ N(2.5s, 0.4s)
mu_load, sigma_load = 2.5, 0.4
prob_slow = 1 - stats.norm.cdf(3.0, loc=mu_load, scale=sigma_load)
print(f"\nCzas ładowania > 3s (odejście użytkownika): {prob_slow*100:.1f}% sesji")
sla_99 = stats.norm.ppf(0.99, loc=mu_load, scale=sigma_load)
print(f"SLA 99%: 99% stron ładuje się poniżej {sla_99:.2f}s")
```

> "Cztery praktyczne pytania — cztery linijki kodu. Rozłóżmy je:"

> "`stats.norm.cdf(X, loc=μ, scale=σ)` — zwraca prawdopodobieństwo, że wartość jest MNIEJSZA od X. Chcemy większe? Odejmujemy od 1."

> "`stats.norm.ppf(p, loc=μ, scale=σ)` — odwrotność CDF. Podajemy prawdopodobieństwo, dostajemy wartość. 'Ppf' to percent point function — czyli kwantyl. Chcemy wiedzieć jaka wartość oddziela górne 10%? Wywołujemy z p=0.9."

> "Przykład z e-commerce: firmę interesuje SLA — Service Level Agreement. Obiecują klientom że 99% stron załaduje się szybciej niż X sekund. Obliczamy X. Trzy linijki Pythona, konkrety dla inżynierów i biznesu."

**[Komórka 4 — generowanie próbek i histogram]**

```python
# Generowanie danych i weryfikacja rozkładu

np.random.seed(42)

# Symulacja: wzrost 200 losowych klientów sklepu odzieżowego
wzrost_klientow = np.random.normal(loc=170, scale=8, size=200)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Histogram vs krzywa teoretyczna
axes[0].hist(wzrost_klientow, bins=25, density=True,
             alpha=0.7, color='steelblue', edgecolor='white', label='Dane (n=200)')
x_range = np.linspace(wzrost_klientow.min(), wzrost_klientow.max(), 200)
axes[0].plot(x_range,
             stats.norm.pdf(x_range, loc=wzrost_klientow.mean(), scale=wzrost_klientow.std()),
             'r-', linewidth=2.5, label=f'N(μ={wzrost_klientow.mean():.1f}, σ={wzrost_klientow.std():.1f})')
axes[0].set_title('Histogram vs rozkład normalny\n(wzrost klientów)', fontsize=11)
axes[0].set_xlabel('Wzrost (cm)')
axes[0].set_ylabel('Gęstość')
axes[0].legend()

# QQ-plot — test wizualny normalności
stats.probplot(wzrost_klientow, dist='norm', plot=axes[1])
axes[1].set_title('QQ-plot — czy dane są normalne?\n(punkty blisko linii = normalność)', fontsize=11)
axes[1].get_lines()[1].set_color('red')
axes[1].get_lines()[1].set_linewidth(2)

plt.tight_layout()
plt.show()
plt.close()
```

> "Dwa wykresy diagnostyczne. Lewy — histogram próbki z nałożoną krzywą normalną. Gdy dane są naprawdę normalne, słupki histogramu kładą się blisko krzywej. Prawy — QQ-plot."

> "QQ-plot to mój ulubiony test normalności. Na osi X: kwantyle teoretycznego rozkładu normalnego. Na osi Y: kwantyle Waszych danych. Jeśli dane są normalne — punkty leżą blisko czerwonej linii prostej. Im bardziej się odchylają — tym bardziej dane odbiegają od normalności. Odchylenia na końcach (tzw. 'heavy tails') — dane mają więcej wartości ekstremalnych niż normalny rozkład. To ważne przy analizie finansowej."

**[Komórka 5 — test Shapiro-Wilka]**

```python
# Test Shapiro-Wilka — formalny test normalności
np.random.seed(42)

# Dane 1: naprawdę normalne
dane_normalne = np.random.normal(170, 8, 100)

# Dane 2: prawicowo asymetryczne (np. zarobki, ceny)
dane_asymetryczne = np.random.exponential(scale=20, size=100) + 5

# Dane 3: realne czasy obsługi klienta (lekko asymetryczne)
czasy_obslugi = np.abs(np.random.normal(5, 2, 100)) + 1

for nazwa, dane in [
    ('Dane normalne (wzrost)', dane_normalne),
    ('Dane asymetryczne (zarobki)', dane_asymetryczne),
    ('Czasy obsługi (realne)', czasy_obslugi)
]:
    stat, p = stats.shapiro(dane)
    normalnosc = "NORMALNY ✓" if p > 0.05 else "NIE-normalny ✗"
    print(f"{nazwa:40s} | W={stat:.4f} | p={p:.4f} | {normalnosc}")
```

> "Test Shapiro-Wilka — formalny test normalności. Hipoteza zerowa H₀: dane pochodzą z rozkładu normalnego. Wyniki:"

> "Pierwsze dane: p=0.98 — wysokie. Nie odrzucamy H₀. Dane są normalne. Seond dane: p bardzo małe (zwykle < 0.001) — odrzucamy H₀. Zarobki prawie nigdy nie są normalne — dlatego do analizy wynagrodzeń używamy mediany, nie średniej. Trzecie: realne dane — p gdzieś w środku, decyzja kontekstowa."

> "Ważna uwaga praktyczna: test Shapiro-Wilka jest bardzo czuły na duże próby. Przy n > 5000 prawie zawsze zwróci p < 0.05, nawet gdy odchylenie od normalności jest marginalne. Zawsze patrzcie na QQ-plot — wizualna ocena jest równie ważna jak liczba."

**[Komórka 6 — porównanie: normalne vs nie-normalne]**

```python
# Wizualizacja: rozkłady normalne vs nie-normalne
np.random.seed(42)

fig, axes = plt.subplots(2, 3, figsize=(14, 8), constrained_layout=True)

datasets = [
    ('Wzrost klientów\n(normalny)', np.random.normal(170, 8, 200)),
    ('Zarobki\n(asymetryczny)', np.random.exponential(20, 200) * 1000 + 2000),
    ('Opóźnienia dostaw\n(długi ogon)', np.random.gamma(2, 3, 200)),
]

for col, (tytul, dane) in enumerate(datasets):
    # Histogram + KDE
    axes[0, col].hist(dane, bins=25, density=True, alpha=0.6,
                      color='steelblue', edgecolor='white')
    x_k = np.linspace(dane.min(), dane.max(), 200)
    kde = stats.gaussian_kde(dane)
    axes[0, col].plot(x_k, kde(x_k), 'r-', linewidth=2)
    stat, p = stats.shapiro(dane)
    axes[0, col].set_title(f'{tytul}\np={p:.4f}', fontsize=10)
    axes[0, col].set_ylabel('Gęstość' if col == 0 else '')

    # QQ-plot
    stats.probplot(dane, dist='norm', plot=axes[1, col])
    axes[1, col].set_title('')
    axes[1, col].set_xlabel('Kwantyle teoretyczne')
    if col > 0:
        axes[1, col].set_ylabel('')

axes[0, 0].set_ylabel('Gęstość')
axes[1, 0].set_ylabel('Kwantyle empiryczne')

fig.suptitle('Rozkłady: normalny vs asymetryczny — histogram i QQ-plot', fontsize=13, fontweight='bold')
plt.show()
plt.close()
```

> "Trzy typy rozkładów — trzy pary wykresów. Górny rząd: histogram. Dolny: QQ-plot. Wzrost — typowy rozkład normalny — QQ-plot prawie idealny. Zarobki — silna asymetria prawostronno — QQ-plot zakrzywiony w górę. Opóźnienia dostaw — rozkład gamma, 'gruby ogon' po prawej — QQ-plot charakterystycznie odchyla na końcach."

> "Dlaczego to ważne biznesowo? Bo wiele testów statystycznych (w tym t-test) zakłada normalność. Jeśli dane nie są normalne — musimy użyć innych testów lub transformacji. Zanim zrobicie test — sprawdzajcie QQ-plot. Dobre nawyki."

---

### 0:30-0:45 — MATERIAŁ 2: T-test — testowanie hipotez (15 min)

> "Teraz serce dzisiejszego wykładu. T-test. Trzy wersje — trzy różne pytania biznesowe."

**[Komórka 7 — t-test jednorodkowy]**

```python
# T-test jednorodkowy — czy średnia próby różni się od założonej wartości?
# SCENARIUSZ: Dział QA twierdzi że czas obsługi klienta wynosi 5 minut.
# Mierzymy 50 faktycznych obsług. Czy QA ma rację?

np.random.seed(42)
czasy_obslugi = np.random.normal(loc=5.4, scale=1.2, size=50)  # realna średnia 5.4 min

print("=== T-test jednorodkowy ===")
print(f"Hipoteza zerowa H₀: μ = 5.0 min (QA twierdzi)")
print(f"Hipoteza robocza H₁: μ ≠ 5.0 min")
print()
print(f"Dane: n={len(czasy_obslugi)}, x̄={czasy_obslugi.mean():.2f} min, s={czasy_obslugi.std():.2f} min")
print()

# Test
t_stat, p_val = stats.ttest_1samp(czasy_obslugi, popmean=5.0)

print(f"Statystyka t  = {t_stat:.4f}")
print(f"p-wartość     = {p_val:.4f}")
print()
if p_val < 0.05:
    print("WYNIK: p < 0.05 → Odrzucamy H₀")
    print("WNIOSEK: Średni czas obsługi STATYSTYCZNIE ISTOTNIE różni się od 5 minut.")
    print(f"Faktyczna średnia ({czasy_obslugi.mean():.1f} min) jest wyższa niż deklarowane 5 min.")
    print("Akcja: rozmowa z działem QA, rewizja normy lub usprawnienie procesu.")
else:
    print("WYNIK: p ≥ 0.05 → Brak podstaw do odrzucenia H₀")
    print("WNIOSEK: Brak statystycznych dowodów, że czas obsługi różni się od 5 min.")
```

> "T-test jednorodkowy. Mamy jedną próbkę danych i porównujemy jej średnią z pewną oczekiwaną wartością. Parametr `popmean` — to właśnie ta oczekiwana wartość."

> "Wynik: p < 0.05. Co to znaczy? Gdyby naprawdę czas obsługi wynosił 5 minut (H₀ prawdziwa), to szansa na uzyskanie takiej próbki jak nasza (z x̄=5.4) wynosi mniej niż 5%. To jest wystarczająco mało, żeby powiedzieć: H₀ nie jest wiarygodna. Różnica jest ISTOTNA STATYSTYCZNIE."

> "Kluczowe słowa: 'istotna statystycznie' NIE OZNACZA 'ważna biznesowo'. Różnica 0.4 minuty może być istotna statystycznie, ale 24 sekundy na obsługę klienta mogą być nieistotne dla biznesu. To odróżnia dobrego analityka."

**[Komórka 8 — t-test niezależnych grup]**

```python
# T-test niezależnych dwóch grup — czy dwie niezależne grupy mają różne średnie?
# SCENARIUSZ: A/B test strony produktowej. Grupa A: stara strona. Grupa B: nowa.
# Mierzymy wartość koszyka (PLN).

np.random.seed(42)
koszyk_A = np.random.normal(loc=250, scale=60, size=80)   # stara strona
koszyk_B = np.random.normal(loc=270, scale=65, size=80)   # nowa strona

print("=== T-test niezależnych grup (A/B test koszyka) ===")
print(f"H₀: μ_A = μ_B (nowa strona nie zmienia wartości koszyka)")
print(f"H₁: μ_A ≠ μ_B (nowa strona zmienia wartość koszyka)")
print()
print(f"Grupa A (stara): n={len(koszyk_A)}, x̄={koszyk_A.mean():.2f} PLN, s={koszyk_A.std():.2f} PLN")
print(f"Grupa B (nowa):  n={len(koszyk_B)}, x̄={koszyk_B.mean():.2f} PLN, s={koszyk_B.std():.2f} PLN")
print(f"Różnica średnich: {koszyk_B.mean() - koszyk_A.mean():.2f} PLN")
print()

# equal_var=False — Welch's t-test (nie zakłada równości wariancji — bezpieczniejszy)
t_stat, p_val = stats.ttest_ind(koszyk_A, koszyk_B, equal_var=False)

print(f"Statystyka t  = {t_stat:.4f}")
print(f"p-wartość     = {p_val:.4f}")
print()
alpha = 0.05
if p_val < alpha:
    print(f"WYNIK: p={p_val:.3f} < α={alpha} → Odrzucamy H₀")
    print("WNIOSEK: Nowa strona statystycznie istotnie zmienia wartość koszyka.")
    roznica = koszyk_B.mean() - koszyk_A.mean()
    print(f"Wzrost średniego koszyka: +{roznica:.0f} PLN ({roznica/koszyk_A.mean()*100:.1f}%)")
else:
    print(f"WYNIK: p={p_val:.3f} ≥ α={alpha} → Brak podstaw do odrzucenia H₀")
    print("WNIOSEK: Brak statystycznych dowodów na różnicę między wersjami stron.")

# Wizualizacja
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Histogramy
axes[0].hist(koszyk_A, bins=20, alpha=0.6, color='steelblue', density=True, label=f'Wersja A (x̄={koszyk_A.mean():.0f} PLN)')
axes[0].hist(koszyk_B, bins=20, alpha=0.6, color='tomato', density=True, label=f'Wersja B (x̄={koszyk_B.mean():.0f} PLN)')
axes[0].axvline(koszyk_A.mean(), color='steelblue', linestyle='--', linewidth=2)
axes[0].axvline(koszyk_B.mean(), color='tomato', linestyle='--', linewidth=2)
axes[0].set_title(f'Rozkład wartości koszyka\np={p_val:.4f} — {"istotna różnica" if p_val < 0.05 else "brak istotnej różnicy"}', fontsize=11)
axes[0].set_xlabel('Wartość koszyka (PLN)')
axes[0].set_ylabel('Gęstość')
axes[0].legend()

# Boxplot
axes[1].boxplot([koszyk_A, koszyk_B], labels=['Wersja A', 'Wersja B'],
                patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='steelblue'),
                medianprops=dict(color='red', linewidth=2))
axes[1].set_title('Boxplot — porównanie grup', fontsize=11)
axes[1].set_ylabel('Wartość koszyka (PLN)')
axes[1].grid(True, axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
plt.close()
```

> "T-test dla dwóch niezależnych grup. Parametr `equal_var=False` — to jest ważne. Domyślnie t-test zakłada że obie grupy mają taką samą wariancję (test Studenta). Welch's t-test (equal_var=False) nie zakłada tego. Prawie zawsze używajcie Welcha — jest bezpieczniejszy."

> "Interpretacja: p < 0.05, odrzucamy H₀. Nowa strona ISTOTNIE zmienia wartość koszyka — wzrost o ~20 PLN, czyli ~8%. Teraz manager pyta: 'czy wdrażamy na wszystkich użytkowników?' To jest decyzja biznesowa — do której potrzebujecie więcej danych: ile kosztowała zmiana strony, czy ten wzrost jest trwały, czy próbka była reprezentatywna."

**[Komórka 9 — sparowany t-test]**

```python
# Sparowany t-test — te same osoby/elementy, dwa pomiary
# SCENARIUSZ: Szkolenie sprzedażowe. Mierzymy sprzedaż 30 handlowców
# przed i po szkoleniu. Czy szkolenie pomogło?

np.random.seed(42)
sprzedaz_przed = np.random.normal(loc=42000, scale=8000, size=30)  # PLN/miesiąc
# Szkolenie dało efekt: +15% z losowym szumem
sprzedaz_po = sprzedaz_przed * np.random.normal(1.15, 0.05, 30)

print("=== Sparowany t-test (szkolenie sprzedażowe) ===")
print(f"H₀: μ_różnica = 0 (szkolenie nie zmienia sprzedaży)")
print(f"H₁: μ_różnica ≠ 0 (szkolenie zmienia sprzedaży)")
print()
print(f"Przed: x̄ = {sprzedaz_przed.mean():.0f} PLN/mies, s = {sprzedaz_przed.std():.0f} PLN")
print(f"Po:    x̄ = {sprzedaz_po.mean():.0f} PLN/mies, s = {sprzedaz_po.std():.0f} PLN")
roznice = sprzedaz_po - sprzedaz_przed
print(f"Średnia zmiana: +{roznice.mean():.0f} PLN/mies ({roznice.mean()/sprzedaz_przed.mean()*100:.1f}%)")
print()

t_stat, p_val = stats.ttest_rel(sprzedaz_przed, sprzedaz_po)

print(f"Statystyka t = {t_stat:.4f}")
print(f"p-wartość   = {p_val:.6f}")
print()
if p_val < 0.05:
    print("WYNIK: p < 0.05 → Odrzucamy H₀")
    print("WNIOSEK: Szkolenie STATYSTYCZNIE ISTOTNIE zwiększyło sprzedaż.")
    roczny_wzrost = roznice.mean() * 12 * 30
    print(f"Roczny wzrost sprzedaży (30 handlowców): +{roczny_wzrost:,.0f} PLN")
```

> "Sparowany t-test — gdy mamy tych samych 30 ludzi zmierzonych dwukrotnie. To NIE są dwie niezależne grupy. Każdy handlowiec ma swoje 'przed' i 'po'. Dlatego liczymy różnice dla każdej pary i testujemy czy te różnice różnią się od zera. `stats.ttest_rel()` — 'rel' od 'related', powiązane."

> "Sparowany test jest MOCNIEJSZY niż test niezależnych grup na tych samych danych, bo eliminuje zmienność między osobami. Każdy handlowiec ma inną naturalną skuteczność — sparowany test to 'wyzeruje'. Efekt szkolenia widać wyraźniej."

> "Wynik: p bardzo małe. Szkolenie faktycznie pomogło. Policzmy ROI: wzrost sprzedaży 30 handlowców przez rok. Teraz zarząd ma liczbę do porównania z kosztem szkolenia."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: A/B testing w biznesie (20 min)

> "Po przerwie: kompletna analiza A/B testu. Nie tylko test statystyczny, ale cały workflow — od pytania do decyzji."

> "A/B testing — to jest chleb powszedni każdej firmy technologicznej. Netflix testuje miniatury filmów. Amazon testuje układ koszyka. Booking.com testuje kolory przycisków. Każda taka decyzja opiera się na t-teście lub jego wariancie."

**[Komórka 10 — pełna analiza A/B testu]**

```python
# SCENARIUSZ: Sklep internetowy z elektroniką
# Kampania e-mailowa: wersja A = standardowy email, wersja B = email z personalizacją
# Metryka: wartość zakupu po kliknięciu (PLN)
# Pytanie: Czy personalizacja emaila zwiększa wartość zakupu?

np.random.seed(42)
n_A = 150  # użytkownicy wersji A
n_B = 150  # użytkownicy wersji B

# Wersja A: standardowy email
# Wartość koszyka — normalna z ogonem (realistyczny rozkład)
kampania_A = np.concatenate([
    np.random.normal(320, 80, 130),    # większość klientów
    np.random.normal(800, 100, 20)     # klienci premium (20 osób)
])
np.random.shuffle(kampania_A)

# Wersja B: personalizowany email — +12% wzrost
kampania_B = np.concatenate([
    np.random.normal(360, 85, 130),    # większość — wyższy koszyk
    np.random.normal(850, 100, 20)     # klienci premium
])
np.random.shuffle(kampania_B)

# --- Krok 1: Eksploracja ---
print("=" * 55)
print("ANALIZA A/B TESTU — Kampania e-mailowa")
print("=" * 55)
print()
print("KROK 1: Statystyki opisowe")
print(f"  Wersja A: n={n_A}, x̄={kampania_A.mean():.2f} PLN, "
      f"mediana={np.median(kampania_A):.2f}, s={kampania_A.std():.2f}")
print(f"  Wersja B: n={n_B}, x̄={kampania_B.mean():.2f} PLN, "
      f"mediana={np.median(kampania_B):.2f}, s={kampania_B.std():.2f}")
print(f"  Różnica średnich: {kampania_B.mean() - kampania_A.mean():.2f} PLN "
      f"({(kampania_B.mean()/kampania_A.mean()-1)*100:.1f}%)")
print()

# --- Krok 2: Sprawdzenie normalności ---
print("KROK 2: Test normalności (Shapiro-Wilk, podpróba 50 obs.)")
# Shapiro najlepiej dla n<50; użyjemy podpróby
idx = np.random.choice(len(kampania_A), 50, replace=False)
stat_A, p_A = stats.shapiro(kampania_A[idx])
stat_B, p_B = stats.shapiro(kampania_B[idx])
print(f"  Wersja A: W={stat_A:.4f}, p={p_A:.4f} {'(normalny)' if p_A > 0.05 else '(nie-normalny)'}")
print(f"  Wersja B: W={stat_B:.4f}, p={p_B:.4f} {'(normalny)' if p_B > 0.05 else '(nie-normalny)'}")
print()

# --- Krok 3: Test właściwy ---
print("KROK 3: Welch's t-test (dwustronny)")
t_stat, p_val = stats.ttest_ind(kampania_A, kampania_B, equal_var=False)
print(f"  t = {t_stat:.4f}, p = {p_val:.4f}")
print()

# --- Krok 4: Przedział ufności dla różnicy ---
n1, n2 = len(kampania_A), len(kampania_B)
mean_diff = kampania_B.mean() - kampania_A.mean()
se_diff = np.sqrt(kampania_A.var()/n1 + kampania_B.var()/n2)
df = n1 + n2 - 2
ci_low = mean_diff - stats.t.ppf(0.975, df) * se_diff
ci_high = mean_diff + stats.t.ppf(0.975, df) * se_diff
print(f"KROK 4: Przedział ufności 95% dla różnicy (B–A):")
print(f"  [{ci_low:.2f}, {ci_high:.2f}] PLN")
print()

# --- Krok 5: Wniosek biznesowy ---
print("KROK 5: WNIOSEK BIZNESOWY")
print("-" * 45)
if p_val < 0.05 and ci_low > 0:
    print(f"  Personalizowany email ISTOTNIE zwiększa wartość zakupu.")
    print(f"  Szacowany wzrost: {mean_diff:.0f} PLN/klienta (95% CI: [{ci_low:.0f}, {ci_high:.0f}] PLN).")
    print(f"  Przy 10 000 klientach/mies. → dodatkowy przychód: ~{mean_diff*10000:,.0f} PLN/mies.")
    print(f"  REKOMENDACJA: Wdrożyć wersję B jako standard.")
else:
    print(f"  Brak statystycznych dowodów na przewagę personalizacji.")
    print(f"  REKOMENDACJA: Nie wdrażać, rozważyć inne optymalizacje.")
```

> "Pięć kroków pełnej analizy A/B. Zapamiętajcie ten schemat — przyda się w każdej pracy z danymi."

> "Krok 1: statystyki opisowe. Zawsze zaczynajcie od PATRZENIA na dane. Krok 2: sprawdzenie założeń testu. Krok 3: test. Krok 4: przedział ufności. To jest kluczowe — p-wartość mówi 'jest istotne', ale przedział ufności mówi 'o ile'. Krok 5: wniosek w języku biznesowym — nie 'p=0.032', ale 'dodatkowy przychód 350 000 PLN miesięcznie'."

**[Komórka 11 — wizualizacja wyników A/B]**

```python
# Wizualizacja A/B testu
fig, axes = plt.subplots(2, 2, figsize=(13, 9), constrained_layout=True)

# Panel 1: Histogramy
axes[0, 0].hist(kampania_A, bins=25, alpha=0.6, color='steelblue', density=True,
                label=f'Wersja A (x̄={kampania_A.mean():.0f} PLN)')
axes[0, 0].hist(kampania_B, bins=25, alpha=0.6, color='tomato', density=True,
                label=f'Wersja B (x̄={kampania_B.mean():.0f} PLN)')
axes[0, 0].axvline(kampania_A.mean(), color='steelblue', linestyle='--', lw=2)
axes[0, 0].axvline(kampania_B.mean(), color='tomato', linestyle='--', lw=2)
axes[0, 0].set_title(f'Rozkład wartości zakupu\n(t={t_stat:.2f}, p={p_val:.4f})', fontsize=11)
axes[0, 0].set_xlabel('Wartość zakupu (PLN)')
axes[0, 0].set_ylabel('Gęstość')
axes[0, 0].legend(fontsize=9)

# Panel 2: Boxplot
bp = axes[0, 1].boxplot([kampania_A, kampania_B],
                         labels=['Wersja A\n(standardowa)', 'Wersja B\n(personalizowana)'],
                         patch_artist=True,
                         boxprops=dict(facecolor='lightblue'),
                         medianprops=dict(color='red', linewidth=2))
bp['boxes'][1].set_facecolor('lightsalmon')
axes[0, 1].set_title('Boxplot — porównanie rozkładów', fontsize=11)
axes[0, 1].set_ylabel('Wartość zakupu (PLN)')
axes[0, 1].grid(True, axis='y', alpha=0.3)

# Panel 3: Przedział ufności dla różnicy
diff_point = kampania_B.mean() - kampania_A.mean()
axes[1, 0].errorbar(
    x=['Różnica B–A\n(personalizacja vs standard)'],
    y=[diff_point],
    yerr=[[diff_point - ci_low], [ci_high - diff_point]],
    fmt='o', color='darkgreen', markersize=10, capsize=10, linewidth=2.5,
    label=f'Różnica = {diff_point:.1f} PLN'
)
axes[1, 0].axhline(0, color='red', linestyle='--', linewidth=1.5, label='H₀: różnica = 0')
axes[1, 0].set_title('Przedział ufności 95% dla różnicy', fontsize=11)
axes[1, 0].set_ylabel('Różnica wartości zakupu (PLN)')
axes[1, 0].legend(fontsize=9)
axes[1, 0].grid(True, axis='y', alpha=0.3)

# Panel 4: Skumulowany efekt biznesowy
klienci_miesiecznie = np.arange(1000, 15001, 1000)
dodatkowy_przychod = klienci_miesiecznie * diff_point
axes[1, 1].bar(klienci_miesiecznie // 1000, dodatkowy_przychod / 1000,
               color='mediumseagreen', edgecolor='white')
axes[1, 1].set_title('Szacowany dodatkowy przychód\n(per liczba klientów)', fontsize=11)
axes[1, 1].set_xlabel('Klienci miesięcznie (tysiące)')
axes[1, 1].set_ylabel('Dodatkowy przychód (tys. PLN/mies.)')
axes[1, 1].grid(True, axis='y', alpha=0.3)

fig.suptitle('A/B Test — Kampania e-mailowa: Wyniki pełnej analizy',
             fontsize=13, fontweight='bold')
plt.show()
plt.close()
```

> "Cztery panele wynikowe. To jest raport. Panel 3 — przedział ufności dla różnicy — jest najważniejszy. Widzimy że cały przedział jest powyżej zera. To znaczy: nawet w pesymistycznym scenariuszu (dolna granica CI) personalizacja daje pozytywny efekt. Panel 4 — przeliczamy efekt na pieniądze. Manager nie rozumie p-wartości, rozumie 'dodatkowe 400 000 PLN miesięcznie'."

---

### 1:15-1:25 — MATERIAŁ 4: Chi-kwadrat i przedziały ufności (10 min)

**[Komórka 12 — test chi-kwadrat]**

```python
# Test chi-kwadrat — dla danych kategorycznych
# SCENARIUSZ: Czy preferencja produktu zależy od grupy wiekowej?
# Mamy dane z ankiety: 300 klientów, 3 grupy wiekowe, 3 produkty

np.random.seed(42)

# Tabela kontyngencji — dane ankietowe
# Wiersze: grupa wiekowa (18-35, 36-55, 55+)
# Kolumny: wybrany produkt (Budżetowy, Średni, Premium)
dane_ankieta = np.array([
    [55, 35, 10],   # 18-35 lat: preferują budżetowy
    [30, 50, 20],   # 36-55 lat: preferują średni
    [15, 35, 50],   # 55+ lat:   preferują premium
])

grupy = ['18-35 lat', '36-55 lat', '55+ lat']
produkty = ['Budżetowy', 'Średni', 'Premium']

print("=== Test Chi-kwadrat — zależność preferencji od wieku ===")
print()
print("Tabela kontyngencji (obserwowane):")
df_ankieta = pd.DataFrame(dane_ankieta, index=grupy, columns=produkty)
print(df_ankieta)
print()

chi2_stat, p_val, dof, expected = stats.chi2_contingency(dane_ankieta)

print(f"Chi² = {chi2_stat:.4f}")
print(f"df   = {dof}")
print(f"p    = {p_val:.6f}")
print()
print("Wartości oczekiwane (przy H₀: brak zależności):")
print(pd.DataFrame(expected.round(1), index=grupy, columns=produkty))
print()

if p_val < 0.05:
    print("WYNIK: p < 0.05 → Zależność ISTOTNA STATYSTYCZNIE")
    print("WNIOSEK: Preferencje produktowe SĄ zależne od grupy wiekowej.")
    print("AKCJA: Segmentacja marketingowa wg wieku — personalizacja oferty!")
else:
    print("WYNIK: p ≥ 0.05 → Brak istotnej zależności")

# Wizualizacja
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Stacked bar chart
colors = ['#3498db', '#2ecc71', '#e74c3c']
bottom = np.zeros(3)
for i, (prod, kolor) in enumerate(zip(produkty, colors)):
    values = dane_ankieta[:, i]
    axes[0].bar(grupy, values, bottom=bottom, label=prod, color=kolor, alpha=0.85, edgecolor='white')
    bottom += values
axes[0].set_title('Preferencje produktowe wg grupy wiekowej\n(obserwowane)', fontsize=11)
axes[0].set_xlabel('Grupa wiekowa')
axes[0].set_ylabel('Liczba klientów')
axes[0].legend(title='Produkt')

# Heatmapa residuów
residua = (dane_ankieta - expected) / np.sqrt(expected)
im = axes[1].imshow(residua, cmap='RdBu_r', aspect='auto', vmin=-3, vmax=3)
axes[1].set_xticks(range(len(produkty)))
axes[1].set_yticks(range(len(grupy)))
axes[1].set_xticklabels(produkty)
axes[1].set_yticklabels(grupy)
for i in range(len(grupy)):
    for j in range(len(produkty)):
        axes[1].text(j, i, f'{residua[i,j]:.2f}', ha='center', va='center',
                     fontsize=11, fontweight='bold',
                     color='white' if abs(residua[i,j]) > 1.5 else 'black')
plt.colorbar(im, ax=axes[1], label='Residuum standaryzowane')
axes[1].set_title(f'Residua standaryzowane\n(|>2| = silne odchylenie, χ²={chi2_stat:.1f}, p={p_val:.4f})', fontsize=11)

plt.tight_layout()
plt.show()
plt.close()
```

> "Test chi-kwadrat — dla danych kategorycznych. T-test porównuje ŚREDNIE (liczby). Chi-kwadrat pyta: 'czy dwie zmienne kategoryczne są od siebie niezależne?'"

> "Tutaj: czy wiek wpływa na wybór produktu? H₀: wiek i produkt są niezależne — każda grupa wiekowa rozkłada się tak samo. Oczekiwane wartości to ile obserwacji byłoby gdyby H₀ była prawdą."

> "Residua standaryzowane na heatmapie: ciemnoczerwone = więcej niż oczekiwano, ciemnoniebieskie = mniej. Widać wyraźnie: seniorzy (55+) wybierają Premium o wiele częściej niż przypadek by sugerował. Młodzi preferują Budżetowy. To jest wartość actionable dla marketera — segmentacja!"

**[Komórka 13 — przedziały ufności]**

```python
# Przedziały ufności — pewność co do naszej estymacji
np.random.seed(42)

# SCENARIUSZ: Badamy NPS (Net Promoter Score) — 0-10 — u 80 klientów
nps_scores = np.random.normal(loc=7.2, scale=1.8, size=80).clip(0, 10)

n = len(nps_scores)
mean_nps = nps_scores.mean()
se = stats.sem(nps_scores)   # błąd standardowy

# Przedziały ufności przy różnych poziomach ufności
poziomy = [0.90, 0.95, 0.99]
print("=== Przedziały ufności dla średniego NPS ===")
print(f"Próba: n={n}, x̄={mean_nps:.3f}, SE={se:.4f}")
print()
print(f"{'Poziom ufności':18} {'Dolna granica':16} {'Górna granica':16} {'Szerokość':12}")
print("-" * 65)
ci_results = []
for poziom in poziomy:
    ci = stats.t.interval(poziom, df=n-1, loc=mean_nps, scale=se)
    szerokosc = ci[1] - ci[0]
    ci_results.append((poziom, ci[0], ci[1], szerokosc))
    print(f"{poziom*100:.0f}%               [{ci[0]:.3f},         {ci[1]:.3f}]         {szerokosc:.3f}")
print()
print("Interpretacja 95% CI:")
print(f"  'Jesteśmy w 95% pewni, że prawdziwy średni NPS firmy")
print(f"  mieści się między {ci_results[1][1]:.2f} a {ci_results[1][2]:.2f}'")
print()
print("Praktyczna decyzja: Cel firmy to NPS > 7.5.")
ci_95 = ci_results[1]
if ci_95[1] < 7.5:
    print(f"  Górna granica CI ({ci_95[2]:.2f}) < 7.5 → Cel prawdopodobnie NIE jest osiągnięty.")
elif ci_95[0] > 7.5:
    print(f"  Dolna granica CI ({ci_95[1]:.2f}) > 7.5 → Cel prawdopodobnie jest osiągnięty.")
else:
    print(f"  CI obejmuje 7.5 → wynik niejednoznaczny — potrzeba więcej danych.")

# Wizualizacja
fig, ax = plt.subplots(figsize=(9, 5))

colors_ci = ['#f39c12', '#2980b9', '#8e44ad']
for i, (poziom, ci_low, ci_high, szer) in enumerate(ci_results):
    ax.errorbar(
        x=[poziom], y=[mean_nps],
        yerr=[[mean_nps - ci_low], [ci_high - mean_nps]],
        fmt='o', color=colors_ci[i], markersize=10, capsize=12, linewidth=2.5,
        label=f'{poziom*100:.0f}% CI: [{ci_low:.2f}, {ci_high:.2f}]'
    )
ax.axhline(7.5, color='red', linestyle='--', linewidth=1.5, label='Cel NPS = 7.5')
ax.axhline(mean_nps, color='black', linestyle='-', linewidth=1, alpha=0.4, label=f'Próbkowa x̄ = {mean_nps:.2f}')
ax.set_title('Przedziały ufności dla średniego NPS\n(im wyższy poziom ufności, tym szerszy przedział)', fontsize=11)
ax.set_xlabel('Poziom ufności')
ax.set_ylabel('Średni NPS')
ax.set_xticks(poziomy)
ax.set_xticklabels([f'{p*100:.0f}%' for p in poziomy])
ax.legend(fontsize=9, loc='lower right')
ax.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
plt.close()
```

> "Przedziały ufności — jedna z najbardziej użytecznych i jednocześnie najczęściej źle interpretowanych koncepcji statystycznych."

> "Co NIE znaczy 95% CI: 'jest 95% szansy że prawdziwa wartość jest w tym przedziale'. Prawdziwa wartość jest stała — albo tam jest, albo nie. Co ZNACZY: 'gdybyśmy powtórzyli to badanie 100 razy, w 95 przypadkach przedział zbudowany tą metodą zawierałby prawdziwą wartość'."

> "Biznesowo: szerszy przedział = większa niepewność. Im więcej obserwacji, tym węższy CI. Jeśli CI obejmuje Wasz cel (7.5), nie możecie jednoznacznie powiedzieć czy go osiągnęliście — potrzeba więcej danych."

---

### 1:25-1:35 — AKTYWNOŚĆ: A/B test na danych marketingowych (10 min)

> "Wasza kolej. 10 minut. Kompletny A/B test samodzielnie. Kod jest prawie gotowy — Waszym zadaniem jest uzupełnić wywołania funkcji i sformułować wniosek biznesowy."

**[Wyświetl na projektorze]**

```python
# ZADANIE — Przeprowadź A/B test kampanii reklamowej
# Kampania w social media: wersja A = grafika statyczna, wersja B = wideo
# Metryka: czas spędzony na stronie produktu (sekundy)
# Pytanie: Czy reklama wideo zatrzymuje użytkowników dłużej?

np.random.seed(42)
czas_A = np.random.normal(loc=45, scale=15, size=120)   # reklama graficzna
czas_B = np.random.normal(loc=52, scale=18, size=120)   # reklama wideo

# KROK 1: Oblicz i wypisz statystyki opisowe dla obu grup
# (średnia, mediana, std)

# KROK 2: Przeprowadź test Shapiro-Wilka dla obu grup (podpróba 50 obs.)
# Użyj: stats.shapiro(...)

# KROK 3: Przeprowadź Welch's t-test
# t_stat, p_val = stats.ttest_ind(czas_A, czas_B, equal_var=False)
# Wypisz statystykę t i p-wartość

# KROK 4: Oblicz 95% przedział ufności dla różnicy (B-A)
# Wzór: diff ± t_kryt * SE_diff

# KROK 5: Sformułuj wniosek biznesowy w 2 zdaniach
# "Reklama wideo [zwiększa/nie zwiększa] czas na stronie statystycznie istotnie.
#  Rekomendacja: [wdrożyć/nie wdrażać] wideo w kampanii."
```

**Oczekiwany wynik:**
- Wniosek: reklama wideo ISTOTNIE zwiększa czas (p < 0.05)
- Wzrost: ok. +7 sekund (5-10 sekund, zależy od CI)
- Rekomendacja: wdrożyć wersję B

> "Kto skończy szybciej — dodajcie wizualizację: histogram obu grup i boxplot porównawczy."

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy dzisiejszy wykład."

> "**Rozkład normalny** — scipy.stats.norm. Trzy funkcje: `pdf()` — gęstość, `cdf()` — skumulowane prawdopodobieństwo, `ppf()` — kwantyl. Do diagnostyki: QQ-plot wizualnie, Shapiro-Wilk formalnie. Pamiętajcie — Shapiro na dużych próbach (n>5000) prawie zawsze odrzuca H₀, nie wpadajcie w pułapkę."

> "**T-test** — trzy wersje. Jednorodkowy (`ttest_1samp`) — jedna próba vs wartość oczekiwana. Niezależny (`ttest_ind`, Welch: `equal_var=False`) — dwie różne grupy. Sparowany (`ttest_rel`) — te same osoby dwa razy. Wybór wersji = wybór scenariusza biznesowego."

> "**p-wartość** — nie czytajcie jako 'prawdopodobieństwo że H₀ jest prawdą'. Czytajcie jako: 'gdyby H₀ była prawdą, szansa na uzyskanie takich danych jak nasze'. p < 0.05 = odrzucamy H₀ = istotna statystycznie różnica."

> "**A/B test** — pięć kroków: statystyki opisowe, sprawdzenie normalności, test, przedział ufności, wniosek biznesowy. Zawsze kończcie na kroku piątym — liczby dla managera, nie dla statystyka."

> "**Chi-kwadrat** — dla danych kategorycznych. Preferencje, ankiety, kliknięcia TAK/NIE. `chi2_contingency()` na tabeli kontyngencji."

> "**Przedziały ufności** — szerokość zależy od n i poziomu ufności. Węższy = więcej danych. Zawsze lepsze niż sama p-wartość, bo pokazują SKALĘ efektu."

> "Następny tydzień: **W13 — scikit-learn i Plotly**. Machine learning: pierwsza regresja liniowa w 10 liniach kodu, interaktywne wykresy Plotly. Statystyka z dzisiaj będzie fundamentem do oceny modeli ML."

**Zadanie domowe (nieoceniane):**
> "Znajdźcie publiczny zbiór danych z co najmniej 2 grupami do porównania (Kaggle, datasets UCI). Przeprowadźcie pełną analizę A/B według pięciu kroków z wykładu. Wniosek biznesowy po polsku. Notebook na GitHub."
