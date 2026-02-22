# L02 Laboratorium — Plan zajęć

## Temat: Jupyter Notebook i pierwsza eksploracja danych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** ćwiczenia praktyczne przy komputerach
- **Prowadzący:** doktorant
- **Wymagane:** działające środowisko z L01 (Python, uv, VS Code, venv z pandas/matplotlib)

### Efekty uczenia się (Bloom)
Po tym laboratorium osoba studiująca:
1. **Tworzy** notebook w VS Code z komórkami Code i Markdown (Bloom 3)
2. **Stosuje** podstawowe metody Pandas do eksploracji danych: head, shape, describe, dtypes (Bloom 3)
3. **Odpowiada** na pytania biznesowe korzystając z danych w DataFrame (Bloom 3-4)
4. **Tworzy** prosty wykres z danych przy użyciu Pandas/Matplotlib (Bloom 3)

### Przed zajęciami — przygotowanie prowadzącego
1. Sprawdź, czy studenci mają działające venv z pakietami (pandas, matplotlib, numpy)
2. Jeśli ktoś nie skończył L01 — daj mu 10 min na nadrobienie, pomóż
3. Przetestuj wszystkie ćwiczenia w swoim notebooku
4. Przygotuj dataset tips (online) — sprawdź czy internet w sali działa

### Plan minutowy

| Czas | Etap | Co robisz | Uwagi |
|------|------|-----------|-------|
| 0:00-0:10 | **WPROWADZENIE** | Sprawdź środowiska, nawiąż do wykładu, plan lab | Pomóż spóźnionym z L01 |
| 0:10-0:30 | **ĆW. 1** | Jupyter Notebook — tworzenie, komórki, skróty | Krok po kroku |
| 0:30-0:55 | **ĆW. 2** | Eksploracja datasetu — pipeline analityczny | Live coding + samodzielnie |
| 0:55-1:05 | **PRZERWA** | 10 minut | — |
| 1:05-1:30 | **ĆW. 3** | Pytania biznesowe — samodzielna analiza | Studenci pracują |
| 1:30-1:40 | **ĆW. 4** | Wykres + commit na GitHub | Zamknięcie |
| 1:40-1:45 | **PODSUMOWANIE** | Sprawdź kto skończył, zapowiedz NumPy | Zbierz feedback |

---

## INSTRUKCJA DLA PROWADZĄCEGO — krok po kroku

### 0:00-0:10 — WPROWADZENIE

**Co mówisz:**
> "Dzisiaj pracujemy z Jupyter Notebook i prawdziwymi danymi. Na wykładzie widzieliście pipeline analityczny — od pytania do odpowiedzi. Dzisiaj przejdziecie ten pipeline samodzielnie."

**Sprawdź środowiska:**
> "Zanim zaczniemy — otwórzcie terminal i wpiszcie:"

```bash
source .venv/bin/activate  # Linux
python -c "import pandas; print(pandas.__version__)"
```

> "Jeśli widzicie wersję pandas — jesteście gotowi. Jeśli nie — zgłoście się."

**Dla spóźnionych z L01:** daj im 10 min na instalację, przydziel kolegę do pomocy. Nie blokuj reszty grupy.

---

### 0:10-0:30 — ĆWICZENIE 1: Jupyter Notebook (20 min)

**Cel:** Student pewnie tworzy i nawiguje po notebooku.

**Co robisz:**
1. Pokaż na projektorze ćwiczenie 1 z cwiczenia.md
2. Pokaż każdy krok, poczekaj aż studenci zrobią
3. Daj czas na eksperymentowanie ze skrótami

**Ważne:**
- Upewnij się, że studenci potrafią przełączać między Code a Markdown
- Pokaż różnicę między Esc (tryb komend) i Enter (tryb edycji)
- Niech każdy uruchomi przynajmniej 3 komórki kodu i 1 komórkę Markdown

**Typowy problem:** Kernel nie działa → Ctrl+Shift+P → "Python: Select Interpreter" → .venv

---

### 0:30-0:55 — ĆWICZENIE 2: Eksploracja datasetu (25 min)

**Cel:** Student wczytuje dane i stosuje head(), shape, describe(), dtypes.

