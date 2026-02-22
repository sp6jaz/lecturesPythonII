# S09 Wykład — Plan zajęć dla prowadzącego

## Temat: LLM i AI w analizie danych

### Informacje organizacyjne
- **Czas:** 90 min (blok wykładowy) + 90 min (blok laboratoryjny) = 180 min total
- **Forma:** wykład konwersatoryjny z demonstracjami konceptualnymi (bez kluczy API)
- **Tryb:** zaoczny — prowadzący prowadzi wykład i laboratorium osobiście
- **Potrzebne:** komputer z projektorem, VS Code, przeglądarka (Claude.ai / ChatGPT)
- **Przed zajęciami:** otwórz ten plan + `cwiczenia.md` — w bloku lab studenci pracują z AI
- **Kontekst kursu:** studenci mają za sobą S01-S08 (pełny stack: NumPy, Pandas, Matplotlib, Seaborn, statystyka, scikit-learn, Plotly)
- **Kluczowe hasło:** "AI nie zastąpi analityka danych — ale analityk używający AI zastąpi tego, który nie używa"

### Efekty uczenia się (Bloom poziom 2-5)
Po tym spotkaniu osoba studiująca:
1. **Wyjaśnia** czym jest model językowy (LLM), czym są tokeny i temperatura, oraz jak modele GPT/Claude/Gemini różnią się w zastosowaniach analitycznych (Bloom 2)
2. **Stosuje** strukturę API (system/user/assistant) do formułowania zapytań do modeli językowych z Pythona (Bloom 3)
3. **Projektuje** efektywne prompty do zadań analitycznych: generowanie kodu, interpretacja wyników, czyszczenie danych, executive summary (Bloom 5)
4. **Ocenia** przydatność i ograniczenia narzędzi AI w kontekście analizy danych — halucynacje, knowledge cutoff, prywatność, odpowiedzialność (Bloom 4)
5. **Konstruuje** workflow analizy danych wspomagany przez AI, łącząc własne umiejętności analityczne z możliwościami generatywnego AI (Bloom 5)

### Plan minutowy (90 min wykład)

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **WPROWADZENIE** | Temat, cele, plan zajęć. "Ostatni nowy temat semestru." | Rozmowa |
| 0:05-0:25 | **MATERIAŁ 1** | Co to są LLM — historia Transformera, GPT/Claude/Gemini, pipeline | Pokaz konceptualny + tablica |
| 0:25-0:40 | **MATERIAŁ 2** | Tokeny i temperatura — kiedy niska, kiedy wysoka, koszty | Notebook (mock) |
| 0:40-0:55 | **MATERIAŁ 3** | API z Pythona: OpenAI i Anthropic — system/user/assistant, structured output | Notebook (mock) |
| 0:55-1:05 | **PRZERWA** | 10 minut | — |
| 1:05-1:20 | **MATERIAŁ 4** | 4 zastosowania AI w analizie: generowanie kodu, interpretacja, czyszczenie, summary | Notebook + dyskusja |
| 1:20-1:25 | **MATERIAŁ 5** | Narzędzia: Claude.ai, ChatGPT, GitHub Copilot (darmowy dla studentów) | Pokaz przeglądarki |
| 1:25-1:35 | **MATERIAŁ 6** | Ograniczenia i etyka: halucynacje, cutoff, prywatność, odpowiedzialność | Dyskusja |
| 1:35-1:45 | **PODSUMOWANIE** | 3 bullet points, zapowiedź bloku laboratoryjnego (od razu po przerwie) | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — WPROWADZENIE

> "Dzisiejsze spotkanie to ostatni nowy temat tego semestru. Następne spotkanie — S10 — to prezentacje Waszych projektów i zaliczenia."

> "Temat dzisiaj: **LLM i AI w analizie danych**. Kto z Was korzystał z ChatGPT lub Claude'a? [Ręce w górę.] A kto używał tych narzędzi konkretnie do pisania kodu Python lub analizy danych — nie do pisania esejów? [Mniej rąk.] To właśnie jest luka, którą dziś zamkniemy."

