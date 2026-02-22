# W13 Wykład — Plan zajęć dla prowadzącego

## Temat: Zaawansowane biblioteki — scikit-learn, Plotly, Polars

### Informacje organizacyjne
- **Czas:** 90 min (2h akademickie)
- **Forma:** wykład konwersatoryjny z live coding
- **Potrzebne:** komputer z projektorem, VS Code, venv z scikit-learn/plotly zainstalowanymi
- **Przed wykładem:** otwórz `advanced_libs_demo.ipynb`, uruchom pierwszą komórkę `%pip install scikit-learn plotly -q`
- **Kluczowe hasło:** "Opanowaliśmy fundament. Teraz pierwszy smak tego, co dalej — ML, interaktywne wykresy, szybsze DataFrames"

### WAŻNE — zależności
- **scikit-learn** i **plotly** NIE są w domyślnym venv kursu — pierwsza komórka notebooka instaluje je automatycznie
- Jeśli jest problem z instalacją: `source .venv/bin/activate && uv pip install scikit-learn plotly`
- Weryfikacja: `python -c "import sklearn; import plotly; print('OK')`

### Efekty uczenia się (Bloom poziom 3-5)
Po tym wykładzie osoba studiująca:
1. **Stosuje** `train_test_split` i `StandardScaler` do przygotowania danych pod model ML (Bloom 3)
2. **Stosuje** `KMeans` do segmentacji klientów i interpretuje klastry jako decyzje biznesowe (Bloom 3)
3. **Projektuje** pipeline regresji liniowej w scikit-learn: fit → predict → ocena R² i MSE (Bloom 4)
4. **Tworzy** interaktywne wykresy Plotly Express (scatter, bar, line z hover) i osadza je w notebooku (Bloom 5)
5. **Ocenia** kiedy użyć Polars zamiast Pandas i jakie korzyści przynosi zmiana biblioteki (Bloom 5)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **QUIZ** | Spaced repetition — 5 pytań (2 z W12, 3 nowe) | Kartka/Mentimeter |
| 0:05-0:10 | **WPROWADZENIE** | "Opanowaliśmy fundament. Teraz smak tego, co dalej" | Rozmowa |
| 0:10-0:30 | **MATERIAŁ 1** | scikit-learn: train/test split, StandardScaler, KMeans (segmentacja klientów) | Live coding |
| 0:30-0:45 | **MATERIAŁ 2** | scikit-learn: regresja liniowa, ocena modelu (R², MSE) | Live coding |
| 0:45-0:55 | **PRZERWA** | 10 minut | — |
| 0:55-1:15 | **MATERIAŁ 3** | Plotly Express: scatter, bar, line, hover, kolorowanie po kategorii | Live coding |
| 1:15-1:25 | **MATERIAŁ 4** | Polars — brief mention, benchmark vs Pandas, kiedy użyć | Slajd + demo |
| 1:25-1:35 | **AKTYWNOŚĆ** | KMeans segmentacja + wizualizacja Plotly — studenci sami | Studenci piszą |
| 1:35-1:45 | **PODSUMOWANIE** | Zapowiedź W14: LLM/AI API w Pythonie | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — QUIZ (spaced repetition z W12)

> "Pięć pytań — pierwsze dwa z zeszłego tygodnia, trzy nowe. Trzy minuty, kartka lub Mentimeter."

**[Użyj quiz_w13.md — pytania 1 i 2 to powtórka W12]**

> "Odpowiedzi: 1-B, 2-B. Pytania 3-5 to nowy materiał — do nich wrócimy pod koniec zajęć."

> "Kto miał 2/2 na pytaniach z W12? Świetnie. Pamiętacie: p > α to nie ma podstaw do odrzucenia H₀. To wróci dziś — bo R² to też miara 'jak dobrze model wyjaśnia dane'."

---

### 0:05-0:10 — WPROWADZENIE

> "Przez dwanaście tygodni budowaliśmy fundament. NumPy, Pandas, Matplotlib, Seaborn, statystyka, testy hipotez. To jest rdzeń pracy z danymi w Pythonie."

> "Ale jeśli spojrzycie na oferty pracy dla Data Analyst czy Data Scientist — zawsze pojawia się scikit-learn. I zawsze pojawia się coś z ML. I wykresy interaktywne. I często 'coś szybszego niż Pandas'."

> "Dzisiaj robimy dokładnie to: krótki, praktyczny smak trzech rzeczy, które otwierają kolejny poziom."

