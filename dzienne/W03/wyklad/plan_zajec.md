# W03 Wykład — Plan zajęć dla prowadzącego

## Temat: NumPy — podstawy

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, terminal, venv z numpy
- **Przed wykładem:** otwórz `numpy_demo.ipynb` w VS Code

### Efekty uczenia się (Bloom)
Po tym wykładzie osoba studiująca:
1. **Tworzy** tablice NumPy różnymi sposobami: z listy, zeros, ones, arange, linspace, random (Bloom 3)
2. **Stosuje** indeksowanie i slicing do wydobywania danych z tablic 1D i 2D (Bloom 3)
3. **Wykonuje** operacje wektorowe na tablicach (arytmetyka, agregacje, filtrowanie) (Bloom 3)
4. **Porównuje** wydajność list Pythona i tablic NumPy (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W02 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | Po co NumPy, nawiązanie do benchmarku z W02 | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Tworzenie tablic — 7 sposobów | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | Indeksowanie i slicing — 1D i 2D | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | Operacje wektorowe — arytmetyka, agregacje, filtrowanie | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Przykład biznesowy — analiza sprzedaży z NumPy | Live coding |
| 1:25-1:35 | **AKTYWNOŚĆ** | Mini-ćwiczenie: operacje na tablicy danych | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | 3 bullet points, zapowiedź NumPy zaawansowane | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W02)

> "Dzień dobry. Pięć pytań z zeszłego tygodnia — 3 minuty."

**[Użyj quiz_w02.md]**

Szybkie omówienie:
> "Pipeline analityczny: pytanie → dane → analiza → wizualizacja → decyzja. Zawsze zaczynamy od pytania biznesowego. A `describe()` daje statystyki opisowe — średnia, min, max, kwartyle."

---

### 0:05-0:10 — WPROWADZENIE

> "Zeszły tydzień — pokazałem wam, że listy Pythona są za wolne. NumPy był 10-20 razy szybszy. Dzisiaj dowiecie się **dlaczego** i nauczycie się z niego korzystać."

> "NumPy — Numerical Python. Fundament całego ekosystemu data science. Pandas, Matplotlib, scikit-learn — wszystko pod spodem używa NumPy. Jeśli NumPy to fundamenty domu, to Pandas to ściany, a Matplotlib to dekoracja."

> "Kluczowe pojęcie: **ndarray** — n-dimensional array, tablica n-wymiarowa. To podstawowa struktura danych w NumPy."

---

### 0:10-0:30 — MATERIAŁ 1: Tworzenie tablic (20 min)

**[Otwórz notebook `numpy_demo.ipynb`]**

> "7 sposobów tworzenia tablic. Nie musicie zapamiętać wszystkich — najważniejsze to `array`, `zeros`, `arange` i `random`."

**[Komórka 1 — import]**

```python
import numpy as np   # konwencja: zawsze np
```

> "`import numpy as np` — to konwencja. Cały świat Pythona pisze `np`. Nie `numpy`, nie `num`. Zawsze `np`."

**[Komórka 2 — z listy]**

```python
# Sposób 1: Z listy Pythona
a = np.array([10, 20, 30, 40, 50])
print(f"Tablica: {a}")
print(f"Typ: {type(a)}")     # numpy.ndarray
print(f"Dtype: {a.dtype}")   # int64
```

> "Najprostszy sposób — zawijamy listę w `np.array()`. NumPy sam rozpoznaje typ: same liczby całkowite → `int64`."

**[Komórka 3 — zeros, ones]**

```python
# Sposób 2 i 3: Zera i jedynki
zera = np.zeros(5)
print(f"Zera: {zera}")

jedynki = np.ones((3, 4))    # 3 wiersze, 4 kolumny
print(f"Jedynki 3×4:\n{jedynki}")
```

> "Zera i jedynki. Przydatne do inicjalizacji — np. tworzysz macierz wyników i wypełniasz ją w pętli. Zauważcie: `ones((3,4))` — krotka w środku, bo podajecie kształt."