> "Pokażę Wam nie tylko co AI może, ale jak je używać jako narzędzie w codziennej pracy analityka. Z głową. Z rozumieniem ograniczeń. I z konkretną wartością dla pracodawcy."

> "Uwaga organizacyjna: wykład trwa 90 minut, potem przerwa, a w drugiej części — laboratorium — będziecie sami pracować z darmowymi narzędziami AI. Do ćwiczeń NIE potrzeba kluczy API ani żadnych płatności."

**[Wyświetl plan na projektorze]**

```
PLAN S09 — WYKŁAD (90 min):
1. Co to są LLM?                      0:05-0:25
2. Tokeny i temperatura               0:25-0:40
3. API z Pythona                       0:40-0:55
── PRZERWA ──
4. AI w praktycznej analizie danych    1:05-1:20
5. Narzędzia darmowe                   1:20-1:25
6. Ograniczenia i etyka                1:25-1:35
7. Podsumowanie                        1:35-1:45
```

---

### 0:05-0:25 — MATERIAŁ 1: Co to są LLM (20 min)

> "Zaczniemy od podstaw — nie od głębokiej matematyki, ale od tego co każdy analityk danych powinien rozumieć żeby używać tych narzędzi dobrze."

**[Narysuj na tablicy lub wyświetl]**

```
HISTORIA W 3 MINUTACH:

2017 — Google: "Attention is all you need" → architektura Transformer
        (Rewolucja: model patrzy na CAŁY kontekst naraz, nie słowo po słowie)

2020 — OpenAI: GPT-3
        (175 miliardów parametrów — AI pisze teksty nie do odróżnienia od ludzkich)

2022 — ChatGPT
        (Interfejs czatu → 100 milionów użytkowników w 2 miesiące)

2023 — GPT-4, Claude, Gemini, Llama
        (Wyścig zbrojeń, open source, specjalistyczne modele)

2024-2026 — AI w każdym narzędziu
        (GitHub Copilot, Claude Code, Cursor, NotebookLM, Gemini w Sheets...)
```

> "Kluczowe słowo: **Transformer**. Rewolucja nie polegała na tym, że modele są większe. Zmieniła się architektura — zamiast czytać sekwencyjnie, model patrzy na WSZYSTKIE słowa kontekstu naraz i oblicza które są ważne dla siebie nawzajem. Mechanizm 'attention' — uwagi. Stąd tytuł pracy: 'Attention is all you need'."

> "Ale co to znaczy dla Was? Nie musicie znać matematyki transformera. Musicie rozumieć trzy rzeczy: czym są tokeny, czym jest temperatura, i jakie modele istnieją."

**[Wyświetl porównanie modeli]**

```
TRZY RODZINY MODELI:

GPT-4o / o1 / o3 (OpenAI)
    + Bardzo dobre w kodzie i rozumowaniu matematycznym
    + Ogromna baza wiedzy
    + Integracja z Microsoft/Azure/Office
    - Stosunkowo drogi na dużą skalę

Claude Sonnet / Opus (Anthropic)
    + Szczególnie silny w rozumieniu długich dokumentów (200K tokenów)
    + Bardzo dobre śledzenie instrukcji
    + Najrzetelniejszy — najmniej halucynacji faktów
    + Sonnet = szybszy/tańszy, Opus = najmocniejszy

Gemini (Google)
    + Natywna integracja z Google Workspace, BigQuery, Sheets
    + Silny w multimodalności (obraz + tekst + audio)
    + Dobry do analiz gdy dane są w ekosystemie Google
    - Słabszy w złożonym kodzie niż GPT/Claude
```

> "Na rynku pracy — znacie jedno API, łatwo przejść na drugie. Struktura żądania jest niemal identyczna. Dzisiaj pokażę oba: OpenAI i Anthropic."

**[Wyświetl pipeline LLM]**