> "Pierwsze: scikit-learn. Najważniejsza biblioteka ML w Pythonie. Dzisiaj nauczycie się dwóch algorytmów — segmentacja klientów i prognozowanie sprzedaży. Nie jako teoria, ale jako narzędzie które można użyć w pracy w poniedziałek."

> "Drugie: Plotly. Wykresy które klient może klikać. Hover, zoom, filter. Prezentacja w Excelu vs interaktywny dashboard — co robi lepsze wrażenie?"

> "Trzecie: Polars. Szybszy Pandas. Krótko, bo to na przyszłość — ale warto wiedzieć że istnieje."

> "Zaczynamy od scikit-learn. Otwórzcie notebook `advanced_libs_demo.ipynb`."

---

### 0:10-0:30 — MATERIAŁ 1: scikit-learn — KMeans clustering

**[Uruchom komórkę 1 — instalacja, pokaż że %pip install działa bez wychodzenia z notebooka]**

> "Pierwsza komórka instaluje scikit-learn i Plotly jeśli ich nie ma. Cicha instalacja, `-q` = quiet. Uruchamiamy raz i zapominamy."

**[Komórka 2 — import i generowanie danych klientów]**

> "Wyobraźcie sobie: jesteście analitykiem w firmie e-commerce. Masz bazę 300 klientów. Dla każdego masz dwie zmienne: średnią wartość zamówienia i częstotliwość zakupów w roku."

> "Pytanie biznesowe: czy możemy podzielić klientów na segmenty i traktować ich różnie? Segmenty premium, standard, okazjonalni? To właśnie robi clustering."

```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n = 300
klienci = pd.DataFrame({
    'srednia_wartosc': np.concatenate([
        np.random.normal(500, 80, 100),   # segment okazjonalny
        np.random.normal(1200, 150, 100), # segment standard
        np.random.normal(2500, 200, 100)  # segment premium
    ]),
    'zamowienia_rok': np.concatenate([
        np.random.normal(2, 0.5, 100),
        np.random.normal(8, 1.5, 100),
        np.random.normal(20, 3, 100)
    ])
})
```

> "Trzy skupiska — jakbyśmy wiedzieli że są trzy segmenty. W prawdziwych danych tego nie wiemy — K-Means to odkryje."

**[Komórka 3 — StandardScaler]**

> "Zanim puścimy K-Means, musimy znormalizować dane. Dlaczego? Wartość zamówienia to setki i tysiące złotych. Liczba zamówień to 2-20. Bez normalizacji K-Means będzie zdominowany przez wartość zamówienia, bo te liczby są po prostu większe."

> "StandardScaler: odejmuje średnią, dzieli przez odchylenie standardowe. Po skalowaniu obie kolumny mają średnią 0 i std 1. Porównywalne."

```python
scaler = StandardScaler()
X = scaler.fit_transform(klienci[['srednia_wartosc', 'zamowienia_rok']])
```

> "`fit_transform` — dwa kroki w jednym: `fit` uczy skalera (liczy średnią i std), `transform` aplikuje. Ważne: na zbiorze testowym zawsze tylko `transform`, nigdy `fit_transform`. Inaczej 'zaglądacie' do danych testowych."

**[Komórka 4 — KMeans]**

```python
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)
klienci['segment'] = kmeans.labels_
```

> "Trzy linijki. Tworzymy model z k=3 klastrami. `fit` uczy model. `labels_` to przypisanie każdego klienta do klastra — 0, 1 lub 2."

> "random_state=42 — ta sama 'losowość' przy każdym uruchomieniu. Reprodukowalność wyników."

**[Komórka 5 — analiza klastrów]**

```python
print(klienci.groupby('segment')[['srednia_wartosc', 'zamowienia_rok']].mean().round(0))
```

> "Każdy klaster możemy teraz opisać. Klaster 0 — niskie wartości i rzadkie zakupy → klienci okazjonalni. Klaster 2 — wysokie wartości i częste → premium. To jest wynik biznesowy. Możemy teraz wysłać inne kampanie do każdego segmentu."

---

### 0:30-0:45 — MATERIAŁ 2: scikit-learn — regresja liniowa

> "Teraz drugi algorytm: regresja liniowa. Nie clustering — tym razem chcemy PRZEWIDYWAĆ wartość liczbową."

