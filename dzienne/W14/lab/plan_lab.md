# L14 — Plan laboratorium dla prowadzącego

## Temat: LLM i AI w analizie danych — praktyczne użycie

**Programowanie w Pythonie II** | Laboratorium 14
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne przy komputerze
**Prowadzący:** doktorant (laboratoria prowadzone samodzielnie)

---

## Efekty uczenia się (Bloom poziom 4-5)

Po tych zajęciach osoba studiująca:
1. **Projektuje** efektywne prompty do zadań analitycznych, stosując strukturę: kontekst + zadanie + format + ograniczenia (Bloom 5)
2. **Ocenia** kod wygenerowany przez AI pod kątem poprawności, kompletności i zgodności z wymaganiami (Bloom 4)
3. **Konstruuje** kompletny workflow analizy danych z pomocą AI: od eksploracji przez interpretację po formułowanie wniosków (Bloom 5)
4. **Uzasadnia** ograniczenia etyczne i techniczne stosowania AI w analizie danych na konkretnych przykładach (Bloom 4)

---

## Plan minutowy

| Czas | Etap | Opis | Uwagi |
|------|------|------|-------|
| 0:00-0:05 | Organizacja | Sprawdzenie listy, weryfikacja narzędzi, omówienie zasad | Otwierają przeglądarki |
| 0:05-0:10 | Wprowadzenie | Krótki kontekst: "AI jako współpracownik, nie wyrocznię" | Bez live coding |
| 0:10-0:30 | Ćwiczenie 1 | Prompt engineering — pisanie efektywnych promptów (20 min) | Para lub samodzielnie |
| 0:30-0:50 | Ćwiczenie 2 | Generowanie kodu z AI — ocena i weryfikacja (20 min) | Samodzielnie |
| 0:50-1:20 | Ćwiczenie 3 | AI-wspomagana analiza datasetu (30 min) | Samodzielnie |
| 1:20-1:35 | Ćwiczenie 4 | Etyka, ograniczenia, refleksja, commit (15 min) | Para lub grupy 3 |
| 1:35-1:45 | Podsumowanie | Omówienie wyników, zapowiedź L15 (prezentacje) | Dyskusja |

---

## Organizacja sali

- Studenci pracują przy komputerach — dostęp do internetu wymagany
- Narzędzia AI (free tier — bez kluczy API):
  - **Claude.ai** — https://claude.ai (konto Google/email, darmowe)
  - **ChatGPT** — https://chat.openai.com (konto OpenAI, darmowe)
  - **GitHub Copilot** — jeśli ktoś już ma zainstalowany w VS Code
- Tworzą notebook `.ipynb` o nazwie: `lab14_ai_analysis.ipynb`
- Commit na koniec zajęć (Ćwiczenie 4)

### Uwagi do narzędzi
- Claude free tier: ok. 20-30 wiadomości co kilka godzin — w zupełności wystarczy na te zajęcia
- ChatGPT free: GPT-4o mini jest dostępny bez limitów, GPT-4o z limitem
- Studenci mogą używać dowolnego narzędzia — nie narzucamy wyboru
- Ćwiczenia są zaprojektowane tak żeby działały z KAŻDYM narzędziem

### Środowisko Python
```bash
# Aktywacja środowiska
cd ~/python2_projekt
source .venv/bin/activate   # Linux/Mac
# lub
.venv\Scripts\activate      # Windows

# Wymagane pakiety (powinny być z poprzednich tygodni)
python -c "import pandas, numpy, matplotlib, seaborn; print('OK')"

# Otwarcie VS Code
code .
```

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przed zajęciami (10 min wcześniej)
- [ ] Przetestuj dostęp do claude.ai lub chat.openai.com na komputerze w sali
- [ ] Sprawdź czy sieć uczelniana nie blokuje tych stron
- [ ] Miej przygotowane konto demonstracyjne (ewentualnie własne claude.ai) do pokazania interfejsu
- [ ] Przejrzyj ćwiczenia — zrozum co studenci będą robić żeby sprawnie pomagać

### Podczas zajęć

**Kluczowa filozofia tych laboratoriów:**
> Celem NIE jest nauczyć studentów używać chatbota. Celem jest nauczyć ich *jak myśleć* przy pracy z AI — co podać, co sprawdzić, jak ocenić wynik.

- Gdy student mówi "AI mi to napisało i działa" — zapytaj: "Rozumiesz co ten kod robi? Zmień jedną rzecz."
- Gdy student jest sfrustrowany że "AI nie odpowiada dobrze" — naprowadzaj na ulepszenie promptu, nie na zmianę narzędzia
- Ćwiczenie 1 polecane w parach — "pair prompting" jest produktywną techniką

**Typowe pułapki:**
- Student kopiuje kod z AI i nie uruchamia go → nakłoń do uruchomienia ZARAZ, nie "potem"
- Student pisze zbyt ogólny prompt i dostaje ogólną odpowiedź → "co jest niejasne dla modelu w tym prompcie?"
- Student tratuje każdą odpowiedź AI jako prawdę → "jak byś to zweryfikował?"

