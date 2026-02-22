# S02 Wykład (zaoczne) — Plan zajęć dla prowadzącego

## Temat: NumPy — od podstaw do zaawansowanych technik

### Informacje organizacyjne
- **Czas:** 90 min (wykład) + 90 min (lab) = 180 min razem
- **Forma:** wykład konwersatoryjny z live coding
- **Prowadzący:** ta sama osoba prowadzi wykład i lab
- **Potrzebne:** komputer z projektorem, VS Code, terminal, venv z numpy
- **Kontekst:** łączy treści z W03 (NumPy podstawy) i W04 (NumPy zaawansowane) — skondensowane tempo
- **Założenie:** studenci mają skonfigurowane środowisko z S01 (Python, uv, VS Code, Git)

### Efekty uczenia się (Bloom)
Po tym spotkaniu osoba studiująca:
1. **Tworzy** tablice NumPy różnymi sposobami i rozpoznaje ich atrybuty (Bloom 3)
2. **Stosuje** indeksowanie, slicing i filtrowanie boolean do wydobywania danych z tablic 1D i 2D (Bloom 3)
3. **Wykonuje** operacje wektorowe i agregacje na osiach (axis=0, axis=1) (Bloom 3)
4. **Wyjaśnia** mechanizm broadcastingu i stosuje go w obliczeniach biznesowych (Bloom 2-3)
5. **Zmienia** kształt tablic za pomocą reshape i generuje dane syntetyczne (Bloom 3)

### Plan minutowy — WYKŁAD (90 min)

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **WPROWADZENIE** | Czym jest NumPy, dlaczego nie listy Pythona | Rozmowa |
| 0:05-0:25 | **MATERIAŁ 1** | Tworzenie tablic — 7 sposobów + atrybuty | Live coding |
| 0:25-0:40 | **MATERIAŁ 2** | Indeksowanie i slicing — 1D i 2D | Live coding |
| 0:40-0:55 | **MATERIAŁ 3** | Operacje wektorowe, filtrowanie boolean, axis | Live coding |
| 0:55-1:05 | **PRZERWA** | 10 minut | — |
| 1:05-1:20 | **MATERIAŁ 4** | Broadcasting — kluczowa koncepcja | Live coding |
| 1:20-1:30 | **MATERIAŁ 5** | Reshape + generowanie danych (random) | Live coding |
| 1:30-1:35 | **AKTYWNOŚĆ** | Mini-ćwiczenie na projektorze — 3 pytania | Studenci odpowiadają |
| 1:35-1:40 | **PODSUMOWANIE** | 4 bullet points, przejście do labu | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — WPROWADZENIE

> "Dzień dobry. Dzisiaj wchodzimy w NumPy — bibliotekę, która jest fundamentem całego ekosystemu data science w Pythonie. Pandas, Matplotlib, scikit-learn — wszystko pod spodem używa NumPy."

> "Pytanie na rozgrzewkę: ile czasu zajmuje pomnożenie miliona liczb przez 2? Z listą Pythona — około 100 milisekund. Z NumPy — 2 milisekundy. **50 razy szybciej**. Dlaczego?"

> "Dwa powody. Pierwszy: NumPy przechowuje dane w ciągłym bloku pamięci — jednorodne typy, brak narzutu obiektów Pythona. Drugi: operacje wektorowe — C pod spodem, bez pętli Pythona."

> "Jeśli NumPy to fundamenty domu, to Pandas to ściany, a Matplotlib to dekoracja. Dzisiaj stawiamy fundamenty."

---

### 0:05-0:25 — MATERIAŁ 1: Tworzenie tablic (20 min)

**[Otwórz nowy notebook lub terminal VS Code]**

> "Siedem sposobów tworzenia tablic. Nie musicie zapamiętać wszystkich — najważniejsze to `array`, `zeros`, `arange` i `random`."

**Import:**

```python
import numpy as np   # konwencja: zawsze np
```

> "`import numpy as np` — to konwencja. Cały świat Pythona pisze `np`. Nie `numpy`, nie `num`. Zawsze `np`."

**Z listy:**

```python
a = np.array([10, 20, 30, 40, 50])
print(f"Tablica: {a}")
print(f"Typ: {type(a)}")     # numpy.ndarray
print(f"Dtype: {a.dtype}")   # int64
```

