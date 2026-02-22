# L14 — Ćwiczenia: LLM i AI w analizie danych

**Programowanie w Pythonie II** | Laboratorium 14
**Notebook:** `lab14_ai_analysis.ipynb`
**Narzędzia AI:** Claude.ai (free) lub ChatGPT (free) — bez kluczy API

---

## Setup — uruchom jako pierwszą komórkę

```python
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
sns.set_theme(style='whitegrid', palette='muted')

print("numpy:", np.__version__)
print("pandas:", pd.__version__)
print("Środowisko gotowe.")
```

---

## Ćwiczenie 1: Prompt engineering dla analizy danych (20 min)

**Cel:** Nauczyć się pisać prompty które dają użyteczne, konkretne odpowiedzi — nie ogólne.

**Kontekst:** Dobry prompt do zadań analitycznych zawiera cztery elementy:
1. **Kontekst** — jakie mam dane, jakie kolumny, skąd pochodzą
2. **Zadanie** — co konkretnie chcę uzyskać
3. **Format** — jak ma wyglądać odpowiedź (kod Python, tabela, opis)
4. **Ograniczenia** — czego NIE robić (np. "tylko pandas", "bez zewnętrznych bibliotek")

### Dataset roboczy

```python
# Generujemy dataset e-commerce — używamy go przez całe laboratorium
np.random.seed(42)
n = 500

df = pd.DataFrame({
    'zamowienie_id': range(1, n+1),
    'data': pd.date_range('2024-01-01', periods=n, freq='D')[:n],
    'klient_id': np.random.randint(1, 101, n),
    'kategoria': np.random.choice(
        ['elektronika', 'odzież', 'dom_i_ogrod', 'sport', 'ksiazki'],
        n, p=[0.3, 0.25, 0.2, 0.15, 0.1]
    ),
    'wartosc': np.round(np.random.lognormal(5.5, 0.8, n), 2),
    'status': np.random.choice(
        ['zrealizowane', 'anulowane', 'zwrócone'],
        n, p=[0.78, 0.12, 0.10]
    ),
    'ocena_klienta': np.random.choice([1, 2, 3, 4, 5, None], n, p=[0.05, 0.08, 0.15, 0.32, 0.30, 0.10]),
})

print(df.head())
print(f"\nKształt: {df.shape}")
print(f"\nKolumny:\n{df.dtypes}")
```

### 1a. Zły prompt vs dobry prompt

Otwórzcie Claude.ai lub ChatGPT. Wyślijcie najpierw poniższy **zły prompt**:

```
ZŁY PROMPT:
"Przeanalizuj dane sprzedażowe dla mnie"
```

Zanotujcie co dostaliście. Następnie wyślijcie **dobry prompt** (dostosowany do Waszego datasetu):

```
DOBRY PROMPT (szablon — uzupełnijcie):
"""
Mam DataFrame pandas o nazwie `df` z kolumnami:
- zamowienie_id (int): identyfikator zamówienia
- data (datetime): data zamówienia
- klient_id (int): identyfikator klienta (1-100)
- kategoria (str): kategoria produktu: 'elektronika', 'odzież', 'dom_i_ogrod', 'sport', 'ksiazki'
- wartosc (float): wartość zamówienia w PLN
- status (str): 'zrealizowane', 'anulowane', 'zwrócone'
- ocena_klienta (float lub None): ocena 1-5, może być NaN

Zadanie: Napisz kod Python który oblicza i wypisuje:
1. Całkowity przychód (suma wartości tylko dla statusu='zrealizowane')
2. TOP 3 kategorie według przychodu
3. Wskaźnik zwrotów (% zamówień z statusem='zwrócone')
4. Średnią ocenę klienta (pomijając NaN)

Ograniczenia: tylko biblioteki pandas i numpy. Żadnych wykresów.
Format wyjścia: wydruk tekstowy z etykietami po polsku.
"""
```

**Zadanie:** Skopiuj wygenerowany kod do swojego notebooka i uruchom go. Czy działa poprawnie?

```python
# Wklej tutaj kod wygenerowany przez AI:
# (usuń ten komentarz i zastąp wygenerowanym kodem)
```

### 1b. Iteracyjne ulepszanie promptu

