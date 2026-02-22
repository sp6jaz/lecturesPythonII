# L03 Laboratorium — Plan zajęć

## Temat: NumPy — tablice, operacje, analiza danych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** ćwiczenia praktyczne przy komputerach
- **Prowadzący:** doktorant
- **Wymagane:** venv z numpy, matplotlib (z L01)

### Efekty uczenia się (Bloom)
Po tym laboratorium osoba studiująca:
1. **Tworzy** tablice NumPy różnymi metodami i identyfikuje ich atrybuty (Bloom 3)
2. **Stosuje** indeksowanie i slicing do wydobywania danych z tablic 1D i 2D (Bloom 3)
3. **Wykonuje** operacje wektorowe i agregacje na danych biznesowych (Bloom 3)
4. **Porównuje** wydajność list i tablic NumPy na benchmarkach (Bloom 4)

### Przed zajęciami — przygotowanie prowadzącego
1. Sprawdź czy numpy działa: `python -c "import numpy; print(numpy.__version__)"`
2. Przetestuj benchmark z ćwiczenia 4 — wyniki zależą od komputera
3. Przeczytaj plan wykładu W03 — lab bezpośrednio ćwiczy te same koncepcje

### Plan minutowy

| Czas | Etap | Co robisz | Uwagi |
|------|------|-----------|-------|
| 0:00-0:05 | **WPROWADZENIE** | Nawiąż do wykładu, plan lab | Krótko |
| 0:05-0:25 | **ĆW. 1** | Tworzenie tablic + atrybuty | Krok po kroku |
| 0:25-0:45 | **ĆW. 2** | Indeksowanie i slicing | Ważne — dużo ćwiczenia |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:20 | **ĆW. 3** | Operacje wektorowe — dane biznesowe | Samodzielna praca |
| 1:20-1:35 | **ĆW. 4** | Benchmark lista vs NumPy | Efekt wow |
| 1:35-1:40 | **ĆW. 5** | Commit na GitHub | Zamknięcie |
| 1:40-1:45 | **PODSUMOWANIE** | Sprawdź postępy, zapowiedz W04 | Feedback |

---

## INSTRUKCJA DLA PROWADZĄCEGO

### 0:00-0:05 — WPROWADZENIE

> "Na wykładzie poznaliście NumPy — tworzenie tablic, indeksowanie, operacje wektorowe. Dzisiaj to wszystko przećwiczycie na danych biznesowych."

### 0:05-0:25 — ĆWICZENIE 1: Tworzenie tablic (20 min)

Pokaż na projektorze cwiczenia.md — ćwiczenie 1. Studenci piszą w notebooku.

**Kluczowe momenty:**
- Upewnij się, że każdy ma `import numpy as np` (konwencja!)
- Pokaż różnicę: `np.zeros(5)` vs `np.zeros((3,4))` — krotka dla kształtu 2D
- `np.random.seed()` — wyjaśnij dlaczego (powtarzalność)

### 0:25-0:45 — ĆWICZENIE 2: Indeksowanie (20 min)

**Najważniejsze ćwiczenie.** Indeksowanie to fundament Pandas.

**Typowe błędy:**
- Zapominanie, że indeks startuje od 0
- Mylenie `dane[2:5]` — stop NIE jest włączony
- W 2D: `macierz[wiersz, kolumna]` — kolejność!

**Podpowiedzi:**
- `[:, 0]` — "wszystkie wiersze, kolumna 0"
- `[1:, :]` — "od wiersza 1, wszystkie kolumny"

### 0:55-1:20 — ĆWICZENIE 3: Operacje (25 min)

Samodzielna praca. Studenci rozwiązują zadania biznesowe.

**Chodź między rzędami**, sprawdzaj kto się blokuje. Podpowiadaj **metody** (np. "spróbuj `.mean()`"), nie dawaj gotowych rozwiązań.

**Pair programming:** Jeśli ktoś jest zagubiony, połącz z sąsiadem.

### 1:20-1:35 — ĆWICZENIE 4: Benchmark (15 min)

**Efekt wow.** Studenci widzą na własne oczy jak szybki jest NumPy.

> "Uruchomcie benchmark i zapiszcie wynik. Na moim komputerze NumPy jest ~15× szybszy. U was?"

### Najczęstsze problemy

| Problem | Rozwiązanie |
|---------|-------------|
| `ModuleNotFoundError: No module named 'numpy'` | Aktywuj venv: `source .venv/bin/activate` |
| `ValueError: operands could not be broadcast` | Tablice mają różne kształty — sprawdź `.shape` |
| Wynik `array([ ... ])` zamiast liczby | Użyj `.sum()`, `.mean()` itp. do agregacji |
| `IndexError: index out of bounds` | Indeks za duży — sprawdź `.shape` |
