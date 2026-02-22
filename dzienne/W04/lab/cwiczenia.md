# L04 — Ćwiczenia laboratoryjne

## Temat: NumPy zaawansowane — broadcasting, reshape, analiza finansowa

**Programowanie w Pythonie II** | Laboratorium 4
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne

---

## Przydatne materiały

| Temat | Link |
|-------|------|
| NumPy — broadcasting | https://numpy.org/doc/stable/user/basics.broadcasting.html |
| NumPy — `reshape()` | https://numpy.org/doc/stable/reference/generated/numpy.reshape.html |
| NumPy — `np.where()` | https://numpy.org/doc/stable/reference/generated/numpy.where.html |
| NumPy — `np.random` | https://numpy.org/doc/stable/reference/random/index.html |
| NumPy — operacje na tablicach 2D | https://numpy.org/doc/stable/user/absolute_beginners.html#more-useful-array-operations |

### Kluczowe pojęcia tego laboratorium

- **Broadcasting** — mechanizm NumPy pozwalający wykonywać operacje na tablicach o różnych kształtach. Np. tablica (4x3) x wektor (3,) -> każdy wiersz pomnożony przez wektor.
- **Reshape** — zmiana kształtu tablicy bez zmiany danych. Np. tablica 12-elementowa -> macierz 3x4.
- **`np.where(warunek, wartość_tak, wartość_nie)`** — wektorowy odpowiednik `if/else` — działa na całych tablicach naraz.

---

## Ćwiczenie 1: Broadcasting — zastosowania biznesowe (20 min)

### Cel
Użyj broadcastingu do obliczeń na danych o różnych kształtach.

### Krok 1 — Rabaty kwartalne

```python
import numpy as np

# Ceny 4 produktów w 3 sklepach
ceny = np.array([[29.99, 31.99, 28.99],    # Produkt A
                  [49.99, 52.99, 47.99],    # Produkt B
                  [14.99, 15.99, 13.99],    # Produkt C
                  [99.99, 104.99, 94.99]])  # Produkt D

sklepy = ['Centrum', 'Galeria', 'Online']
produkty = ['A', 'B', 'C', 'D']
```

**Zadanie 1a:** Podnieś ceny we wszystkich sklepach o 5% (inflacja).
```python
# Twój kod — broadcasting: macierz * skalar
```

**Zadanie 1b:** Każdy sklep daje inny rabat: Centrum 10%, Galeria 5%, Online 15%.
```python
rabaty = np.array([0.10, 0.05, 0.15])
# Twój kod — broadcasting: macierz (4×3) * wektor (3,)
```

**Zadanie 1c:** Każdy produkt ma inną marżę: A=30%, B=40%, C=25%, D=50%.
```python
marza = np.array([[0.30], [0.40], [0.25], [0.50]])
# Twój kod — broadcasting: macierz (4×3) * wektor kolumnowy (4×1)
# Oblicz koszt zakupu (cena / (1 + marża))
```

### Sprawdzenie ✅

- 1a: Cena A w Centrum po inflacji = 31.49
- 1b: Cena B Online po rabacie = 40.79
- 1c: Koszt zakupu D w Centrum = 66.66

---

## Ćwiczenie 2: Reshape i łączenie danych (20 min)

### Cel
Zmień kształt danych i połącz tablice z różnych źródeł.

### Zadanie 2a — Reshape

```python
# Dane miesięczne z jednego roku (flat)
dane_flat = np.array([120, 135, 98, 142, 167, 189, 201, 178, 156, 143, 198, 221])

# Przekształć na kwartały (4 kwartały × 3 miesiące)
kwartaly = dane_flat.reshape(4, 3)
print(f"Kwartały:\n{kwartaly}")
print(f"Suma per kwartał: {kwartaly.sum(axis=1)}")
print(f"Najlepszy kwartał: Q{kwartaly.sum(axis=1).argmax() + 1}")
```

### Zadanie 2b — Stacking

```python
# Dane z 3 oddziałów (osobne tablice)
warszawa = np.array([150, 160, 170, 180])
krakow = np.array([120, 130, 140, 150])
wroclaw = np.array([90, 100, 110, 120])

# Połącz w macierz (3 oddziały × 4 kwartały)
wszystkie = np.vstack([warszawa, krakow, wroclaw])
print(f"Wszystkie:\n{wszystkie}")
print(f"Suma per oddział: {wszystkie.sum(axis=1)}")
print(f"Suma per kwartał: {wszystkie.sum(axis=0)}")
```

### Zadanie 2c — Praktyczne

```python
# Masz dane o sprzedaży 6 produktów jako wektor
sprzedaz_flat = np.array([100, 200, 150, 300, 250, 180, 120, 220, 170, 310, 260, 190])
# Wiesz, że to 6 produktów × 2 miesiące

# 1. Reshape na macierz 6×2
# 2. Oblicz średnią sprzedaż per produkt
# 3. Oblicz zmianę między miesiącem 1 a 2 (kolumna 2 - kolumna 1)
```

---

## Ćwiczenie 3: Analiza danych finansowych (30 min)

### Cel
Samodzielna analiza danych finansowych firmy z użyciem zaawansowanych operacji NumPy.

### Dane

