# S02 Lab (zaoczne) — Ćwiczenia laboratoryjne

## Temat: NumPy — tablice, operacje wektorowe, broadcasting, analiza danych

**Programowanie w Pythonie II** | Spotkanie 2 (zaoczne)
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne
**Prowadzący:** ta sama osoba co wykład

---

## Ćwiczenie 1: Tworzenie tablic i atrybuty (15 min)

### Cel
Naucz się tworzyć tablice NumPy różnymi sposobami i odczytywać ich atrybuty (shape, dtype, ndim).

### Krok 1 — Utwórz notebook

1. Otwórz VS Code, aktywuj venv
2. Utwórz notebook `s02_numpy.ipynb`
3. Pierwsza komórka Markdown:

```markdown
# Spotkanie 2 — NumPy
**Autor:** [Twoje imię i nazwisko]
**Data:** [data zajęć]
```

### Krok 2 — Import

```python
import numpy as np
```

### Krok 3 — Tworzenie tablic

Utwórz każdą tablicę w osobnej komórce:

```python
# 1. Z listy — przychody miesięczne (tys. zł)
przychody = np.array([45.2, 51.8, 48.3, 55.1, 62.7, 58.9])
print(f"Przychody: {przychody}")
print(f"Dtype: {przychody.dtype}")
```

```python
# 2. Zera — inicjalizacja macierzy wyników 4x3
wyniki = np.zeros((4, 3))
print(f"Wyniki:\n{wyniki}")
```

```python
# 3. Jedynki — macierz współczynników 3x3
wspolczynniki = np.ones((3, 3))
print(f"Współczynniki:\n{wspolczynniki}")
```

```python
# 4. Sekwencja — numery faktur od 1000 do 1050, co 5
faktury = np.arange(1000, 1051, 5)
print(f"Numery faktur: {faktury}")
```

```python
# 5. Równomiernie rozłożone — 6 progów rabatowych od 0% do 25%
progi = np.linspace(0, 0.25, 6)
print(f"Progi rabatowe: {progi}")
```

```python
# 6. Losowe — 15 ocen pracowników (1-5)
np.random.seed(42)
oceny = np.random.randint(1, 6, size=15)
print(f"Oceny: {oceny}")
```

### Krok 4 — Atrybuty

```python
# Zbadaj macierz 2D
macierz = np.array([[10, 20, 30],
                     [40, 50, 60],
                     [70, 80, 90],
                     [100, 110, 120]])

print(f"Tablica:\n{macierz}")
print(f"shape: {macierz.shape}")    # → (4, 3)
print(f"ndim: {macierz.ndim}")      # → 2
print(f"size: {macierz.size}")      # → 12
print(f"dtype: {macierz.dtype}")    # → int64
```

**Zadanie samodzielne:** Utwórz tablicę 2D z losowymi liczbami zmiennoprzecinkowymi (rozkład normalny, średnia=100, std=15, kształt 5x4). Wyświetl jej atrybuty.

```python
# Twój kod tutaj
```

### Sprawdzenie

- Potrafisz tworzyć tablice: `array`, `zeros`, `ones`, `arange`, `linspace`, `random`
- Odczytujesz atrybuty: `shape`, `ndim`, `size`, `dtype`
- Tablica z zadania samodzielnego: `shape=(5, 4)`, `ndim=2`, `size=20`, `dtype=float64`

---

## Ćwiczenie 2: Operacje wektorowe vs pętla for — benchmark (20 min)

### Cel
Porównaj wydajność list Pythona i tablic NumPy. Przekonaj się, dlaczego operacje wektorowe zastępują pętle.

### Krok 1 — Benchmark mnożenia

```python
import time

rozmiar = 1_000_000

# Przygotowanie danych
lista = list(range(rozmiar))
tablica = np.array(lista)

# Test: pomnóż każdy element przez 2
start = time.perf_counter()
wynik_lista = [x * 2 for x in lista]
czas_lista = time.perf_counter() - start

start = time.perf_counter()
wynik_numpy = tablica * 2
czas_numpy = time.perf_counter() - start

print(f"=== Mnożenie x2 ({rozmiar:,} elementów) ===")
print(f"Lista Python: {czas_lista*1000:.1f} ms")
print(f"NumPy:        {czas_numpy*1000:.1f} ms")
print(f"NumPy jest {czas_lista/czas_numpy:.0f}x szybszy!")
```

