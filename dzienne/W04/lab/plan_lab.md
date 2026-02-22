# L04 Laboratorium — Plan zajęć

## Temat: NumPy zaawansowane — broadcasting, analiza danych finansowych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** ćwiczenia praktyczne
- **Prowadzący:** doktorant
- **Wymagane:** venv z numpy, matplotlib

### Efekty uczenia się (Bloom)
Po tym laboratorium osoba studiująca:
1. **Stosuje** broadcasting do obliczeń na danych różnych kształtów (Bloom 3)
2. **Zmienia** kształt tablic z reshape, łączy dane ze stacking (Bloom 3)
3. **Analizuje** dane finansowe stosując where, sort, korelację (Bloom 4)
4. **Generuje** dane syntetyczne do symulacji biznesowych (Bloom 3)

## Przydatne linki dla prowadzącego

- [NumPy — Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [NumPy — Reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
- [NumPy — np.where()](https://numpy.org/doc/stable/reference/generated/numpy.where.html)

### Plan minutowy

| Czas | Etap | Co robisz | Uwagi |
|------|------|-----------|-------|
| 0:00-0:05 | **WPROWADZENIE** | Plan lab, nawiązanie do wykładu | Krótko |
| 0:05-0:25 | **ĆW. 1** | Broadcasting — zastosowania biznesowe | Krok po kroku |
| 0:25-0:45 | **ĆW. 2** | Reshape + stacking — przygotowanie danych | Praktyczne |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:25 | **ĆW. 3** | Analiza danych finansowych — samodzielna | Praca własna |
| 1:25-1:40 | **ĆW. 4** | Generowanie danych + commit | Zamknięcie |
| 1:40-1:45 | **PODSUMOWANIE** | Zapowiedź Pandas na W05 | Feedback |

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Kluczowe momenty

**Broadcasting (ćw. 1):**
- Studenci mylą axis — rysuj na tablicy: axis=0 = "w dół", axis=1 = "w prawo"
- Częsty błąd: tablice 3×4 i wektor 3 elementów — nie pasuje! Trzeba reshape na (3,1)
- Podpowiedź: "od prawej porównuj kształty"

**Reshape (ćw. 2):**
- `-1` w reshape = "oblicz sam" — przydatne, ale studenci się gubią
- flatten vs ravel — na tym etapie mówcie: "używajcie flatten"

**Ćwiczenie 3 — samodzielna praca:**
- Chodź między rzędami, pomagaj
- Nie podawaj gotowych rozwiązań — dawaj nazwy metod
- Pair programming dla zagubionych

### Najczęstsze problemy

| Problem | Rozwiązanie |
|---------|-------------|
| `ValueError: could not broadcast` | Sprawdź `.shape` obu tablic — kształty muszą być kompatybilne |
| `ValueError: cannot reshape` | Rozmiary się nie zgadzają (np. 12 elementów nie da się w 5×3) |
| Korelacja = NaN | Tablica ma stałe wartości (std = 0) — dodaj losowy szum |