```
Wasz prompt (system + user)
         ↓
   Tokenizer (tekst → tokeny)
         ↓
  Transformer (setki warstw attention)
         ↓
   Sampling (temperatura kontroluje losowość)
         ↓
   Detokenizer (tokeny → tekst)
         ↓
      Odpowiedź modelu
```

> "Każdy token generowany jest jeden po drugim — stąd wrażenie że model 'myśli na żywo'. To nie refleksja — to autoregresja: każdy nowy token bazuje na wszystkich poprzednich. Model NIE ma dostępu do internetu (chyba że ma narzędzia), NIE 'myśli' — generuje statystycznie prawdopodobny ciąg tokenów. Nie ma pamięci między sesjami. To kluczowe ograniczenia."

---

### 0:25-0:40 — MATERIAŁ 2: Tokeny i temperatura (15 min)

> "Dwie kwestie techniczne, które bezpośrednio wpływają na to jak dobrze AI będzie działać w Waszych analizach."

**[Pokaz konceptualny — tokenizacja]**

> "**Tokeny** — LLM nie widzi liter ani słów. Widzi tokeny — kawałki słów, najczęściej 3-4 znaki w angielskim, więcej w polskim. 'Data analysis' to 3 tokeny. 'Analiza danych' to 5 tokenów — języki z bogatą fleksją mają gęstszą tokenizację."

> "Dlaczego to ważne? Trzy powody:"

```
1. KOSZTY — API rozliczane PER TOKEN
   Typowe zadanie analityczne:
   - Prompt + dane (tabela 100 wierszy): ~2 000 tokenów input
   - Odpowiedź z kodem: ~500 tokenów output
   - Koszt jednego zapytania: ~$0.01 - $0.05

2. LIMITY KONTEKSTU — ile tekstu model "widzi" naraz
   - GPT-4o: 128 000 tokenów (~100 000 słów)
   - Claude Sonnet: 200 000 tokenów (~150 000 słów)
   - Dla większości analiz: w zupełności wystarczy

3. JAKOŚĆ W POLSKIM — więcej tokenów = mniej "miejsca" w kontekście
   - Prompty po angielsku = tańsze i czasem dokładniejsze
   - Ale odpowiedzi po polsku działają dobrze — warto prosić wprost
```

> "Dla projektów studenckich — free tier w zupełności wystarczy. W firmach — to decyzja o ROI: czy asystent AI oszczędzający analitykowi 2h dziennie jest warty $100 miesięcznie? Odpowiedź jest zwykle oczywista."

**[Pokaz konceptualny — temperatura]**

> "**Temperatura** — parametr od 0 do 2. Kontroluje 'kreatywność' modelu. Technicznie: ile losowości dodajemy przy wyborze następnego tokenu."

```
temperatura = 0.0  → deterministyczny, zawsze ta sama odpowiedź
                     KIEDY: generowanie kodu, analiza danych, fakty
                     DLACZEGO: chcecie żeby "SELECT COUNT(*)" było
                     zawsze tym samym zapytaniem

temperatura = 0.7  → zrównoważony (domyślny w większości interfejsów)
                     KIEDY: ogólne zapytania, wyjaśnienia, asystentura

temperatura = 1.5  → kreatywny, różnorodny, mniej przewidywalny
                     KIEDY: brainstorming, copywriting, fikcja
                     DLACZEGO: szukamy niestandardowych pomysłów
```

> "Zasada: w analizie danych — zawsze używajcie temperatury blisko 0. Kreatywność w kodzie = błędy."

> "Kiedy używacie Claude.ai lub ChatGPT przez przeglądarkę — nie macie kontroli nad temperaturą. Model używa domyślnej (~0.7). Dlatego ten sam prompt może dawać trochę inne odpowiedzi za każdym razem. Przez API — macie pełną kontrolę."

---

### 0:40-0:55 — MATERIAŁ 3: API z Pythona (15 min)

> "Teraz konkret: jak wywołać model z Pythona. Pokażę konceptualny kod — żeby zrozumieć strukturę, a nie żebyście to uruchamiali teraz. Na labach będziecie pracować przez przeglądarkę (darmowe)."

