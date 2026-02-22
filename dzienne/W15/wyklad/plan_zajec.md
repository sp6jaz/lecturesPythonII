# W15 Wykład — Plan zajęć dla prowadzącego

## Temat: Prezentacje mini-projektów i podsumowanie semestru

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** prezentacje studenckie + podsumowanie prowadzącego
- **Potrzebne:** komputer z projektorem, lista studentów z kartą ocen, timer (telefon)
- **Przed wykładem:** przygotuj listę kolejności prezentacji (losowa lub alfabetyczna), wydrukuj rubryki oceny
- **Kluczowe hasło:** "Dzisiaj Wy jesteście prowadzącymi — pokażcie co potraficie"

### Efekty uczenia się (Bloom poziom 4-5)
Po tym wykładzie osoba studiująca:
1. **Prezentuje** wyniki samodzielnej analizy danych przed grupą, stosując jasną strukturę: problem → dane → metoda → wyniki → wnioski (Bloom 5)
2. **Ocenia** prezentacje kolegów pod kątem poprawności metodologicznej, czytelności wizualizacji i trafności wniosków biznesowych (Bloom 4)
3. **Podsumowuje** kluczowe umiejętności nabyte w semestrze i identyfikuje obszary do dalszego rozwoju (Bloom 4)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **OTWARCIE** | Zasady prezentacji, kolejność, kryteria oceny | Rozmowa |
| 0:05-0:50 | **PREZENTACJE 1** | ~6 prezentacji × 7 min (5 min + 2 min pytania) | Studenci |
| 0:50-1:00 | **PRZERWA** | 10 minut | — |
| 1:00-1:20 | **PREZENTACJE 2** | ~3 prezentacje lub doprezentowanie opóźnionych | Studenci |
| 1:20-1:35 | **PODSUMOWANIE** | Podsumowanie semestru, roadmapa umiejętności, informacje o egzaminie | Prowadzący |
| 1:35-1:45 | **ZAMKNIĘCIE** | Ankieta ewaluacyjna, podziękowania | Prowadzący |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — OTWARCIE

> "Ostatni wykład w tym semestrze. Dzisiaj role się odwracają — to Wy prezentujecie, ja słucham i oceniam. Każdy i każda z Was ma 5 minut na prezentację swojego mini-projektu plus 2 minuty na pytania ode mnie i od kolegów."

**[Wyświetl na projektorze — zasady]**

```
ZASADY PREZENTACJI W15:

⏱  Czas: 5 minut prezentacja + 2 minuty pytania
   (po 5 minutach przerywam — szanujmy czas wszystkich)

📊 Struktura (sugerowana):
   1. Problem biznesowy / pytanie badawcze (30 sek)
   2. Dataset — skąd, ile wierszy, jakie kolumny (30 sek)
   3. Co zrobiłem/zrobiłam — pipeline analizy (1 min)
   4. Kluczowe wizualizacje — 2-3 wykresy (1.5 min)
   5. Wnioski i rekomendacje (1 min)
   6. Czego się nauczyłem/nauczyłam (30 sek)

💻 Format: notebook Jupyter otwarty na projektorze
   (nie robimy slajdów — pokazujemy żywy notebook)

📋 Oceniam:
   • Czy analiza jest kompletna (EDA → czyszczenie → wizualizacja → wnioski)
   • Czy wizualizacje są czytelne i mają etykiety
   • Czy wnioski są poparte danymi
   • Czy kod jest na GitHubie z historią commitów
   • Czy potraficie wyjaśnić swój kod i wyniki
```

> "Kolejność prezentacji — losowa. Wylosuję teraz."

**[Wylosuj kolejność — np. karteczki z nazwiskami lub random.sample() w Pythonie]**

```python
# Można pokazać na żywo:
import random
studenci = ["..."]  # lista z dziennika
random.seed(42)  # dla powtarzalności
kolejnosc = random.sample(studenci, len(studenci))
for i, s in enumerate(kolejnosc, 1):
    print(f"{i}. {s}")
```

> "Podczas prezentacji kolegów — słuchajcie aktywnie. Dostaniecie rubrykę oceny koleżeńskiej — po każdej prezentacji krótko oceńcie. To nie wpływa na ocenę, ale uczy Was krytycznego patrzenia na analizy — co jest kluczowe w pracy."

---

