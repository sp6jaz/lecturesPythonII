# W14 Wykład — Plan zajęć dla prowadzącego

## Temat: LLM i AI w analizie danych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z demonstracją konceptualną (notebook bez kluczy API)
- **Potrzebne:** komputer z projektorem, VS Code, venv z podstawowymi bibliotekami
- **Przed wykładem:** otwórz `llm_demo.ipynb` — notebook działa bez API keys
- **Kluczowe hasło:** "AI nie zastąpi analityka danych — ale analityk używający AI zastąpi tego, który nie używa"

### Efekty uczenia się (Bloom poziom 4-5)
Po tym wykładzie osoba studiująca:
1. **Wyjaśnia** czym jest model językowy (LLM), czym są tokeny i temperatura, oraz jak modele GPT/Claude/Gemini różnią się w zastosowaniach analitycznych (Bloom 2)
2. **Stosuje** biblioteki `openai` i `anthropic` do wysyłania zapytań z Pythona, rozumiejąc strukturę żądania API (chat completions, system/user/assistant) (Bloom 3)
3. **Projektuje** efektywne prompty do zadań analitycznych: generowanie kodu, interpretacja wyników, czyszczenie opisów danych (Bloom 5)
4. **Ocenia** przydatność i ograniczenia narzędzi AI (ChatGPT, Claude, Copilot) w kontekście analizy danych — włącznie z ryzykiem halucynacji i kwestiami etycznymi (Bloom 4)
5. **Konstruuje** workflow analizy danych wspomagany przez AI, łącząc własne umiejętności analityczne z możliwościami generatywnego AI (Bloom 5)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W13 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | "Ostatni nowy temat. Jak AI zmienia analizę danych na zawsze." | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Co to są LLM — historia, GPT/Claude/Gemini, tokeny, temperatura | Pokaz konceptualny |
| 0:30-0:45 | **MATERIAŁ 2** | Użycie API AI z Pythona — biblioteki, chat completions, structured output | Notebook (mock) |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | AI w analizie danych — generowanie kodu, interpretacja wyników, czyszczenie danych | Notebook (mock) |
| 1:15-1:25 | **MATERIAŁ 4** | Narzędzia praktyczne — Claude Code, Copilot, ChatGPT. Etyka i ograniczenia | Pokaz + dyskusja |
| 1:25-1:35 | **AKTYWNOŚĆ** | Napisz prompty dla 3 zadań analitycznych | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Co dalej, zapowiedź W15 (prezentacje projektów) | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W13)

> "Tradycyjnie — pięć pytań z poprzedniego tygodnia. Trzy minuty."

**[Użyj quiz_w14.md — pytania 1 i 2 z W13]**

> "Odpowiedzi omówimy razem. Na W13 mieliśmy scikit-learn, Plotly i Polars. Kto przejrzał notebook z tamtego tygodnia przed dzisiaj? Brawo — właśnie tak się uczy. Kto nie przejrzał — do końca semestru zostały dwa tygodnie, warto nadrobić przed egzaminem."

---

### 0:05-0:10 — WPROWADZENIE

> "Ostatni nowy temat tego semestru. Kolejny tydzień — W15 — to już prezentacje Waszych mini-projektów i zaliczenia. Więc to, co dzisiaj usłyszycie, jest ważne — bo to jest temat, który przez najbliższe pięć lat będzie fundamentem pracy każdego analityka danych."

> "Pokażę Wam ręce — kto z Was korzystał z ChatGPT, Claude'a lub Copilota w ciągu ostatniego miesiąca? Prawie wszystkie ręce. A kto używał tych narzędzi do pisania kodu lub analizy danych — nie tylko do pisania esejów? Mniej rąk. Właśnie tutaj jest przepaść między 'użytkownikiem AI' a 'analitykiem używającym AI jako narzędzia'."

> "Dzisiaj chcę zamknąć tę przepaść. Pokażę Wam nie tylko to co AI może — ale jak go używać w codziennej pracy analityka. Z głową. Z rozumieniem ograniczeń. I z konkretną wartością dla pracodawcy."

> "Nota organizacyjna: dziś będę pokazywał przykłady kodu, który używa API — interfejsu programistycznego do modeli AI. Do faktycznego uruchomienia takiego kodu potrzeba kluczy API, które są płatne lub mają bezpłatne limity. Podczas wykładu pokażę symulowane wyjścia — dokładnie takie, jakie dostałby kod z prawdziwym kluczem. Na laboratorium będziecie pracować z darmowymi warstwami narzędzi — Claude.ai free, ChatGPT free, lub GitHub Copilot (dostępny dla studentów za darmo)."

**[Wyświetl na projektorze — plan zajęć]**

