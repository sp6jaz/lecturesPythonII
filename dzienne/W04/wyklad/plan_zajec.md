# W04 Wykład — Plan zajęć dla prowadzącego

## Temat: NumPy — zaawansowane

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z numpy/matplotlib
- **Przed wykładem:** otwórz `numpy_advanced_demo.ipynb`

### Efekty uczenia się (Bloom)
Po tym wykładzie osoba studiująca:
1. **Wyjaśnia** mechanizm broadcastingu i stosuje go w obliczeniach (Bloom 2-3)
2. **Zmienia** kształt tablic za pomocą reshape, flatten, stacking (Bloom 3)
3. **Stosuje** zaawansowane operacje: where, sort, argsort, unique, korelacja (Bloom 3)
4. **Generuje** dane syntetyczne z rozkładów (normal, uniform, randint) (Bloom 3)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W03 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | Nawiązanie do W03, plan wykładu | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Broadcasting — operacje na tablicach różnych kształtów | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | Reshape, flatten, stacking — zmiana kształtu | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | Zaawansowane operacje: where, sort, unique, korelacja | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Generowanie danych + statystyki | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Analiza danych finansowych z NumPy | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Przejście do Pandas na W05 | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W03)

> "Pięć pytań z zeszłego tygodnia — 3 minuty."

**[Użyj quiz_w03.md]**

---

### 0:05-0:10 — WPROWADZENIE

> "Zeszły tydzień — podstawy NumPy: tablice, indeksowanie, operacje wektorowe. Dzisiaj wchodzimy głębiej. Zobaczycie broadcasting — sztuczka, która pozwala operować na tablicach różnych rozmiarów. Nauczycie się zmieniać kształt danych. I zobaczycie jak generować dane syntetyczne — przydatne do testowania i symulacji."

> "Po dzisiejszym wykładzie kończymy z czystym NumPy. Od W05 — **Pandas**. Ale wszystko co robiliście z NumPy będzie się przydawać — bo Pandas pod spodem to NumPy z etykietami."

---

### 0:10-0:30 — MATERIAŁ 1: Broadcasting (20 min)

**[Otwórz notebook]**

> "Broadcasting — co to jest? To mechanizm, dzięki któremu NumPy potrafi operować na tablicach **różnych kształtów**."

**[Komórka 1 — scalar + array]**

```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(f"a * 10 = {a * 10}")
```

> "Najprostszy przypadek: tablica razy liczba. NumPy 'rozciąga' 10 na [10, 10, 10, 10] i mnoży element po elemencie. To jest broadcasting — już go używaliście, nie wiedząc o tym."

**[Komórka 2 — 1D + 2D]**

```python
# Macierz cen: 3 produkty × 4 kwartały
ceny = np.array([[100, 110, 120, 130],
                  [200, 210, 220, 230],
                  [50,  55,  60,  65]])

# Rabat różny dla każdego kwartału
rabat = np.array([0.05, 0.10, 0.15, 0.20])

# Broadcasting: macierz 3×4 * wektor 1×4
ceny_po_rabacie = ceny * (1 - rabat)
print(f"Ceny:\n{ceny}")
print(f"Rabat: {rabat}")
print(f"Po rabacie:\n{ceny_po_rabacie}")
```

> "Macierz 3×4 razy wektor 4 elementów. NumPy rozciąga wektor na 3 wiersze i mnoży. Każdy kwartał ma inny rabat — i działa na wszystkie produkty naraz. Bez pętli."

**[Komórka 3 — kolumnowy broadcast]**

```python
# Mnożnik różny dla każdego produktu (premia za markę)
premia = np.array([[1.2],    # produkt A: +20%
                    [1.0],    # produkt B: bez premii
                    [1.5]])   # produkt C: +50%

ceny_z_premia = ceny * premia
print(f"Premia per produkt:\n{premia.flatten()}")
print(f"Ceny z premią:\n{ceny_z_premia}")
```

> "Wektor kolumnowy 3×1 razy macierz 3×4. NumPy rozciąga kolumnę na 4 kolumny. Każdy produkt ma inną premię — działa na wszystkie kwartały."

**[Komórka 4 — zasady broadcastingu]**

> "Kiedy broadcasting działa? Prosta zasada: NumPy porównuje kształty **od prawej** do lewej. Wymiar musi być **taki sam** lub **równy 1**."

