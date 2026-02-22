# S10 Wykład — Plan zajec dla prowadzacego

## Temat: Prezentacje mini-projektow i podsumowanie semestru

### Informacje organizacyjne
- **Czas:** 90 min (wykład, część 1 z 2 — po przerwie lab z rubrykami oceny)
- **Forma:** prezentacje studenckie + podsumowanie prowadzącego
- **Odpowiednik dzienny:** W15
- **Tryb:** zaoczne — wykład + lab prowadzi ta sama osoba (180 min łącznie)
- **Potrzebne:** komputer z projektorem, lista studentów z kartą ocen, timer (telefon), wydrukowane rubryki oceny koleżeńskiej (patrz `lab/cwiczenia.md`)
- **Przed zajęciami:** przygotuj listę kolejności prezentacji (losowa), wydrukuj rubryki, sprawdź projektor+HDMI
- **Kluczowe hasło:** "Dzisiaj Wy jesteście prowadzącymi — pokażcie co potraficie"

### Efekty uczenia się (Bloom poziom 4-5)
Po tym spotkaniu osoba studiująca:
1. **Prezentuje** wyniki samodzielnej analizy danych przed grupą, stosując jasną strukturę: problem -> dane -> metoda -> wyniki -> wnioski (Bloom 5)
2. **Ocenia** prezentacje kolegów pod kątem poprawności metodologicznej, czytelności wizualizacji i trafności wniosków biznesowych (Bloom 4)
3. **Podsumowuje** kluczowe umiejętności nabyte w semestrze i identyfikuje obszary do dalszego rozwoju (Bloom 4)

---

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **OTWARCIE** | Zasady prezentacji, kolejność, kryteria oceny | Rozmowa |
| 0:05-0:50 | **PREZENTACJE 1** | ~6-7 prezentacji x 7 min (5 min + 2 min pytania) | Studenci |
| 0:50-1:00 | **PRZERWA** | 10 minut | --- |
| 1:00-1:15 | **PREZENTACJE 2** | ~2-3 prezentacje lub doprezentowanie opóźnionych | Studenci |
| 1:15-1:25 | **PODSUMOWANIE** | Roadmapa S01-S10, co dalej po kursie | Prowadzący |
| 1:25-1:30 | **EGZAMIN** | Zakres, format, ściąga A4, materiały do powtórki | Prowadzący |

> Po przerwie 10-15 min zaczynasz część lab (kolejne 90 min) — tam: weryfikacja portfolio GitHub, ocena koleżeńska, checklist, ankieta ewaluacyjna. Patrz `lab/cwiczenia.md`.

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — OTWARCIE

> "Ostatnie spotkanie w tym semestrze. Dzisiaj role się odwracają — to Wy prezentujecie, ja słucham i oceniam. Każdy i każda z Was ma 5 minut na prezentację swojego mini-projektu plus 2 minuty na pytania ode mnie i od kolegów."

**[Wyświetl na projektorze — zasady]**

```
ZASADY PREZENTACJI S10:

  Czas: 5 minut prezentacja + 2 minuty pytania
   (po 5 minutach przerywam — szanujmy czas wszystkich)

  Struktura (sugerowana):
   1. Problem biznesowy / pytanie badawcze (30 sek)
   2. Dataset — skąd, ile wierszy, jakie kolumny (30 sek)
   3. Co zrobiłem/zrobiłam — pipeline analizy (1 min)
   4. Kluczowe wizualizacje — 2-3 wykresy (1.5 min)
   5. Wnioski i rekomendacje (1 min)
   6. Czego się nauczyłem/nauczyłam (30 sek)

  Format: notebook Jupyter otwarty na projektorze
   (nie robimy slajdów — pokazujemy żywy notebook)

  Oceniam (szczegółowa rubryka — dostaliście ją na S08):
   - Czy analiza jest kompletna (EDA -> czyszczenie -> wizualizacja -> wnioski)
   - Czy wizualizacje są czytelne i mają etykiety
   - Czy wnioski są poparte danymi
   - Czy kod jest na GitHubie z historią commitów
   - Czy potraficie wyjaśnić swój kod i wyniki
```

> "Kolejność prezentacji — losowa. Wylosuję teraz."

**[Wylosuj kolejność — np. karteczki z nazwiskami lub random.sample() w Pythonie]**

```python
# Można pokazać na żywo:
import random
studenci = ["..."]  # lista z dziennika
random.seed(42)     # dla powtarzalności
kolejnosc = random.sample(studenci, len(studenci))
for i, s in enumerate(kolejnosc, 1):
    print(f"{i}. {s}")
```

> "Podczas prezentacji kolegów — słuchajcie aktywnie. Dostaniecie rubrykę oceny koleżeńskiej — po każdej prezentacji krótko oceńcie. To nie wpływa na ocenę, ale uczy Was krytycznego patrzenia na analizy — co jest kluczowe w pracy analityka."

**[Rozdaj wydrukowane rubryki oceny koleżeńskiej — szablon w lab/cwiczenia.md]**