**[Wyświetl: Struktura API OpenAI]**

```python
# UWAGA: Wymaga zmiennej środowiskowej OPENAI_API_KEY
# W notebooku wykładowym: wersja symulowana (mock)

from openai import OpenAI

client = OpenAI()  # czyta klucz z os.environ["OPENAI_API_KEY"]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Jesteś asystentem analityka danych."},
        {"role": "user",   "content": "Napisz funkcję do wczytania CSV i wypisania info()."}
    ],
    temperature=0.1,   # niskie = deterministyczny kod
    max_tokens=500
)

answer = response.choices[0].message.content
print(answer)
```

> "Trzy kluczowe elementy:"

> "**System message** — instrukcja dla modelu o tym 'kim jest' i jak się zachowywać. To jest Wasz punkt kontroli. Możecie tu wpisać: 'Odpowiadaj tylko kodem Python', 'Nigdy nie używaj bibliotek innych niż pandas', 'Zawsze komentuj kod po polsku'."

> "**User message** — właściwe pytanie lub zadanie. Tu idzie Wasz prompt."

> "**Messages jako lista** — możecie budować historię konwersacji, dodając kolejne wiadomości z rolami 'assistant' i 'user'. Model widzi cały kontekst."

**[Wyświetl: Struktura API Anthropic]**

```python
# Analogiczna struktura w Anthropic SDK
import anthropic

client = anthropic.Anthropic()  # czyta ANTHROPIC_API_KEY

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=500,
    system="Jesteś asystentem analityka danych. Odpowiadaj zwięźle.",
    messages=[
        {"role": "user", "content": "Wyjaśnij czym jest p-wartość w jednym zdaniu."}
    ]
)

print(message.content[0].text)
```

> "Różnica: w Anthropic `system` jest osobnym parametrem, nie elementem listy. Poza tym — identyczna koncepcja: role, temperature, max_tokens."

**[Wyświetl: Structured Output]**

> "Bardzo ważna technika w analizie danych: **structured output** — wymuszenie odpowiedzi w formacie JSON zamiast luźnego tekstu."

```python
# System prompt wymuszający format JSON
system = """Jesteś asystentem do analizy danych.
Zawsze odpowiadaj WYŁĄCZNIE w formacie JSON:
{
  "wynik": <treść odpowiedzi>,
  "pewnosc": <0-100>,
  "ostrzezenie": <null lub opis problemu>
}"""

user = "Czy korelacja r=0.15 między wiekiem a satysfakcją z pracy jest silna?"

# Model odpowiedziałby:
# {
#   "wynik": "Nie. Korelacja r=0.15 jest bardzo słaba.",
#   "pewnosc": 95,
#   "ostrzezenie": "Korelacja liniowa nie wyklucza nieliniowego związku."
# }
```

> "Dlaczego structured output? Bo jeśli budujecie pipeline analizy danych — potrzebujecie wyciągnąć konkretną informację z odpowiedzi. JSON z polami 'wynik' i 'ostrzezenie' jest gotowy do dalszego przetwarzania w Pythonie. Nowe API mają oficjalne wsparcie przez JSON Schema."

---

### 0:55-1:05 — PRZERWA (10 min)

---

### 1:05-1:20 — MATERIAŁ 4: AI w praktycznej analizie danych (15 min)

> "Cztery konkretne zastosowania AI w codziennej pracy analityka. Każde pokażę z przykładem."

**Zastosowanie 1: Generowanie kodu**

> "Najbardziej oczywiste, ale robimy to źle. Zły prompt: 'napisz mi analizę danych'. Dobry prompt: precyzyjny kontekst + konkretne zadanie + ograniczenia."