> "Najprostszy sposób — zawijamy listę w `np.array()`. NumPy sam rozpoznaje typ danych: same liczby całkowite → `int64`."

**Zeros, ones:**

```python
zera = np.zeros(5)
print(f"Zera: {zera}")        # [0. 0. 0. 0. 0.]

jedynki = np.ones((3, 4))    # 3 wiersze, 4 kolumny
print(f"Jedynki 3x4:\n{jedynki}")
```

> "Zera i jedynki do inicjalizacji. Zwróćcie uwagę: `ones((3,4))` — krotka w środku, bo podajemy kształt tablicy."

**Arange i linspace:**

```python
sekwencja = np.arange(0, 10, 2)     # start, stop, krok
print(f"arange(0,10,2): {sekwencja}")  # [0, 2, 4, 6, 8]

rownomierne = np.linspace(0, 1, 5)   # start, stop, ile punktów
print(f"linspace(0,1,5): {rownomierne}")  # [0, 0.25, 0.5, 0.75, 1]
```

> "`arange` — jak `range()`, ale zwraca tablicę NumPy. Działa też z floatami. `linspace` — podajesz start, stop i **ile punktów** chcesz. Idealne do wykresów."

**Random:**

```python
np.random.seed(42)   # powtarzalność wyników
losowe_int = np.random.randint(1, 100, size=10)
print(f"Losowe int 1-99: {losowe_int}")

losowe_normal = np.random.randn(5)
print(f"Rozkład normalny: {losowe_normal}")
```

> "Dane losowe. `randint` — losowe całkowite. `randn` — rozkład normalny (średnia 0, odchylenie 1). `seed(42)` — zapewnia powtarzalność: te same 'losowe' liczby za każdym razem."

**Atrybuty tablicy:**

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Tablica:\n{m}")
print(f"shape: {m.shape}")    # (2, 3) — 2 wiersze, 3 kolumny
print(f"ndim: {m.ndim}")      # 2 wymiary
print(f"size: {m.size}")      # 6 elementów
print(f"dtype: {m.dtype}")    # int64
```

> "Każda tablica ma atrybuty. `shape` to najważniejszy — mówi jaki jest kształt. `(2, 3)` = 2 wiersze, 3 kolumny. `ndim` — ile wymiarów. `size` — ile elementów łącznie. `dtype` — typ danych."

---

### 0:25-0:40 — MATERIAŁ 2: Indeksowanie i slicing (15 min)

> "Mamy tablicę. Teraz — jak wyciągać z niej dane. To kluczowa umiejętność, będzie wam towarzyszyć przez cały kurs."

**Indeksowanie 1D:**

```python
dane = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(f"dane[0]: {dane[0]}")      # 10 — pierwszy
print(f"dane[-1]: {dane[-1]}")    # 100 — ostatni
print(f"dane[3]: {dane[3]}")      # 40 — czwarty (indeks od 0!)
```

> "Indeksowanie od zera — znacie z Pythona I. Minus oznacza od końca."

**Slicing 1D:**

```python
print(f"dane[2:5]: {dane[2:5]}")     # [30, 40, 50] — od 2 do 5 (bez 5!)
print(f"dane[:3]: {dane[:3]}")       # [10, 20, 30] — pierwsze 3
print(f"dane[7:]: {dane[7:]}")       # [80, 90, 100] — od 7 do końca
print(f"dane[::2]: {dane[::2]}")     # [10, 30, 50, 70, 90] — co drugi
```

> "Slicing: `start:stop:step`. Ważne: **stop nie jest włączony**. `dane[2:5]` to elementy o indeksach 2, 3, 4 — ale NIE 5."

**Indeksowanie 2D:**

```python
macierz = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print(f"macierz[0, 1]: {macierz[0, 1]}")   # 2 — wiersz 0, kolumna 1
print(f"macierz[1]: {macierz[1]}")          # [4, 5, 6] — cały wiersz
print(f"macierz[:, 0]: {macierz[:, 0]}")    # [1, 4, 7] — pierwsza kolumna
print(f"macierz[1:, 1:]:\n{macierz[1:, 1:]}")  # [[5,6],[8,9]]
```

> "2D: dwa indeksy oddzielone przecinkiem. `[wiersz, kolumna]`. Dwukropek sam = 'wszystko'. `[:, 0]` = wszystkie wiersze, kolumna zerowa. To jest fundament — w Pandas będziecie tego używać codziennie."

---

### 0:40-0:55 — MATERIAŁ 3: Operacje wektorowe, filtrowanie, axis (15 min)

> "Najlepsza cecha NumPy: **operacje wektorowe**. Żadnych pętli for."

**Arytmetyka wektorowa:**

```python
ceny = np.array([100, 200, 150, 300, 250])