Jeśli kod z 1a nie działa lub jest niekompletny — odeślijcie do AI z informacją o błędzie:

```
PROMPT KORYGUJĄCY:
"Kod zwraca błąd: [WKLEIĆ TREŚĆ BŁĘDU].
Popraw kod zachowując oryginalne wymagania."
```

Jeśli kod działa, ale chcecie dodać coś więcej — użyjcie promptu rozszerzającego:

```
PROMPT ROZSZERZAJĄCY:
"Dodaj do kodu obliczenie mediany wartości zamówień per kategoria.
Zachowaj istniejący format wyjścia."
```

```python
# Wklej poprawioną wersję kodu (jeśli była potrzebna poprawa):
```

### 1c. Prompt do wizualizacji

Napiszcie własny prompt (bez szablonu) który poprosi AI o kod Python tworzący wykres słupkowy pokazujący przychód per kategoria. Uwzględnijcie w prompcie:
- kontekst DataFrame (możecie użyć szablonu z 1a)
- zadanie: wykres słupkowy poziomy, posortowany malejąco
- ograniczenia: matplotlib lub seaborn, tytuł i etykiety po polsku

```python
# Wklej prompt który napisałeś/napisałaś (jako komentarz lub string):
moj_prompt = """
[TU WPISZ SWÓJ PROMPT]
"""

# Wklej wygenerowany kod wizualizacji poniżej i uruchom:
```

### Sprawdzenie 1 ✅

- [ ] Zły i dobry prompt porównane — student potrafi wyjaśnić czemu dobry jest lepszy
- [ ] Kod z dobrego promptu uruchomiony bez błędów — wyniki wypisane po polsku
- [ ] Własny prompt do wizualizacji napisany i zawiera 4 elementy (kontekst, zadanie, format, ograniczenia)
- [ ] Wykres wygenerowany i widoczny w notebooku

---

## Ćwiczenie 2: Generowanie kodu z AI — ocena i weryfikacja (20 min)

**Cel:** Nauczyć się krytycznie oceniać kod wygenerowany przez AI — nie każdy kod AI jest poprawny.

**Kontekst:** AI może generować kod który: (a) działa poprawnie, (b) działa ale jest nieefektywny, (c) ma błędy logiczne mimo poprawnej składni, (d) nie obsługuje edge cases. Wasz task to odróżniać te przypadki.

### 2a. Generowanie i testowanie funkcji

Wyślijcie do AI poniższy prompt:

```
PROMPT:
"""
Mam DataFrame `df` z kolumnami: klient_id (int), wartosc (float), status (str),
data (datetime), kategoria (str).

Napisz funkcję `analiza_klienta(df, klient_id)` która:
1. Filtruje zamówienia danego klienta
2. Liczy liczbę zamówień per status
3. Oblicza łączną wartość zakupów (tylko 'zrealizowane')
4. Zwraca dict: {'zamowienia_per_status': ..., 'wartosc_total': ..., 'pierwsza_data': ..., 'ostatnia_data': ...}
5. Obsługuje przypadek gdy klient nie istnieje w df — zwraca None z komunikatem

Tylko pandas i numpy.
"""
```

```python
# 1. Wklej tutaj funkcję wygenerowaną przez AI:

# 2. Przetestuj na konkretnym kliencie:
wynik = analiza_klienta(df, klient_id=5)
print(wynik)

# 3. Przetestuj edge case — klient którego nie ma w danych:
wynik_nieistniejacy = analiza_klienta(df, klient_id=9999)
print(wynik_nieistniejacy)
```

### 2b. Ocena krytyczna wygenerowanego kodu

Uzupełnij poniższą tabelę oceny kodu z 2a. Bądź konkretny/konkretna — nie pisz "jest ok" lub "nie działa".

```python
# Dodaj komórkę Markdown z oceną:
```

Wzór tabeli oceny (skopiuj do komórki Markdown w notebooku):

