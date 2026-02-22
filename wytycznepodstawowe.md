# Wytyczne podstawowe — lecturesPythonII

## Cel projektu
Tworzenie materiałów dydaktycznych z Pythona II dla studentów kierunku **Analityka danych w biznesie**: **wykłady** + **laboratoria**, sukcesywnie z tygodnia na tydzień.

## Kontekst kierunku
- Studenci to przyszli analitycy danych w biznesie — przykłady i zadania powinny nawiązywać do realiów biznesowych (sprzedaż, marketing, finanse, HR, logistyka)
- Python II to narzędzie do ich głównej specjalności, nie cel sam w sobie

## Formy materiałów
1. **Wykłady** — teoria, wyjaśnienia, przykłady
2. **Laboratoria** — ćwiczenia praktyczne, zadania do samodzielnego rozwiązania

## Podział zajęć i prowadzący
- **Studia dzienne (15 spotkań):** wykład — prowadzący, laboratorium — doktorant
- **Studia zaoczne (10 spotkań):** wykład + laboratorium — prowadzący (oba osobiście)
- Poprzedni kurs (Python I): Colab + trochę PyCharm, inny prowadzący
- Wcześniejsze edycje Python II używały Anacondy — **rezygnujemy z Anacondy**

## Narzędzia kursu (decyzja 2026)
- **Python 3.12+** — z python.org lub apt
- **uv** — ultraszybki menedżer pakietów i venv (Astral), zastępuje pip+venv+pyenv
- **VS Code** — edytor + Jupyter extension + Git integration
- **Jupyter Notebook** — przez VS Code lub przeglądarkę
- **Git + GitHub** — od pierwszych zajęć
- Rezygnacja z Anacondy: ciężka, komercyjna licencja, conda vs pip konflikty, nie uczy prawdziwego ekosystemu Python
- **VS Code = oficjalne IDE kursu** — wszystkie materiały, instrukcje, screenshoty pod VS Code
- PyCharm dozwolony, ale bez dedykowanych instrukcji — kto chce, radzi sobie sam
- Nie robimy podwójnych instrukcji — jeden spójny przekaz
- Prowadzący migruje z PyCharm na VS Code — sam pracuje na tym samym narzędziu co studenci
- **Jupyter Notebook** — głównie przez VS Code (extension), pokazać też klasyczny w przeglądarce
- Format pracy: `.ipynb` (eksploracja, wykresy) + `.py` (czysty kod, moduły) — oba w Git