### Krok 2 — Benchmark sumowania

```python
start = time.perf_counter()
suma_lista = sum(lista)
czas_lista = time.perf_counter() - start

start = time.perf_counter()
suma_numpy = tablica.sum()
czas_numpy = time.perf_counter() - start

print(f"\n=== Suma ({rozmiar:,} elementów) ===")
print(f"Lista Python: {czas_lista*1000:.1f} ms")
print(f"NumPy:        {czas_numpy*1000:.1f} ms")
print(f"NumPy jest {czas_lista/czas_numpy:.0f}x szybszy!")
```

### Krok 3 — Benchmark filtrowania

```python
start = time.perf_counter()
filtr_lista = [x for x in lista if x > 500_000]
czas_lista = time.perf_counter() - start

start = time.perf_counter()
filtr_numpy = tablica[tablica > 500_000]
czas_numpy = time.perf_counter() - start

print(f"\n=== Filtrowanie > 500k ({rozmiar:,} elementów) ===")
print(f"Lista Python: {czas_lista*1000:.1f} ms")
print(f"NumPy:        {czas_numpy*1000:.1f} ms")
print(f"NumPy jest {czas_lista/czas_numpy:.0f}x szybszy!")
```

### Krok 4 — Porównanie wyraziste: obliczenia biznesowe

```python
# Scenariusz: 1 mln transakcji, oblicz wartość brutto (z VAT 23%)
transakcje = np.random.uniform(10, 1000, size=rozmiar)
transakcje_lista = transakcje.tolist()

# Pętla for
start = time.perf_counter()
brutto_lista = [x * 1.23 for x in transakcje_lista]
czas_lista = time.perf_counter() - start

# NumPy
start = time.perf_counter()
brutto_numpy = transakcje * 1.23
czas_numpy = time.perf_counter() - start

print(f"\n=== VAT na {rozmiar:,} transakcji ===")
print(f"Pętla for: {czas_lista*1000:.1f} ms")
print(f"NumPy:     {czas_numpy*1000:.1f} ms")
print(f"Przyspieszenie: {czas_lista/czas_numpy:.0f}x")
```

### Krok 5 — Podsumowanie benchmarku

Dodaj komórkę Markdown z wnioskami:

```markdown
## Wnioski z benchmarku
- NumPy jest **...x** szybszy w mnożeniu
- NumPy jest **...x** szybszy w sumowaniu
- NumPy jest **...x** szybszy w filtrowaniu
- **Wniosek:** przy danych > 1000 elementów zawsze używaj NumPy zamiast list i pętli
```

### Sprawdzenie

- Benchmark działa i wyświetla czasy
- NumPy jest typowo 10-50x szybszy (zależy od operacji i sprzętu)
- Uzupełniłeś wnioski własnymi liczbami

---

## Ćwiczenie 3: Filtrowanie, axis i broadcasting (25 min)

### Cel
Użyj filtrowania boolean, operacji na osiach i broadcastingu do analizy danych biznesowych.

### Dane — sieć sklepów

```python
np.random.seed(2026)

# 5 sklepów, sprzedaż w 4 kwartałach (tys. zł)
sklepy = ['Centrum', 'Galeria', 'Outlet', 'Online', 'Dworzec']
kwartaly = ['Q1', 'Q2', 'Q3', 'Q4']

sprzedaz = np.array([
    [120, 135, 98,  142],   # Centrum
    [89,  102, 115, 128],   # Galeria
    [67,  73,  81,  94],    # Outlet
    [210, 245, 278, 312],   # Online
    [45,  52,  48,  55],    # Dworzec
])
```

### Zadanie 3a — Agregacje z axis

```python
# 1. Roczna sprzedaż każdego sklepu (axis=1)
roczna = sprzedaz.sum(axis=1)
for s, r in zip(sklepy, roczna):
    print(f"  {s:10s}: {r} tys. zł")

# 2. Sprzedaż per kwartał (axis=0)
kwartalna = sprzedaz.sum(axis=0)
for k, s in zip(kwartaly, kwartalna):
    print(f"  {k}: {s} tys. zł")

# 3. Najlepszy sklep i najlepszy kwartał
print(f"Najlepszy sklep:   {sklepy[roczna.argmax()]}")
print(f"Najlepszy kwartał: {kwartaly[kwartalna.argmax()]}")
```

### Zadanie 3b — Filtrowanie boolean