---

### 0:05-0:50 — PREZENTACJE (runda 1, ~6-7 prezentacji)

**Dla każdej prezentacji:**

1. Zaproś studenta: *"Proszę — [imię]. 5 minut, czas start."*
2. Odmierzaj czas (telefon/timer)
3. Po 4:30 — sygnał "30 sekund"
4. Po 5:00 — "Dziękuję. Pytania?"
5. 1-2 pytania (Twoje lub z sali)
6. Krótki komentarz (1-2 zdania): co było dobre, co można poprawić

**Pytania do zadania studentom (wybierz 1-2 na prezentację):**

```
PYTANIA WERYFIKUJĄCE:
- "Dlaczego wybrałeś/wybrałaś ten dataset?"
- "Co było najtrudniejsze w czyszczeniu danych?"
- "Gdybyś miał/miała więcej czasu — co byś dodał/dodała?"
- "Jak interpretujesz ten wykres dla kogoś kto nie zna Pythona?"
- "Ile commitów masz na GitHubie? Pokaż git log."
- "Czy użyłeś/użyłaś AI do pomocy? W czym konkretnie?"
- "Co by się zmieniło gdybyś usunął/usunęła outliersy?"
- "Jaka jest Twoja rekomendacja biznesowa?"
- "Której techniki z kursu użyłeś/aś najczęściej?"
- "Co byś zrobił/a inaczej gdybyś zaczynał/a projekt od nowa?"
```

**Jeśli student nie przygotował prezentacji:**
> "Rozumiem. Masz czas do [data — +1 tydzień] żeby przesłać notebook z analizą na GitHuba i umówić się na krótką rozmowę online (5 min). Bez prezentacji — brak pełnej oceny za projekt."

**Między prezentacjami** (30 sek przerwa):
> "Zapiszcie ocenę koleżeńską. Następny/następna — [imię]."

**Wskazówka czasowa:** Na zaocznych grupa jest zazwyczaj mniejsza (8-12 osób). Przy 7 min/osoba:
- 7 prezentacji = 49 min (mieści się w rundzie 1)
- 10 prezentacji = 70 min (potrzebujesz obu rund)
- Jeśli >10 prezentacji — skróć czas do 6 min (4+2)

---

### 0:50-1:00 — PRZERWA (10 min)

---

### 1:00-1:15 — PREZENTACJE (runda 2)

Kontynuacja prezentacji. Jeśli wszyscy zaprezentowali w rundzie 1:

> "Czy ktoś chce pokazać coś dodatkowego — na przykład jak użył AI do pomocy w analizie? Albo interesujący bug który znalazł w danych?"

**Jeśli zostaje czas — mini dyskusja:**

> "Jakie prezentacje najbardziej Was zaskoczyły? Co Was zainspirowało? Kto z Was zobaczył technikę której sam nie użył a chciałby?"

---

### 1:15-1:25 — PODSUMOWANIE SEMESTRU (10 min)

> "Pozwólcie że podsumujemy co zrobiliśmy w tym semestrze."

**[Wyświetl na projektorze — roadmapa]**

```
ROADMAPA PYTHON II (zaoczne) — CO UMIECIE:

S01  [check] Warsztat pracy: Git, GitHub, Markdown, VS Code, Jupyter
S02  [check] NumPy: tablice, operacje wektorowe, broadcasting, generowanie
S03  [check] Pandas I: Series, DataFrame, wczytywanie, loc/iloc, filtrowanie
S04  [check] Pandas II: czyszczenie danych, merge, groupby, pivot_table
S05  [check] Wizualizacja: Matplotlib + Seaborn, subplots, dashboard
S06  [check] Statystyka opisowa: miary, korelacja, rozkłady
S07  [check] Statystyka: testy hipotez, A/B testing, chi-kwadrat
S08  [check] Zaawansowane: scikit-learn, Plotly, Polars
S09  [check] LLM i AI: API, prompty, generowanie kodu, etyka
S10  [check] Prezentacje projektów  <-- DZIS JESTESMY TUTAJ
```

> "Spójrzcie na tę listę. Na początku semestru — większość z Was nie wiedziała co to DataFrame. Dzisiaj robicie samodzielne analizy, piszecie kod, commitujecie na GitHuba, tworzycie wizualizacje i wyciągacie wnioski biznesowe. To jest kompletny fundament analityka danych."

> "Chcę powiedzieć jedną ważną rzecz: to co umiecie to FUNDAMENT. Rynek pracy wymaga ciągłego uczenia się. Ale fundamenty się nie starzeją — NumPy, Pandas, Matplotlib, Git — to narzędzia które za 10 lat nadal będą w użyciu. Nazwy mogą się zmienić, ale koncepcje zostaną."

**[Wyświetl — co dalej]**