print(f"Po rabacie 10%: {ceny * 0.9}")
print(f"Z VAT 23%: {ceny * 1.23}")
print(f"Podwyżka o 50: {ceny + 50}")
```

> "Nie ma pętli. `ceny * 0.9` — NumPy mnoży KAŻDY element przez 0.9. Jedna linia zamiast pętli for."

**Agregacje:**

```python
print(f"Suma: {ceny.sum()}")           # 1000
print(f"Średnia: {ceny.mean()}")       # 200.0
print(f"Std: {ceny.std():.2f}")        # 70.71
print(f"Min/Max: {ceny.min()} / {ceny.max()}")
print(f"Indeks max: {ceny.argmax()}")  # 3
```

> "Agregacje — jedna wartość z wielu. `argmax` — daje INDEKS maksymalnego elementu, nie wartość. Przydatne do znajdowania 'najlepszego produktu'."

**Filtrowanie boolean:**

```python
print(f"Ceny > 200: {ceny > 200}")           # [False, False, False, True, True]
print(f"Drogie: {ceny[ceny > 200]}")          # [300, 250]
print(f"Ile drogich: {(ceny > 200).sum()}")   # 2
```

> "**Filtrowanie boolean** — potężne narzędzie. `ceny > 200` tworzy maskę True/False. Wsadzamy ją w nawiasy kwadratowe — dostajemy tylko te elementy, gdzie True. `sum()` liczy True, bo True = 1."

> "Wyobraźcie sobie milion transakcji — 'pokaż wszystkie powyżej 1000 zł' — jedna linia kodu."

**Operacje między tablicami:**

```python
ilosci = np.array([5, 3, 10, 2, 7])
wartosc = ceny * ilosci
print(f"Wartość: {wartosc}")           # [500, 600, 1500, 600, 1750]
print(f"Obrót: {wartosc.sum()} zł")    # 4950
```

> "Mnożenie dwóch tablic — element po elemencie. Cena razy ilość = wartość. W Excelu byłoby kilka kolumn — tu jedna linia."

**axis=0 vs axis=1:**

```python
np.random.seed(42)
sprzedaz = np.random.randint(50, 500, size=(5, 4))
produkty = ['Laptop', 'Mysz', 'Klawiatura', 'Monitor', 'Słuchawki']
kwartaly = ['Q1', 'Q2', 'Q3', 'Q4']

print("Sprzedaż (szt.):")
for i, p in enumerate(produkty):
    print(f"  {p:12s}: {sprzedaz[i]}")

print(f"\nSuma per produkt (axis=1): {sprzedaz.sum(axis=1)}")
print(f"Suma per kwartał (axis=0): {sprzedaz.sum(axis=0)}")
print(f"Najlepszy produkt: {produkty[sprzedaz.sum(axis=1).argmax()]}")
print(f"Najlepszy kwartał: {kwartaly[sprzedaz.sum(axis=0).argmax()]}")
```

> "**axis=0** — działaj wzdłuż wierszy, wynik per kolumna. Jak 'w dół'. **axis=1** — działaj wzdłuż kolumn, wynik per wiersz. Jak 'w prawo'. To jest mylące na początku — ale zapamiętajcie: axis=0 zgniata wiersze, axis=1 zgniata kolumny."

---

### 0:55-1:05 — PRZERWA (10 min)

> "Przerwa. Po przerwie — broadcasting, reshape i generowanie danych."

---

### 1:05-1:20 — MATERIAŁ 4: Broadcasting (15 min)

> "Broadcasting — kluczowa koncepcja. Pozwala operować na tablicach **różnych kształtów**."

> "Właściwie już go używaliście. `ceny * 0.9` — skalar razy tablica — to broadcasting. NumPy 'rozciąga' 0.9 na cały kształt tablicy."

**Wektor wierszowy na macierz:**

```python
# Ceny 3 produktów w 4 kwartałach
ceny = np.array([[100, 110, 120, 130],
                  [200, 210, 220, 230],
                  [50,  55,  60,  65]])

