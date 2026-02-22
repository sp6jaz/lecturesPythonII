# S09 — Ćwiczenia laboratoryjne: LLM i AI w analizie danych

**Programowanie w Pythonie II** | Spotkanie 9 (zaoczne) — blok laboratoryjny
**Czas:** 90 min | **Prowadzący:** prowadzący (osobiście)
**Notebook:** `s09_ai_analysis.ipynb`
**Narzędzia AI:** Claude.ai (free) lub ChatGPT (free) — bez kluczy API, bez płatności

---

## Organizacja pracy

- Otwórzcie **przeglądarkę** z Claude.ai lub ChatGPT (po jednej stronie ekranu)
- Otwórzcie **VS Code** z notebookiem (po drugiej stronie ekranu)
- Każdy wynik z AI wklejajcie do notebooka, uruchamiajcie i oceniajcie
- Wszystkie prompty i odpowiedzi AI zapisujcie — to jest Wasz materiał do oceny

### Rejestracja (jeśli jeszcze nie macie konta)
- **Claude.ai:** https://claude.ai — konto Google lub email (2 min)
- **ChatGPT:** https://chat.openai.com — konto OpenAI (2 min)
- Możecie użyć dowolnego z tych narzędzi — ćwiczenia działają z każdym

---

## Plan minutowy

| Czas | Ćwiczenie | Opis |
|------|-----------|------|
| 0:00-0:05 | Setup | Otwarcie narzędzi, notebook, rejestracja konta AI |
| 0:05-0:25 | **Ćwiczenie 1** | Prompt engineering — zły vs dobry prompt |
| 0:25-0:45 | **Ćwiczenie 2** | Generowanie kodu z AI — ocena krytyczna |
| 0:45-1:15 | **Ćwiczenie 3** | AI-wspomagana analiza datasetu (4 kroki) |
| 1:15-1:30 | **Ćwiczenie 4** | Case studies etyczne + commit |
| 1:30-1:35 | Podsumowanie | Omówienie, zapowiedź S10 |

---

## Setup — pierwsza komórka notebooka

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

## Dataset roboczy — e-commerce (500 zamówień)

Użyj tego datasetu we wszystkich ćwiczeniach. Wklej jako drugą komórkę notebooka:

```python
# Dataset e-commerce — 500 zamówień
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
    'ocena_klienta': np.random.choice(
        [1, 2, 3, 4, 5, None],
        n, p=[0.05, 0.08, 0.15, 0.32, 0.30, 0.10]
    ),
})

print(df.head(10))
print(f"\nKształt: {df.shape}")
print(f"\nKolumny i typy:\n{df.dtypes}")
print(f"\nBraki danych:\n{df.isna().sum()}")
```

---

## Ćwiczenie 1: Prompt engineering (20 min)

**Cel:** Nauczyć się pisać prompty które dają użyteczne, konkretne odpowiedzi — nie ogólne.

**Kontekst (z wykładu):** Dobry prompt zawiera cztery elementy:
1. **Kontekst** — jakie dane, kolumny, typy, skąd pochodzą
2. **Zadanie** — co konkretnie chcę uzyskać
3. **Format** — jak ma wyglądać odpowiedź (kod Python, tabela, opis)
4. **Ograniczenia** — czego NIE robić (np. "tylko pandas", "bez zewnętrznych bibliotek")

### Krok 1: Zły prompt

Otwórz Claude.ai lub ChatGPT. Wyślij poniższy prompt:

```
Przeanalizuj dane sprzedażowe dla mnie
```

Zanotuj co dostałeś/dostałaś. Czy ta odpowiedź jest użyteczna? Czy kod zadziałałby na Twoim DataFrame?

```python
# Komórka Markdown — zapisz obserwację:
# Co było złego w odpowiedzi na "zły prompt"?
# (np.: zbyt ogólne, nie pasuje do moich danych, brak kontekstu...)
```

### Krok 2: Dobry prompt

Wyślij poniższy prompt do tego samego narzędzia AI:

```
Mam DataFrame pandas o nazwie `df` z kolumnami:
- zamowienie_id (int): identyfikator zamówienia
- data (datetime): data zamówienia, zakres 2024-01-01 do 2025-05-15
- klient_id (int): identyfikator klienta (1-100)
- kategoria (str): 'elektronika', 'odzież', 'dom_i_ogrod', 'sport', 'ksiazki'
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
```

### Krok 3: Uruchom i oceń

Skopiuj wygenerowany kod do notebooka i uruchom:

```python
# Wklej tutaj kod wygenerowany przez AI z "dobrego promptu":

```

Czy kod działa? Jeśli nie — wyślij błąd do AI z promptem korygującym:

```
Kod zwraca błąd: [WKLEIĆ TREŚĆ BŁĘDU].
Popraw kod zachowując oryginalne wymagania.
```

### Krok 4: Własny prompt do wizualizacji

Napisz **samodzielnie** (bez szablonu) prompt do AI, który poprosi o wykres słupkowy pokazujący przychód per kategoria. Uwzględnij:
- kontekst DataFrame (skorzystaj z opisu z Kroku 2)
- zadanie: wykres słupkowy poziomy, posortowany malejąco
- format: matplotlib lub seaborn
- ograniczenia: tytuł i etykiety po polsku, wartości na słupkach

```python
# Zapisz swój prompt jako string:
moj_prompt_wizualizacja = """
[TU WPISZ SWÓJ PROMPT]
"""

# Wklej kod wygenerowany przez AI i uruchom:

```

### Sprawdzenie 1 ✅

- [ ] Zły i dobry prompt porównane — potrafisz wyjaśnić czemu dobry jest lepszy
- [ ] Kod z dobrego promptu uruchomiony bez błędów — wyniki wypisane po polsku
- [ ] Własny prompt do wizualizacji napisany i zawiera 4 elementy (kontekst, zadanie, format, ograniczenia)
- [ ] Wykres wygenerowany i widoczny w notebooku

---

## Ćwiczenie 2: Generowanie kodu z AI — ocena krytyczna (20 min)

**Cel:** Nauczyć się krytycznie oceniać kod wygenerowany przez AI. Nie każdy kod AI jest poprawny — nawet jeśli wygląda dobrze.

### Krok 1: Wygeneruj funkcję

Wyślij do AI poniższy prompt:

```
Mam DataFrame `df` z kolumnami: klient_id (int), wartosc (float), status (str),
data (datetime), kategoria (str).

Napisz funkcję `analiza_klienta(df, klient_id)` która:
1. Filtruje zamówienia danego klienta
2. Liczy liczbę zamówień per status
3. Oblicza łączną wartość zakupów (tylko status='zrealizowane')
4. Zwraca dict: {'zamowienia_per_status': ..., 'wartosc_total': ...,
                  'pierwsza_data': ..., 'ostatnia_data': ...}
5. Obsługuje przypadek gdy klient nie istnieje w df — zwraca None z komunikatem

Tylko pandas i numpy.
```

### Krok 2: Uruchom i przetestuj

Wklej wygenerowany kod do notebooka i przetestuj:

```python
# 1. Wklej funkcję wygenerowaną przez AI:


# 2. Test na istniejącym kliencie:
wynik = analiza_klienta(df, klient_id=5)
print("Klient 5:", wynik)

# 3. Test na nieistniejącym kliencie (edge case!):
wynik_brak = analiza_klienta(df, klient_id=9999)
print("Klient 9999:", wynik_brak)

# 4. Test na kliencie z samymi anulowanymi (edge case!):
# Sprawdź: czy wartosc_total = 0, nie NaN ani błąd?
```

### Krok 3: Wypełnij tabelę oceny

Dodaj komórkę Markdown z oceną kodu:

```markdown
## Ocena kodu wygenerowanego przez AI — Ćwiczenie 2

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
**Główna uwaga:** [1 zdanie — co AI zrobiło dobrze, a co źle?]
```

### Krok 4: Popraw (jeśli potrzeba)

Jeśli znalazłeś problem — wyślij do AI:

```
Znalazłem problem w funkcji analiza_klienta:
[OPISZ KONKRETNY PROBLEM]
Popraw funkcję. Zachowaj resztę logiki.
```