```
PLAN W14:
1. Co to są LLM (modele językowe)?    0:10-0:30
2. Jak wywołać AI z Pythona?          0:30-0:45
── PRZERWA ──
3. AI w praktycznej analizie danych   0:55-1:15
4. Narzędzia + etyka                  1:15-1:25
5. Aktywność: piszemy prompty         1:25-1:35
6. Podsumowanie semestru             1:35-1:45
```

---

### 0:10-0:30 — MATERIAŁ 1: Co to są LLM (20 min)

> "Zaczniemy od podstaw — nie od głębokiej teorii matematycznej, ale od tego co każdy analityk danych powinien rozumieć żeby używać tych narzędzi dobrze."

**[Narysuj na tablicy lub wyświetl diagram]**

```
HISTORIA W 3 MINUTACH:

2017 — Google: "Attention is all you need" → architektura Transformer
        (Rewolucja: zamiast czytać słowo po słowie — patrz na CAŁY kontekst naraz)

2020 — OpenAI: GPT-3
        (175 miliardów parametrów, nagle AI pisze teksty nie do odróżnienia od ludzkiego)

2022 — ChatGPT
        (Interfejs czatu → AI dostępny dla 100 milionów użytkowników w 2 miesiące)

2023 — GPT-4, Claude, Gemini, Llama
        (Wyścig zbrojeń, open source, specjalistyczne modele)

2024-2025 — AI w każdym narzędziu
        (GitHub Copilot, Claude Code, Cursor, NotebookLM...)
```

> "Transformer — to jest kluczowe słowo. Rewolucja nie polegała na tym że modele są większe. Polegała na tym że zmieniła się architektura: zamiast czytać sekwencyjnie, model patrzy na WSZYSTKIE słowa kontekstu naraz i oblicza, które są ważne dla siebie nawzajem. Mechanizm 'attention' — uwagi. Stąd tytuł pracy: 'Attention is all you need'."

> "Dla Was, jako analityków — nie musicie znać matematyki stojącej za transformerem. Musicie rozumieć trzy rzeczy."

**[Otwórz llm_demo.ipynb — komórka 1: TOKENY]**

> "Pierwsza rzecz: **tokeny**. LLM nie widzi liter ani słów — widzi tokeny. Token to kawałek słowa, najczęściej 3-4 znaki w języku angielskim, więcej w polskim. 'programowanie' to około 4-5 tokenów w zależności od modelu."

> "Dlaczego to ważne? Bo API jest rozliczane PER TOKEN. Jak wysyłacie 10 000 słów do analizy — płacicie za tokeny. A modele mają limit kontekstu — maksymalną liczbę tokenów jaką mogą 'widzieć' naraz. GPT-4 — 128 000 tokenów (około 100 000 słów). Claude Sonnet — 200 000 tokenów. Dla większości zadań analitycznych — w zupełności wystarczy."

**[Notebook — komórka z demonstracją tokenizacji]**

> "Zobaczcie w notebooku — symulujemy jak wygląda podział na tokeny. 'Data analysis' to 3 tokeny. 'Analiza danych' to już 5 tokenów — języki z bogatą fleksją (jak polski) mają gęstszą tokenizację."

**[Notebook — komórka z demonstracją temperatury]**

> "Druga rzecz: **temperatura**. Parametr od 0 do 2. Kontroluje 'kreatywność' modelu — technicznie: ile losowości dodajemy przy wyborze następnego tokenu."

```
temperatura = 0.0  → deterministyczny, zawsze ta sama odpowiedź
                     KIEDY: generowanie kodu, analiza danych, fakty
temperatura = 0.7  → zrównoważony (domyślny)
                     KIEDY: ogólne zapytania, wyjaśnienia, asystentura
temperatura = 1.5  → kreatywny, różnorodny
                     KIEDY: brainstorming, copywriting, fikcja
```

> "W analizie danych — zawsze używajcie temperatury blisko 0. Chcecie że 'SELECT COUNT(*) FROM orders WHERE status = cancelled' jest zawsze tym samym zapytaniem, nie co drugi raz innym. Kreatywność w kodzie = błędy."

**[Notebook — komórka z porównaniem modeli]**

> "Trzecia rzecz: **różne modele do różnych zadań**. Dzisiaj mamy trzy główne rodziny:"