```python
# 1. Które sklepy miały roczną sprzedaż > 400 tys. zł?
maska = roczna > 400
print(f"Sklepy > 400 tys. roczne: {np.array(sklepy)[maska]}")

# 2. Które wartości kwartalne przekroczyły 200 tys. zł?
print(f"Ile kwartałów > 200: {(sprzedaz > 200).sum()}")

# 3. Średnia sprzedaż TYLKO dla sklepów stacjonarnych (bez Online)
stacjonarne = sprzedaz[np.array([True, True, True, False, True])]
print(f"Średnia stacjonarne: {stacjonarne.mean():.1f} tys. zł")
```

### Zadanie 3c — Broadcasting

```python
# Każdy kwartał ma inny współczynnik inflacji
inflacja = np.array([1.00, 1.02, 1.04, 1.06])

# 1. Przelicz sprzedaż na wartości realne (ceny stałe Q1)
sprzedaz_realna = sprzedaz / inflacja    # broadcasting (5x4) / (4,)
print(f"Sprzedaż realna:\n{sprzedaz_realna.astype(int)}")

# 2. Każdy sklep ma inny cel roczny (tys. zł)
cele = np.array([[500], [450], [350], [1000], [250]])  # kolumna (5x1)

# Oblicz % realizacji celu per kwartał (cel/4 per kwartał)
realizacja = sprzedaz / (cele / 4) * 100   # broadcasting (5x4) / (5x1)
print(f"\n% realizacji celu kwartalnego:")
for i, s in enumerate(sklepy):
    print(f"  {s:10s}: {realizacja[i].astype(int)}")
```

### Zadanie 3d — Samodzielne (5 min)

```python
# Analiza samodzielna:
# 1. Który sklep miał NAJWYŻSZĄ sprzedaż w Q4?
# 2. Jaka jest średnia kwartalna sprzedaż sklepu Online?
# 3. O ile % wzrosła sprzedaż między Q1 a Q4 (dla każdego sklepu)?
# 4. Ile sklepów przekroczyło cel roczny?

# Twój kod tutaj
```

### Sprawdzenie

- 3a: Najlepszy sklep = **Online** (1045 tys. zł), najlepszy kwartał = **Q4** (731 tys. zł)
- 3b: Sklepy > 400 tys. roczne: **Centrum** (495), **Galeria** (434), **Online** (1045). Kwartały > 200: **4** (wszystkie kwartały Online: Q1=210, Q2=245, Q3=278, Q4=312)
- 3c: Cel roczny Online = 1000 tys., realizacja = 1045/1000 = 104.5%
- 3d odpowiedzi:
  - Q4 najwyższy: **Online** (312 tys. zł)
  - Średnia kwartalna Online: **261.25 tys. zł**
  - Wzrost Q1->Q4: Centrum +18.3%, Galeria +43.8%, Outlet +40.3%, Online +48.6%, Dworzec +22.2%
  - Sklepy powyżej celu: Centrum (495 > 500? NIE), Galeria (434 < 450? NIE), Outlet (315 < 350? NIE), Online (1045 > 1000? TAK), Dworzec (200 < 250? NIE) → **1 sklep** (Online)

---

## Ćwiczenie 4: Reshape + analiza ocen studentów (20 min)

### Cel
Zmień kształt tablic i przeprowadź analizę danych edukacyjnych z użyciem zaawansowanych operacji NumPy.

### Dane — oceny studentów

```python
np.random.seed(42)

# 8 studentów, oceny z 6 przedmiotów (flat — np. z arkusza CSV)
studenci = ['Anna', 'Bartek', 'Celina', 'Dawid', 'Ewa', 'Filip', 'Gosia', 'Hubert']
przedmioty = ['Matematyka', 'Fizyka', 'Python I', 'Statystyka', 'Ekonomia', 'Angielski']

# Dane przyszły jako płaski wektor (48 wartości)
oceny_flat = np.array([
    4.0, 3.5, 5.0, 4.5, 3.0, 4.5,   # Anna
    3.0, 2.0, 4.0, 3.5, 4.0, 3.5,   # Bartek
    5.0, 4.5, 5.0, 5.0, 4.0, 5.0,   # Celina
    3.5, 3.0, 3.0, 2.5, 3.5, 3.0,   # Dawid
    4.5, 4.0, 4.5, 4.0, 4.5, 4.0,   # Ewa
    2.0, 2.5, 3.0, 2.0, 3.0, 2.5,   # Filip
    4.0, 3.5, 4.5, 4.0, 3.5, 4.0,   # Gosia
    3.5, 3.0, 4.0, 3.5, 3.0, 3.5,   # Hubert
])
```

