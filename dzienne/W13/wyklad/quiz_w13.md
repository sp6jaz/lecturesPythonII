# Quiz W13 — Zaawansowane biblioteki: scikit-learn i Plotly

**Temat:** Powtórka W12 (testy hipotez, rozkład normalny) + nowy materiał W13 (scikit-learn, Plotly)
**Czas:** 5 minut | **Forma:** kartka lub Mentimeter

---

## Pytania (do wyświetlenia na projektorze — po jednym)

---

### Pytanie 1 (powtórka W12 — testy hipotez)

Wykonujesz test t-studenta i otrzymujesz **p-wartość = 0.12** przy poziomie istotności α = 0.05. Co robisz?

**A)** Odrzucasz hipotezę zerową H₀ — wynik jest istotny statystycznie

**B)** Nie ma podstaw do odrzucenia H₀ — różnica może być przypadkowa (p > α)

**C)** Odrzucasz hipotezę alternatywną H₁ — udowodniłeś że efektu nie ma

**D)** Powtarzasz test z większym α = 0.15, aż p < α

**Odpowiedź: B** — Gdy p > α nie odrzucamy H₀. Nie udowadniamy tym samym że efektu nie ma (błąd C) — może po prostu za mała próba. Manipulowanie α po fakcie (D) to p-hacking — poważny błąd metodologiczny. Właściwa interpretacja: brak wystarczających dowodów do odrzucenia H₀.

---

### Pytanie 2 (powtórka W12 — rozkład normalny)

Wzrost dorosłych Polaków ma rozkład normalny N(175, 7²). Jaki procent populacji ma wzrost **powyżej 182 cm**?

**A)** Około 2.3% — powyżej 2 odchyleń standardowych od średniej

**B)** Około 15.9% — powyżej 1 odchylenia standardowego od średniej

**C)** Około 50% — połowa populacji

**D)** Około 68% — zasada empiryczna

**Odpowiedź: B** — 182 = 175 + 1×7, czyli dokładnie 1 SD powyżej średniej. Według zasady 68-95-99.7, 68% leży w przedziale ±1σ, więc 32% poza nim, a 16% powyżej. Dokładnie: `stats.norm.sf(182, 175, 7)` ≈ 0.159. Odpowiedź A (2.3%) byłaby dla 2σ = 189 cm.

---

### Pytanie 3 (nowy — scikit-learn, train/test split)

Dlaczego przed trenowaniem modelu ML dzielimy dane na zbiór treningowy i testowy?

**A)** Żeby mieć mniej danych do trenowania — szybszy trening

**B)** Żeby ocenić, jak model radzi sobie z **nowymi, niewidzianymi danymi** — testujemy generalizację

**C)** Scikit-learn wymaga tego technicznie — bez podziału biblioteka zgłasza błąd

**D)** Zbiór testowy poprawia dokładność modelu podczas treningu

**Odpowiedź: B** — Model "uczący się" na wszystkich danych może zapamiętać przykłady (overfitting) i świetnie radzić sobie na danych treningowych, ale fatalnie na nowych. Zbiór testowy symuluje "produkcję" — dane których model nigdy nie widział. To kluczowa zasada ML: mierzymy generalizację, nie zapamiętywanie.

---

### Pytanie 4 (nowy — KMeans clustering)

Algorytm K-Means dzieli klientów na 3 grupy. Jak interpretujemy parametr **k=3**?

**A)** Model wykona 3 iteracje trenowania

**B)** Dane zostaną podzielone na **3 klastry** — grupy podobnych obiektów

**C)** Potrzebujemy co najmniej 3 000 próbek danych

**D)** Dokładność modelu będzie wynosić 3/10 = 30%

**Odpowiedź: B** — K w K-Means to liczba klastrów (grup). Algorytm szuka k centroidów tak, żeby zminimalizować sumę odległości każdego punktu do jego centroidu. k=3 = 3 segmenty klientów, np. "oszczędni / średni / premium". Wybór k to decyzja analityczna — metoda łokcia (elbow method) pomaga dobrać optymalną wartość.

---

### Pytanie 5 (nowy — Plotly vs Matplotlib)

Jaka jest kluczowa zaleta wykresów Plotly Express w porównaniu z Matplotlib?

**A)** Plotly rysuje wykresy szybciej — mniejsze zużycie CPU

**B)** Plotly obsługuje wyłącznie wykresy słupkowe i liniowe

**C)** Wykresy Plotly są **interaktywne** — hover, zoom, pan, eksport — bez dodatkowego kodu

**D)** Plotly wymaga mniej importów — jedna linia zamiast trzech

**Odpowiedź: C** — Kluczowa różnica: Matplotlib generuje statyczne obrazy (PNG/SVG), Plotly generuje interaktywny HTML z JavaScript. W Jupyter Notebook możesz najechać myszą i zobaczyć dokładne wartości, odfiltrować serie, przybliżyć wybrany zakres, a gotowy wykres możesz udostępnić jako stronę WWW. Dla prezentacji i dashboardów biznesowych Plotly jest znacznie efektywniejszy.

---

## Klucz odpowiedzi (dla prowadzącego)

| Pytanie | Odpowiedź | Temat |
|---------|-----------|-------|
| 1 | B | W12 — interpretacja p-wartości, brak odrzucenia H₀ |
| 2 | B | W12 — rozkład normalny, zasada 68-95-99.7 |
| 3 | B | W13 — train/test split, generalizacja modelu |
| 4 | B | W13 — KMeans, liczba klastrów k |
| 5 | C | W13 — Plotly interaktywność vs Matplotlib |