```python
# Wklej poprawioną wersję i przetestuj ponownie:

```

### Sprawdzenie 2 ✅

- [ ] Funkcja `analiza_klienta` wygenerowana i wklejona do notebooka
- [ ] Przetestowana na istniejącym kliencie — wynik sensowny (dict z 4 kluczami)
- [ ] Przetestowana na nieistniejącym kliencie — obsługuje edge case (nie wywala błędu)
- [ ] Tabela oceny wypełniona konkretnie (nie "ok" lub "nie wiem")
- [ ] Jeśli były problemy — poprawiona wersja działa

---

## Ćwiczenie 3: AI-wspomagana analiza datasetu (30 min)

**Cel:** Przeprowadzenie pełnej analizy z AI jako asystentem — ale z WŁASNYM myśleniem analitycznym i weryfikacją wyników.

**Kontekst:** Pracujesz jako junior analityk w firmie e-commerce. Manager dał Ci zadanie:
*"Przeanalizuj dane zamówień i zaproponuj trzy działania biznesowe które poprawią wyniki."*

Używasz tego samego `df` co przez całe laboratorium.

### KROK 1: Eksploracja z pomocą AI (~ 8 min)

Napisz prompt do AI prosząc o kod eksploracji danych. Prompt powinien opisywać:
- strukturę DataFrame (użyj opisu z Ćwiczenia 1)
- jakie pytania chcesz zadać: rozkład kategorii, trendy czasowe, rozkład wartości, brakujące dane
- że chcesz wykresy + statystyki w jednym kroku

```python
# Wklej Twój prompt:
prompt_eksploracja = """
[TU WPISZ SWÓJ PROMPT]
"""

# Wklej kod z AI i uruchom — powinien dać minimum 2 wykresy + statystyki:

```

**Po uruchomieniu kodu — napisz samodzielnie (bez AI!):**

```markdown
## Moje obserwacje z eksploracji (KROK 1)
<!-- Co jest interesujące w tych danych? Co jest nieoczekiwane? -->
1.
2.
3.
```

### KROK 2: Analiza głębsza (~ 10 min)

Na podstawie obserwacji z KROKU 1 — wybierz **jeden** aspekt danych do pogłębienia.

Propozycje (wybierz jedną lub zaproponuj własną):
- **A:** Analiza wskaźnika zwrotów per kategoria — czy elektronika ma wyższy wskaźnik?
- **B:** Segmentacja klientów wg wartości zakupów (top klienci vs reszta)
- **C:** Czy ocena klienta koreluje z wartością zamówienia?
- **D:** Trendy miesięczne — jak zmieniają się przychody w czasie?

Napisz prompt do AI opisujący wybrany aspekt. Poproś o kod który:
- przeprowadza analizę
- tworzy jedną kluczową wizualizację
- wypisuje 2-3 liczby podsumowujące wynik

```python
# Wklej Twój prompt:
prompt_glebsza = """
[TU WPISZ SWÓJ PROMPT — opisz który aspekt wybrałeś i dlaczego]
"""

# Wklej kod z AI i uruchom:

```

### KROK 3: Interpretacja — poproś AI o pomoc (~ 7 min)

Masz wyniki z KROKU 2 — liczby, tabele, wykres. Teraz poproś AI o interpretację biznesową.

```
PROMPT:
"""
Przeprowadziłem/łam analizę [OPISZ CO ANALIZOWAŁEŚ] w danych e-commerce (500 zamówień, 2024).

Wyniki:
[WKLEJ KONKRETNE LICZBY Z TWOJEJ ANALIZY, np.:
 - Wskaźnik zwrotów elektroniki: X%
 - Wskaźnik zwrotów odzieży: Y%
 - Korelacja ocena-wartość: r = Z]

Napisz interpretację dla Managera Sprzedaży (nie-analityka):
1. Główne odkrycie (1 zdanie)
2. Co to oznacza biznesowo (2-3 zdania)
3. Jedno konkretne działanie które rekomenduje ta analiza

Format: krótki, bez wzorów matematycznych, po polsku.
"""
```