```python
# ZŁY PROMPT (za ogólny):
zly = "Przeanalizuj te dane sprzedażowe"

# DOBRY PROMPT (precyzyjny):
dobry = """
Mam DataFrame pandas `df_sprzedaz` z kolumnami:
- data_zamowienia (datetime)
- klient_id (int)
- produkt_kategoria (str: 'elektronika', 'odzież', 'dom')
- wartosc_zamowienia (float, PLN)
- status (str: 'zrealizowane', 'zwrócone', 'anulowane')

Zadanie: Napisz funkcję raport_miesięczny(df, rok, miesiac) która:
1. Filtruje zamówienia z danego miesiąca (tylko status='zrealizowane')
2. Liczy: przychód, liczbę zamówień, średnią wartość
3. Tworzy breakdown per kategoria (przychód, %, rank)
4. Zwraca dict z kluczami: 'summary', 'categories'

Ograniczenia: tylko pandas i numpy.
"""
```

> "Widzicie różnicę? Dobry prompt daje modelowi KONTEKST (kolumny, typy), ZADANIE (co zwracać), OGRANICZENIA (biblioteki). Kod z dobrego promptu jest zwykle bezpośrednio używalny."

> "Zasada absolutna: zawsze testujcie wygenerowany kod. AI nie widzi Waszych danych. Wasze zadanie to verification — nie authoring."

**Zastosowanie 2: Interpretacja wyników**

> "Macie wynik testu statystycznego — p-wartość, CI, effect size. Prosicie AI: 'przetłumacz to na język biznesu dla osoby bez wykształcenia statystycznego'."

```python
wyniki = """
A/B test: Wersja B koszyka daje +38 PLN (11% więcej).
Welch t-test: p=0.000025, 95% CI [21, 56] PLN, Cohen d=0.48
"""

prompt = f"""
Wyniki A/B testu: {wyniki}
Napisz dla Dyrektora Marketingu (NIE statystyka):
1. Główny wniosek (1 zdanie)
2. Co to oznacza finansowo (zakładając 50 000 emaili/mies.)
3. Rekomendację + jedno zastrzeżenie
Po polsku, bez wzorów.
"""
```

> "Ten typ użycia jest może najbardziej niedoceniany. Wiecie co p < 0.05 znaczy. Ale napisanie jednego akapitu po polsku dla zarządu bez błędów zajmuje czas. AI zrobi to w sekundę — Wy oceniacie i poprawiacie."

**Zastosowanie 3: Czyszczenie danych**

> "Macie kolumnę z opisami wpisywanymi ręcznie przez pracowników — 17 wariantów tego samego statusu."

```python
# Dane CRM — opisy statusów wpisywane ręcznie
warianty = [
    "zrealizowane", "Zrealizowane", "ZREALIZOWANE",
    "anulowanie", "anulowane", "Anulowane",
    "zwrot", "Zwrot", "zwrócone", "zwrocone",
    "w realizacji", "W Realizacji", "W trakcie realizacji"
]

# Prosicie AI: "Napisz słownik Python mapujący każdy wariant
#   na jedną z 5 kategorii docelowych."
# Normalizacja 17 wariantów ręcznie = 20 minut. Z AI = 2 minuty.
# ZAWSZE sprawdzacie mapę ręcznie.
```

> "To nawiązuje do tego co robiliśmy na S05 — czyszczenie danych. AI nie zastępuje myślenia o tym CO trzeba wyczyścić, ale przyspiesza JAK to zrobić."

**Zastosowanie 4: Executive summary**

> "Macie gotową analizę — wiele tabel, wykresów, wyników testów. Prosicie AI o executive summary."

```python
prompt = """
Na podstawie wyników analizy Q4 2024:
- Przychód: 2.85 mln PLN (+12% r/r)
- Top kategoria: elektronika (38%)
- Zwroty elektroniki: 14.2% (norma: 10%)
- Retencja 90-dniowa: 61% (cel: 65%)
- A/B test onboardingu: +9% retencja (p=0.031)

Napisz executive summary (max 150 słów):
1. Główne osiągnięcia
2. Obszary wymagające uwagi
3. Trzy priorytetowe rekomendacje
Styl: rzeczowy, zorientowany na decyzje.
"""
```