## Struktura katalogów
```
dzienne/
  W01/ .. W15/        — 15 tygodni
    wyklad/           — materiały wykładowe
    lab/              — materiały laboratoryjne (dla doktoranta)
zaoczne/
  S01/ .. S10/        — 10 spotkań
    wyklad/           — materiały wykładowe
    lab/              — materiały laboratoryjne
```
- Każdy tydzień/spotkanie ma **wyklad/** + **lab/** — spójność treści w jednym miejscu
- Materiały lab dzienne tworzy prowadzący → udostępnia doktorantowi (zachowanie spójności z wykładem)
- Materiały zaoczne: jednolita struktura, skondensowana wersja dziennych (10 vs 15 spotkań)
- Wykłady dzienne i zaoczne prowadzi ta sama osoba — treść spójna, różni się tempo
- **`skryptdlastudentow/skrypt.md`** — skrypt wydawany na koniec semestru, budowany równolegle z materiałami zajęć

## Zasada: materiały → skrypt + notatki
- Przy tworzeniu każdych zajęć **równocześnie** uzupełniać odpowiedni rozdział w `skryptdlastudentow/skrypt.md`
- Skrypt to spójny, zredagowany dokument (nie kopia slajdów) — nadaje się do samodzielnej nauki
- **`notatki_i_porady.md`** — analizy, rekomendacje i przemyślenia agenta z dyskusji; zapisywać tam każdą istotną poradę/analizę

## Sposób pracy
- Użytkownik podaje obszar tematyczny i wytyczne
- Agent tworzy materiały bazując na:
  - sprawdzonych informacjach z internetu
  - własnej wiedzy
  - **weryfikacji lokalnej** — każde rozwiązanie/przykład musi być przetestowane na komputerze (skrypty, venv, uruchomienie kodu)
- Materiały tworzone przyrostowo, tydzień po tygodniu

## Rola agenta — aktywny współtwórca
- **Zawsze podpowiadaj** co warto dodać lub zmienić w obrębie przedmiotu
- Użytkownik ma doświadczenie w Pythonie i wizję zajęć, ale jest otwarty na modyfikacje
- Agent wnosi doświadczenie, sprawność w wyszukiwaniu informacji i świeże pomysły

## Struktura każdej jednostki dydaktycznej (Backward Design + Kolba + Mayer)
1. **WPROWADZENIE** (5 min) — temat, cele językiem studenta, plan, powiązanie z poprzednimi
2. **MATERIAŁ** (30-40 min wykład / 15 min lab) — bloki 5-12 min, kod na żywo, diagramy, przykłady biznesowe
3. **AKTYWNOŚĆ** (10-15 min wykład / 60 min lab) — zadanie, quiz, dyskusja; jasne kryteria
4. **PODSUMOWANIE** (5 min) — 3 bullet points, zapowiedź następnych zajęć, zadanie domowe

## Efekty uczenia się — zasady
- Perspektywa studenta: "Osoba studiująca **potrafi/stosuje/analizuje**..."
- Czasowniki z taksonomii Blooma (nie "zna", "rozumie", "zapoznaje się")
- Każdy efekt = przypisana forma weryfikacji
- Pełna teoria: `teoriadydaktyki/ramy_dydaktyczne.md`

## Cel dydaktyczny — zaangażowanie studentów
- Kluczowe: **utrzymać uwagę i motywację studentów** przez cały semestr
- Zapobiec zjawisku odpuszczania ("przedmiot nie jest ważny")
- Stosować metody oparte na badaniach naukowych dot. efektywnego nauczania:
  - **Active learning** — angażowanie studentów w rozwiązywanie problemów, nie tylko słuchanie
  - **Spaced repetition** — powracanie do kluczowych koncepcji w kolejnych tygodniach
  - **Scaffolding** — stopniowe zwiększanie trudności, budowanie na wcześniejszej wiedzy
  - **Real-world relevance** — przykłady z prawdziwych zastosowań, nie abstrakcyjne ćwiczenia
  - **Immediate feedback** — szybka informacja zwrotna (testy, autocheck w zadaniach)
  - **Gamifikacja** — elementy rywalizacji, punkty, wyzwania (w miarę możliwości)
  - **Efekt IKEA** — studenci bardziej cenią to, co sami zbudowali

## Sylabus — dane formalne
- **Przedmiot:** Programowanie w języku Python II (K.05)
- **Uczelnia:** Politechnika Opolska, WEAiI
- **Kierunek:** Analityka danych w biznesie, I stopień, semestr 2
- **ECTS:** 5.0 | **Zaliczenie:** Egzamin pisemny + cząstkowe zadania lab
- **Wykład:** 30h (konwersatoryjny, interakcja, Moodle)
- **Laboratorium:** 30h (sala komputerowa, Jupyter/Anaconda, Moodle)
- **Praca własna studenta:** 65h (przygotowanie 30h, sprawozdania 20h, studiowanie 13h, egzamin 2h)
- **Prowadzący:** dr hab. inż. Zygarlicki Jarosław

## Sylabus — tematy wykładów (oryginał z KOP)
1. Wprowadzenie do przedmiotu, KOP, warunki zaliczenia, literatura
2. Wprowadzenie do analizy danych i narzędzi analitycznych
3. Biblioteka NumPy
4. Biblioteka Pandas
5. Biblioteka Matplotlib
6. Wprowadzenie do statystyki w Python
7. Biblioteki Python w zaawansowanej analizie danych
8. Podsumowanie

## Wizja prowadzącego — modyfikacje do sylabusa

### Wykład 1 — Warsztat pracy analityka (zamiast suchego "wprowadzenia")
Pierwszy wykład to **ustalenie zasad + wytypowanie narzędzi + zasady tworzenia kodu i dokumentacji**:
- **Git i GitHub** — od pierwszych zajęć studenci tworzą repo, commitują prace, uczą się workflow
- **Markdown** — dokumentacja w .md, pięknie formatowana na GitHubie, standard branży
- **Mermaid** — schematy blokowe, diagramy przepływu danych, wizualizacja procesów analitycznych
- **Zasady tworzenia kodu** — struktura projektu, nazewnictwo, czytelność
- Cel: studenci od razu pracują jak profesjonaliści, nie "na pendrive'ach"

## Sylabus — tematy laboratoriów
1. Warunki formalne
2. Instalacja i konfiguracja narzędzi (Jupyter Notebook, Anaconda)
3. Ćwiczenia z biblioteką NumPy
4. Ćwiczenia z biblioteką Pandas
5. Ćwiczenia z biblioteką Matplotlib
6. Ćwiczenia z wykorzystaniem statystyki w Python
7. Zaliczenia i wpisy

## Sylabus — efekty kształcenia
- **K1_W05** — zaawansowana wiedza o narzędziach do gromadzenia, przetwarzania i analizy danych
- **K1_W06** — kluczowe terminy i paradygmaty w technologiach programowania
- **K1_U05** — stosowanie metod obliczeniowych i narzędzi do analizy danych
- **K1_U06** — pisanie kodu do analizy danych z wykorzystaniem bibliotek
- **K1_K04** — współpraca w grupie, wymiana wiedzy

## Sylabus — literatura
- VanderPlas — *Python Data Science Handbook* (2016, nowsze wyd. 2023)
- McKinney — *Python for Data Analysis* (2nd ed. 2018, nowsze 3rd ed. 2022)
- Müller & Guido — *Introduction to Machine Learning with Python* (2016)

## Blok zaawansowany — LLM i AI w analizie danych
- Na późniejszym etapie kursu wprowadzić **zaawansowane analizy z wykorzystaniem LLM**
- Pokazać studentom praktyczne użycie:
  - **API AI** (np. OpenAI API, Anthropic API) — wywoływanie modeli z Pythona
  - **Agenty AI** — automatyzacja analiz, łańcuchy promptów, tool use
  - **LLM do analizy danych** — generowanie kodu, interpretacja wyników, czyszczenie danych z pomocą AI
- To wpisuje się w punkt sylabusa "Biblioteki Python w zaawansowanej analizie danych"
- Ogromna wartość dla kierunku Analityka danych w biznesie — to umiejętności, które rynek pracy już wymaga

## Datasety — podejście hybrydowe
- **W01-W10: wspólny dataset** — wszyscy na tych samych danych (doktorant ogarnia, egzamin spójny)
- **Ankieta w W01** — pytamy o zainteresowania → wpływa na wybór wspólnego datasetu
- **W11-W14: mini-projekt indywidualny** — student wybiera własny dataset, stosuje wszystkie techniki
- Egzamin oparty na technikach (W01-W12), nie na konkretnym datasecie

## Metody dydaktyczne (z researchu)
- **Live coding** — na każdym wykładzie, błędy celowe, participatory
- **Parsons Problems** — układanie bloków kodu (na początku kursu)
- **Fill-in-the-blanks** — notebooki z lukami do uzupełnienia
- **Faded worked examples** — od kompletnego przykładu do pisania od zera
- **Pair programming** — na laborkach, zmniejsza frustrację
- **Max 3 nowe koncepty na jedno laboratorium**
- **Pierwsza linia kodu w 15 min** od początku zajęć

## Uwagi do sylabusa (wnioski agenta)
- 8 tematów na 15 tygodni → duża swoboda w rozłożeniu materiału
- NumPy, Pandas, Matplotlib — każdy zasługuje na 2-3 wykłady
- "Zaawansowane biblioteki" — szeroka kategoria (seaborn, scikit-learn, scipy, polars, plotly)
- Brak jawnego tematu o czyszczeniu danych (missing values, merge, groupby) — wpleść w Pandas
- Literatura przestarzała — bazować na nowszych wydaniach
- Blok LLM/AI idealnie pasuje do "zaawansowanych bibliotek" z sylabusa