### Krok 1 — Reshape

```python
# Przekształć flat → macierz 8 studentów x 6 przedmiotów
oceny = oceny_flat.reshape(8, 6)
print(f"Macierz ocen (8x6):\n{oceny}")
print(f"Shape: {oceny.shape}")
```

### Krok 2 — Analiza per student (axis=1)

```python
# Średnia ocen każdego studenta
srednie = oceny.mean(axis=1)
for s, sr in zip(studenci, srednie):
    print(f"  {s:8s}: {sr:.2f}")

# Najlepszy i najsłabszy student
print(f"\nNajlepszy: {studenci[srednie.argmax()]} ({srednie.max():.2f})")
print(f"Najsłabszy: {studenci[srednie.argmin()]} ({srednie.min():.2f})")
```

### Krok 3 — Analiza per przedmiot (axis=0)

```python
# Średnia per przedmiot
srednie_przedm = oceny.mean(axis=0)
for p, sr in zip(przedmioty, srednie_przedm):
    print(f"  {p:12s}: {sr:.2f}")

# Najtrudniejszy przedmiot (najniższa średnia)
print(f"\nNajtrudniejszy: {przedmioty[srednie_przedm.argmin()]} ({srednie_przedm.min():.2f})")

# Najłatwiejszy przedmiot
print(f"Najłatwiejszy: {przedmioty[srednie_przedm.argmax()]} ({srednie_przedm.max():.2f})")
```

### Krok 4 — Filtrowanie i np.where

```python
# Studenci zagrożeni (średnia < 3.0)
zagrozeni = srednie < 3.0
print(f"Zagrożeni: {np.array(studenci)[zagrozeni]}")

# Status zdania każdego przedmiotu (ocena >= 3.0 = ZDAŁ)
status = np.where(oceny >= 3.0, 'ZDAL', 'NZAL')
print(f"\nStatus:\n{status}")

# Ile niezdanych ocen ma każdy student?
niezdane = (oceny < 3.0).sum(axis=1)
for s, n in zip(studenci, niezdane):
    if n > 0:
        print(f"  {s:8s}: {n} niezdanych")
```

### Krok 5 — Broadcasting: standaryzacja ocen

```python
# Standaryzacja: (ocena - średnia_przedmiotu) / std_przedmiotu
# Kto wypada powyżej/poniżej normy?
std_przedm = oceny.std(axis=0)

# Broadcasting: (8x6) - (6,) / (6,)
oceny_std = (oceny - srednie_przedm) / std_przedm
print(f"Oceny standaryzowane (z-score):\n{oceny_std.round(2)}")

# Kto ma najwyższy z-score z Pythona I (kolumna 2)?
python_idx = 2
print(f"\nNajlepszy z Pythona I (standaryzowany): {studenci[oceny_std[:, python_idx].argmax()]}")
```

### Sprawdzenie

- Reshape: macierz `(8, 6)`, 48 elementów
- Najlepszy student: **Celina** (4.75)
- Najsłabszy student: **Filip** (2.50)
- Najtrudniejszy przedmiot: **Fizyka** (3.25)
- Najłatwiejszy przedmiot: **Python I** (4.12)
- Zagrożeni (< 3.0): **Filip** (2.50)
- Niezdane: Bartek (1 — Fizyka), Dawid (1 — Statystyka), Filip (4 — Matematyka, Fizyka, Statystyka, Angielski)

---

## Ćwiczenie 5 (bonus): Syntetyczny dataset + statystyki (10 min)

### Cel
Wygeneruj realistyczne dane pracowników i przeprowadź pełną analizę opisową.

### Krok 1 — Generowanie danych

```python
np.random.seed(2026)

n = 50  # 50 pracowników

# Wynagrodzenie brutto (rozkład normalny)
pensje = np.clip(np.random.normal(loc=6000, scale=1500, size=n), 3500, 15000).astype(int)

# Staż pracy w latach (rozkład jednostajny)
staz = np.random.randint(1, 21, size=n)

# Ocena roczna (1.0 - 5.0, krok 0.5)
oceny_mozliwe = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
oceny_roczne = np.random.choice(oceny_mozliwe, size=n)

# Dział (tekst)
dzialy = np.random.choice(['IT', 'HR', 'Sprzedaż', 'Finanse', 'Marketing'], size=n)
```