```python
# Działa:
# (3, 4) * (4,)   → 4 == 4  ✓
# (3, 4) * (3, 1) → 4 != 1, ale 3 == 3, 1 się rozciąga  ✓
# (3, 4) * (1, 4) → 3 != 1, ale 1 się rozciąga, 4 == 4  ✓

# NIE działa:
# (3, 4) * (3,)   → 4 != 3  ✗  ← częsty błąd!
try:
    blad = ceny * np.array([1, 2, 3])    # 3×4 * 3 → nie pasuje!
except ValueError as e:
    print(f"Błąd: {e}")
```

> "Najczęstszy błąd: macierz 3×4 razy wektor 3 elementów. NumPy patrzy od prawej: 4 ≠ 3. Nie działa. Rozwiązanie: reshape na kolumnę (3,1)."

---

### 0:30-0:45 — MATERIAŁ 2: Reshape i stacking (15 min)

> "Zmiana kształtu tablic. Dane nie zawsze przychodzą w formacie, który potrzebujemy."

**[Komórka 5 — reshape]**

```python
a = np.arange(12)
print(f"Flat: {a}")
print(f"Reshape 3×4:\n{a.reshape(3, 4)}")
print(f"Reshape 4×3:\n{a.reshape(4, 3)}")
print(f"Reshape -1 (auto):\n{a.reshape(3, -1)}")  # NumPy sam oblicza drugi wymiar
```

> "`.reshape(3, 4)` — 12 elementów → 3 wiersze, 4 kolumny. `-1` oznacza: oblicz sam. 12 / 3 = 4. Przydatne, gdy nie chcecie liczyć."

**[Komórka 6 — flatten]**

```python
macierz = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Macierz:\n{macierz}")
print(f"Flatten: {macierz.flatten()}")    # kopia
print(f"Ravel: {macierz.ravel()}")        # widok (szybszy)
```

> "`flatten` — spłaszcza do 1D, tworzy kopię. `ravel` — to samo, ale tworzy widok (szybszy, ale zmiana w wyniku zmienia oryginał). Na początek — używajcie `flatten`, jest bezpieczniejszy."

**[Komórka 7 — łączenie tablic]**

```python
q1 = np.array([100, 200, 150])
q2 = np.array([120, 210, 160])
q3 = np.array([130, 230, 180])

# Pionowo — nowe wiersze
print(f"vstack:\n{np.vstack([q1, q2, q3])}")

# Poziomo — dłuższy wektor
print(f"hstack: {np.hstack([q1, q2, q3])}")

# Kolumny obok siebie
print(f"column_stack:\n{np.column_stack([q1, q2, q3])}")
```

> "`vstack` — stawia tablice jedna pod drugą. `hstack` — obok siebie. `column_stack` — każda tablica jako kolumna. Przydatne gdy łączycie dane z różnych źródeł."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: Operacje zaawansowane (20 min)

**[Komórka 8 — np.where]**

> "`np.where` — warunkowe przypisanie. Jak IF w Excelu, ale na całej tablicy."

```python
oceny = np.array([3.0, 4.5, 2.0, 5.0, 3.5, 4.0, 2.5])

# Zdał (>= 3.0) / Nie zdał
status = np.where(oceny >= 3.0, 'ZDAŁ', 'NIE ZDAŁ')
print(f"Oceny: {oceny}")
print(f"Status: {status}")

# Premia za wyniki — powyżej 4.0 dostaje 500 zł
premia = np.where(oceny >= 4.0, 500, 0)
print(f"Premia: {premia}")
```

> "Trzy argumenty: warunek, wartość gdy True, wartość gdy False. Jak Excel IF. Ale działa na milionach elementów w ułamku sekundy."

**[Komórka 9 — sort i argsort]**

```python
sprzedaz = np.array([340, 120, 560, 90, 420])
produkty = ['A', 'B', 'C', 'D', 'E']

# Sortowanie
print(f"Posortowane: {np.sort(sprzedaz)}")

# Indeksy sortowania — TOP-3
indeksy = np.argsort(sprzedaz)[::-1]  # malejąco
print(f"Ranking:")
for i, idx in enumerate(indeksy[:3]):
    print(f"  {i+1}. {produkty[idx]} — {sprzedaz[idx]} szt.")
```

> "`argsort` — nie daje wartości, daje **indeksy**. Dzięki temu możemy powiązać wynik z nazwami produktów. To kluczowe — w danych biznesowych same liczby nie wystarczą."

**[Komórka 10 — unique]**

```python
transakcje_dzial = np.array(['IT', 'HR', 'IT', 'Finanse', 'HR', 'IT', 'Finanse', 'Finanse'])
unikalne, ile = np.unique(transakcje_dzial, return_counts=True)
print(f"Działy: {unikalne}")
print(f"Liczba transakcji: {ile}")
```