**Naprowadzające pytania do ćwiczenia 2:**
- "Czy ten kod zadziała na Twoich danych? Przetestuj."
- "Co się stanie jak podasz pustą kolumnę?"
- "Czy AI użyło bibliotek zgodnie z ograniczeniami które podałeś?"

**Naprowadzające pytania do ćwiczenia 3:**
- "Co AI zaproponowało jako wniosek? Czy zgadzasz się z tą interpretacją?"
- "Gdyby AI się pomyliło — jak byś to wykrył?"
- "Czy ten wniosek odpowiada na pytanie biznesowe z początku analizy?"

### Tempo grup
- Szybcy studenci: Ćwiczenie 3 rozszerzenie — pipeline z wieloma krokami AI
- Wolni studenci: Ćwiczenia 1 + 2 + commit podstawowy wystarczają

### Pair programming
- Studenci mogą pracować w parach: **pilot** (pisze kod) + **navigator** (czyta instrukcję, podpowiada, sprawdza)
- Co 15-20 minut zamiana ról
- Pair programming zmniejsza frustrację i przyspiesza naukę — zachęcaj, ale nie wymuszaj

---

## Tabela rozwiązywania problemów (Troubleshooting)

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| Claude/ChatGPT zablokowane przez sieć uczelnianą | Firewall uczelniany | Spróbuj przez hotspot mobilny; lub użyj notebooka llm_demo.ipynb z mock responses |
| Rate limit — "Too many requests" | Darmowy tier ma limity | Poczekaj 5-10 min lub przejdź na inne narzędzie (Claude → ChatGPT) |
| AI generuje kod z nieistniejącą funkcją | Halucynacja (zwł. starsze modele) | Uruchomić kod, odczytać błąd, zapytać AI o poprawkę z treścią błędu |
| Kod AI nie obsługuje edge cases | Ogólny prompt bez przykładów danych | Dodaj do promptu przykładowe dane: "np. kolumna zawiera: None, '', '0', 0" |
| Student nie ma konta w Claude/ChatGPT | Brak rejestracji | Pomoc w rejestracji (wymaga adresu email, zajmuje 2 min) |
| AI odpowiada po angielsku | Brak instrukcji języka | Dodaj do promptu: "Odpowiadaj po polsku" lub użyj system message |
| AI daje bardzo długą odpowiedź z dużą ilością teorii | Za ogólny prompt | Dodaj: "Tylko kod, bez wyjaśnień" lub "Odpowiedź max 100 słów" |
| Wyniki ćwiczenia 3 różnią się między studentami | Różne wersje AI, różne prompty — to normalne | Przedyskutuj różnice jako ciekawość: "Dlaczego wasze wyniki się różnią?" |
| Student nie może uruchomić Pythona obok chata AI | Organizacja okien | Pokaż jak otworzyć VS Code i przeglądarkę obok siebie (split screen) |
| Brak dostępu do internetu | Awaria sieci | Użyj llm_demo.ipynb z wykładu — wszystkie ćwiczenia mają wersję offline |

---

## Weryfikacja wyników — klucz oceniania

### Ćwiczenie 1 (Prompt engineering)
- Prompt zawiera: kontekst (DataFrame + kolumny), zadanie, format wyjścia, ograniczenia
- Student potrafi wyjaśnić DLACZEGO każdy element promptu jest ważny
- Ulepszony prompt daje lepszą odpowiedź niż wersja wyjściowa

### Ćwiczenie 2 (Ocena kodu)
- Kod uruchomiony — działa lub błąd zidentyfikowany i zgłoszony do AI
- Lista "co zrobione dobrze / co brakuje" nie jest pusta
- Poprawiona wersja kodu działa na przykładowych danych z ćwiczenia

### Ćwiczenie 3 (Analiza z AI)
- Co najmniej 3 kroki analizy przeprowadzone z udziałem AI
- Wniosek końcowy jest w języku polskim, bez żargonu statystycznego
- Notebook ma komórkę Markdown z wnioskiem wygenerowanym przez AI i oceną studenta

### Ćwiczenie 4 (Etyka + commit)
- Komórka Markdown z odpowiedziami na pytania refleksyjne
- `git log` — widoczny commit z plikiem `lab14_ai_analysis.ipynb`

---

## Zapowiedź L15

> "Za tydzień: ostatnie zajęcia. Prezentacje Waszych mini-projektów — każdy/każda prezentuje 5-7 minut: co to za dataset, jakie pytania biznesowe postawiliście, co znaleźliście, jak wyglądają Wasze wizualizacje i kluczowy wniosek. Notebook musi być na GitHubie z historią commitów. Zacznijcie gotować się TERAZ — mam nadzieję że użyjecie AI do przygotowania dobrego executive summary projektu."