```python
# Wklej Twój prompt z WŁASNYMI liczbami:
prompt_interpretacja = """
[TU WPISZ SWÓJ PROMPT]
"""

# Odpowiedź AI wklej do komórki Markdown poniżej:
```

```markdown
## Interpretacja AI (KROK 3)
<!-- Wklej odpowiedź AI tutaj -->

## Moja ocena interpretacji
<!-- Przeczytaj krytycznie. Czy zgadzasz się z każdym zdaniem? Co poprawić? -->
```

### KROK 4: Wniosek końcowy — samodzielnie (~ 5 min)

Napisz w komórce Markdown (samodzielnie — **NIE proś AI**) odpowiedź na pytanie Managera:

```markdown
## Wyniki analizy zamówień e-commerce — [Twoje imię]

**Pytanie biznesowe:** Co możemy poprawić żeby zwiększyć zyski i satysfakcję klientów?

**Dane:** [opisz dataset — n zamówień, okres, kategorie]

**Kluczowe odkrycia:**
1. [Twoje odkrycie 1 — z konkretnymi liczbami]
2. [Twoje odkrycie 2 — z konkretnymi liczbami]
3. [Opcjonalnie: odkrycie 3]

**Trzy rekomendacje biznesowe:**
1. [Konkretne działanie + uzasadnienie liczbami]
2. [Konkretne działanie + uzasadnienie liczbami]
3. [Konkretne działanie + uzasadnienie liczbami]

**Jak AI pomogło w tej analizie:**
[1-2 zdania: co robiło AI, a co robiłeś/robiłaś Ty]
```

### Sprawdzenie 3 ✅

- [ ] KROK 1: Eksploracja wykonana — minimum 2 wykresy widoczne w notebooku
- [ ] KROK 1: Własne obserwacje zapisane (komórka Markdown — bez AI)
- [ ] KROK 2: Jeden aspekt wybrany i przeanalizowany z pomocą AI — kod działa
- [ ] KROK 3: Interpretacja AI wklejona + Twoja krytyczna ocena
- [ ] KROK 4: Komórka Markdown z wnioskami — pisana samodzielnie, zawiera liczby
- [ ] Całość logicznie spójna: pytanie --> analiza --> odkrycia --> rekomendacje

---

## Ćwiczenie 4: Case studies etyczne + commit (15 min)

### 4a. Case studies — omów z sąsiadem/sąsiadką (5 min)

Przeczytajcie każdy scenariusz i odpowiedzcie: **co powinien zrobić analityk?**

**Scenariusz 1 — Prywatność:**
> Twoja firma ma plik CSV z danymi 10 000 klientów: imię, email, historia zakupów (ze zniżkami i porzuconymi koszykami). Chcesz użyć ChatGPT żeby napisał Ci skrypt do segmentacji tych klientów. Najszybciej byłoby uploadować CSV bezpośrednio do ChatGPT Code Interpreter.

Pytania pomocnicze:
- Jakie dane osobowe są w pliku?
- Co mówi RODO o przesyłaniu danych osobowych do zewnętrznych usług?
- Jak możesz osiągnąć ten sam cel BEZ wysyłania prawdziwych danych?

**Scenariusz 2 — Weryfikacja:**
> AI wygenerował Ci raport z analizy sprzedaży. W raporcie pada zdanie: "Konwersja wyniosła 4.7%, co jest powyżej średniej branżowej wynoszącej 3.2% dla sektora e-commerce w Polsce (źródło: Raport E-commerce 2024)." Masz oddać raport Dyrektorowi za 30 minut.

Pytania pomocnicze:
- Czy 4.7% to Twoja prawdziwa konwersja (policzona z danych)?
- Czy "Raport E-commerce 2024" istnieje? Jak szybko sprawdzić?
- Co się stanie jeśli Dyrektor zapyta o to źródło?

**Scenariusz 3 — Odpowiedzialność:**
> Stworzyłeś model predykcji churnu klientów z pomocą AI — AI wygenerował cały kod od A do Z. Model działa (accuracy 78%). Wdrożenie automatycznie wysyła mailing z kuponem 30% rabatu do klientów "zagrożonych churnem". Po miesiącu okazuje się że model błędnie klasyfikuje 40% klientów premium — firma traci 80 000 PLN na niepotrzebnych kuponach.