```markdown
## Ocena kodu wygenerowanego przez AI — Ćwiczenie 2a

| Kryterium | Ocena (OK / Problem / Brak) | Komentarz |
|-----------|----------------------------|-----------|
| Poprawna składnia Python | | |
| Filtrowanie per klient_id działa | | |
| Zliczanie per status poprawne | | |
| Suma tylko 'zrealizowane' | | |
| Dict zawiera wszystkie 4 klucze | | |
| Obsługa nieistniejącego klienta | | |
| Czytelność kodu (komentarze) | | |
| Efektywność (bez zbędnych pętli) | | |

**Ogólna ocena:** [Dobry / Wymaga poprawek / Zły]
**Główna uwaga:** [1 zdanie]
```

### 2c. Zgłoś problem do AI i poproś o poprawkę

Jeśli znalazłeś/znalazłaś problem w kodzie z 2a — wyślij do AI:

```
PROMPT KORYGUJĄCY:
"Znalazłem problem w funkcji analiza_klienta:
[OPISZ KONKRETNY PROBLEM, np.: "gdy klient_id nie istnieje, kod zwraca błąd KeyError zamiast None"]

Popraw funkcję tak żeby: [OPISZ OCZEKIWANE ZACHOWANIE]
Zachowaj resztę logiki bez zmian."
```

```python
# Wklej poprawioną wersję funkcji (jeśli była potrzebna):

# Przetestuj ponownie:
wynik_v2 = analiza_klienta(df, klient_id=5)
print("Klient 5:", wynik_v2)

wynik_v2_edge = analiza_klienta(df, klient_id=9999)
print("Klient 9999:", wynik_v2_edge)
```

### Sprawdzenie 2 ✅

- [ ] Funkcja `analiza_klienta` wygenerowana przez AI i wklejona do notebooka
- [ ] Przetestowana na istniejącym kliencie — wynik sensowny
- [ ] Przetestowana na nieistniejącym kliencie — obsługuje edge case
- [ ] Tabela oceny wypełniona konkretnie (nie "ok" lub "nie wiem")
- [ ] Jeśli były problemy — poprawiona wersja działa

---

## Ćwiczenie 3: AI-wspomagana analiza datasetu (30 min) — samodzielna praca

**Cel:** Przeprowadzenie pełnej analizy używając AI jako asystenta na każdym etapie — ale zachowując własne myślenie analityczne i weryfikację wyników.

**Kontekst:** Pracujesz jako junior analityk w firmie e-commerce. Manager dał Ci zadanie: *"Przeanalizuj dane zamówień i zaproponuj trzy działania biznesowe które poprawią wyniki."*

Używasz tego samego `df` co przez całe laboratorium.

### KROK 1: Eksploracja z pomocą AI (~ 8 min)

**Napisz prompt do AI** który poprosi o kod eksploracji danych. Prompt powinien opisywać:
- strukturę DataFrame
- jakie pytania chcesz zadać (np. rozkład kategorii, trendy czasowe, rozkład wartości)
- że chcesz wykresy + statystyki w jednym kroku

```python
# Wklej Twój prompt jako string:
prompt_eksploracja = """
[TU WPISZ SWÓJ PROMPT]
"""

# Wklej kod z AI i uruchom — powinien dać minimum 2 wykresy + podstawowe statystyki:
```

**Pytanie do siebie:** Co z eksploracji jest nieoczekiwane lub interesujące?

```python
# Komórka Markdown — zapisz swoje obserwacje po uruchomieniu kodu:
# (nie pytaj AI — napisz co TY zauważasz w danych)
```

### KROK 2: Analiza głębsza (~ 10 min)

Na podstawie obserwacji z Kroku 1 — wybierz **jeden** aspekt danych do głębszej analizy.

Propozycje (wybierz jeden lub zaproponuj własny):
- A: Analiza wskaźnika zwrotów per kategoria — czy elektronika ma wyższy wskaźnik zwrotów?
- B: Segmentacja klientów wg wartości zakupów (RFM uproszczone)
- C: Czy ocena klienta koreluje z wartością zamówienia?
- D: Trendy miesięczne — jak zmieniają się przychody w czasie?

**Napisz prompt do AI** opisujący wybrany aspekt. Poproś o kod który:
- przeprowadza analizę
- tworzy jedną kluczową wizualizację
- wypisuje 2-3 liczby podsumowujące wynik

```python
# Wklej Twój prompt jako string:
prompt_glebsza = """
[TU WPISZ SWÓJ PROMPT — opisz który aspekt wybrałeś i dlaczego]
"""

# Wklej kod z AI i uruchom:
```