> "`unique` — unikalne wartości. Z `return_counts=True` — od razu ile razy każda wartość wystąpiła. Jak `value_counts()` w Pandas, które poznacie za tydzień."

**[Komórka 11 — korelacja]**

```python
np.random.seed(42)
reklama = np.random.normal(1000, 200, 30)     # budżet reklamy
sprzedaz = 500 + 0.8 * reklama + np.random.normal(0, 100, 30)  # sprzedaż

korelacja = np.corrcoef(reklama, sprzedaz)
print(f"Macierz korelacji:\n{korelacja}")
print(f"r = {korelacja[0, 1]:.3f}")
```

> "Korelacja Pearsona. `r = 0.85` — silna dodatnia korelacja. Więcej reklamy = więcej sprzedaży. Ale uwaga — **korelacja to nie przyczynowość**! To powiemy sobie szerzej przy statystyce na W11."

---

### 1:15-1:25 — MATERIAŁ 4: Generowanie danych (10 min)

> "W pracy analityka często potrzebujecie danych do testów. Albo do symulacji."

**[Komórka 12 — rozkłady]**

```python
np.random.seed(42)

# Rozkład normalny — wynagrodzenia
wynagrodzenia = np.random.normal(loc=5000, scale=1000, size=100)
print(f"Wynagrodzenia — średnia: {wynagrodzenia.mean():.0f}, std: {wynagrodzenia.std():.0f}")

# Rozkład jednostajny — ceny w przedziale
ceny = np.random.uniform(low=10, high=500, size=50)
print(f"Ceny — min: {ceny.min():.0f}, max: {ceny.max():.0f}")

# Rozkład Poissona — liczba zamówień dziennie
zamowienia = np.random.poisson(lam=20, size=30)
print(f"Zamówienia dziennie: {zamowienia}")
```

**[Komórka 13 — statystyki]**

```python
# Pełny zestaw statystyk opisowych
dane = wynagrodzenia
print(f"Średnia: {dane.mean():.0f}")
print(f"Mediana: {np.median(dane):.0f}")
print(f"Std: {dane.std():.0f}")
print(f"Min: {dane.min():.0f}, Max: {dane.max():.0f}")
print(f"Q1 (25%): {np.percentile(dane, 25):.0f}")
print(f"Q3 (75%): {np.percentile(dane, 75):.0f}")
print(f"IQR: {np.percentile(dane, 75) - np.percentile(dane, 25):.0f}")
```

> "Percentyle i IQR — spotkaliście na statystyce. Q1 = 25% danych poniżej, Q3 = 75% poniżej. IQR = Q3 - Q1 — miara rozproszenia odporna na wartości odstające."

---

### 1:25-1:35 — AKTYWNOŚĆ: analiza danych finansowych (10 min)

> "Zadanie. Firma ma 5 oddziałów. Dane o przychodach miesięcznych:"

**[Wyświetl na projektorze]**

```python
np.random.seed(123)
oddzialy = ['Warszawa', 'Kraków', 'Wrocław', 'Gdańsk', 'Poznań']
przychody = np.random.randint(50, 200, size=(5, 12))  # 5 oddziałów × 12 miesięcy
```

**Pytania (5 min):**
1. Który oddział miał najwyższy roczny przychód?
2. Który miesiąc był najlepszy (łącznie)?
3. Ile oddziałów miało średni miesięczny przychód powyżej 100?
4. Jaka jest korelacja między oddziałem Warszawa i Kraków?

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy. Dzisiaj poznaliście:"

> "1. **Broadcasting** — operacje na tablicach różnych kształtów. Rabat per kwartał, premia per produkt."
> "2. **Reshape i stacking** — zmiana kształtu, łączenie danych."
> "3. **Zaawansowane operacje** — where, sort, argsort, unique, korelacja."
> "4. **Generowanie danych** — rozkład normalny, jednostajny, Poisson."

> "To jest wszystko co potrzebujecie z NumPy. Od przyszłego tygodnia — **Pandas**. DataFrame, wczytywanie CSV, selekcja danych. NumPy robił obliczenia — Pandas doda etykiety, nazwy kolumn i mnóstwo wygodnych metod."

**Zadanie domowe (nieoceniane):**
> "Wygenerujcie dane o 50 pracownikach: pensja (rozkład normalny, średnia 6000, std 1500), staż (randint 1-20), ocena roczna (uniform 1-5). Policzcie korelację między stażem a pensją. Wrzućcie notebook na GitHub."