```python
np.random.seed(2026)

# 8 pracowników, dane roczne
pracownicy = ['Anna', 'Jan', 'Ewa', 'Marek', 'Kasia', 'Piotr', 'Zofia', 'Tomek']
pensje = np.array([5500, 7200, 4800, 9100, 6300, 4200, 8500, 5800])
staz = np.array([3, 8, 2, 15, 5, 1, 12, 4])
oceny = np.array([4.2, 3.8, 4.5, 4.0, 4.7, 3.5, 4.3, 3.9])

# Sprzedaż miesięczna 4 produktów przez 6 miesięcy
produkty_nazwy = ['Laptop', 'Tablet', 'Smartfon', 'Akcesorium']
sprzedaz = np.random.randint(20, 200, size=(4, 6))
ceny_produktow = np.array([3500, 1800, 2500, 150])
```

### Zadania

**Zadanie 3a: Analiza wynagrodzeń**
```python
# 1. Średnia, mediana, std pensji
# 2. Kto zarabia powyżej średniej? (nazwy)
# 3. Kto zarabia poniżej mediany? (nazwy)
# 4. Rozstęp (max - min) i IQR
```

**Zadanie 3b: System premii (np.where)**
```python
# Zasady premii:
# - ocena >= 4.5 → premia 2000 zł
# - ocena >= 4.0 → premia 1000 zł
# - ocena < 4.0 → premia 0 zł
# Użyj zagnieżdżonego np.where

# Oblicz nowe wynagrodzenie (pensja + premia)
# Kto dostał najwyższą premię?
```

**Zadanie 3c: Ranking (argsort)**
```python
# Posortuj pracowników wg pensji (od najwyższej)
# Wyświetl ranking: pozycja, imię, pensja, staż
```

**Zadanie 3d: Korelacja**
```python
# Oblicz korelację: staż vs pensja
# Oblicz korelację: staż vs ocena
# Który związek jest silniejszy?
```

**Zadanie 3e: Analiza sprzedaży (broadcasting)**
```python
# Oblicz przychód: sprzedaz (4×6) * ceny_produktow (4,) — UWAGA na broadcasting!
# Podpowiedź: ceny muszą być kolumną (4×1)

# Który produkt przyniósł największy łączny przychód?
# Który miesiąc był najlepszy (łącznie)?
# Trend: porównaj pierwsze 3 miesiące vs ostatnie 3
```

### Sprawdzenie ✅

- 3a: Średnia pensji = 6425.0 zł
- 3b: Zagnieżdżony where: `np.where(oceny >= 4.5, 2000, np.where(oceny >= 4.0, 1000, 0))`
- 3d: Korelacja staż-pensja powinna być dodatnia (wyższy staż = wyższa pensja)

---

## Ćwiczenie 4: Generowanie danych + commit (15 min)

### Cel
Wygeneruj realistyczne dane biznesowe i zapisz analizę.

### Zadanie

```python
np.random.seed(42)

# Wygeneruj dane o 100 klientach sklepu:
# - wiek: rozkład normalny, średnia 35, std 10, zaokrąglony do int, min 18
# - wydatki_miesiecznie: rozkład normalny, średnia 500, std 200, min 0
# - liczba_wizyt: rozkład Poissona, lambda=5

# Podpowiedź: np.clip() ogranicza wartości do zakresu
wiek = np.clip(np.random.normal(35, 10, 100).astype(int), 18, None)
wydatki = np.clip(np.random.normal(500, 200, 100), 0, None)
wizyty = np.random.poisson(5, 100)

# Analiza:
# 1. Statystyki opisowe każdej zmiennej
# 2. Korelacja wiek vs wydatki
# 3. Korelacja wizyty vs wydatki
# 4. Segmentacja: "wysoki wydatek" (> średnia + std) vs "niski wydatek" (< średnia - std) vs "średni"
```

### Commit

```bash
git add lab04_numpy_advanced.ipynb
git commit -m "L04: NumPy zaawansowane — broadcasting, analiza finansowa"
git push
```

---

## Podsumowanie

Po dzisiejszych zajęciach umiesz:
- ✅ Używać broadcastingu do obliczeń na danych różnych kształtów
- ✅ Zmieniać kształt tablic (reshape, flatten, stacking)
- ✅ Stosować where, sort, argsort, korelację
- ✅ Generować realistyczne dane syntetyczne

**Na następnych zajęciach:** Pandas — DataFrame, wczytywanie CSV, selekcja danych. NumPy pod spodem, ale z etykietami i wygodą.

---

## Jeśli utkniesz

| Problem | Rozwiązanie |
|---------|-------------|
| `ValueError: operands could not be broadcast` | Sprawdź kształty: `print(a.shape, b.shape)`. Broadcasting wymaga kompatybilnych wymiarów |
| Nie rozumiem broadcasting | Wyobraź sobie że mniejsza tablica jest "rozciągana" do rozmiaru większej. (3,) + (4,3) -> każdy wiersz + wektor |
| `reshape(-1, 4)` — co oznacza `-1`? | `-1` = "oblicz automatycznie". Jeśli masz 12 elementów i chcesz 4 kolumny -> `-1` wylicza 3 wiersze |
| `np.where` z wieloma warunkami | Zagnieżdżaj: `np.where(w1, val1, np.where(w2, val2, val3))` |
| Wynik operacji ma zły kształt | Sprawdź: `print(wynik.shape)` — porównaj z oczekiwanym |