### 0:05-0:50 — PREZENTACJE (runda 1, ~6 prezentacji)

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
• "Dlaczego wybrałeś/wybrałaś ten dataset?"
• "Co było najtrudniejsze w czyszczeniu danych?"
• "Gdybyś miał/miała więcej czasu — co byś dodał/dodała?"
• "Jak interpretujesz ten wykres dla kogoś kto nie zna Pythona?"
• "Ile commitów masz na GitHubie? Pokaż git log."
• "Czy użyłeś/użyłaś AI do pomocy? W czym konkretnie?"
• "Co by się zmieniło gdybyś usunął/usunęła outliersy?"
• "Jaka jest Twoja rekomendacja biznesowa?"
```

**Jeśli student nie przygotował prezentacji:**
> "Rozumiem. Masz czas do [data] żeby przesłać notebook z analizą na GitHuba i umówić się na krótką rozmowę. Bez prezentacji — brak oceny za projekt."

**Między prezentacjami** (30 sek przerwa):
> "Zapiszcie ocenę koleżeńską. Następny/następna — [imię]."

---

### 0:50-1:00 — PRZERWA (10 min)

---

### 1:00-1:20 — PREZENTACJE (runda 2 + rezerwa)

Kontynuacja prezentacji. Jeśli zostanie czas:

> "Czy ktoś chce pokazać coś dodatkowego — np. jak użył AI do pomocy w analizie? Albo interesujący bug który znalazł w danych?"

**Jeśli wszyscy zaprezentowali wcześniej — mini dyskusja:**

> "Jakie prezentacje najbardziej Was zaskoczyły? Co Was zainspirował? Kto z Was zobaczył technikę której sam nie użył a chciałby?"

---

### 1:20-1:35 — PODSUMOWANIE SEMESTRU (15 min)

> "Pozwólcie że podsumujemy co zrobiliśmy w tym semestrze."

**[Wyświetl na projektorze — roadmapa]**

```
ROADMAPA PYTHON II — CO UMIECIE:

W01  ✓ Git, GitHub, Markdown, Mermaid, VS Code
W02  ✓ Pipeline analityczny, Jupyter, typy danych
W03  ✓ NumPy — tworzenie tablic, operacje wektorowe, broadcasting
W04  ✓ NumPy — reshape, zaawansowane operacje, generowanie danych
W05  ✓ Pandas — Series, DataFrame, wczytywanie danych, EDA
W06  ✓ Pandas — loc/iloc, filtrowanie, segmentacja
W07  ✓ Pandas — czyszczenie danych (NaN, duplikaty, typy, stringi)
W08  ✓ Pandas — merge, concat, groupby, pivot_table
W09  ✓ Matplotlib — Figure/Axes, wykresy liniowe, słupkowe, scatter, histogramy
W10  ✓ Seaborn + dashboard, subplots, eksport
W11  ✓ Statystyka opisowa, korelacja, rozkłady
W12  ✓ Testy hipotez, A/B testing, chi-kwadrat
W13  ✓ scikit-learn (KMeans, regresja), Plotly (interaktywne), Polars
W14  ✓ LLM i AI w analizie danych — API, prompty, etyka
W15  ✓ Prezentacje projektów ← DZIŚ JESTEŚMY TUTAJ
```

> "Spójrzcie na tę listę. Na początku semestru — większość z Was nie wiedziała co to DataFrame. Dzisiaj robicie samodzielne analizy, piszecie kod, commitujecie na GitHuba, tworzycie wizualizacje i wyciągacie wnioski biznesowe. To jest kompletny fundament analityka danych."

> "Chcę powiedzieć jedną ważną rzecz: to co umiecie to FUNDAMENT. Rynek pracy wymaga ciągłego uczenia się. Ale fundamenty się nie starzeją — NumPy, Pandas, Matplotlib, Git — to narzędzia które za 10 lat nadal będą w użyciu. Nazwy mogą się zmienić, ale koncepcje zostaną."

**[Wyświetl — co dalej]**

```
CO DALEJ — ŚCIEŻKI ROZWOJU:

🔬 ANALITYKA ZAAWANSOWANA
   → SQL (PostgreSQL, BigQuery)
   → Power BI / Tableau (dashboardy)
   → A/B testing w skali (Bayesian methods)

🤖 MACHINE LEARNING
   → scikit-learn pogłębiony (Random Forest, XGBoost)
   → Deep Learning (PyTorch, TensorFlow)
   → MLOps (MLflow, Docker, deployment)

