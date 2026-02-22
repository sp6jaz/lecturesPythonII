# L06 Laboratorium — Plan zajęć

## Temat: Pandas — selekcja, filtrowanie, sortowanie

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** ćwiczenia praktyczne
- **Prowadzący:** doktorant
- **Wymagane:** venv z pandas, numpy

### Efekty uczenia się (Bloom)
Po tym laboratorium osoba studiująca:
1. **Stosuje** loc i iloc do wybierania wierszy i kolumn (Bloom 3)
2. **Filtruje** dane z warunkami logicznymi (AND, OR, isin, between) (Bloom 3)
3. **Sortuje** dane i tworzy rankingi (nlargest, nsmallest) (Bloom 3)
4. **Analizuje** dane biznesowe odpowiadając na złożone pytania (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Uwagi |
|------|------|-----------|-------|
| 0:00-0:05 | **WPROWADZENIE** | Plan lab, nawiązanie do wykładu | Krótko |
| 0:05-0:25 | **ĆW. 1** | loc i iloc — selekcja wierszy i kolumn | Krok po kroku |
| 0:25-0:45 | **ĆW. 2** | Filtrowanie — warunki logiczne | Praktyczne |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:25 | **ĆW. 3** | Analiza danych sprzedażowych — samodzielna | Praca własna |
| 1:25-1:40 | **ĆW. 4** | Segmentacja + commit | Zamknięcie |
| 1:40-1:45 | **PODSUMOWANIE** | Zapowiedź czyszczenia danych na W07 | Feedback |

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Kluczowe momenty

**loc vs iloc (ćw. 1):**
- Najczęstszy błąd: `df.loc[0]` na domyślnym indeksie — działa, ale mylące (0 to etykieta, nie pozycja)
- Podkreślaj: iloc = **i**nteger, loc = **l**abel
- Studenci z NumPy automatycznie sięgają po iloc — zachęcaj do loc z warunkami

**Filtrowanie (ćw. 2):**
- **Krytyczny błąd:** `and` zamiast `&` — Python rzuci wyjątek, wyjaśnij dlaczego
- **Zapominają nawiasów** — `df[df.a > 5 & df.b < 10]` vs `df[(df.a > 5) & (df.b < 10)]`
- `isin` ratuje przed wieloma `|` — pokaż, że 3 warunki OR = 1 isin

**Ćwiczenie 3 — samodzielna praca:**
- Chodź między rzędami
- Podpowiadaj nazwy metod, nie rozwiązania
- Najszybsi mogą pomóc wolniejszym

### Najczęstsze problemy

| Problem | Rozwiązanie |
|---------|-------------|
| `ValueError: The truth value of a Series is ambiguous` | Użyj `&` zamiast `and`, `|` zamiast `or`. Nawiasy! |
| `KeyError` przy loc | Sprawdź pisownię etykiety: `df.columns` lub `df.index` |
| Wynik filtrowania pusty | Sprawdź warunki: może za restrykcyjne? Testuj po jednym |
| `TypeError: 'Series' objects are mutable` | Literówka: `=` zamiast `==` w warunku |
