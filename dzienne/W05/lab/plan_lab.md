# L05 Laboratorium — Plan zajęć

## Temat: Pandas — Series, DataFrame, eksploracja danych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** ćwiczenia praktyczne
- **Prowadzący:** doktorant
- **Wymagane:** venv z pandas, numpy, matplotlib

### Efekty uczenia się (Bloom)
Po tym laboratorium osoba studiująca:
1. **Tworzy** Series i DataFrame z dict, listy i pliku CSV (Bloom 3)
2. **Stosuje** metody eksploracyjne: head(), info(), describe(), value_counts() (Bloom 3)
3. **Analizuje** dane biznesowe odpowiadając na pytania z użyciem podstawowych metod Pandas (Bloom 4)
4. **Porównuje** Series i DataFrame, rozumiejąc relację między nimi (Bloom 2)

### Plan minutowy

| Czas | Etap | Co robisz | Uwagi |
|------|------|-----------|-------|
| 0:00-0:05 | **WPROWADZENIE** | Plan lab, nawiązanie do wykładu | Krótko |
| 0:05-0:25 | **ĆW. 1** | Series — tworzenie, indeks, operacje | Krok po kroku |
| 0:25-0:45 | **ĆW. 2** | DataFrame — tworzenie, atrybuty, read_csv | Praktyczne |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:25 | **ĆW. 3** | Eksploracja datasetu — samodzielna analiza | Praca własna |
| 1:25-1:40 | **ĆW. 4** | Pytania biznesowe + commit | Zamknięcie |
| 1:40-1:45 | **PODSUMOWANIE** | Zapowiedź loc/iloc na W06 | Feedback |

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Kluczowe momenty

**Series (ćw. 1):**
- Studenci mogą myśleć, że Series to lista — podkreśl, że ma indeks (etykiety)
- Pokaz `idxmax()` vs `argmax()` NumPy — to "aha moment"
- Dict → Series to naturalny most od czystego Pythona

**DataFrame (ćw. 2):**
- Najczęstszy problem: podwójne nawiasy `df[['a', 'b']]` — wyjaśnij, że wewnątrz jest lista
- `read_csv` z URL — upewnij się, że internet działa na sali
- Jeśli brak internetu, przygotuj lokalne pliki CSV (tips.csv, penguins.csv)

**Eksploracja (ćw. 3):**
- Chodź między rzędami, sprawdzaj czy robią info() i describe()
- Studenci, którzy szybko kończą — niech pomogą innym (pair programming)
- Kluczowe: studenci muszą **wyciągać wnioski** z danych, nie tylko odpalać metody

### Najczęstsze problemy

| Problem | Rozwiązanie |
|---------|-------------|
| `KeyError: 'kolumna'` | Sprawdź pisownię: `df.columns` pokaże dokładne nazwy |
| `ModuleNotFoundError: pandas` | Aktywuj venv: `source .venv/bin/activate` |
| `URLError` / brak internetu | Użyj lokalnego pliku: `pd.read_csv('tips.csv')` |
| Jupyter nie widzi pandas | Sprawdź kernel: powinien wskazywać na .venv |
| `TypeError: unhashable type: 'list'` | Podwójne nawiasy `[['a','b']]`, nie `[['a','b']]` — sprawdź składnię |

### Materiały zapasowe (offline)
Jeśli brak internetu, przygotuj z wyprzedzeniem:
```bash
source .venv/bin/activate
python -c "
import pandas as pd
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips.to_csv('tips.csv', index=False)
penguins = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
penguins.to_csv('penguins.csv', index=False)
"
```