Pytania pomocnicze:
- Kto ponosi odpowiedzialność — Ty czy AI?
- Co powinieneś/powinnaś był/a zrobić PRZED wdrożeniem?
- Jakie testy pomogłyby wykryć problem wcześniej?

```markdown
## Ćwiczenie 4a — Case studies etyczne

**Scenariusz 1 (Prywatność):**
[Co powinien zrobić analityk? Jakie ryzyko? Jak obejść problem?]

**Scenariusz 2 (Weryfikacja):**
[Co powinien zrobić analityk? Jak szybko sprawdzić "fakty" AI?]

**Scenariusz 3 (Odpowiedzialność):**
[Kto ponosi odpowiedzialność? Co należało zrobić inaczej?]
```

### 4b. Pytania refleksyjne (5 min)

Napisz krótkie odpowiedzi (2-4 zdania każda) w komórce Markdown:

```markdown
## Refleksja — AI w pracy analityka

**Pytanie 1:** W którym z Ćwiczeń 1-3 AI było najbardziej pomocne? Dlaczego?

**Pytanie 2:** Był moment na dzisiejszych zajęciach gdy zaufałeś/zaufałaś AI "za bardzo"?
(kiedy powinieneś/powinnaś był/a zweryfikować wynik ale tego nie zrobiłeś/zrobiłaś)

**Pytanie 3:** Jeśli za rok 80% kodu analitycznego będzie generowane przez AI —
jakie umiejętności człowieka będą najważniejsze? Wymień 3.
```

### 4c. Commit do repozytorium Git

```bash
# W terminalu VS Code:
cd ~/python2_projekt

# Sprawdź status
git status

# Dodaj notebook
git add s09_ai_analysis.ipynb

# Commit
git commit -m "S09: AI w analizie danych — prompty, ocena kodu AI, analiza z asystentem, etyka"

# Wypchnij (jeśli masz remote)
git push
```

### Sprawdzenie 4 ✅

- [ ] Case studies omówione — każdy scenariusz ma odpowiedź (min. 2 zdania)
- [ ] 3 pytania refleksyjne mają konkretne odpowiedzi
- [ ] `git log` — widoczny commit z plikiem `s09_ai_analysis.ipynb`
- [ ] Notebook działa end-to-end (Restart & Run All — komórki z kodem wykonują się bez błędów)

---

## Podsumowanie kluczowych zasad pracy z AI

```
DOBRY PROMPT = KONTEKST + ZADANIE + FORMAT + OGRANICZENIA

AI DOBRZE RADZI SOBIE Z:
  - Generowaniem kodu z precyzyjnym opisem
  - Tłumaczeniem wyników na język biznesowy
  - Mapowaniem/normalizacją kategorii (czyszczenie danych)
  - Pisaniem szablonowego kodu (transformacje, filtrowanie)
  - Wyjaśnianiem błędów (wklej traceback = dostaniesz diagnozę)

AI WYMAGA WERYFIKACJI PRZY:
  - Obliczeniach numerycznych (ZAWSZE uruchom kod)
  - Aktualnych danych i faktach (knowledge cutoff!)
  - Nazwach funkcji/parametrów nowych bibliotek (halucynacje!)
  - Edge cases w danych (NaN, puste DataFrame, string zamiast int)

ZASADY BEZPIECZEŃSTWA:
  - Nie wysyłaj danych osobowych klientów do publicznego API
  - Nie publikuj kluczy API w kodzie (zmienne środowiskowe!)
  - Anonimizuj dane przed wysłaniem (email -> hash, imię -> ID)
  - Sprawdź politykę prywatności narzędzia przed użyciem firmowych danych
```

---

## Zapowiedź S10

> "Ostatnie spotkanie: prezentacje mini-projektów — każdy/każda prezentuje 5-7 minut. Co to za dataset, jakie pytania biznesowe postawiliście, co znaleźliście, jakie wizualizacje. Notebook musi być na GitHubie z historią commitów. Zacznijcie przygotowania teraz — i śmiało użyjcie AI do przygotowania executive summary projektu."