📊 DATA ENGINEERING
   → Apache Spark / Polars (duże dane)
   → ETL/ELT (Airflow, dbt)
   → Cloud (AWS/GCP/Azure)

🧠 AI / LLM
   → Prompt engineering zaawansowany
   → RAG (Retrieval-Augmented Generation)
   → Agenty AI (LangChain, Claude Code SDK)

💼 PORTFOLIO
   → GitHub = Wasze CV techniczne
   → Kaggle — konkury i datasety
   → Blog techniczny (Medium, Substack)
```

> "Moja rekomendacja: nie próbujcie uczyć się wszystkiego naraz. Wybierzcie JEDNĄ ścieżkę i zainwestujcie w nią 2-3 miesiące. Potem kolejną. Portfolio na GitHubie — to jest Wasza wizytówka na rozmowach kwalifikacyjnych."

**[Informacje o egzaminie]**

> "Teraz informacje o egzaminie."

```
EGZAMIN — INFORMACJE:

📅 Termin: [do ustalenia — podać datę z harmonogramu]
⏱  Czas: 90 minut
📝 Forma: pisemny — zadania praktyczne + pytania teoretyczne

ZAKRES:
• NumPy — operacje, broadcasting, axis
• Pandas — DataFrame, loc/iloc, filtrowanie, groupby, merge, czyszczenie
• Matplotlib/Seaborn — tworzenie i odczytywanie wykresów
• Statystyka — opisowa, korelacja, testy hipotez, interpretacja p-wartości
• Git — podstawowe komendy, workflow

CZEGO NIE BĘDZIE:
• scikit-learn, Plotly, Polars (W13) — to był bonus
• Szczegóły API AI (W14) — to był przegląd
• Kod z pamięci — będziecie mieli dostęp do ściągi (1 kartka A4)

MATERIAŁY DO POWTÓRKI:
• Skrypt studenta (skryptdlastudentow/skrypt.md)
• Quizy z każdego tygodnia (W01-W12)
• Notebooki demonstracyjne — uruchomcie je jeszcze raz
• Ćwiczenia laboratoryjne — przejrzyjcie rozwiązania
```

> "Egzamin to nie jest test pamięci. Daję Wam ściągę — jedną kartkę A4 z czym chcecie. Pytania będą wymagały MYŚLENIA — dam Wam fragment kodu i zapytam co zwróci, pokażę wykres i zapytam o interpretację, dam dataset i zapytam jak go wyczyścić. Techniki z W01-W12 — to jest zakres."

---

### 1:35-1:45 — ZAMKNIĘCIE

> "Na koniec — ankieta ewaluacyjna. Kilka pytań, anonimowo. Zależy mi na Waszej opinii — każdy komentarz pomaga mi ulepszyć ten kurs na przyszłość."

**[Ankieta — wyświetl QR kod do formularza lub rozdaj kartki]**

```
ANKIETA EWALUACYJNA (anonimowa):

1. Które tematy były najbardziej przydatne? (1-3 odpowiedzi)
   □ Git/GitHub  □ NumPy  □ Pandas  □ Matplotlib/Seaborn
   □ Statystyka  □ scikit-learn/Plotly  □ LLM/AI

2. Co było najtrudniejsze?

3. Co zmieniłbyś/zmieniłabyś w tym kursie?

4. Czy tempo było: □ za wolne  □ odpowiednie  □ za szybkie

5. Oceń ogólną przydatność kursu (1-5): ___

6. Wolny komentarz (opcjonalnie):
```

> "Wypełnijcie w ciągu 3-4 minut. Możecie zostawić kartki na biurku wychodząc."

**[Po zebraniu ankiet]**

> "Dziękuję Wam za ten semestr. Widziałem jak rośliście z tygodnia na tydzień — od pierwszego commita na W01 do samodzielnych analiz na W15. To jest dokładnie to, o co chodzi w tym kursie."

> "Powodzenia na egzaminie. Skrypt, quizy, notebooki — macie wszystko na GitHubie. Pytania przed egzaminem — piszcie na mail, odpowiadam w ciągu 24 godzin."

> "Do zobaczenia na egzaminie. Kto chce porozmawiać indywidualnie o dalszej ścieżce rozwoju — zapraszam na dyżur."
