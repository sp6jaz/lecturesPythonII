# W02 Wykład — Plan zajęć dla prowadzącego

## Temat: Wprowadzenie do analizy danych

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code z Jupyter, terminal, internet
- **Przed wykładem:** otwórz `pipeline_demo.ipynb` w VS Code, przygotuj dataset tips

### Efekty uczenia się (Bloom)
Po tym wykładzie osoba studiująca:
1. **Opisuje** pipeline analityczny: pytanie → dane → analiza → wizualizacja → decyzja (Bloom 2)
2. **Identyfikuje** typy danych w Pythonie i DataFrame (int, float, str, object, datetime) (Bloom 1)
3. **Stosuje** Jupyter Notebook do eksploracji danych: komórki, Shift+Enter, Markdown (Bloom 3)
4. **Wyjaśnia** dlaczego listy Pythona nie wystarczają do analizy danych (motywacja do NumPy) (Bloom 2)

### Quiz z W01 (spaced repetition, 5 min na początku)

Użyj `quiz_w01.md` z materiałów W01 — 5 pytań, studenci odpowiadają na kartce lub przez Moodle/Mentimeter.

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań z W01 | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | Nawiązanie do W01, plan wykładu, cel | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | Pipeline analityczny — od pytania do decyzji | Live coding (notebook) |
| 0:30-0:45 | **MATERIAŁ 2** | Typy danych w Pythonie — powtórka i rozszerzenie | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | Jupyter Notebook — praca z notebookiem | Live coding |
| 1:15-1:30 | **MATERIAŁ 4** | Źródła danych w biznesie + dlaczego potrzebujemy NumPy | Live demo + benchmark |
| 1:30-1:40 | **AKTYWNOŚĆ** | Mini-ćwiczenie: eksploracja datasetu w notebooku | Studenci piszą |
| 1:40-1:45 | **PODSUMOWANIE** | 3 bullet points, zapowiedź NumPy na W03 | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W01)

> "Dzień dobry. Zanim zaczniemy nowy materiał — 5 pytań z zeszłego tygodnia. Macie 3 minuty."

**[Wyświetl pytania z quiz_w01.md lub przez Mentimeter]**

Po 3 minutach — szybko omów odpowiedzi:
> "Pytanie 1: co robi git commit? Odpowiedź B — zapisuje migawkę lokalnie, nie na GitHub. Push wysyła na GitHub."

> "Pytanie 3: po co venv? Izolacja bibliotek. Projekt A chce pandas 1.5, projekt B chce pandas 2.0 — bez venv się kłócą."

> "Nie przejmujcie się jeśli nie wszystko pamiętacie — po to robimy te quizy, żeby te rzeczy wam się utrwaliły."

---

### 0:05-0:10 — WPROWADZENIE

> "Zeszły tydzień — narzędzia. Git, VS Code, Markdown. Dzisiaj zaczynamy używać tych narzędzi do **prawdziwej roboty**."

> "Dzisiejszy temat: **jak wygląda analiza danych od początku do końca**. Nie chodzi o jedną funkcję czy bibliotekę — chodzi o cały proces. Bo w pracy nikt wam nie powie 'użyj pandas'. Powie wam: '**Który produkt sprzedaje się najlepiej w grudniu?**' — a wy musicie wiedzieć jak od tego pytania dojść do odpowiedzi."

> "Plan: pokażę wam pipeline analityczny, powtórzymy typy danych w Pythonie, pogłębimy pracę z Jupyter Notebook, a na koniec zobaczycie dlaczego potrzebujemy specjalnych bibliotek do danych."

---

### 0:10-0:30 — MATERIAŁ 1: Pipeline analityczny (live coding, 20 min)

**[Otwórz `pipeline_demo.ipynb` w VS Code]**

> "Pipeline analityczny. Brzmi groźnie, ale to po prostu **sekwencja kroków** od pytania biznesowego do odpowiedzi."

**[Narysuj na tablicy lub pokaż slajd z diagramem]**

```
Pytanie biznesowe → Pozyskanie danych → Czyszczenie → Analiza → Wizualizacja → Decyzja
```

> "Pokażę wam to na żywym przykładzie. Wyobraźcie sobie, że pracujecie w restauracji. Szef pyta: **'Który dzień tygodnia przynosi nam największe napiwki?'** — bo chce wiedzieć kiedy zatrudnić więcej kelnerów."

**[Komórka 1 — importy i wczytanie danych]**

```python
import pandas as pd
import matplotlib.pyplot as plt
```

> "Importujemy dwie biblioteki. pandas do danych, matplotlib do wykresów. Za tydzień zaczniemy od NumPy, ale dzisiaj skupiamy się na procesie, nie na bibliotekach."

```python
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
```