### KROK 3: Interpretacja — poproś AI o pomoc (~ 7 min)

Masz wyniki z Kroku 2 — liczby, tabele, wykres. Teraz poproś AI o interpretację biznesową.

**Szablon promptu do interpretacji:**

```
PROMPT INTERPRETACJA:
"""
Przeprowadziłem/łam analizę [OPISZ CO ANALIZOWAŁEŚ] w danych e-commerce.

Wyniki:
[WKLEJ KONKRETNE LICZBY Z TWOJEJ ANALIZY — np.:
 - Wskaźnik zwrotów elektroniki: 16.3%
 - Wskaźnik zwrotów odzieży: 9.8%
 - Średnia wartość zamówień z oceną 5: 312 PLN
 - Średnia wartość zamówień z oceną 1: 198 PLN]

Napisz interpretację dla Managera Sprzedaży (nie-analityka):
1. Główne odkrycie (1 zdanie)
2. Co to oznacza biznesowo (2-3 zdania)
3. Jedno konkretne działanie które rekomenduje ta analiza

Format: krótki, bez wzorów, po polsku.
"""
```

```python
# Wklej Twój prompt (z własnymi liczbami):
prompt_interpretacja = """
[TU WPISZ SWÓJ PROMPT Z WŁASNYMI WYNIKAMI]
"""

# Odpowiedź AI wklej do komórki Markdown:
```

**Ważne:** Po otrzymaniu interpretacji od AI — przeczytaj ją krytycznie. Czy zgadzasz się z każdym zdaniem? Czy coś wymaga poprawki? Dodaj swój komentarz.

### KROK 4: Wniosek końcowy (~ 5 min)

Napisz w komórce Markdown (samodzielnie — nie proś AI) odpowiedź na pytanie Managera.

Wzór komórki Markdown:

```markdown
## Wyniki analizy zamówień e-commerce — [Twoje imię]

**Pytanie biznesowe:** Co możemy poprawić żeby zwiększyć zyski i satysfakcję klientów?

**Dane:** [opisz dataset — n zamówień, okres, kategorie]

**Kluczowe odkrycia:**
1. [Twoje odkrycie 1 z analizy]
2. [Twoje odkrycie 2 z analizy]
3. [Opcjonalnie: odkrycie 3]

**Trzy rekomendacje biznesowe:**
1. [Konkretne działanie + uzasadnienie liczbami]
2. [Konkretne działanie + uzasadnienie liczbami]
3. [Konkretne działanie + uzasadnienie liczbami]

**Jak AI pomogło w tej analizie:**
[1-2 zdania: co AI robiło, a co robiłeś/robiłaś Ty]
```

### Sprawdzenie 3 ✅

- [ ] KROK 1: Eksploracja wykonana — minimum 2 wykresy widoczne w notebooku
- [ ] KROK 1: Własne obserwacje zapisane (komórka Markdown — bez AI)
- [ ] KROK 2: Jeden aspekt wybrany i przeanalizowany z pomocą AI — kod działa
- [ ] KROK 3: Interpretacja AI wklejona do notebooka — z własnym komentarzem
- [ ] KROK 4: Komórka Markdown z wnioskami — pisana samodzielnie, zawiera liczby
- [ ] Całość logicznie spójna — pytanie → analiza → odkrycia → rekomendacje

---

## Ćwiczenie 4: Etyka, ograniczenia i commit (15 min)

### 4a. Case studies — omów z sąsiadem/sąsiadką (5 min)

Omówcie w parach każdy z trzech scenariuszy. Dla każdego odpowiedzcie: **co powinien zrobić analityk?**

**Scenariusz 1 — Prywatność:**
> Twoja firma ma plik CSV z danymi 10 000 klientów: imię, email, historia zakupów (ze zniżkami i porzuconymi koszykami). Chcesz użyć ChatGPT żeby napisał Ci skrypt do segmentacji tych klientów. Najszybciej byłoby uploadować CSV bezpośrednio do ChatGPT Code Interpreter.

**Scenariusz 2 — Weryfikacja:**
> AI wygenerował Ci raport z analizy sprzedaży. W raporcie pada zdanie: "Według naszej analizy, konwersja wyniosła 4.7%, co jest powyżej średniej branżowej wynoszącej 3.2% dla sektora e-commerce w Polsce (źródło: Raport E-commerce 2024)." Masz oddać raport Dyrektorowi za 30 minut.