**Co robisz:**
1. Pokaż wczytanie danych na projektorze
2. Pokrocz z nimi przez head(), shape, describe()
3. Daj czas na samodzielne eksplorowanie

**Ważne:**
- Studenci powinni **pisać** kod, nie kopiować
- Każda komórka = jeden krok + komentarz Markdown wyjaśniający co robią
- Pokaż df.info() — dodatkowa metoda, której nie było na wykładzie

**Sprawdzenie:** Każdy student ma notebook z minimum 6 komórkami: import, wczytanie, head, shape, describe, dtypes.

---

### 0:55-1:05 — PRZERWA (10 min)

---

### 1:05-1:30 — ĆWICZENIE 3: Pytania biznesowe (25 min)

**Cel:** Student samodzielnie odpowiada na pytania korzystając z danych.

**Co robisz:**
1. Wyświetl pytania z ćwiczenia 3
2. Daj studentom czas na samodzielną pracę
3. Chodź między rzędami, pomagaj, dawaj podpowiedzi (nie rozwiązania!)

**Podpowiedzi gdy student się zablokuje:**
- "Jaki rachunek jest największy?" → `df['total_bill'].max()`
- "Ile rachunków w każdym dniu?" → `df['day'].value_counts()`
- "Średnia wg dnia?" → `df.groupby('day')['tip'].mean()`

**Ważne:** Nie podawaj gotowych rozwiązań od razu. Daj podpowiedź (nazwę metody) i pozwól studentowi samemu napisać kod. To buduje pewność siebie.

**Pair programming:** Jeśli ktoś jest kompletnie zagubiony — połącz z sąsiadem. Jeden pisze, drugi dyktuje.

---

### 1:30-1:40 — ĆWICZENIE 4: Wykres + commit (10 min)

**Cel:** Student tworzy wykres i commituje notebook na GitHub.

**Co robisz:**
1. Pokaż jak zrobić prosty bar chart
2. Pokaż jak zapisać notebook i commitnąć

**Ważne:**
- Nie zmuszaj do skomplikowanych wykresów — prosty bar chart wystarczy
- Commit message powinien być sensowny, np. "Dodaj analizę datasetu tips"
- Sprawdź czy na GitHubie wyświetla się notebook (GitHub renderuje .ipynb!)

---

### 1:40-1:45 — PODSUMOWANIE

**Co mówisz:**
> "Dzisiaj zrobiliście swoją pierwszą analizę danych — od wczytania przez eksplorację do wykresu. Na GitHubie macie teraz notebook, który jest częścią waszego portfolio."

> "Na następnych zajęciach — NumPy. Dowiecie się dlaczego listy Pythona to za mało i jak robić szybkie obliczenia na dużych danych."

**Sprawdź:**
- Kto ma notebook na GitHubie? (ręce w górę)
- Kto odpowiedział na wszystkie 5 pytań? (bonus: pochwal)

---

## Notatki dla prowadzącego

### Najczęstsze problemy i rozwiązania

| Problem | Rozwiązanie |
|---------|-------------|
| Kernel nie odpowiada | Restart kernel (Ctrl+Shift+P → "Restart Kernel") |
| `ModuleNotFoundError: No module named 'pandas'` | Sprawdź kernel — musi być z .venv, nie systemowy |
| Wykres nie wyświetla się | Dodaj `plt.show()` lub sprawdź czy jest `%matplotlib inline` |
| Komórka zawiesza się | Ctrl+C w terminalu lub Interrupt kernel w VS Code |
| Brak internetu → nie można wczytać CSV | Miej plik tips.csv lokalnie jako backup |

### Backup datasetu

Na wypadek braku internetu — przygotuj plik tips.csv:
```bash
python -c "import pandas as pd; pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv').to_csv('tips.csv', index=False)"
```

### Tempo
- Ćwiczenie 1 powinno iść szybko jeśli L01 poszło dobrze
- Ćwiczenie 3 (pytania) pochłania najwięcej czasu — studenci uczą się myśleć danymi
- Ćwiczenie 4 (wykres + commit) można skrócić jeśli brakuje czasu