> "Wczytaliśmy dane wprost z internetu. Jedną linią. `df` to skrót od DataFrame — tabelka, jak w Excelu."

**[Komórka 2 — poznaj dane]**

```python
print(f"Rozmiar: {df.shape[0]} wierszy, {df.shape[1]} kolumn")
print(f"Kolumny: {list(df.columns)}")
```

> "Krok pierwszy: **poznaj dane**. Ile mamy wierszy? 244 rachunki. 7 kolumn. Jakie kolumny? Rachunek, napiwek, płeć, palący, dzień, pora, rozmiar stolika."

**[Komórka 3 — przejrzyj dane]**

```python
df.head()
```

> "`.head()` — pokaż 5 pierwszych wierszy. To ZAWSZE pierwszy krok. Nie analizuj danych, których nie widziałeś."

**[Komórka 4 — statystyki]**

```python
df.describe()
```

> "`.describe()` — podstawowe statystyki. Średnia, minimum, maximum, kwartyle. Od razu widać: średni rachunek to ~20 dolarów, średni napiwek ~3 dolary, stoliki od 1 do 6 osób."

> "Zauważcie — nie napisałem ani jednej pętli. Pandas robi to za nas."

**[Komórka 5 — odpowiedź na pytanie]**

```python
df.groupby('day')['tip'].mean().sort_values(ascending=False)
```

> "I odpowiedź na pytanie szefa: **niedziela** — średni napiwek 3.26 dolara. Sobota na drugim miejscu. Szef wie kiedy potrzebuje więcej kelnerów."

> "Ile linii kodu? Jedna. Ale żeby wiedzieć jak ją napisać — musicie rozumieć cały proces."

**[Komórka 6 — wizualizacja]**

```python
df.groupby('day')['tip'].mean().plot(kind='bar', title='Średni napiwek wg dnia')
plt.ylabel('USD')
plt.tight_layout()
plt.show()
```

> "Wykres. Bo dane w tabelce są dobre dla was, ale szef chce **obrazek**. Decyzja biznesowa zapada na podstawie wykresu, nie surowych liczb."

**[Komórka 7 — drugi wykres]**

```python
df.plot.scatter(x='total_bill', y='tip', alpha=0.5, title='Rachunek vs napiwek')
plt.xlabel('Rachunek ($)')
plt.ylabel('Napiwek ($)')
plt.show()
```

> "Scatter plot — każdy punkt to jeden rachunek. Widać korelację: wyższy rachunek → wyższy napiwek. Ale są wyjątki — ktoś dał 1 dolar napiwku przy rachunku 50 dolarów. Ciekawe, prawda?"

> "To jest pipeline analityczny: **pytanie → dane → przejrzenie → analiza → wykres → odpowiedź**. Przez następne 13 tygodni będziemy doskonalić każdy z tych kroków."

---

### 0:30-0:45 — MATERIAŁ 2: Typy danych w Pythonie (15 min)

> "Zanim pójdziemy dalej — powtórka z Python I. Typy danych. Ale tym razem w kontekście **danych biznesowych**."

**[Nowa komórka w notebooku]**

```python
# Typy danych w Pythonie
cena = 19.99           # float — liczba zmiennoprzecinkowa
ilosc = 42             # int — liczba całkowita
produkt = "Laptop"     # str — tekst
w_magazynie = True     # bool — prawda/fałsz
```

> "To znacie z Pythona I. Ale w analizie danych pojawiają się nowe problemy."

```python
# Problem 1: lista cen produktów
ceny = [19.99, 29.99, 9.99, 49.99, 14.99]
# Ile wynosi średnia cena?
print(sum(ceny) / len(ceny))
```

> "Lista. Działa. Ale co jeśli mamy milion cen?"

```python
# Problem 2: tabela danych — lista list
zamowienia = [
    ["Laptop", 2999.99, 3],
    ["Mysz", 49.99, 15],
    ["Klawiatura", 149.99, 8],
]
# Jak policzyć średnią cenę? Sumę zamówień?
suma = sum(row[1] * row[2] for row in zamowienia)
print(f"Suma zamówień: {suma:.2f} zł")
```

> "Da się. Ale to brzydkie, wolne i łatwo o błąd. Co jeśli ktoś wstawi tekst zamiast liczby? Co jeśli brakuje wartości?"

```python
# Problem 3: brakujące dane — codzienność analityka
dane_hr = [
    {"imie": "Anna", "pensja": 8500, "dzial": "IT"},
    {"imie": "Jan", "pensja": None, "dzial": "HR"},     # brak pensji!
    {"imie": "Ewa", "pensja": 7200, "dzial": None},     # brak działu!
]
```

> "W realnych danych **zawsze** czegoś brakuje. Klient nie podał adresu, sensor nie zapisał pomiaru, ankieta ma puste pola. Listy i słowniki nie mają wbudowanego radzenia sobie z tym. Pandas — ma."