**[Komórka 4 — arange]**

```python
# Sposób 4: Sekwencja (jak range, ale NumPy)
sekwencja = np.arange(0, 10, 2)     # start, stop, krok
print(f"arange(0,10,2): {sekwencja}")  # [0, 2, 4, 6, 8]
```

> "`arange` — jak `range()`, ale zwraca tablicę NumPy. I działa z floatami!"

**[Komórka 5 — linspace]**

```python
# Sposób 5: Równomiernie rozłożone wartości
rownomierne = np.linspace(0, 1, 5)   # start, stop, ile punktów
print(f"linspace(0,1,5): {rownomierne}")  # [0, 0.25, 0.5, 0.75, 1]
```

> "`linspace` — 'linear space'. Podajesz start, stop i ile punktów chcesz. Idealne do wykresów."

**[Komórka 6 — random]**

```python
# Sposób 6 i 7: Losowe
losowe_int = np.random.randint(1, 100, size=10)
print(f"Losowe int 1-99: {losowe_int}")

losowe_normal = np.random.randn(5)
print(f"Rozkład normalny: {losowe_normal}")
```

> "Dane losowe. `randint` — losowe liczby całkowite. `randn` — rozkład normalny (średnia 0, odchylenie 1). Przydatne do symulacji i testowania."

**[Komórka 7 — atrybuty]**

```python
# Atrybuty tablicy — poznaj swoją tablicę
m = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Tablica:\n{m}")
print(f"shape: {m.shape}")    # (2, 3) — 2 wiersze, 3 kolumny
print(f"ndim: {m.ndim}")      # 2 wymiary
print(f"size: {m.size}")      # 6 elementów
print(f"dtype: {m.dtype}")    # int64
```

> "Każda tablica ma atrybuty. `shape` to najważniejszy — mówi jaki jest kształt. (2, 3) = 2 wiersze, 3 kolumny. `ndim` — ile wymiarów. `size` — ile elementów łącznie."

---

### 0:30-0:45 — MATERIAŁ 2: Indeksowanie i slicing (15 min)

> "Mamy tablicę. Teraz — jak wyciągać z niej dane. To kluczowa umiejętność."

**[Komórka 8 — indeksowanie 1D]**

```python
dane = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"dane: {dane}")

# Pojedynczy element
print(f"dane[0]: {dane[0]}")      # 10 — pierwszy
print(f"dane[-1]: {dane[-1]}")    # 100 — ostatni
print(f"dane[3]: {dane[3]}")      # 40 — czwarty (indeks od 0!)
```

> "Indeksowanie od zera — znacie z Pythona I. Minus oznacza od końca."

**[Komórka 9 — slicing 1D]**

```python
# Slicing — wycinanie fragmentów
print(f"dane[2:5]: {dane[2:5]}")     # [30, 40, 50] — od 2 do 5 (bez 5!)
print(f"dane[:3]: {dane[:3]}")       # [10, 20, 30] — pierwsze 3
print(f"dane[7:]: {dane[7:]}")       # [80, 90, 100] — od 7 do końca
print(f"dane[::2]: {dane[::2]}")     # [10, 30, 50, 70, 90] — co drugi
print(f"dane[::-1]: {dane[::-1]}")   # odwrócona
```

> "Slicing: `start:stop:step`. Jak w listach. Ważne: **stop nie jest włączony**. `dane[2:5]` to elementy o indeksach 2, 3, 4 — ale NIE 5."

**[Komórka 10 — indeksowanie 2D]**

```python
# Macierz 3×3
macierz = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print(f"Macierz:\n{macierz}")

# Pojedynczy element: [wiersz, kolumna]
print(f"macierz[0, 1]: {macierz[0, 1]}")   # 2 — wiersz 0, kolumna 1

# Cały wiersz
print(f"macierz[1]: {macierz[1]}")          # [4, 5, 6]

# Cała kolumna
print(f"macierz[:, 0]: {macierz[:, 0]}")    # [1, 4, 7] — pierwsza kolumna

# Fragment
print(f"macierz[1:, 1:]:\n{macierz[1:, 1:]}")  # [[5,6],[8,9]]
```