```
GPT-4o / o1 (OpenAI)
    + Bardzo dobre w kodzie i rozumowaniu matematycznym
    + Ogromna baza wiedzy
    + Integracja z Microsoft/Azure

Claude Sonnet / Opus (Anthropic)
    + Szczególnie silny w rozumieniu długich dokumentów
    + Bardzo dobre śledzenie instrukcji
    + Najbardziej "bezpieczny" — najmniej halucynacji faktów
    + Sonnet = szybszy i tańszy, Opus = najmocniejszy

Gemini (Google)
    + Natywna integracja z Google Workspace, BigQuery
    + Silny w multimodalności (obraz + tekst)
    + Dobry do analiz gdzie dane są w Google Sheets/Drive
```

> "Na laboratorium będziecie pracować głównie z Claude'em i ChatGPT przez interfejs webowy (darmowe). Na rynku pracy — znacie jedno API, łatwo przejść na drugie. Struktura żądania jest niemal identyczna."

**[Komórka z omówieniem pipeline'u LLM]**

```
Wasz prompt (system + user)
         ↓
   Tokenizer (tekst → tokeny)
         ↓
  Transformer (setki warstw attention)
         ↓
   Sampling (temperatura wybiera token)
         ↓
   Detokenizer (tokeny → tekst)
         ↓
      Odpowiedź modelu
```

> "Każdy token generowany jest jeden po drugim — stąd wrażenie że model 'myśli na żywo'. To nie refleksja — to autoregresja: każdy nowy token bazuje na wszystkich poprzednich."

> "Co model NIE robi: nie ma dostępu do internetu (chyba że ma tool use / web search), nie 'myśli' — generuje statystycznie prawdopodobny ciąg tokenów, nie ma pamięci między sesjami (poza kontekstem okna). To są kluczowe ograniczenia o których za chwilę."

---

### 0:30-0:45 — MATERIAŁ 2: Użycie API AI z Pythona (15 min)

> "Teraz praktyczna część: jak wywołać model z Pythona. Pokażę Wam konceptualny kod — w notebooku są symulowane odpowiedzi, żeby móc pokazać wyniki bez kluczy API. Gdy będziecie mieć klucz — zamienicie mock na prawdziwe wywołanie jedną linią."

**[Otwórz notebook — komórka 2: Struktura API]**

> "Oba główne API — OpenAI i Anthropic — mają bardzo podobną strukturę. Zacznijmy od OpenAI, bo jest najszerzej stosowane:"

```python
# UWAGA: Wymaga zmiennej środowiskowej OPENAI_API_KEY
# W notebooku używamy wersji symulowanej (mock)

from openai import OpenAI

client = OpenAI()  # czyta klucz z os.environ["OPENAI_API_KEY"]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Jesteś asystentem analityka danych."},
        {"role": "user",   "content": "Napisz funkcję Python do wczytania CSV i wypisania info()."}
    ],
    temperature=0.1,   # niskie = deterministyczny kod
    max_tokens=500
)

answer = response.choices[0].message.content
print(answer)
```

> "Trzy kluczowe elementy tej struktury:"

> "**System message** — instrukcja dla modelu o tym 'kim jest' i jak się zachowywać. To jest Wasz punkt kontroli. Możecie tu wpisać: 'Odpowiadaj tylko kodem Python', 'Nigdy nie używaj bibliotek innych niż pandas i numpy', 'Zawsze komentuj kod po polsku'. Model będzie to przestrzegał."

> "**User message** — właściwe pytanie lub zadanie. Tu idzie Wasz prompt."

> "**Messages jako lista** — możecie budować historię konwersacji, dodając kolejne wiadomości z rolami 'assistant' i 'user'. Model widzi cały kontekst."

**[Notebook — komórka: Anthropic API]**

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

> "Różnica strukturalna: w Anthropic `system` jest osobnym parametrem, nie elementem listy. Poza tym — identyczna koncepcja."

**[Notebook — komórka: Structured output]**

> "Bardzo ważna technika w analizie danych: **structured output** — odpowiedź w formacie JSON. Zamiast dostawać luźny tekst, prosicie model żeby odpowiedział w określonej strukturze."

```python
# Przykład systemu + promptu do structured output
system = """Jesteś asystentem do analizy danych.
Zawsze odpowiadaj w formacie JSON:
{
  "wynik": <treść odpowiedzi>,
  "pewnosc": <0-100>,
  "ostrzezenie": <null lub opis problemu>
}"""

user = "Czy korelacja r=0.15 między wiekiem a satysfakcją z pracy jest silna?"

# Symulowana odpowiedź (jak by odpowiedział model):
mock_response = {
    "wynik": "Nie. Korelacja r=0.15 jest bardzo słaba (prawie brak związku liniowego).",
    "pewnosc": 95,
    "ostrzezenie": "Korelacja liniowa nie wyklucza nieliniowego związku — warto sprawdzić scatterplot."
}
```

> "Dlaczego structured output? Bo jeśli budujecie pipeline analizy danych — potrzebujecie wyciągnąć konkretną informację z odpowiedzi. Nie chcecie parsować tekstu. JSON z polami `wynik` i `ostrzezenie` jest gotowy do dalszego przetwarzania."

> "Nowe API (od 2024) mają oficjalne wsparcie dla structured output przez JSON Schema — ale te pokazane tu techniki działają na każdej wersji modelu."

**[Notebook — komórka: Koszty i tokeny]**

> "Jedna komórka o kosztach — bo to ważne dla biznesu:"

```
Orientacyjne ceny (2025, mogą się zmieniać):

GPT-4o:           $2.50 / 1M tokenów input,   $10 / 1M output
Claude Sonnet 4:  $3.00 / 1M tokenów input,   $15 / 1M output
GPT-4o mini:      $0.15 / 1M tokenów input,   $0.60 / 1M output

Typowe zadanie analityczne:
- Prompt + dane (tabela 100 wierszy): ~2 000 tokenów input
- Odpowiedź z kodem: ~500 tokenów output
- Koszt jednego zapytania: ~$0.01 - $0.05

Miesięczny koszt przy 100 zapytań dziennie: ~$30-150
```

> "Dla projektów studenckich — free tier w zupełności wystarczy. W firmach — to decyzja o ROI: czy asystent AI oszczędzający analitykowi 2h dziennie jest warty $100 miesięcznie? Odpowiedź jest zwykle oczywista."

---

### 0:45-0:55 — PRZERWA (10 min)

---

### 0:55-1:15 — MATERIAŁ 3: AI-wspomagana analiza danych (20 min)

> "Po przerwie — najbardziej praktyczna część. Cztery zastosowania AI w codziennej pracy analityka."

**[Notebook — komórka 3a: Generowanie kodu]**

> "Zastosowanie pierwsze: **generowanie kodu**. To jest najbardziej oczywiste, ale robimy to źle. Zły prompt: 'napisz mi analizę danych'. Dobry prompt: precyzyjny kontekst + konkretne zadanie + ograniczenia."

```python
# ===== TECHNIKA 1: GENEROWANIE KODU =====

# Zły prompt (za ogólny):
zly_prompt = "Przeanalizuj te dane sprzedażowe"

# Dobry prompt (precyzyjny kontekst + zadanie + ograniczenia):
dobry_prompt = """
Mam DataFrame pandas o nazwie `df_sprzedaz` z kolumnami:
- data_zamowienia (datetime)
- klient_id (int)
- produkt_kategoria (str: 'elektronika', 'odzież', 'dom')
- wartosc_zamowienia (float, PLN)
- status (str: 'zrealizowane', 'zwrócone', 'anulowane')

Zadanie: Napisz funkcję `raport_miesięczny(df, rok, miesiac)` która:
1. Filtruje zamówienia z danego miesiąca i roku (tylko status='zrealizowane')
2. Liczy: całkowity przychód, liczbę zamówień, średnią wartość zamówienia
3. Tworzy breakdown per kategoria produktu (przychód, %, rank)
4. Zwraca dict z kluczami: 'summary', 'categories'

Ograniczenia: tylko pandas i numpy. Żadnych zewnętrznych bibliotek.
"""

# Symulowana odpowiedź modelu:
mock_generated_code = '''
def raport_miesięczny(df, rok, miesiac):
    """Raport miesięczny sprzedaży — filtruje, agreguje, rankuje."""
    mask = (
        (df['data_zamowienia'].dt.year == rok) &
        (df['data_zamowienia'].dt.month == miesiac) &
        (df['status'] == 'zrealizowane')
    )
    df_m = df[mask].copy()

    total_revenue = df_m['wartosc_zamowienia'].sum()
    n_orders = len(df_m)

    cat_stats = (
        df_m.groupby('produkt_kategoria')['wartosc_zamowienia']
        .agg(['sum', 'count', 'mean'])
        .rename(columns={'sum': 'przychod', 'count': 'zamowienia', 'mean': 'sr_wartosc'})
        .assign(udzial_pct=lambda x: (x['przychod'] / total_revenue * 100).round(1))
        .sort_values('przychod', ascending=False)
        .assign(rank=lambda x: range(1, len(x)+1))
    )

    return {
        'summary': {
            'rok': rok, 'miesiac': miesiac,
            'przychod_total': round(total_revenue, 2),
            'liczba_zamowien': n_orders,
            'sr_wartosc_zamowienia': round(total_revenue / n_orders, 2) if n_orders else 0
        },
        'categories': cat_stats.to_dict('index')
    }
'''
print(mock_generated_code)
```

> "Widzicie różnicę? Dobry prompt daje modelowi KONTEKST (jakie kolumny, jakie typy), KONKRETNE ZADANIE (co ma zwracać), OGRANICZENIA (tylko pandas/numpy). Kod z dobrego promptu jest zwykle bezpośrednio używalny. Kod z złego promptu wymaga przeróbek."

> "Ważna zasada: zawsze testujcie wygenerowany kod. AI nie widzi Waszych danych. Może napisać poprawnie składniowo ale logicznie błędny kod. Wasza rola to verification — nie authoring."

**[Notebook — komórka 3b: Interpretacja wyników]**

> "Zastosowanie drugie: **interpretacja wyników**. Macie tabelę statystyk, wykres, wynik testu. Pytacie AI: 'co to znaczy dla biznesu?'"

```python
# ===== TECHNIKA 2: INTERPRETACJA WYNIKÓW =====

# Wyniki analizy statystycznej (np. z W12)
wyniki_ab_testu = """
A/B test kampanii e-mailowej:
- Wersja A (n=150): średnia wartość koszyka = 342.80 PLN, SD = 78.5
- Wersja B (n=150): średnia wartość koszyka = 381.20 PLN, SD = 82.3
- Welch's t-test: t = -4.28, p = 0.000025
- 95% CI dla różnicy (B-A): [21.1, 55.7] PLN
- Effect size Cohen's d = 0.48 (efekt umiarkowany)
"""

prompt_interpretacja = f"""
Jesteś analitykiem danych w firmie e-commerce. Masz wyniki A/B testu:
{wyniki_ab_testu}

Napisz dla Dyrektora Marketingu (nie-statystyka):
1. Główny wniosek (1 zdanie)
2. Co oznaczają liczby praktycznie
3. Rekomendację z uzasadnieniem finansowym (zakładając 50 000 emaili miesięcznie)
4. Jedno ostrzeżenie / zastrzeżenie

Format: krótki raport, bez wzorów matematycznych, po polsku.
"""

# Symulowana odpowiedź:
mock_interpretacja = """
**Raport: A/B test kampanii e-mail — wyniki**

**Wniosek:** Personalizowana wersja emaila (B) statystycznie istotnie zwiększa wartość koszyka o ok. 38 PLN.

**Co to znaczy:** Klienci którzy dostali spersonalizowaną wiadomość (wersja B) kupowali średnio o 38 PLN więcej (wzrost o 11%). Ta różnica nie jest przypadkowa — prawdopodobieństwo przypadkowego wystąpienia takiego wyniki wynosi mniej niż 1 na 40 000. Efekt jest umiarkowany, ale konsekwentny.

**Rekomendacja finansowa:** Przy 50 000 emailach miesięcznie szacowany dodatkowy przychód to ok. **1 900 000 PLN/rok** (38 PLN × 50 000 × 12). Rekomendujemy wdrożenie wersji B jako standardu kampanii e-mailowych.

**Zastrzeżenie:** Wyniki dotyczą jednej kampanii w jednym okresie. Warto powtórzyć test w różnych miesiącach i segmentach klientów przed pełnym wdrożeniem — efekt personalizacji może być sezonowy.
"""
print(mock_interpretacja)
```

> "Ten typ użycia jest może najbardziej niedoceniany. Macie wyniki testu. Wiecie co p < 0.05 znaczy. Ale napisanie jednego akapitu po polsku dla Dyrektora Marketingu bez błędów zajmuje czas. AI zrobi to w sekundę — Wy oceniacie i poprawiacie. To jest efektywne użycie AI."

**[Notebook — komórka 3c: Czyszczenie opisów danych]**

> "Zastosowanie trzecie: **czyszczenie i standaryzacja opisów w danych**. Macie kolumnę z opisami kategorii wpisywanymi ręcznie przez pracowników."

```python
# ===== TECHNIKA 3: CZYSZCZENIE OPISÓW =====
import pandas as pd

# Dane z systemu CRM — opisy statusów wpisywane ręcznie
opisy_crm = pd.Series([
    "zrealizowane", "Zrealizowane", "ZREALIZOWANE",
    "anulowanie", "anulowane", "Anulowane", "ANULOWANE",
    "zwrot", "Zwrot", "zwrócone", "zwrocone",
    "w realizacji", "W Realizacji", "W trakcie realizacji",
    "oczekuje na płatność", "oczekuje na platnosc", "Oczekuje na płatnosc"
])

prompt_czyszczenie = """
Mam kolumnę pandas z opisami statusów zamówień — wpisywanymi ręcznie przez pracowników.
Wartości są niejednorodne (różna wielkość liter, literówki, synonimy).

Docelowe kategorie:
- "zrealizowane"
- "anulowane"
- "zwrócone"
- "w_realizacji"
- "oczekuje_platnosc"

Napisz słownik Python `MAPA_STATUSOW` mapujący każdy z poniższych wariantów
na odpowiednią kategorię docelową. Użyj lowercase kluczy.
"""

# Symulowana odpowiedź modelu:
MAPA_STATUSOW = {
    "zrealizowane": "zrealizowane",
    "Zrealizowane": "zrealizowane",
    "ZREALIZOWANE": "zrealizowane",
    "anulowanie": "anulowane",
    "anulowane": "anulowane",
    "Anulowane": "anulowane",
    "ANULOWANE": "anulowane",
    "zwrot": "zwrócone",
    "Zwrot": "zwrócone",
    "zwrócone": "zwrócone",
    "zwrocone": "zwrócone",
    "w realizacji": "w_realizacji",
    "W Realizacji": "w_realizacji",
    "W trakcie realizacji": "w_realizacji",
    "oczekuje na płatność": "oczekuje_platnosc",
    "oczekuje na platnosc": "oczekuje_platnosc",
    "Oczekuje na płatnosc": "oczekuje_platnosc",
}

# Zastosowanie mapy:
opisy_czyste = opisy_crm.map(MAPA_STATUSOW).fillna("nieznany")
print("Unikalne wartości po czyszczeniu:")
print(opisy_czyste.value_counts())
```

> "Ten przykład ilustruje coś o czym mówiliśmy na W07 — czyszczenie danych. Normalizacja 17 wariantów do 5 kategorii ręcznie = 20 minut. Z AI = 2 minuty. Wy sprawdzacie poprawność, ewentualnie poprawiacie. Zawsze."

**[Notebook — komórka 3d: Podsumowanie wyników analizy]**

> "Zastosowanie czwarte: **automatyczne podsumowania**. Macie gotową analizę — wiele tabel, wizualizacji, wyników testów. Prosicie AI żeby napisało executive summary."

```python
# ===== TECHNIKA 4: AUTOMATYCZNE PODSUMOWANIE =====

kontekst_analizy = """
Przeprowadzono analizę danych e-commerce za Q4 2024:
- Przychód total: 2 847 430 PLN (wzrost +12% r/r)
- Top kategoria: elektronika (38% przychodów, 15% wolumenu)
- NPS klientów: 7.2/10 (95% CI: [7.0, 7.4])
- Wskaźnik zwrotów: 8.3% (elektronika: 14.2% — powyżej normy 10%)
- Retencja klientów 90-dni: 61% (cel: 65%)
- A/B test nowego onboardingu: +9% retencja (p=0.031)
"""

prompt_summary = f"""
Jesteś analitykiem przygotowującym raport kwartalny dla Zarządu.
Na podstawie wyników analizy:

{kontekst_analizy}

Napisz executive summary (max 150 słów) zawierające:
1. Główne osiągnięcia
2. Obszary wymagające uwagi
3. Trzy rekomendacje priorytetowe

Styl: rzeczowy, zorientowany na decyzje. Bez zbędnych słów.
"""

mock_summary = """
**Executive Summary — Q4 2024**

Przychód Q4 wyniósł 2,85 mln PLN (+12% r/r) — głównie dzięki elektronice (38% udziału).
NPS 7.2 utrzymuje się w bezpiecznym zakresie, a nowy onboarding pokazuje pozytywny efekt
(+9% retencja, wynik istotny statystycznie).

**Obszary wymagające uwagi:**
Wskaźnik zwrotów elektroniki (14.2%) przekracza normę firmową. Retencja 90-dniowa (61%)
jest poniżej celu (65%) — wymaga interwencji.

**Rekomendacje:**
1. Wdrożyć nowy onboarding na wszystkich użytkownikach (A/B potwierdzone)
2. Audyt procesu zwrotów elektroniki — zbadać główne przyczyny
3. Program retencyjny dla klientów po 60 dniach nieaktywności

*Pełna analiza: raport_q4_2024.ipynb*
"""
print(mock_summary)
```

> "Zauważcie co zrobiłem: nie poprosiłem AI o 'napisz mi raport'. Podałem konkretne dane, określiłem długość, format, styl. AI wypełniło szablon z danymi. To jest prawdziwa efektywność — nie zastępuję myślenia analitycznego, tylko automatyzuję pisanie."

---

### 1:15-1:25 — MATERIAŁ 4: Narzędzia praktyczne i etyka (10 min)

> "Teraz przegląd narzędzi, których będziecie używać w pracy — i ważna rozmowa o tym gdzie AI zawodzi."

**[Wyświetl na projektorze: przegląd narzędzi]**

```
NARZĘDZIA AI DLA ANALITYKA DANYCH:

1. CLAUDE.AI (anthropic.com) — FREE TIER DOSTĘPNY
   • Interfejs webowy — chat
   • Bardzo dobre do: długich dokumentów, kodu Python, wyjaśnień statystycznych
   • Darmowy: ~20 wiadomości / kilka godzin, potem cooldown
   • Claude API: darmowe $5 credit na start

2. CHATGPT (chat.openai.com) — FREE TIER DOSTĘPNY
   • GPT-4o mini gratis, GPT-4o z limitem
   • Dobre do: szybkich pytań, generowania kodu, brainstormingu
   • Plugin Code Interpreter: analizuje uploadowane CSV/Excel!
   • Można uploadować swoje dane (uwaga: prywatność!)

3. GITHUB COPILOT — DARMOWY DLA STUDENTÓW
   • github.com/education → GitHub Student Developer Pack
   • Integracja z VS Code — sugestie kodu w czasie rzeczywistym
   • Zna kontekst Waszego projektu (widzi cały plik, repo)
   • "Tab to accept" — akceptujesz sugestię jednym klawiszem

4. CLAUDE CODE (terminal) — WYMAGANA SUBSKRYPCJA
   • Narzędzie do pracy z całymi projektami w terminalu
   • Agent który może czytać, pisać, uruchamiać pliki
   • Idealne do złożonych projektów analitycznych

5. CURSOR (cursor.sh) — DARMOWY STARTER
   • VS Code z wbudowanym AI
   • "Cmd+K" — napisz co zmienić, AI edytuje kod
   • Dobra alternatywa dla Copilota
```

> "GitHub Copilot przez GitHub Education jest naprawdę darmowy dla studentów z adresem uczelnianym. Zarejestrujcie się po zajęciach — to powinien być Wasz standardowy tool w IDE."

**[Wyświetl: Ograniczenia i etyka]**

> "Teraz najważniejsza część tej sekcji — ograniczenia. AI jest jak bardzo pewny siebie kolega, który zna odpowiedź na WSZYSTKO — ale czasem się myli. Problem w tym, że myli się tak samo pewnym tonem jak gdy ma rację."

```
OGRANICZENIA LLM — MUSICIE O NICH WIEDZIEĆ:

1. HALUCYNACJE
   Model może:
   - Wymyślać funkcje które nie istnieją (np. "pd.DataFrame.super_clean()")
   - Podawać fałszywe statystyki z wiarygodnie brzmiącymi źródłami
   - Mylić nazwy parametrów API (zwłaszcza w nowszych bibliotekach)

   REGUŁA: zawsze weryfikujcie wygenerowany kod uruchomieniem

2. ODCIĘCIE WIEDZY (knowledge cutoff)
   Model nie wie o:
   - Nowych wersjach bibliotek wydanych po dacie treningu
   - Aktualnych danych rynkowych, kursach, cenach
   - Wydarzeniach po cutoff

   REGUŁA: dla aktualnych informacji — sprawdźcie dokumentację

3. PRYWATNOŚĆ DANYCH
   Dane wysłane do publicznego API (OpenAI, Anthropic) mogą być:
   - Logowane przez dostawcę
   - Użyte do trenowania (zależnie od ustawień)

   REGUŁA FIRMOWA: nigdy nie wysyłajcie danych osobowych, numerów klientów,
   danych finansowych firmy do publicznego API bez zgody prawników

4. MATEMATYKA I OBLICZENIA
   LLM = model językowy, NIE kalkulator
   Może popełniać błędy przy złożonych obliczeniach

   REGUŁA: wyniki obliczeń zawsze weryfikujcie Pythonem

5. ODPOWIEDZIALNOŚĆ
   AI generuje kod — ale ODPOWIEDZIALNOŚĆ jest Wasza.
   Jeśli wdrożycie błędny model predykcyjny w firmie —
   tłumaczenie "AI tak powiedział" nie wystarczy.
```

> "Kwestia etyczna — akademicka: czy można używać AI do odrabiania zadań? W tym kursie: tak, z jednym warunkiem. Musicie rozumieć co AI wygenerowało. Na laboratorium sprawdzam — nie czy kod działa, ale czy umiecie go wyjaśnić. W pracy: musicie podpisać się pod każdą analizą którą oddajecie. Podpis = odpowiedzialność = musicie rozumieć."

> "Na rynku pracy: firmy oczekują że umiecie używać AI produktywnie. Nie oczekują że wiecie jak je trenować. Ale oczekują że wiecie kiedy AI się myli — i to jest wartość Waszego wykształcenia."

---

### 1:25-1:35 — AKTYWNOŚĆ: Piszemy prompty (10 min)

> "Wasza kolej. 10 minut. Trzy zadania analityczne — dla każdego napiszcie prompt, który dałby użytecznemu AI konkretną, wykonalną instrukcję."

**[Wyświetl na projektorze]**

```
AKTYWNOŚĆ — NAPISZ PROMPT DLA:

ZADANIE 1 (Ćwiczenie):
Masz DataFrame z kolumnami: klient_id, data_urodzenia, plec, miasto, kategoria_klienta.
Chcesz przeprowadzić segmentację wiekową (18-25, 26-35, 36-50, 51+).

Napisz prompt który poprosi AI o:
→ Kod Python tworzący nową kolumnę 'segment_wiekowy'
→ Tabelę przestawną pokazującą rozkład segmentów per miasto
→ Użycie tylko pandas

---

ZADANIE 2 (Interpretacja):
Masz wyniki testu chi-kwadrat:
χ² = 18.4, df = 4, p = 0.001, n = 300

Napisz prompt który poprosi AI o:
→ Wyjaśnienie wyniku prostym językiem
→ Interpretację biznesową (kontekst: badanie satysfakcji klientów wg segmentu)
→ Format: 3 bullet points, bez wzorów matematycznych

---

ZADANIE 3 (Czyszczenie):
Masz kolumnę 'opis_problemu' z ticketów supportowych — 500 różnych wariantów.
Chcesz skategoryzować je do 5 typów: 'platnosc', 'dostawa', 'produkt', 'konto', 'inne'.

Napisz prompt który:
→ Opisuje zadanie modelowi
→ Podaje przykłady kilku wariantów do skategoryzowania
→ Określa format wyjściowy (np. dict Python lub DataFrame)
```

**Po 8 minutach:**

> "Kto chce pokazać swój prompt do Zadania 1? [Ochotnicy]. Co zmienilibyście żeby był precyzyjniejszy?"

> "Klucz do dobrego promptu: **kontekst + zadanie + format + ograniczenia**. Każde z tych czterech elementów redukuje niepewność modelu i zwiększa szansę na odpowiedź, którą możecie bezpośrednio użyć."

---

### 1:35-1:45 — PODSUMOWANIE

> "Podsumujmy wszystko — i powiedzmy sobie kilka słów o tym co Was czeka."

> "**LLM** — Large Language Models — to narzędzia generujące tekst token po tokenie, uczone na ogromnych zbiorach danych. GPT, Claude, Gemini — różne silne strony, podobne interfejsy. Temperatura niska = kod, wysoka = kreatywność."

> "**API z Pythona** — trzy linijki. `client = OpenAI()`, `response = client.chat.completions.create(...)`, `answer = response.choices[0].message.content`. System message + user message = kontrola zachowania modelu. Structured output = JSON gotowy do przetwarzania."

> "**Cztery zastosowania w praktyce** — generowanie kodu (precyzyjny prompt z kontekstem), interpretacja wyników (piszemy dla zarządu, nie dla statystyka), czyszczenie opisów (normalizacja kategorii), podsumowania (szablon + dane = raport)."

> "**Narzędzia** — GitHub Copilot w IDE (darmowy dla studentów), Claude.ai i ChatGPT przez przeglądarkę (free tier). Klucz API — gdy budujecie pipeline automatyczny."

> "**Ograniczenia** — halucynacje, knowledge cutoff, prywatność danych, odpowiedzialność. AI asystuje — nie zastępuje."

> "**W15 — za tydzień:** prezentacje mini-projektów. Każdy/każda z Was prezentuje 5-7 minut na temat swojego datasetu i przeprowadzonej analizy. Oceniam: czy analiza jest kompletna (eksploracja → czyszczenie → wizualizacja → statystyka), czy kod jest na GitHubie z historią commitów, czy potraficie wyjaśnić wyniki. Przygotujcie się!"

> "Jedno zdanie na zakończenie: W tym semestrze nauczyliście się NumPy, Pandas, Matplotlib, Seaborn, Scipy, Scikit-learn, Plotly, Polars — i teraz jeszcze AI. To jest kompletny toolkit nowoczesnego analityka danych. Nie wszyscy będą go używali w pełni od razu — ale fundamenty macie. Każde nowe narzędzie, które przyjdzie — będziecie mogli na to zbudować."

**Zadanie domowe (nieoceniane):**
> "Weźcie jeden Notebook z Waszego projektu. Użyjcie Claude'a lub ChatGPT (free) żeby: 1) wygenerować dodatkową wizualizację której Wam brakowało, 2) poprosić o interpretację jednego wyniku po polsku dla 'nie-analityka'. Przynieście to na prezentację — fajny bonus do omówienia."