> "Nie poprosiłem AI o 'napisz mi raport'. Podałem konkretne dane, format, styl. AI wypełniło szablon danymi. To prawdziwa efektywność — nie zastępuję myślenia analitycznego, automatyzuję pisanie."

---

### 1:20-1:25 — MATERIAŁ 5: Narzędzia darmowe (5 min)

> "Przegląd narzędzi, z których będziecie korzystać w bloku laboratoryjnym — i w pracy."

```
NARZĘDZIA AI DLA ANALITYKA — DARMOWE:

1. CLAUDE.AI (claude.ai) — FREE TIER
   • Interfejs czat — rejestracja przez email lub konto Google
   • Bardzo dobre do: kodu Python, długich dokumentów, statystyki
   • ~20-30 wiadomości co kilka godzin (free), potem cooldown
   • Najbardziej "rzetelny" — najmniej halucynacji

2. CHATGPT (chat.openai.com) — FREE TIER
   • GPT-4o mini gratis, GPT-4o z limitem
   • Code Interpreter: uploaduje CSV i analizuje — w przeglądarce!
   • Dobry do: szybkich pytań, generowania kodu, brainstormingu
   • Uwaga przy uploadzie: dane idą do serwerów OpenAI

3. GITHUB COPILOT — DARMOWY DLA STUDENTÓW
   • github.com/education → GitHub Student Developer Pack
   • Integracja z VS Code — sugestie kodu w czasie rzeczywistym
   • "Tab to accept" — akceptujesz sugestię jednym klawiszem
   • Zna kontekst Waszego projektu (widzi cały plik/repo)
   • POLECAM: zarejestrujcie się z adresem uczelnianym
```

> "Na laboratorium użyjecie Claude.ai lub ChatGPT — oba działają bez kluczy API, bez płatności. Copilot — polecam zainstalować po zajęciach, działa w VS Code."

---

### 1:25-1:35 — MATERIAŁ 6: Ograniczenia i etyka (10 min)

> "Najważniejsza część — ograniczenia. AI jest jak bardzo pewny siebie kolega, który zna odpowiedź na WSZYSTKO — ale czasem się myli. Problem: myli się tak samo pewnym tonem jak gdy ma rację."

```
OGRANICZENIA LLM — 5 ZAGROŻEŃ:

1. HALUCYNACJE
   Model może:
   - Wymyślać funkcje które nie istnieją ("pd.DataFrame.super_clean()")
   - Podawać fałszywe statystyki ze "wiarygodnymi źródłami"
   - Mylić nazwy parametrów API
   → REGUŁA: zawsze uruchom wygenerowany kod

2. KNOWLEDGE CUTOFF (odcięcie wiedzy)
   Model nie wie o:
   - Nowych wersjach bibliotek po dacie treningu
   - Aktualnych danych rynkowych, kursach, cenach
   → REGUŁA: sprawdź dokumentację dla aktualnych informacji

3. PRYWATNOŚĆ DANYCH
   Dane wysłane do publicznego API/chatu mogą być:
   - Logowane przez dostawcę
   - Użyte do trenowania (zależy od ustawień)
   → REGUŁA FIRMOWA: nigdy nie wysyłaj danych osobowych klientów,
     NIP-ów, danych finansowych firmy do publicznego API
     bez zgody prawników. RODO!

4. MATEMATYKA I OBLICZENIA
   LLM = model językowy, NIE kalkulator
   Może popełniać błędy przy złożonych obliczeniach
   → REGUŁA: wyniki obliczeń ZAWSZE weryfikuj Pythonem

5. ODPOWIEDZIALNOŚĆ
   AI generuje kod — ale ODPOWIEDZIALNOŚĆ jest Wasza.
   "AI tak powiedział" to nie jest argument w firmie.
   Podpisujecie się pod analizą = musicie ją rozumieć.
```

> "Kwestia akademicka: czy można używać AI do odrabiania zadań? W tym kursie: tak, z jednym warunkiem — musicie rozumieć co AI wygenerowało. Na laboratorium sprawdzam nie czy kod działa, ale czy umiecie go wyjaśnić."