**[Pokaż typy danych w DataFrame]**

```python
print(df.dtypes)
```

> "DataFrame ma swoje typy: `float64` to liczba zmiennoprzecinkowa, `int64` to liczba całkowita, `object` to najczęściej tekst. Pandas sam rozpoznaje typ każdej kolumny przy wczytywaniu."

```python
# Typy kolumn w kontekście biznesowym
# float64 — kwoty, ceny, wyniki pomiarów
# int64   — ilości, identyfikatory, liczba sztuk
# object  — nazwy, kategorie, opisy
# bool    — flagi (aktywny/nieaktywny, zapłacone/niezapłacone)
# datetime64 — daty i czasy (dojdzie w Pandas)
```

> "Na kolejnych wykładach nauczycie się konwertować typy, radzić sobie z brakującymi wartościami, operować na datach. Dzisiaj — świadomość, że te problemy istnieją i że Pandas je rozwiązuje."

---

### 0:45-0:55 — PRZERWA (10 min)

> "10 minut przerwy."

---

### 0:55-1:15 — MATERIAŁ 3: Jupyter Notebook w praktyce (20 min)

> "Na zeszłym labie widzieliście Jupyter Notebook — dzisiaj pogłębimy. Bo notebook to wasze **główne narzędzie eksploracji danych**."

**[Utwórz nowy notebook: Ctrl+Shift+P → "Create New Jupyter Notebook"]**

> "Notebook składa się z **komórek**. Dwa typy: **Code** i **Markdown**."

**[Komórka Code]**

```python
# To jest komórka kodu — Shift+Enter uruchamia
wynik = 2 + 2
print(f"Wynik: {wynik}")
```

> "Shift+Enter — uruchom komórkę i przejdź do następnej. Ctrl+Enter — uruchom i zostań."

**[Komórka Markdown — zmień typ]**

```markdown
# Analiza napiwków w restauracji

## Pytanie badawcze
Który dzień tygodnia przynosi największe napiwki?

## Dane
Dataset: 244 rachunki z restauracji w USA.
```

> "Komórki Markdown to **opowieść**. Notebook to nie skrypt — to **narracja z kodem**. Piszesz co robisz, dlaczego, i jakie wnioski wyciągasz. To właśnie odróżnia analityka od programisty — analityk **opowiada historię**."

**[Pokaż przydatne skróty]**

> "Kilka skrótów, które wam oszczędzą mnóstwo czasu:"

| Skrót | Co robi |
|-------|---------|
| `Shift+Enter` | Uruchom komórkę, przejdź dalej |
| `Ctrl+Enter` | Uruchom komórkę, zostań |
| `A` | Dodaj komórkę powyżej (w trybie komend) |
| `B` | Dodaj komórkę poniżej |
| `M` | Zmień na Markdown |
| `Y` | Zmień na Code |
| `DD` | Usuń komórkę |
| `Esc` | Tryb komend (niebieska ramka) |
| `Enter` | Tryb edycji (zielona ramka) |

> "Tryb komend vs tryb edycji. Jak w Vimie, jeśli ktoś zna. `Esc` — tryb komend, możesz nawigować. `Enter` — wchodzisz do edycji komórki."

**[Pokaż ważne funkcje]**

```python
# Autouzupełnianie — Tab
# df. + Tab → lista metod

# Dokumentacja — Shift+Tab
# df.groupby + Shift+Tab → docstring

# Magiczna komenda — czas wykonania
%timeit sum(range(1000))
```

> "Procent `timeit` — mierzy czas wykonania. Przydatne gdy chcecie sprawdzić co jest szybsze."

```python
# Wyświetlanie ostatniego wyrażenia
df.head()  # nie trzeba print() — notebook wyświetla automatycznie
```

> "Notebook automatycznie wyświetla wynik ostatniego wyrażenia w komórce. Nie musicie pisać `print()` dla tabel i wykresów."

**[Pokaż kolejność uruchamiania komórek]**

> "UWAGA — ważna pułapka. Komórki możecie uruchamiać w dowolnej kolejności. To daje elastyczność, ale może powodować błędy."

```python
# Komórka 1
x = 10
```

```python
# Komórka 2
print(x + y)  # BŁĄD! y jeszcze nie istnieje
```

```python
# Komórka 3
y = 20
```

> "Jeśli uruchomicie komórkę 2 przed komórką 3 — błąd. Numer w nawiasie `[3]` obok komórki mówi w jakiej kolejności ją uruchomiliście. Zasada: **uruchamiajcie od góry do dołu**. Gdy się pogubicie — 'Restart Kernel and Run All'."

---