> "Przykład: masz dane o wydatkach reklamowych (TV, radio, internet) i sprzedaży w 200 regionach. Chcesz model który powie: 'jeśli zwiększę budżet na reklamę TV o 10 tys. PLN, to sprzedaż wzrośnie o...?'"

**[Komórka 6 — dane sprzedażowe]**

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

np.random.seed(42)
n = 200
reklama_tv = np.random.uniform(0, 300, n)
reklama_radio = np.random.uniform(0, 50, n)
szum = np.random.normal(0, 2, n)
sprzedaz = 5 + 0.05 * reklama_tv + 0.1 * reklama_radio + szum

df_reklama = pd.DataFrame({
    'tv': reklama_tv,
    'radio': reklama_radio,
    'sprzedaz': sprzedaz
})
```

> "Celowo budujemy dane z prawdziwą zależnością: TV ma mniejszy wpływ (0.05), radio ma większy (0.1). Model powinien to 'odkryć'."

**[Komórka 7 — train/test split]**

```python
X = df_reklama[['tv', 'radio']]
y = df_reklama['sprzedaz']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Trening: {len(X_train)}, Test: {len(X_test)}")
```

> "80% na trening, 20% na test. To standardowy podział. `random_state=42` — zawsze te same dane w podziale. `X` — cechy (features), `y` — to co przewidujemy (target)."

> "Zasada: model NIE widzi danych testowych podczas treningu. Piszemy po przerwie 'sprawdzian z materiału którego nie miałeś'. To uczciwa ocena."

**[Komórka 8 — trening i predykcja]**

```python
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"R² = {r2:.4f}")
print(f"RMSE = {rmse:.4f}")
print(f"Współczynniki: TV={model.coef_[0]:.4f}, Radio={model.coef_[1]:.4f}")
print(f"Wyraz wolny (intercept): {model.intercept_:.4f}")
```

> "R² — współczynnik determinacji. 0 = model nic nie wyjaśnia, 1 = model perfekcyjny. Wartość 0.95+ to bardzo dobry model. Zapytajcie siebie: 'ile procent zmienności sprzedaży wyjaśniają nasze zmienne reklamowe?'"

> "RMSE — Root Mean Squared Error. Średni błąd predykcji w jednostkach zmiennej celu. Jeśli RMSE = 2.1, to nasze prognozy błądzą średnio o 2.1 jednostki sprzedaży."

> "Współczynniki powinny być zbliżone do prawdziwych wartości 0.05 (TV) i 0.10 (radio). Model odtworzył rzeczywistą zależność z danych."

> "Trzy linijki ML: `model = LinearRegression()`, `model.fit(X_train, y_train)`, `model.predict(X_test)`. To jest scikit-learn API — identyczne dla wszystkich algorytmów."

---

### 0:45-0:55 — PRZERWA

> "Dziesięć minut przerwy. Po przerwie: Plotly — wykresy które klient może klikać."

---

### 0:55-1:15 — MATERIAŁ 3: Plotly — interaktywne wykresy

> "Wracamy. Plotly. Kto widział interaktywny wykres w dashboardzie i pomyślał 'chcę to umieć robić'? Dzisiaj się nauczycie."

> "Plotly Express — wysokopoziomowy interfejs. Jedna funkcja = cały wykres z interaktywnością. Porównanie:"

**[Komórka 9 — scatter interaktywny]**

```python
import plotly.express as px

fig = px.scatter(
    klienci,
    x='srednia_wartosc',
    y='zamowienia_rok',
    color='segment',
    title='Segmentacja klientów — KMeans k=3',
    labels={
        'srednia_wartosc': 'Średnia wartość zamówienia [PLN]',
        'zamowienia_rok': 'Liczba zamówień w roku'
    },
    color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96']
)
fig.show()
```

> "Uruchomcie to. Teraz najedźcie myszą na dowolny punkt — widzicie wszystkie wartości. Kliknijcie na legendę — ukryjecie/pokażecie segment. Zaznaczcie obszar — zoom. Podwójne kliknięcie — reset widoku."

> "To HTML z JavaScript pod spodem. W Jupyter Notebook działa natywnie. Możecie też wyeksportować: `fig.write_html('wykres.html')` — plik który otwiera się w każdej przeglądarce."

**[Komórka 10 — bar chart]**

```python
srednie_segmentow = klienci.groupby('segment')[['srednia_wartosc', 'zamowienia_rok']].mean().reset_index()
srednie_segmentow['nazwa_segmentu'] = ['Okazjonalni', 'Standard', 'Premium']