> "Na rynku pracy: firmy oczekują że umiecie używać AI produktywnie. Nie oczekują że wiecie jak je trenować. Ale oczekują że wiecie kiedy AI się myli — i to jest wartość Waszego wykształcenia."

**[Pytanie do sali]**

> "Scenariusz: firma ma plik CSV z danymi 10 000 klientów — imię, email, historia zakupów. Chcecie użyć ChatGPT żeby napisał skrypt do segmentacji. Najszybciej byłoby uploadować CSV. Co robicie? [Poczekaj na odpowiedzi.] Dokładnie — anonimizujecie dane. Zamieniacie imiona na ID, email na hash. Albo — opisujecie strukturę danych w prompcie BEZ wklejania prawdziwych wartości."

---

### 1:32-1:35 — AKTYWNOŚĆ — Mini-quiz (3 min)

> **Prowadzący mówi:** "Zanim podsumujemy — szybki quiz. Odpowiedzcie na kartce lub w parach."

1. Czym rozni sie `system message` od `user message` w API? Do czego sluzy kazdy z nich?
2. Dlaczego przy analizie danych ustawiamy temperature blisko 0, a nie 1.5?
3. Firma ma CSV z danymi 10 000 klientow (imie, email, zakupy). Chcesz uzyc ChatGPT do napisania skryptu segmentacji. Czy uploadujesz plik? Co robisz zamiast tego?

> **[Po 2 min]** "Kto chce odpowiedzieć? [Omów odpowiedzi: 1) system = instrukcja 'kim jestes' i jak sie zachowywac, user = wlasciwe pytanie/zadanie. System kontroluje ton i format; 2) Niska temperatura = deterministyczny, powtarzalny kod. Wysoka = losowy, kreatywny — w kodzie to bledy; 3) NIE uploadujesz — dane osobowe + RODO. Anonimizujesz (ID zamiast imion, hash zamiast emaili) lub OPISUJESZ strukture w prompcie bez prawdziwych wartosci]"

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy wykład w trzech punktach:"

> "**Punkt 1:** LLM to modele generujące tekst token po tokenie, uczone na ogromnych zbiorach danych. Różne modele (GPT, Claude, Gemini) mają różne mocne strony, ale identyczną strukturę API: system + user + assistant. Temperatura niska = kod i fakty, wysoka = kreatywność."

> "**Punkt 2:** Cztery zastosowania w codziennej pracy analityka — generowanie kodu (precyzyjny prompt z kontekstem), interpretacja wyników (tłumaczenie na język biznesu), czyszczenie danych (normalizacja kategorii), executive summary (szablon + dane = raport). Wszystkie wymagają WASZEJ weryfikacji."

> "**Punkt 3:** Ograniczenia — halucynacje, knowledge cutoff, prywatność danych, odpowiedzialność. AI asystuje — nie zastępuje. Narzędzia darmowe: Claude.ai, ChatGPT, GitHub Copilot (darmowy z adresem uczelnianym)."

> "Za chwilę — przerwa, a potem blok laboratoryjny. Będziecie sami pracować z AI: pisać prompty, generować kod, oceniać wyniki, przeprowadzać analizę z AI jako asystentem. Potrzebujecie: laptop, przeglądarka, konto w Claude.ai lub ChatGPT."

> "Na **S10 — ostatnie spotkanie** — prezentacje mini-projektów. Każdy/każda z Was prezentuje 5-7 minut: co to za dataset, jakie pytania postawiliście, co znaleźliście. Notebook musi być na GitHubie z historią commitów. Zacznijcie przygotowywać się już teraz — i śmiało użyjcie AI do przygotowania executive summary projektu."

---

## Materiały uzupełniające dla studentów

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic API Documentation](https://docs.anthropic.com)
- [GitHub Copilot for Students](https://education.github.com/pack)
- [Prompt Engineering Guide](https://www.promptingguide.ai)
- VanderPlas, *Python Data Science Handbook* (2023) — rozdz. o nowoczesnych narzędziach