# Rabat różny per kwartał
rabat = np.array([0.05, 0.10, 0.15, 0.20])

# Broadcasting: macierz (3x4) * wektor (4,)
ceny_po_rabacie = ceny * (1 - rabat)
print(f"Ceny:\n{ceny}")
print(f"Rabat per kwartał: {rabat}")
print(f"Po rabacie:\n{ceny_po_rabacie}")
```

> "Macierz 3x4 razy wektor 4 elementów. NumPy rozciąga wektor na 3 wiersze i mnoży. Każdy kwartał ma inny rabat — i działa na wszystkie produkty naraz."

**Wektor kolumnowy na macierz:**

```python
# Premia za markę — różna per produkt
premia = np.array([[1.2],    # +20%
                    [1.0],    # bez premii
                    [1.5]])   # +50%

ceny_z_premia = ceny * premia
print(f"Premia per produkt: {premia.flatten()}")
print(f"Ceny z premią:\n{ceny_z_premia}")
```

> "Wektor kolumnowy (3x1) razy macierz (3x4). NumPy rozciąga kolumnę na 4 kolumny. Każdy produkt ma inną premię."

**Reguła broadcastingu:**

> "Kiedy broadcasting działa? NumPy porównuje kształty **od prawej** do lewej. Wymiar musi być **taki sam** lub **równy 1**."

```python
# Działa:
# (3, 4) * (4,)   → 4 == 4  OK
# (3, 4) * (3, 1) → 4 != 1, ale 1 się rozciąga; 3 == 3  OK
# (3, 4) * (1, 4) → 3 != 1, ale 1 się rozciąga; 4 == 4  OK

# NIE działa:
# (3, 4) * (3,)   → 4 != 3  BŁĄD!
try:
    blad = ceny * np.array([1, 2, 3])
except ValueError as e:
    print(f"Błąd: {e}")
```

> "Najczęstszy błąd: macierz 3x4 razy wektor 3 elementów. NumPy patrzy od prawej: 4 nie równa się 3. Nie zadziała. Rozwiązanie: `reshape` na kolumnę `(3,1)`."

---

### 1:20-1:30 — MATERIAŁ 5: Reshape + generowanie danych (10 min)

> "Dwa tematy na koniec: zmiana kształtu tablic i generowanie danych."

**Reshape:**

```python
a = np.arange(12)
print(f"Flat: {a}")
print(f"Reshape 3x4:\n{a.reshape(3, 4)}")
print(f"Reshape 4x3:\n{a.reshape(4, 3)}")
print(f"Reshape -1 (auto):\n{a.reshape(3, -1)}")
```

> "`reshape(3, 4)` — 12 elementów staje się macierzą 3x4. `-1` oznacza: oblicz sam. 12 / 3 = 4. Warunek: iloczyn wymiarów musi się zgadzać."

**Flatten i stacking:**

```python
macierz = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Flatten: {macierz.flatten()}")    # [1, 2, 3, 4, 5, 6]

q1 = np.array([100, 200, 150])
q2 = np.array([120, 210, 160])
print(f"vstack:\n{np.vstack([q1, q2])}")       # pionowo
print(f"hstack: {np.hstack([q1, q2])}")        # poziomo
```

> "`flatten` spłaszcza macierz do 1D. `vstack` stawia tablice jedna pod drugą, `hstack` obok siebie. Przydatne gdy łączycie dane z różnych źródeł."

**Generowanie danych:**

```python
np.random.seed(42)

# Wynagrodzenia — rozkład normalny
wynagrodzenia = np.random.normal(loc=5000, scale=1000, size=100)
print(f"Wynagrodzenia — średnia: {wynagrodzenia.mean():.0f}, std: {wynagrodzenia.std():.0f}")

# Ceny — rozkład jednostajny
ceny = np.random.uniform(low=10, high=500, size=50)
print(f"Ceny — min: {ceny.min():.0f}, max: {ceny.max():.0f}")