fig_bar = px.bar(
    srednie_segmentow,
    x='nazwa_segmentu',
    y='srednia_wartosc',
    color='nazwa_segmentu',
    title='Średnia wartość zamówienia per segment',
    labels={'srednia_wartosc': 'Średnia wartość [PLN]', 'nazwa_segmentu': 'Segment'},
    text_auto='.0f'
)
fig_bar.update_layout(showlegend=False)
fig_bar.show()
```

> "`text_auto='.0f'` — automatyczne etykiety na słupkach, format bez miejsc dziesiętnych. Jeden parametr zamiast pętli w Matplotlib."

**[Komórka 11 — line chart z błędami]**

```python
np.random.seed(42)
miesiace = list(range(1, 13))
sprzedaz_A = [100 + i*5 + np.random.normal(0, 8) for i in miesiace]
sprzedaz_B = [80 + i*8 + np.random.normal(0, 10) for i in miesiace]

df_trend = pd.DataFrame({
    'miesiac': miesiace * 2,
    'sprzedaz': sprzedaz_A + sprzedaz_B,
    'produkt': ['Produkt A'] * 12 + ['Produkt B'] * 12
})

fig_line = px.line(
    df_trend,
    x='miesiac',
    y='sprzedaz',
    color='produkt',
    title='Trend sprzedaży 2024 — Porównanie produktów',
    labels={'miesiac': 'Miesiąc', 'sprzedaz': 'Sprzedaż [tys. PLN]'},
    markers=True
)
fig_line.show()
```

> "Hover na linii — widzicie dokładną wartość dla każdego miesiąca i każdego produktu. Zoom na wybrane miesiące. Kliknięcie na legendę — porównanie z jednym produktem."

> "W Matplotlib ten sam wykres: `plt.plot()` × 2, `plt.xlabel`, `plt.ylabel`, `plt.title`, `plt.legend`, `plt.xticks`. I wciąż nie ma interaktywności. Plotly: jeden `px.line()` z parametrami."

**[Komórka 12 — customizacja]**

```python
fig_custom = px.scatter(
    klienci,
    x='srednia_wartosc',
    y='zamowienia_rok',
    color='segment',
    size='srednia_wartosc',
    hover_data=['srednia_wartosc', 'zamowienia_rok'],
    title='Segmentacja klientów — rozmiar punktu = wartość zamówienia',
)
fig_custom.update_traces(marker=dict(opacity=0.7))
fig_custom.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white'
)
fig_custom.show()
```

> "Rozmiar punktu proporcjonalny do wartości zamówienia. Trzy wymiary danych w jednym wykresie: x, y i rozmiar. Interaktywne hovery. Taki wykres w prezentacji dla zarządu robi bardzo dobre wrażenie."

---

### 1:15-1:25 — MATERIAŁ 4: Polars — brief mention

> "Ostatni temat: Polars. Nie robimy dzisiaj żadnego kodu. Tylko wytłumaczę czym jest i kiedy po to sięgniecie."

> "Polars to biblioteka do pracy z danymi — jak Pandas. Ale napisana w Rust. Co to znaczy w praktyce?"

**[Komórka 13 — benchmark demo]**

```python
import pandas as pd
import time

# Generujemy duży DataFrame
np.random.seed(42)
n_rows = 1_000_000
df_big = pd.DataFrame({
    'id': range(n_rows),
    'wartosc': np.random.normal(1000, 200, n_rows),
    'kategoria': np.random.choice(['A', 'B', 'C'], n_rows)
})

# Pandas
start = time.time()
wynik_pandas = df_big.groupby('kategoria')['wartosc'].mean()
czas_pandas = time.time() - start
print(f"Pandas: {czas_pandas:.3f}s")

# Polars (jeśli zainstalowany)
try:
    import polars as pl
    df_polars = pl.from_pandas(df_big)
    start = time.time()
    wynik_polars = df_polars.group_by('kategoria').agg(pl.col('wartosc').mean())
    czas_polars = time.time() - start
    print(f"Polars: {czas_polars:.3f}s")
    print(f"Polars {czas_pandas/czas_polars:.1f}x szybszy")
except ImportError:
    print("Polars nie zainstalowany — zainstaluj: pip install polars")
    print("Na 1M wierszy Polars jest typowo 5-20x szybszy niż Pandas")