### Krok 2 — Statystyki opisowe

```python
print("=== WYNAGRODZENIA ===")
print(f"Średnia:  {pensje.mean():.0f} zł")
print(f"Mediana:  {np.median(pensje):.0f} zł")
print(f"Std:      {pensje.std():.0f} zł")
print(f"Min/Max:  {pensje.min()} / {pensje.max()} zł")
print(f"Q1 (25%): {np.percentile(pensje, 25):.0f} zł")
print(f"Q3 (75%): {np.percentile(pensje, 75):.0f} zł")
print(f"IQR:      {np.percentile(pensje, 75) - np.percentile(pensje, 25):.0f} zł")
```

### Krok 3 — Analiza segmentowa

```python
# Podział na segmenty wg oceny rocznej
wysoka = oceny_roczne >= 4.0
niska = oceny_roczne < 3.0

print(f"\n=== SEGMENTACJA ===")
print(f"Pracownicy z wysoką oceną (>=4.0): {wysoka.sum()}")
print(f"  Średnia pensja: {pensje[wysoka].mean():.0f} zł")
print(f"  Średni staż: {staz[wysoka].mean():.1f} lat")

print(f"\nPracownicy z niską oceną (<3.0): {niska.sum()}")
print(f"  Średnia pensja: {pensje[niska].mean():.0f} zł")
print(f"  Średni staż: {staz[niska].mean():.1f} lat")
```

### Krok 4 — Analiza per dział

```python
# Statystyki per dział
unikalne_dzialy = np.unique(dzialy)
print(f"\n=== ANALIZA PER DZIAŁ ===")
for dzial in unikalne_dzialy:
    maska = dzialy == dzial
    print(f"\n{dzial}:")
    print(f"  Pracowników: {maska.sum()}")
    print(f"  Średnia pensja: {pensje[maska].mean():.0f} zł")
    print(f"  Średnia ocena: {oceny_roczne[maska].mean():.2f}")
    print(f"  Średni staż: {staz[maska].mean():.1f} lat")
```

### Krok 5 — Korelacje

```python
# Korelacja: staż vs pensja
r_staz_pensja = np.corrcoef(staz, pensje)[0, 1]
print(f"\n=== KORELACJE ===")
print(f"Staż vs pensja: r = {r_staz_pensja:.3f}")

# Korelacja: ocena vs pensja
r_ocena_pensja = np.corrcoef(oceny_roczne, pensje)[0, 1]
print(f"Ocena vs pensja: r = {r_ocena_pensja:.3f}")

# Interpretacja
for nazwa, r in [("Staż-Pensja", r_staz_pensja), ("Ocena-Pensja", r_ocena_pensja)]:
    if abs(r) > 0.7:
        sila = "silna"
    elif abs(r) > 0.4:
        sila = "umiarkowana"
    else:
        sila = "słaba"
    kierunek = "dodatnia" if r > 0 else "ujemna"
    print(f"  {nazwa}: {sila} korelacja {kierunek}")
```

### Krok 6 — Commit

```bash
git add s02_numpy.ipynb
git commit -m "S02: NumPy — tablice, operacje, broadcasting, analiza"
git push
```

### Sprawdzenie

- Wygenerowano 50 rekordów z seed(2026)
- Statystyki się wyświetlają poprawnie
- Segmentacja i analiza per dział daje sensowne wyniki
- Korelacje mają wartości w zakresie [-1, 1]
- Notebook jest na GitHubie

---

## Podsumowanie

Po dzisiejszych zajęciach umiesz:
- Tworzyć tablice NumPy (7 sposobów) i odczytywać atrybuty
- Mierzyć przewagę wydajnościową NumPy nad listami Pythona
- Stosować operacje wektorowe, filtrowanie boolean i axis
- Używać broadcastingu do obliczeń na tablicach różnych kształtów
- Zmieniać kształt tablic (reshape) i generować dane syntetyczne
- Przeprowadzać analizę statystyczną z NumPy

**Na następnym spotkaniu (S03):** Pandas — DataFrame, wczytywanie CSV, selekcja i filtrowanie danych. NumPy to fundamenty — Pandas doda etykiety i mnóstwo wygodnych metod.