**Scenariusz 3 — Odpowiedzialność:**
> Stworzysz model predykcji churnu klientów z pomocą AI — AI wygenerował cały kod od A do Z. Model działa (accuracy 78%). Wdrożenie automatycznie wysyła mailing do klientów "zagrożonych churnem" z kuponem 30% rabatu. Po miesiącu okazuje się że model błędnie klasyfikuje 40% klientów premium — firma traci 80 000 PLN na niepotrzebnych kuponach.

```python
# Komórka Markdown — zapisz odpowiedzi do każdego scenariusza:
```

Wzór:

```markdown
## Ćwiczenie 4a — Case studies etyczne

**Scenariusz 1 (Prywatność):** [Co powinien zrobić analityk? Jakie ryzyko?]

**Scenariusz 2 (Weryfikacja):** [Co powinien zrobić analityk? Jak szybko można sprawdzić?]

**Scenariusz 3 (Odpowiedzialność):** [Kto ponosi odpowiedzialność? Co należało zrobić inaczej?]
```

### 4b. Pytania refleksyjne (5 min)

Napisz krótkie odpowiedzi (2-4 zdania każda) w komórce Markdown:

```markdown
## Refleksja — AI w pracy analityka

**Pytanie 1:** W którym z Ćwiczeń 1-3 AI było najbardziej pomocne? Dlaczego?

**Pytanie 2:** W którym momencie przez te zajęcia zaufałeś/zaufałaś AI "za bardzo"?
(albo: kiedy powinieneś/powinnaś był/a zweryfikować wynik ale tego nie zrobiłeś/zrobiłaś)

**Pytanie 3:** Jeśli za rok 80% kodu analitycznego będzie generowane przez AI —
jakie umiejętności człowieka będą najważniejsze? Wymień 3.
```

### 4c. Commit do repozytorium Git

```bash
# W terminalu (poza notebookiem):
cd ~/python2_projekt

# Sprawdź status
git status

# Dodaj plik notebooka
git add lab14_ai_analysis.ipynb

# Commit
git commit -m "L14: AI w analizie danych — prompt engineering, ocena kodu AI, analiza z asystentem AI"

# Wypchnij (jeśli masz remote)
git push
```

### Sprawdzenie 4 ✅

- [ ] Case studies omówione w parach — każdy scenariusz ma odpowiedź (min. 2 zdania)
- [ ] 3 pytania refleksyjne mają odpowiedzi — konkretne, nie ogólne
- [ ] `git log` — widoczny commit z plikiem `lab14_ai_analysis.ipynb`
- [ ] Notebook działa end-to-end (Restart & Run All — wszystkie komórki wykonują się bez błędów)

---

## Podsumowanie kluczowych zasad pracy z AI

```
DOBRY PROMPT = KONTEKST + ZADANIE + FORMAT + OGRANICZENIA

AI DOBRZE RADZI SOBIE Z:
  ✓ Generowaniem kodu z precyzyjnym opisem
  ✓ Tłumaczeniem wyników na język biznesowy
  ✓ Mapowaniem/normalizacją kategorii (słowniki, czyszczenie)
  ✓ Pisaniem szablonowego kodu (CRUD, transformacje)
  ✓ Wyjaśnianiem błędów (wklej traceback → dostaniesz diagnozę)

AI WYMAGA WERYFIKACJI PRZY:
  ✗ Obliczeniach numerycznych (zawsze uruchom kod)
  ✗ Aktualnych danych (knowledge cutoff!)
  ✗ Nazwach funkcji/parametrów nowych bibliotek
  ✗ Edge cases w danych (NaN, puste DataFrame, string zamiast int)

ZASADY BEZPIECZEŃSTWA:
  ✗ Nie wysyłaj danych osobowych klientów do publicznego API
  ✗ Nie publikuj kluczy API w kodzie (używaj zmiennych środowiskowych)
  ✓ Anonimizuj dane przed wysłaniem (zamień email → hash, imię → ID)
  ✓ Sprawdź politykę prywatności narzędzia przed użyciem firmowych danych
```