### 1:15-1:30 — MATERIAŁ 4: Źródła danych + motywacja do NumPy (15 min)

> "Skąd analityk bierze dane?"

**[Lista na slajdzie lub w notebooku Markdown]**

> "W pracy analityka dane przychodzą z wielu miejsc:"

```markdown
## Źródła danych w biznesie
- **CSV / Excel** — eksporty z systemów, raporty
- **Bazy danych** — SQL (PostgreSQL, MySQL, SQLite)
- **API** — dane z serwisów (pogoda, giełda, social media)
- **Scraping** — zbieranie danych ze stron WWW
- **Pliki JSON** — logi, konfiguracje, dane z aplikacji
- **Pliki Parquet** — szybki format kolumnowy (big data)
```

> "Na tym kursie będziemy głównie pracować z CSV i Excelem — bo to najpopularniejsze formaty w firmach. Pandas czyta je jedną linią."

```python
# Sposoby wczytywania danych w Pandas
df_csv = pd.read_csv('dane.csv')
df_excel = pd.read_excel('raport.xlsx')
df_json = pd.read_json('dane.json')
# df_sql = pd.read_sql('SELECT * FROM klienci', connection)  # bazy danych
```

> "A teraz — dlaczego potrzebujemy specjalnych narzędzi. Dlaczego nie wystarczą listy Pythona?"

**[Benchmark — lista vs NumPy]**

```python
import numpy as np
import time

# Milion cen produktów
lista = list(range(1_000_000))
tablica = np.array(lista)

# Pomnóż każdą cenę przez 2 (np. konwersja waluty)
start = time.perf_counter()
wynik_lista = [x * 2 for x in lista]
czas_lista = time.perf_counter() - start

start = time.perf_counter()
wynik_numpy = tablica * 2
czas_numpy = time.perf_counter() - start

print(f"Lista:  {czas_lista*1000:.1f} ms")
print(f"NumPy:  {czas_numpy*1000:.1f} ms")
print(f"NumPy jest {czas_lista/czas_numpy:.0f}× szybszy!")
```

> "NumPy jest kilkanaście razy szybszy. A przy milionach wierszy — różnica jest jeszcze większa. Dlaczego? Bo NumPy operuje na **ciągłych blokach pamięci** i używa instrukcji procesora zoptymalizowanych pod obliczenia. Lista Pythona to pudełka rozrzucone po pamięci."

> "Za tydzień — **NumPy**. Nauczycie się tworzyć tablice, indeksować je, robić operacje wektorowe. To fundament, na którym stoi Pandas, Matplotlib i cały ekosystem data science."

---

### 1:30-1:40 — AKTYWNOŚĆ: mini-ćwiczenie (10 min)

> "Czas na was. Otwórzcie notebook (albo weźcie kartkę) i odpowiedzcie na pytania do tego datasetu:"

**[Wyświetl na projektorze]**

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
```

**Pytania:**
1. Ile wierszy i kolumn ma ten dataset? (podpowiedź: `.shape`)
2. Jaka jest największa kwota rachunku? (podpowiedź: `df['total_bill'].max()`)
3. Ile było rachunków na obiad (Dinner) vs lunch? (podpowiedź: `df['time'].value_counts()`)

> "5 minut. Kto nie ma notebooka — kartkę i długopis, napiszcie odpowiedzi."

**[Po 5 minutach]**

> "Sprawdzamy. Ile wierszy? 244, 7 kolumn. Największy rachunek? 50.81 dolarów. Dinner vs Lunch? 176 obiadów, 68 lunchów. Widzicie — restauracja zarabia głównie na obiadach."

---

### 1:40-1:45 — PODSUMOWANIE

> "Podsumujmy. Dzisiaj poznaliście trzy rzeczy:"

> "1. **Pipeline analityczny** — od pytania biznesowego, przez dane, analizę, wykres, do decyzji."
> "2. **Typy danych** — Python ma swoje typy, Pandas ma swoje. W prawdziwych danych zawsze czegoś brakuje."
> "3. **Jupyter Notebook** — wasze główne narzędzie do eksploracji danych. Kod + tekst + wykresy w jednym dokumencie."

> "A na koniec zobaczyliście, że listy Pythona są za wolne do milionów danych. Dlatego za tydzień — **NumPy**. Tablice, operacje wektorowe, szybkość. To fundament całej reszty kursu."

> "Na laboratorium przećwiczycie to wszystko: wczytacie dataset, zbadacie go, odpowiecie na pytania, zrobicie wykresy. Do zobaczenia!"

**Zadanie domowe (nieoceniane):**
> "Wejdźcie na kaggle.com i przejrzyjcie 3 datasety z kategorii Business. Zastanówcie się jakie pytania biznesowe można zadać do tych danych. Na następnym wykładzie zapytam co znaleźliście."