```
CO DALEJ — SCIEZKI ROZWOJU:

ANALITYKA ZAAWANSOWANA
   -> SQL (PostgreSQL, BigQuery)
   -> Power BI / Tableau (dashboardy)
   -> A/B testing w skali (Bayesian methods)

MACHINE LEARNING
   -> scikit-learn pogłębiony (Random Forest, XGBoost)
   -> Deep Learning (PyTorch, TensorFlow)
   -> MLOps (MLflow, Docker, deployment)

DATA ENGINEERING
   -> Apache Spark / Polars (duże dane)
   -> ETL/ELT (Airflow, dbt)
   -> Cloud (AWS/GCP/Azure)

AI / LLM
   -> Prompt engineering zaawansowany
   -> RAG (Retrieval-Augmented Generation)
   -> Agenty AI (LangChain, Claude Code SDK)

PORTFOLIO
   -> GitHub = Wasze CV techniczne
   -> Kaggle — konkursy i datasety
   -> Blog techniczny (Medium, Substack)
```

> "Moja rekomendacja: nie próbujcie uczyć się wszystkiego naraz. Wybierzcie JEDNĄ ścieżkę i zainwestujcie w nią 2-3 miesiące. Potem kolejną. Portfolio na GitHubie — to jest Wasza wizytówka na rozmowach kwalifikacyjnych."

---

### 1:25-1:30 — INFORMACJE O EGZAMINIE (5 min)

> "Teraz najważniejsze informacje o egzaminie."

**[Wyświetl na projektorze]**

```
EGZAMIN — INFORMACJE:

  Termin: [do ustalenia — podać datę z harmonogramu sesji zaocznej]
  Czas: 90 minut
  Forma: pisemny — zadania praktyczne + pytania teoretyczne

ZAKRES (S01-S07 + elementy S08):
  - NumPy — operacje, broadcasting, axis
  - Pandas — DataFrame, loc/iloc, filtrowanie, groupby, merge, czyszczenie
  - Matplotlib/Seaborn — tworzenie i odczytywanie wykresów
  - Statystyka — opisowa, korelacja, testy hipotez, interpretacja p-wartości
  - Git — podstawowe komendy, workflow

CZEGO NIE BEDZIE:
  - scikit-learn, Plotly, Polars (S08) — to był bonus/przegląd
  - Szczegóły API AI (S09) — to był przegląd
  - Kod z pamięci — będziecie mieli dostęp do ściągi

SCIAGA:
  - 1 kartka A4 (obie strony), napisana ręcznie lub wydrukowana
  - Może zawierać: wzory, fragmenty kodu, notatki
  - Nie może to być kompletny wydruk skryptu (sprawdzę)

MATERIALY DO POWTORKI:
  - Skrypt studenta (skryptdlastudentow/skrypt.md)
  - Quizy z każdego spotkania
  - Notebooki demonstracyjne — uruchomcie je jeszcze raz
  - Ćwiczenia laboratoryjne — przejrzyjcie rozwiązania
```

> "Egzamin to nie jest test pamięci. Daję Wam ściągę — jedną kartkę A4 z czym chcecie, obie strony. Pytania będą wymagały MYŚLENIA — dam Wam fragment kodu i zapytam co zwróci, pokażę wykres i zapytam o interpretację, dam dataset i zapytam jak go wyczyścić. Techniki z S01-S07 — to jest zakres."

> "Na zaocznych macie mniej czasu, ale te same fundamenty. Kto regularnie robił ćwiczenia laboratoryjne — nie powinien mieć problemów."

> "Pytania przed egzaminem — piszcie na maila, odpowiadam w ciągu 24 godzin."

---

## Przejście do części laboratoryjnej

> "Teraz 10-15 minut przerwy, a potem część laboratoryjna: weryfikacja portfolio GitHub, zebranie ocen koleżeńskich, ankieta ewaluacyjna i podsumowanie ocen."

---

## Uwagi organizacyjne dla prowadzącego

### Specyfika zaocznych
- Grupa zazwyczaj mniejsza (8-15 osób) — więcej czasu na każdego studenta
- Studenci pracują zawodowo — mogą mieć mniej commitów, ale bardziej dojrzałe projekty
- Niektórzy mogą mieć problemy z obecnością — przygotuj procedurę alternatywną (patrz `lab/cwiczenia.md`)
- Na zaocznych prowadzisz i wykład i lab — masz pełną kontrolę nad czasem i oceną

### Zarządzanie czasem
- Jeśli grupa <8 osób — wszystkie prezentacje zmieszczą się w rundzie 1, masz więcej czasu na podsumowanie
- Jeśli grupa >12 osób — rozważ skrócenie do 6 min (4+2) lub przeniesienie części prezentacji na blok laboratoryjny
- Przerwa między wykładem a labem — elastyczna, minimum 10 min

### Przygotowanie sali
- Sprawdź projektor i HDMI 15 min przed zajęciami
- Przygotuj zapasowy kabel HDMI/USB-C
- Miej otwarty GitHub w przeglądarce — będziesz weryfikować repozytoria
- Timer na telefonie — widoczny na ekranie (opcjonalnie wyświetl na projektorze)
