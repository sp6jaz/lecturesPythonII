# S07 Wykład — Plan zajęć dla prowadzącego (zaoczne)

## Temat: Testy hipotez, A/B testing, chi-kwadrat

### Informacje organizacyjne
- **Czas:** 90 min (wykład) + 90 min (lab) = 180 min, ta sama osoba
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z scipy/numpy/matplotlib/seaborn/pandas
- **Wymagania wstępne:** S06 — statystyka opisowa (describe, hist, boxplot, korelacja)
- **Kluczowe hasło:** "p-wartość to nie magia — to narzędzie decyzyjne"

### Efekty uczenia sie (Bloom poziom 3-4)
Po tym spotkaniu osoba studiująca:
1. **Formułuje** hipotezę zerową i alternatywną dla danego problemu biznesowego, rozróżniając scenariusze wymagające różnych testów (Bloom 3)
2. **Stosuje** jednorodkowy, niezależny (Welch) i sparowany t-test w scipy.stats, interpretując p-wartość w kontekście decyzji biznesowej (Bloom 3)
3. **Projektuje** pełną analizę A/B testu: od sformułowania hipotez przez test po wniosek dla decydenta, z przedziałem ufności (Bloom 4)
4. **Stosuje** test chi-kwadrat (`chi2_contingency`) do badania zależności między zmiennymi kategorycznymi i interpretuje wynik w kontekście segmentacji (Bloom 3)
5. **Interpretuje** przedziały ufności i rozróżnia błędy I i II typu, podając wnioski zrozumiałe dla niestatystyka (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **WPROWADZENIE** | Od opisu do dowodu: "Czy ta różnica jest prawdziwa?" | Rozmowa |
| 0:05-0:20 | **MATERIAŁ 1** | Hipoteza zerowa, alternatywna, p-wartość, alfa=0.05 | Tablica + live coding |
| 0:20-0:35 | **MATERIAŁ 2** | T-test: jednorodkowy, niezależny (Welch), sparowany | Live coding |
| 0:35-0:45 | **PRZERWA** | 10 minut | — |
| 0:45-1:05 | **MATERIAŁ 3** | A/B testing — pełny workflow (5 kroków) | Live coding |
| 1:05-1:15 | **MATERIAŁ 4** | Chi-kwadrat: test niezależności | Live coding |
| 1:15-1:25 | **MATERIAŁ 5** | Przedziały ufności, błędy I i II typu | Live coding + diagram |
| 1:25-1:30 | **PODSUMOWANIE** | 5 kluczowych punktów, zapowiedź lab | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — WPROWADZENIE

> "Dzień dobry. Zeszłe spotkanie: statystyka opisowa. Policzyliście średnie, mediany, odchylenia. Narysowaliście histogramy i boxploty. Umiecie OPISAĆ dane. Dzisiaj robimy krok dalej — będziemy dane TESTOWAĆ."

> "Scenariusz z życia: pracujecie w firmie e-commerce. Manager pyta: 'Wdrożyliśmy nowy email do klientów. Open rate wzrósł z 42% na 47%. Czy warto zostać przy nowej wersji?' Odpowiedź: 'To zależy — czy ta różnica 5 punktów procentowych jest PRAWDZIWA, czy to przypadek?'"

> "Testy hipotez to narzędzie, które odpowiada na to pytanie. Trzy linijki kodu w Pythonie. Ale te trzy linijki muszą być dobrze dobrane — inaczej wyciągniecie błędne wnioski. Dzisiaj nauczycie się wybierać właściwy test i interpretować wynik."

---

### 0:05-0:20 — MATERIAŁ 1: Hipoteza zerowa, p-wartość, reguły decyzji (15 min)

> "Fundamenty. Każdy test statystyczny zaczyna się od dwóch hipotez."

**[Wyświetl na projektorze / napisz na tablicy]**

```
H₀ (hipoteza zerowa)  — "nie ma efektu", "nie ma różnicy"
H₁ (hipoteza robocza) — "jest efekt", "jest różnica"

Zasada: H₀ to status quo. Nie da się UDOWODNIĆ H₀.
Można ją tylko ODRZUCIĆ (gdy mamy wystarczające dowody).

Analogia: sąd. H₀ = "niewinny". Musimy UDOWODNIĆ winę.
Brak dowodów ≠ niewinny. Brak dowodów = "nie udowodniono".
```

> "Przykład: badacie czy nowy lek działa. H₀: lek nie działa (brak różnicy vs placebo). H₁: lek działa. Nie możecie powiedzieć 'lek na pewno nie działa' — możecie powiedzieć 'nie mamy dowodów że działa'."

> "A teraz najważniejsza liczba w statystyce: p-wartość."

**[Komórka 1 — setup i demonstracja p-wartości]**

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

**[Komórka 2 — wizualizacja p-wartości]**

```python
# Czym jest p-wartość? Wizualizacja.
# H₀: średnia pensja w firmie = 5000 PLN
# Nasze dane: próbka 50 pracowników, x̄ = 5242 PLN

x = np.linspace(4500, 5500, 300)
pdf = stats.norm.pdf(x, loc=5000, scale=100)   # rozkład pod H₀

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, pdf, 'b-', linewidth=2.5, label='Rozkład średniej pod H₀ (μ=5000)')
ax.fill_between(x, pdf, where=(x >= 5242), alpha=0.4, color='red',
                label='p-wartość (prawy ogon)')
ax.fill_between(x, pdf, where=(x <= 4758), alpha=0.4, color='red',
                label='p-wartość (lewy ogon)')
ax.axvline(5242, color='red', linestyle='--', linewidth=2, label='Nasza średnia: 5242')
ax.axvline(5000, color='green', linestyle='-', linewidth=2, label='H₀: μ = 5000')
ax.set_title('Co to jest p-wartość?\n(czerwony obszar = prawdopodobieństwo uzyskania takiego wyniku, GDYBY H₀ była prawdą)',
             fontsize=11)
ax.set_xlabel('Średnia pensja (PLN)')
ax.legend(fontsize=9)
plt.tight_layout()
plt.show()
plt.close()
```

> "p-wartość to prawdopodobieństwo uzyskania TAKIEGO lub BARDZIEJ ekstremalnego wyniku, GDYBY hipoteza zerowa była prawdą. Czerwony obszar na wykresie."

> "Jeśli p jest bardzo małe — znaczy: szansa na taki wynik 'przypadkiem' jest znikoma. Więc albo mieliśmy ogromnego pecha, albo H₀ jest fałszywa. Konwencja: próg alfa = 0.05 (5%)."

```
REGUŁA DECYZYJNA:
  p < 0.05  →  odrzucamy H₀  →  wynik istotny statystycznie
  p >= 0.05 →  brak podstaw do odrzucenia H₀  →  brak dowodów na różnicę

UWAGA: "istotny statystycznie" ≠ "ważny biznesowo"!
Różnica 2 PLN może być istotna przy n=10000, ale nieistotna dla firmy.
```

> "Zapamiętajcie: p < 0.05 to konwencja, nie prawo natury. W medycynie stosuje się p < 0.01 lub nawet p < 0.001. W fizyce cząstek: 5 sigma, czyli p < 0.0000003. W A/B testach w marketingu: p < 0.05 zwykle wystarczy."

---

### 0:20-0:35 — MATERIAŁ 2: Trzy rodzaje t-testu (15 min)

> "Trzy pytania biznesowe — trzy t-testy. Każdy porównuje średnie, ale w innym scenariuszu."

**[Komórka 3 — tabela porównawcza + t-test jednorodkowy]**

```python
# Trzy rodzaje t-testu — kiedy który?
info = """
╔══════════════════╦══════════════════════════════╦════════════════════════════╗
║ Rodzaj           ║ Pytanie                      ║ scipy.stats                ║
╠══════════════════╬══════════════════════════════╬════════════════════════════╣
║ Jednorodkowy     ║ Czy średnia = oczekiwana     ║ ttest_1samp(dane, popmean) ║
║                  ║ wartość?                     ║                            ║
╠══════════════════╬══════════════════════════════╬════════════════════════════╣
║ Niezależny       ║ Czy dwie RÓŻNE grupy         ║ ttest_ind(A, B,            ║
║ (Welch)          ║ mają różne średnie?          ║   equal_var=False)         ║
╠══════════════════╬══════════════════════════════╬════════════════════════════╣
║ Sparowany        ║ Czy TE SAME osoby/elementy   ║ ttest_rel(przed, po)       ║
║                  ║ zmieniły się między           ║                            ║
║                  ║ pomiarami?                   ║                            ║
╚══════════════════╩══════════════════════════════╩════════════════════════════╝
"""
print(info)
```

> "Jednorodkowy — mam jedną próbkę, porównuję ze standardem. Niezależny — dwie osobne grupy ludzi. Sparowany — ci sami ludzie, dwa pomiary."

**[Komórka 4 — t-test jednorodkowy]**

```python
# T-TEST JEDNORODKOWY
# Scenariusz: firma twierdzi że średnia pensja = 5000 PLN.
# Zbieramy próbkę 50 pracowników. Sprawdzamy.

np.random.seed(42)
pensje = np.random.normal(loc=5400, scale=700, size=50)

print("=== T-test jednorodkowy ===")
print(f"H₀: μ = 5000 PLN (firma twierdzi)")
print(f"H₁: μ ≠ 5000 PLN (średnia jest inna)")
print(f"\nDane: n={len(pensje)}, x̄={pensje.mean():.2f} PLN, s={pensje.std():.2f} PLN")

t_stat, p_val = stats.ttest_1samp(pensje, popmean=5000)

print(f"\nt = {t_stat:.4f}")
print(f"p = {p_val:.4f}")

if p_val < 0.05:
    print(f"\n>>> p < 0.05 → Odrzucamy H₀")
    print(f">>> Średnia pensja ISTOTNIE różni się od 5000 PLN.")
    print(f">>> Faktyczna średnia ({pensje.mean():.0f} PLN) jest WYŻSZA.")
else:
    print(f"\n>>> p >= 0.05 → Brak podstaw do odrzucenia H₀")
```

> "Jedna linijka: `ttest_1samp(pensje, popmean=5000)`. Wynik: p=0.012. Mniej niż 0.05. Odrzucamy H₀. Firma zaniżała dane — średnia jest istotnie wyższa niż deklarowane 5000."

**[Komórka 5 — t-test niezależny (Welch)]**

```python
# T-TEST NIEZALEŻNY (Welch)
# Scenariusz: porównujemy pensje w dziale A (40 osób) i dziale B (35 osób).
# Czy działy płacą inaczej?

np.random.seed(42)
dzial_A = np.random.normal(loc=5200, scale=800, size=40)
dzial_B = np.random.normal(loc=5800, scale=850, size=35)

print("=== T-test niezależny (Welch) ===")
print(f"H₀: μ_A = μ_B (działy płacą tak samo)")
print(f"H₁: μ_A ≠ μ_B (działy płacą inaczej)")
print(f"\nDział A: n={len(dzial_A)}, x̄={dzial_A.mean():.2f} PLN, s={dzial_A.std():.2f}")
print(f"Dział B: n={len(dzial_B)}, x̄={dzial_B.mean():.2f} PLN, s={dzial_B.std():.2f}")
print(f"Różnica: {dzial_B.mean()-dzial_A.mean():.2f} PLN")

# equal_var=False → Welch (nie zakłada równości wariancji)
t_stat, p_val = stats.ttest_ind(dzial_A, dzial_B, equal_var=False)

print(f"\nt = {t_stat:.4f}")
print(f"p = {p_val:.4f}")

if p_val < 0.05:
    print(f"\n>>> p < 0.05 → Odrzucamy H₀")
    print(f">>> Dział B płaci ISTOTNIE więcej niż dział A.")
    print(f">>> Różnica: ~{dzial_B.mean()-dzial_A.mean():.0f} PLN/mies.")
```

> "Welch's t-test: `equal_var=False`. ZAWSZE używajcie Welcha — jest bezpieczniejszy niż klasyczny test Studenta, bo nie zakłada jednakowej wariancji. p = 0.0001. Potężna różnica — dział B płaci ~780 PLN więcej."

**[Komórka 6 — t-test sparowany]**

```python
# T-TEST SPAROWANY
# Scenariusz: mierzymy produktywność 30 pracowników PRZED i PO szkoleniu.
# Te same osoby — dane powiązane.

np.random.seed(42)
produktywnosc_przed = np.random.normal(loc=75, scale=12, size=30)
produktywnosc_po = produktywnosc_przed * np.random.normal(1.12, 0.05, 30)

roznice = produktywnosc_po - produktywnosc_przed

print("=== T-test sparowany ===")
print(f"H₀: μ_różnica = 0 (szkolenie nie zmienia produktywności)")
print(f"H₁: μ_różnica ≠ 0 (szkolenie zmienia produktywność)")
print(f"\nPrzed: x̄={produktywnosc_przed.mean():.1f}, s={produktywnosc_przed.std():.1f}")
print(f"Po:    x̄={produktywnosc_po.mean():.1f}, s={produktywnosc_po.std():.1f}")
print(f"Śr. zmiana: +{roznice.mean():.1f} ({roznice.mean()/produktywnosc_przed.mean()*100:.1f}%)")

t_stat, p_val = stats.ttest_rel(produktywnosc_przed, produktywnosc_po)

print(f"\nt = {t_stat:.4f}")
print(f"p = {p_val:.6f}")

if p_val < 0.05:
    print(f"\n>>> Szkolenie ISTOTNIE poprawiło produktywność.")
    print(f">>> Wzrost: ~{roznice.mean():.0f} jednostek ({roznice.mean()/produktywnosc_przed.mean()*100:.0f}%)")
```

> "Sparowany test — `ttest_rel`. 'rel' od 'related', powiązane. Dlaczego nie `ttest_ind`? Bo te same 30 osób. Gdybyśmy użyli testu niezależnego, zignorujemy że Jan ma naturalnie wyższą produktywność niż Anna. Sparowany test to 'wyzerowuje' — liczy ZMIANĘ dla każdej osoby."

---

### 0:35-0:45 — PRZERWA (10 min)

---

### 0:45-1:05 — MATERIAŁ 3: A/B testing w biznesie (20 min)

> "Po przerwie: kompletny A/B test krok po kroku. To jest schemat, którego użyjecie w pracy — zapamiętajcie go."

> "A/B testing — chleb powszedni firm technologicznych. Netflix testuje miniatury filmów. Allegro testuje kolory przycisków 'Kup teraz'. Booking.com uruchamia ponad 1000 eksperymentów dziennie. Każdy taki eksperyment to w gruncie rzeczy t-test."

**[Komórka 7 — pełny workflow A/B testu]**

```python
# A/B TEST — PEŁNY WORKFLOW (5 kroków)
# Scenariusz: E-mail marketing. Dwie wersje emaila do klientów.
# Wersja A: standardowy email
# Wersja B: email z personalizacją (imię + rekomendacja)
# Metryka: wartość zakupu po kliknięciu (PLN)

np.random.seed(42)
n_A, n_B = 150, 150

zakupy_A = np.concatenate([
    np.random.normal(280, 70, 130),   # większość klientów
    np.random.normal(700, 90, 20)     # klienci premium
])
np.random.shuffle(zakupy_A)

zakupy_B = np.concatenate([
    np.random.normal(320, 75, 130),   # efekt personalizacji
    np.random.normal(750, 85, 20)     # premium też lepiej reagują
])
np.random.shuffle(zakupy_B)

# ─── KROK 1: Statystyki opisowe ───
print("=" * 55)
print("A/B TEST — Kampania e-mailowa")
print("=" * 55)
print()
print("KROK 1: Statystyki opisowe")
print(f"  Wersja A (standard): n={n_A}, x̄={zakupy_A.mean():.2f} PLN, "
      f"mediana={np.median(zakupy_A):.2f}, s={zakupy_A.std():.2f}")
print(f"  Wersja B (person.):  n={n_B}, x̄={zakupy_B.mean():.2f} PLN, "
      f"mediana={np.median(zakupy_B):.2f}, s={zakupy_B.std():.2f}")
print(f"  Różnica średnich: {zakupy_B.mean()-zakupy_A.mean():.2f} PLN "
      f"({(zakupy_B.mean()/zakupy_A.mean()-1)*100:.1f}%)")

# ─── KROK 2: Sprawdzenie normalności ───
print(f"\nKROK 2: Test normalności (Shapiro-Wilk, podpróba 50)")
idx = np.random.choice(n_A, 50, replace=False)
stat_A, p_A = stats.shapiro(zakupy_A[idx])
stat_B, p_B = stats.shapiro(zakupy_B[idx])
print(f"  A: W={stat_A:.4f}, p={p_A:.4f}")
print(f"  B: W={stat_B:.4f}, p={p_B:.4f}")

# ─── KROK 3: Test właściwy ───
print(f"\nKROK 3: Welch's t-test")
t_stat, p_val = stats.ttest_ind(zakupy_A, zakupy_B, equal_var=False)
print(f"  t = {t_stat:.4f}, p = {p_val:.4f}")

# ─── KROK 4: Przedział ufności ───
diff = zakupy_B.mean() - zakupy_A.mean()
se_diff = np.sqrt(zakupy_A.var()/n_A + zakupy_B.var()/n_B)
df = n_A + n_B - 2
ci_low = diff - stats.t.ppf(0.975, df) * se_diff
ci_high = diff + stats.t.ppf(0.975, df) * se_diff
print(f"\nKROK 4: 95% CI dla różnicy (B−A)")
print(f"  [{ci_low:.2f}, {ci_high:.2f}] PLN")

# ─── KROK 5: Wniosek biznesowy ───
print(f"\nKROK 5: WNIOSEK BIZNESOWY")
print("-" * 45)
if p_val < 0.05 and ci_low > 0:
    print(f"  Personalizowany email ISTOTNIE zwiększa")
    print(f"  wartość zakupu o {diff:.0f} PLN/klienta.")
    print(f"  (95% CI: [{ci_low:.0f}, {ci_high:.0f}] PLN)")
    print(f"  Przy 10 000 klientów/mies.:")
    print(f"  → dodatkowy przychód ~{diff*10000:,.0f} PLN/mies.")
    print(f"  REKOMENDACJA: Wdrożyć wersję B.")
```

> "Pięć kroków. Zapamiętajcie ten schemat — to jest gotowy framework do każdego A/B testu."

> "Krok 1: ZAWSZE patrzcie na dane oczami, zanim odpaliecie test. Krok 2: sprawdźcie czy możecie użyć t-testu (normalność). Krok 3: sam test — jedna linijka kodu. Krok 4: przedział ufności — ważniejszy niż p-wartość, bo mówi O ILE. Krok 5: wniosek w języku managera — nie 'p=0.003', ale 'dodatkowe 350 000 PLN miesięcznie'."

**[Komórka 8 — wizualizacja A/B testu]**

```python
# Wizualizacja A/B testu — 4 panele
fig, axes = plt.subplots(2, 2, figsize=(13, 9), constrained_layout=True)

# Panel 1: Histogramy
axes[0,0].hist(zakupy_A, bins=25, alpha=0.6, color='steelblue', density=True,
               label=f'A: standard (x̄={zakupy_A.mean():.0f})')
axes[0,0].hist(zakupy_B, bins=25, alpha=0.6, color='tomato', density=True,
               label=f'B: personal. (x̄={zakupy_B.mean():.0f})')
axes[0,0].axvline(zakupy_A.mean(), color='steelblue', ls='--', lw=2)
axes[0,0].axvline(zakupy_B.mean(), color='tomato', ls='--', lw=2)
axes[0,0].set_title(f'Rozkład wartości zakupu\n(p={p_val:.4f})')
axes[0,0].set_xlabel('Wartość zakupu (PLN)')
axes[0,0].legend(fontsize=9)

# Panel 2: Boxplot
bp = axes[0,1].boxplot([zakupy_A, zakupy_B],
                        labels=['A: standard', 'B: personalizowany'],
                        patch_artist=True,
                        medianprops=dict(color='red', linewidth=2))
bp['boxes'][0].set_facecolor('lightblue')
bp['boxes'][1].set_facecolor('lightsalmon')
axes[0,1].set_title('Boxplot — porównanie grup')
axes[0,1].set_ylabel('Wartość zakupu (PLN)')
axes[0,1].grid(True, axis='y', alpha=0.3)

# Panel 3: Przedział ufności
axes[1,0].errorbar(['Różnica B−A'], [diff],
    yerr=[[diff-ci_low], [ci_high-diff]],
    fmt='o', color='darkgreen', ms=10, capsize=10, lw=2.5,
    label=f'Różnica = {diff:.0f} PLN')
axes[1,0].axhline(0, color='red', ls='--', lw=1.5, label='H₀: różnica = 0')
axes[1,0].set_title('95% CI dla różnicy')
axes[1,0].set_ylabel('PLN')
axes[1,0].legend(fontsize=9)
axes[1,0].grid(True, axis='y', alpha=0.3)

# Panel 4: Efekt biznesowy
klienci = np.arange(1000, 15001, 1000)
axes[1,1].bar(klienci//1000, klienci*diff/1000,
              color='mediumseagreen', edgecolor='white')
axes[1,1].set_title('Szacowany dodatkowy przychód')
axes[1,1].set_xlabel('Klienci (tysiące/mies.)')
axes[1,1].set_ylabel('Dodatkowy przychód (tys. PLN)')
axes[1,1].grid(True, axis='y', alpha=0.3)

fig.suptitle('A/B Test — Kampania e-mailowa: pełna analiza',
             fontsize=13, fontweight='bold')
plt.show()
plt.close()
```

> "Cztery panele — gotowy raport. Panel 3 jest kluczowy: cały przedział ufności powyżej zera. To znaczy: nawet w pesymistycznym scenariuszu personalizacja daje zysk. Panel 4: przeliczamy na pieniądze. Manager tego potrzebuje."

---

### 1:05-1:15 — MATERIAŁ 4: Test chi-kwadrat (10 min)

> "Wszystkie testy do tej pory porównywały ŚREDNIE — liczby ciągłe. A co jeśli dane są kategoryczne? Mężczyzna/kobieta, Basic/Pro/Enterprise, TAK/NIE?"

**[Komórka 9 — chi-kwadrat]**

```python
# TEST CHI-KWADRAT — zależność między zmiennymi kategorycznymi
# Scenariusz: Czy segment klienta zależy od kanału pozyskania?
# Kanały: Organiczny, Paid Ads, Polecenia
# Segmenty: Basic, Standard, Premium

dane = np.array([
    [60, 30, 10],   # Organiczny: głównie Basic
    [25, 45, 30],   # Paid Ads: mieszane, dużo Standard
    [15, 25, 60],   # Polecenia: głównie Premium
])

kanaly = ['Organiczny', 'Paid Ads', 'Polecenia']
segmenty = ['Basic', 'Standard', 'Premium']

print("=== Test chi-kwadrat: Kanał pozyskania × Segment klienta ===")
print()
df_tab = pd.DataFrame(dane, index=kanaly, columns=segmenty)
print("Tabela kontyngencji (obserwowane):")
print(df_tab)
print()

chi2, p_val, dof, expected = stats.chi2_contingency(dane)

print(f"χ² = {chi2:.4f}")
print(f"df = {dof}")
print(f"p  = {p_val:.6f}")
print()
print("Wartości oczekiwane (gdyby kanał NIE wpływał na segment):")
print(pd.DataFrame(expected.round(1), index=kanaly, columns=segmenty))
print()

if p_val < 0.05:
    print("WYNIK: p < 0.05 → Zależność ISTOTNA STATYSTYCZNIE")
    print("WNIOSEK: Kanał pozyskania WPŁYWA na segment klienta!")
    print("AKCJA: Chcesz klientów Premium? Inwestuj w program poleceń.")
    print("       Chcesz dużo klientów (Basic)? Skup się na SEO (organik).")
```

> "Jedna funkcja: `chi2_contingency()`. Podajemy tabelę kontyngencji — numpy array 2D. Funkcja zwraca chi², stopnie swobody, p-wartość i oczekiwane wartości."

> "Oczekiwane wartości to ile byłoby W KAŻDEJ komórce, gdyby kanał i segment były całkowicie niezależne. Porównanie obserwowanych z oczekiwanymi — tam gdzie duża różnica, tam jest zależność."

**[Komórka 10 — wizualizacja chi-kwadrat]**

```python
# Wizualizacja chi-kwadrat
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Stacked bar chart
colors = ['#3498db', '#2ecc71', '#e74c3c']
bottom = np.zeros(3)
for i, (seg, kolor) in enumerate(zip(segmenty, colors)):
    axes[0].bar(kanaly, dane[:, i], bottom=bottom, label=seg,
                color=kolor, alpha=0.85, edgecolor='white')
    bottom += dane[:, i]
axes[0].set_title('Segment klienta wg kanału pozyskania')
axes[0].set_ylabel('Liczba klientów')
axes[0].legend(title='Segment')

# Heatmapa residuów standaryzowanych
residua = (dane - expected) / np.sqrt(expected)
im = axes[1].imshow(residua, cmap='RdBu_r', aspect='auto', vmin=-4, vmax=4)
axes[1].set_xticks(range(len(segmenty)))
axes[1].set_yticks(range(len(kanaly)))
axes[1].set_xticklabels(segmenty)
axes[1].set_yticklabels(kanaly)
for i in range(len(kanaly)):
    for j in range(len(segmenty)):
        axes[1].text(j, i, f'{residua[i,j]:.1f}', ha='center', va='center',
                     fontsize=12, fontweight='bold',
                     color='white' if abs(residua[i,j]) > 2 else 'black')
plt.colorbar(im, ax=axes[1], label='Residuum standaryzowane')
axes[1].set_title(f'Gdzie jest największe odchylenie?\n(χ²={chi2:.1f}, p<0.001)')

plt.tight_layout()
plt.show()
plt.close()
```

> "Heatmapa residuów to klucz do interpretacji. Czerwone = więcej niż oczekiwano. Niebieskie = mniej. Polecenia → Premium: silnie czerwone. Organik → Basic: silnie czerwone. To jest actionable insight."

---

### 1:15-1:25 — MATERIAŁ 5: Przedziały ufności, błędy I i II typu (10 min)

**[Komórka 11 — przedziały ufności]**

```python
# PRZEDZIAŁY UFNOŚCI — pewność co do estymacji
np.random.seed(42)

# Scenariusz: mierzymy satysfakcję klientów (1-10) u 80 osób
satysfakcja = np.random.normal(loc=7.2, scale=1.8, size=80).clip(1, 10)

n = len(satysfakcja)
mean_s = satysfakcja.mean()
se = stats.sem(satysfakcja)

print("=== Przedziały ufności dla średniej satysfakcji ===")
print(f"n={n}, x̄={mean_s:.3f}, SE={se:.4f}\n")

for poziom in [0.90, 0.95, 0.99]:
    ci = stats.t.interval(poziom, df=n-1, loc=mean_s, scale=se)
    print(f"{poziom*100:.0f}% CI: [{ci[0]:.3f}, {ci[1]:.3f}]  "
          f"(szerokość: {ci[1]-ci[0]:.3f})")

print(f"\nInterpretacja 95% CI:")
ci95 = stats.t.interval(0.95, df=n-1, loc=mean_s, scale=se)
print(f"  'Jesteśmy w 95% pewni, że prawdziwa średnia")
print(f"   satysfakcja mieści się między {ci95[0]:.2f} a {ci95[1]:.2f}'")
```

> "Przedział ufności to lepszy sposób raportowania niż sama p-wartość. p-wartość mówi TAK/NIE. CI mówi: 'o ile, z jaką pewnością'. Im szersza ramka — tym większa niepewność. Im więcej obserwacji — tym węższa."

**[Wyświetl na projektorze — diagram błędów I i II typu]**

```
╔═══════════════════════════════════════════════╗
║         BŁĘDY W TESTOWANIU HIPOTEZ           ║
╠═══════════════════╦═══════════════════════════╣
║                   ║    Rzeczywistość           ║
║                   ╠═════════════╦═════════════╣
║                   ║ H₀ prawda   ║ H₁ prawda   ║
╠═══════════════════╬═════════════╬═════════════╣
║ Decyzja:          ║             ║             ║
║ Odrzucamy H₀      ║ BŁĄD I TYPU ║ OK!         ║
║                   ║ (false      ║ (prawidłowe ║
║                   ║  positive)  ║  wykrycie)  ║
║                   ║ P = α       ║             ║
╠═══════════════════╬═════════════╬═════════════╣
║ Nie odrzucamy H₀  ║ OK!         ║ BŁĄD II TYPU║
║                   ║ (prawidłowa ║ (false      ║
║                   ║  decyzja)   ║  negative)  ║
║                   ║             ║ P = β       ║
╚═══════════════════╩═════════════╩═════════════╝

Przykłady biznesowe:
  Błąd I typu (false positive):
    → Wdrażamy nowy email, który NAPRAWDĘ nie działa lepiej
    → Koszt: czas, zasoby na wdrożenie, możliwy spadek konwersji

  Błąd II typu (false negative):
    → NIE wdrażamy emaila, który NAPRAWDĘ działa lepiej
    → Koszt: utracony przychód

Jak zmniejszyć błąd I typu? → Niższe α (0.01 zamiast 0.05)
Jak zmniejszyć błąd II typu? → Większa próba (więcej danych)
```

> "To jest trade-off. Chcesz mniej fałszywych alarmów? Ustaw surowszy próg. Ale wtedy trudniej wykryć prawdziwe efekty. Chcesz wykrywać nawet małe efekty? Zbierz więcej danych."

> "W A/B testach zazwyczaj bardziej boimy się błędu I typu — wdrożenie czegoś co nie działa kosztuje czas i pieniądze. Dlatego α = 0.05 jest standardem."

---

### 1:25-1:30 — PODSUMOWANIE

> "Pięć kluczowych punktów z dzisiejszego wykładu."

> "**Jeden.** H₀ to status quo. Testujemy czy mamy dowody na jej odrzucenie. p < 0.05 = odrzucamy."

> "**Dwa.** Trzy t-testy: jednorodkowy (`ttest_1samp`) — vs wartość oczekiwana. Niezależny (`ttest_ind`, Welch) — dwie różne grupy. Sparowany (`ttest_rel`) — te same osoby przed/po."

> "**Trzy.** A/B test = 5 kroków: statystyki opisowe, normalność, test, CI, wniosek biznesowy."

> "**Cztery.** Chi-kwadrat (`chi2_contingency`) — dla danych kategorycznych. Tabela kontyngencji na wejściu."

> "**Pięć.** Przedział ufności > p-wartość. CI mówi O ILE, p-wartość mówi tylko TAK/NIE."

> "Za chwilę przechodzimy do laboratorium — sami przeprowadzicie wszystkie te testy na nowych danych. Przygotujcie notebooki."