> "2D: dwa indeksy oddzielone przecinkiem. `[wiersz, kolumna]`. Dwukropek sam = 'wszystko'. `[:, 0]` = 'wszystkie wiersze, kolumna 0'."

> "To jest kluczowe. Będziecie tego używać codziennie w Pandas. Pandas DataFrame to pod spodem macierz NumPy z nagłówkami."

---

### 0:45-0:55 — PRZERWA (10 min)

> "Przerwa. Po przerwie — operacje na tablicach."

---

### 0:55-1:15 — MATERIAŁ 3: Operacje wektorowe (20 min)

> "Najlepsza cecha NumPy: **operacje wektorowe**. Robisz coś z jedną tablicą — działa na WSZYSTKICH elementach naraz."

**[Komórka 11 — arytmetyka]**

```python
ceny = np.array([100, 200, 150, 300, 250])
print(f"Ceny: {ceny}")

# Operacje na całej tablicy — JEDNĄ linią
print(f"Po rabacie 10%: {ceny * 0.9}")
print(f"Z VAT 23%: {ceny * 1.23}")
print(f"Podwyżka o 50 zł: {ceny + 50}")
```

> "Nie ma pętli. Nie ma list comprehension. `ceny * 0.9` — NumPy mnoży KAŻDY element przez 0.9. To jest operacja wektorowa. I jest 10-20 razy szybsza od pętli."

**[Komórka 12 — agregacje]**

```python
# Agregacje — podsumowanie danych
print(f"Suma: {ceny.sum()}")           # 1000
print(f"Średnia: {ceny.mean()}")       # 200.0
print(f"Std: {ceny.std():.2f}")        # 70.71
print(f"Min: {ceny.min()}")            # 100
print(f"Max: {ceny.max()}")            # 300
print(f"Indeks max: {ceny.argmax()}")  # 3 (czwarty element)
```

> "Agregacje — jedna wartość z wielu. `sum`, `mean`, `std`, `min`, `max`. Proste i szybkie. `argmax` — daje INDEKS maksymalnego elementu, nie wartość."

**[Komórka 13 — filtrowanie boolean]**

```python
# Filtrowanie — warunki logiczne
print(f"Ceny > 200: {ceny > 200}")          # [False, False, False, True, True]
print(f"Drogie produkty: {ceny[ceny > 200]}")  # [300, 250]
print(f"Ile drogich: {(ceny > 200).sum()}")    # 2
```

> "**Filtrowanie boolean**. `ceny > 200` tworzy tablicę True/False. Wsadzamy ją do nawiasów kwadratowych — dostajemy tylko elementy, gdzie jest True. Ile jest True? `.sum()` — bo True = 1, False = 0."

> "To jest potężne. Wyobraźcie sobie milion transakcji — 'pokaż mi wszystkie powyżej 1000 zł' — jedna linia kodu."

**[Komórka 14 — operacje między tablicami]**

```python
# Operacje między tablicami — element po elemencie
ilosci = np.array([5, 3, 10, 2, 7])
wartosc = ceny * ilosci    # element-wise
print(f"Ceny:    {ceny}")
print(f"Ilości:  {ilosci}")
print(f"Wartość: {wartosc}")
print(f"Obrót:   {wartosc.sum()} zł")
```

> "Mnożenie dwóch tablic — element po elemencie. Cena razy ilość = wartość. Suma wartości = obrót. Trzy linie kodu. W Excelu to byłoby wiele kolumn i formuł."

---

### 1:15-1:25 — MATERIAŁ 4: Przykład biznesowy (10 min)

> "Połączmy to wszystko w praktyczny przykład."