```

> "Polars jest 5-20 razy szybszy niż Pandas na dużych danych. Dla 100 tys. wierszy — różnica niezauważalna. Dla 10 milionów wierszy — Pandas może trwać minuty, Polars sekundy."

> "Kiedy użyć Polars zamiast Pandas?"

**[Wyświetl tabelę]**

| Sytuacja | Wybór |
|----------|-------|
| Dane < 1M wierszy, szybkie prototypowanie | Pandas |
| Dane > 1M wierszy, przetwarzanie wsadowe | Polars |
| Praca z CSV/Parquet w pipeline'ach | Polars |
| Integracja z scikit-learn, istniejący kod | Pandas |
| Nowy projekt data engineering | Polars |

> "Składnia Polars jest podobna do Pandas ale nie identyczna. Warto znać obie. Na rynku pracy — znajomość Polars to atut, nie wymóg. Znajomość Pandas — wymóg."

> "Jeśli chcecie spróbować: `pip install polars`, a dokumentacja na polars.rs jest świetna."

---

### 1:25-1:35 — AKTYWNOŚĆ: KMeans + Plotly

> "Teraz wy. Macie 10 minut. Zadanie:"

**[Wyświetl na projektorze:]**

```
ZADANIE:
1. Wygeneruj dane 200 klientów z 4 segmentami (k=4)
   - Dane: 'wydatki_miesiac' i 'wiek'
   - Użyj np.random.seed(123)

2. Zastosuj KMeans z k=4
   - Pamiętaj o StandardScaler!

3. Stwórz scatter plot w Plotly:
   - x = wydatki_miesiac, y = wiek
   - color = segment
   - title = 'Segmentacja klientów 4 grupy'

4. Opisz jednym zdaniem każdy znaleziony segment.
```

> "Możecie korzystać z notebooka jako wzorca. Kto skończy szybciej — dodaje do scatter plotu `size='wydatki_miesiac'` i `hover_data`."

**[Po 8 minutach:]**

> "Kto chce pokazać? Jak wyglądają Wasze 4 segmenty? Jakie im daliście nazwy?"

---

### 1:35-1:45 — PODSUMOWANIE i zapowiedź W14

> "Podsumujmy co dziś zrobiliśmy."

> "scikit-learn: standardowy interfejs ML — `fit`, `predict`, `score`. KMeans do segmentacji, LinearRegression do prognozowania. StandardScaler przed K-Means i zawsze `train_test_split`. R² i RMSE to Wasza ocena modelu."

> "Plotly Express: `px.scatter`, `px.bar`, `px.line`. Jeden import, jeden call — interaktywny wykres. `fig.write_html()` żeby udostępnić. `color`, `size`, `hover_data` żeby kodować więcej informacji."

> "Polars: istnieje, jest szybszy, warto wiedzieć."

> "I najważniejsze: te narzędzia łączą się. Segmentacja KMeans → wizualizacja Plotly → raport. Pełny pipeline analityczny w 30 linijkach kodu."

> "W14 — ostatni tydzień kursu. Temat: LLM i AI API w Pythonie. Nauczycie się wywoływać GPT-4 / Claude przez Python, przetwarzać odpowiedzi, budować proste automatyzacje AI. Kto chce się przygotować — OpenAI Python SDK lub Anthropic Python SDK na PyPI."

> "Dziękuję. Laboratorium z tymi samymi narzędziami — macie do zrobienia własną segmentację i własne wykresy."

---

## Materiały do przygotowania

- [ ] Otwórz `advanced_libs_demo.ipynb` przed zajęciami
- [ ] Uruchom komórkę 1 (`%pip install`) — sprawdź czy instalacja działa
- [ ] Przetestuj wszystkie komórki od góry do dołu
- [ ] Przygotuj quiz_w13.md na Mentimeter lub do wydruku

## Typowe problemy techniczne

| Problem | Rozwiązanie |
|---------|-------------|
| `ModuleNotFoundError: sklearn` | Uruchom komórkę 1 z `%pip install scikit-learn` lub aktywuj venv i `uv pip install scikit-learn` |
| `ModuleNotFoundError: plotly` | Uruchom komórkę 1 z `%pip install plotly` |
| Wykres Plotly nie wyświetla się w Jupyter | Sprawdź wersję: `pip install "plotly>=5.0"` i `pip install nbformat` |
| KMeans labels są inne niż w przykładzie | Normalne — kolejność klastrów nie jest deterministyczna, ale zawartość jest ta sama |
| `fig.show()` otwiera przeglądarkę zamiast Jupyter | Zainstaluj: `pip install jupyter nbformat` |