# Zamówienia dziennie — Poisson
zamowienia = np.random.poisson(lam=20, size=30)
print(f"Zamówienia — średnia: {zamowienia.mean():.1f}")
```

> "Trzy rozkłady, które będziecie potrzebować: normalny (pensje, wzrost, temperatury), jednostajny (losowa cena z zakresu), Poisson (liczba zdarzeń — zamówienia dziennie, kliknięcia)."

**Statystyki opisowe:**

```python
dane = wynagrodzenia
print(f"Średnia: {dane.mean():.0f}")
print(f"Mediana: {np.median(dane):.0f}")
print(f"Q1: {np.percentile(dane, 25):.0f}")
print(f"Q3: {np.percentile(dane, 75):.0f}")
print(f"IQR: {np.percentile(dane, 75) - np.percentile(dane, 25):.0f}")
```

> "Pełen zestaw statystyk. Percentyle: Q1 = 25% danych poniżej, Q3 = 75% poniżej. IQR = Q3 - Q1 — miara rozproszenia odporna na wartości odstające. To wrócicie do tego przy statystyce."

---

### 1:30-1:35 — AKTYWNOŚĆ: mini-ćwiczenie (5 min)

> "Trzy szybkie pytania. Kto odpowie?"

**[Wyświetl na projektorze]**

```python
wynagrodzenia = np.array([4500, 5200, 3800, 7100, 6300, 4800, 5500, 8200, 3900, 6100])
```

**Pytania:**
1. Ile osób zarabia powyżej 5000 zł?
2. Jaka jest średnia? Mediana?
3. Broadcasting: `wynagrodzenia * np.array([1.1])` — co się stanie?

**Odpowiedzi:**

```python
print(f"1. Powyżej 5000: {(wynagrodzenia > 5000).sum()}")    # 6
print(f"2. Średnia: {wynagrodzenia.mean()}")                   # 5540.0
print(f"   Mediana: {np.median(wynagrodzenia)}")               # 5350.0
print(f"3. Podwyżka 10%: {wynagrodzenia * np.array([1.1])}")  # broadcasting działa
```

> "Broadcasting w pytaniu 3: skalar (tablica 1-elementowa) razy tablica 10-elementowa — NumPy rozciąga. Wynik: podwyżka 10% dla wszystkich."

---

### 1:35-1:40 — PODSUMOWANIE

> "Podsumujmy. Cztery kluczowe rzeczy z dzisiejszego wykładu:"

> "1. **Tworzenie tablic** — array, zeros, ones, arange, linspace, random. Atrybuty: shape, ndim, size, dtype."
> "2. **Indeksowanie i slicing** — 1D i 2D. `[wiersz, kolumna]`, `:` = wszystko."
> "3. **Operacje wektorowe** — arytmetyka, agregacje, filtrowanie boolean. Bez pętli!"
> "4. **Broadcasting** — operacje na tablicach różnych kształtów. Reguła: porównuj od prawej, wymiar = taki sam lub 1."

> "Teraz przechodzimy do labu — będziecie to ćwiczyć na danych. Za dwa tygodnie — Pandas. NumPy to fundamenty, Pandas doda etykiety i mnóstwo wygodnych metod."

---

## Uwagi dla prowadzącego

### Tempo zaoczne vs dzienne
- Na dziennych te treści zajmują **2 wykłady po 90 min** — tutaj masz 90 min na wszystko
- Skróty: pomiń szczegóły `ravel` vs `flatten`, zaawansowane operacje (np.where, argsort, unique, korelacja) — to studenci dostaną na labie lub w skrypcie
- Broadcasting: pokaż 2 przykłady, nie 4. Reguła broadcastingu musi być jasna
- Jeśli studenci nadążają — dodaj `np.where` jako bonus

### Najczęstsze pytania
- "Czy muszę pamiętać wszystkie sposoby tworzenia tablic?" → Nie, `array`, `zeros`, `arange`, `random` wystarczą na co dzień
- "Dlaczego axis=0 to kolumny, a nie wiersze?" → axis=0 to numer wymiaru (wiersze), `sum(axis=0)` zgniatuje ten wymiar → zostają kolumny
- "Kiedy broadcasting nie zadziała?" → Gdy wymiary od prawej nie pasują i żaden nie jest 1

### Materiały powiązane
- Notebook demo: `dzienne/W03/wyklad/numpy_demo.ipynb`
- Notebook zaawansowany: `dzienne/W04/wyklad/numpy_advanced_demo.ipynb`
- Skrypt studenta: `skryptdlastudentow/skrypt.md` — rozdział 3