**[Komórka 15 — sprzedaż kwartalna]**

```python
# Sprzedaż 5 produktów w 4 kwartałach (macierz 5×4)
np.random.seed(42)    # powtarzalne wyniki
sprzedaz = np.random.randint(50, 500, size=(5, 4))

produkty = ['Laptop', 'Mysz', 'Klawiatura', 'Monitor', 'Słuchawki']
kwartaly = ['Q1', 'Q2', 'Q3', 'Q4']

print("Sprzedaż (szt.):")
for i, p in enumerate(produkty):
    print(f"  {p:12s}: {sprzedaz[i]}")
```

> "Macierz 5×4 — 5 produktów, 4 kwartały. `seed(42)` sprawia, że losowe liczby są zawsze takie same — powtarzalność."

```python
# Pytania biznesowe — odpowiedzi w 1 linii
print(f"Roczna sprzedaż per produkt: {sprzedaz.sum(axis=1)}")
print(f"Sprzedaż per kwartał: {sprzedaz.sum(axis=0)}")
print(f"Najlepszy produkt: {produkty[sprzedaz.sum(axis=1).argmax()]}")
print(f"Najlepszy kwartał: {kwartaly[sprzedaz.sum(axis=0).argmax()]}")
print(f"Średnia kwartalna: {sprzedaz.mean(axis=0).astype(int)}")
```

> "**axis=0** — działaj wzdłuż wierszy (wynik per kolumna). **axis=1** — działaj wzdłuż kolumn (wynik per wiersz). To jest mylące na początku. Zapamiętajcie: axis=0 to 'w dół', axis=1 to 'w prawo'."

> "Najlepszy produkt? Laptop. Najlepszy kwartał? Q4. Ile linii kodu? Dosłownie jedna na każde pytanie."

---

### 1:25-1:35 — AKTYWNOŚĆ: mini-ćwiczenie (10 min)

> "Wasza kolej. Mamy dane o wynagrodzeniach w firmie:"

**[Wyświetl na projektorze]**

```python
wynagrodzenia = np.array([4500, 5200, 3800, 7100, 6300, 4800, 5500, 8200, 3900, 6100])
```

**Pytania (5 min):**
1. Ile osób zarabia powyżej 5000 zł?
2. Jakie jest średnie wynagrodzenie?
3. Jaka jest różnica między najwyższym a najniższym?
4. Podnieś wszystkim pensje o 500 zł — jaka teraz średnia?

**[Po 5 minutach — rozwiązania]**

```python
wynagrodzenia = np.array([4500, 5200, 3800, 7100, 6300, 4800, 5500, 8200, 3900, 6100])
print(f"1. Powyżej 5000: {(wynagrodzenia > 5000).sum()}")     # 5
print(f"2. Średnia: {wynagrodzenia.mean()}")                    # 5540.0
print(f"3. Rozstęp: {wynagrodzenia.max() - wynagrodzenia.min()}")  # 4400
print(f"4. Po podwyżce: {(wynagrodzenia + 500).mean()}")       # 6040.0
```

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy. Dzisiaj nauczyliście się trzech kluczowych rzeczy o NumPy:"

> "1. **Tworzenie tablic** — array, zeros, ones, arange, linspace, random. 7 sposobów."
> "2. **Indeksowanie** — 1D i 2D, slicing, wyciąganie kolumn i wierszy."
> "3. **Operacje wektorowe** — arytmetyka, agregacje, filtrowanie. Bez pętli, szybko."

> "Za tydzień — **NumPy zaawansowane**: broadcasting, algebra liniowa, generowanie danych, reshape. A na lab dzisiaj — ćwiczenia z prawdziwymi danymi."

**Zadanie domowe (nieoceniane):**
> "Stwórzcie tablicę NumPy z 20 losowymi cenami produktów (od 10 do 500). Policzcie: średnią, medianę, ile produktów kosztuje powyżej średniej. Wrzućcie jako notebook na GitHub."
