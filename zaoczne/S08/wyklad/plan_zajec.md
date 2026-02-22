# S08 Wykład — Plan zajęć dla prowadzącego

## Temat: Zaawansowane biblioteki — scikit-learn, Plotly, Polars

### Informacje organizacyjne
- **Czas:** 90 min (1. blok spotkania 8)
- **Forma:** wykład konwersatoryjny z live coding
- **Tryb:** zaoczny — prowadzący prowadzi wykład + laboratorium (ta sama osoba)
- **Potrzebne:** komputer z projektorem, VS Code, venv z scikit-learn/plotly zainstalowanymi
- **Przed wykładem:** otwórz notebook demo, uruchom `%pip install scikit-learn plotly -q`
- **Kluczowe hasło:** "Opanowaliście Pandas, Matplotlib i statystykę. Dzisiaj wchodzimy na kolejny poziom — ML, interaktywne wykresy i szybsze DataFrames."

### WAŻNE — zależności
- **scikit-learn** i **plotly** NIE są w domyślnym venv kursu — pierwsza komórka notebooka instaluje je automatycznie
- Jeśli jest problem z instalacją: `source .venv/bin/activate && uv pip install scikit-learn plotly`
- Weryfikacja: `python -c "import sklearn; import plotly; print('OK')"`

### Kontekst zaoczny
- Studenci mają za sobą S03-S07: Pandas (selekcja, filtrowanie, czyszczenie, łączenie, agregacja), Matplotlib, Seaborn, statystykę opisową i testy hipotez
- Tempo wyższe niż dzienne — mniej czasu na dygresje, więcej na konkrety
- Po 90 min wykładu jest przerwa, a potem 90 min laboratorium — można zapowiadać co będą robić na labie

### Efekty uczenia się (Bloom poziom 3-5)
Po tym wykładzie osoba studiująca:
1. **Stosuje** `train_test_split` i `StandardScaler` do przygotowania danych pod model ML (Bloom 3)
2. **Stosuje** `KMeans` do segmentacji klientów i interpretuje klastry jako decyzje biznesowe (Bloom 3)
3. **Projektuje** pipeline regresji liniowej w scikit-learn: fit, predict, ocena R² i RMSE (Bloom 4)
4. **Tworzy** interaktywne wykresy Plotly Express (scatter, bar, line z hover) i osadza je w notebooku (Bloom 5)
5. **Ocenia** kiedy użyć Polars zamiast Pandas na podstawie rozmiaru danych i wymagań wydajnościowych (Bloom 5)

### Plan minutowy

| Czas | Etap | Co robisz | Jak |
|------|------|-----------|-----|
| 0:00-0:05 | **WPROWADZENIE** | "Opanowaliście fundament. Teraz trzy narzędzia z kolejnego poziomu" | Rozmowa |
| 0:05-0:25 | **MATERIAŁ 1** | scikit-learn: StandardScaler, KMeans — segmentacja klientów | Live coding |
| 0:25-0:42 | **MATERIAŁ 2** | scikit-learn: train_test_split, LinearRegression, R², RMSE | Live coding |
| 0:42-0:50 | **PRZERWA** | 8 minut | — |
| 0:50-1:10 | **MATERIAŁ 3** | Plotly Express: px.scatter, px.bar, px.line — hover, color, size | Live coding |
| 1:10-1:20 | **MATERIAŁ 4** | Polars: benchmark vs Pandas, kiedy użyć, składnia | Slajd + demo |
| 1:20-1:30 | **PODSUMOWANIE** | Co dalej, zapowiedź laba (segmentacja + Plotly) | Rozmowa |

---

## STENOGRAM — co mówić i robić

### 0:00-0:05 — WPROWADZENIE

> "Dzień dobry. Spotkanie 8 — dzisiaj robimy trzy rzeczy, które na ofertach pracy dla analityków pojawiają się praktycznie zawsze: scikit-learn, Plotly i krótko o Polars."

> "Przez siedem spotkań budowaliśmy fundament. Pandas, Matplotlib, Seaborn, statystyka. To są podstawowe narzędzia pracy z danymi. Ale jeśli otworzycie dowolną ofertę Data Analyst lub Data Scientist, zobaczycie tam jeszcze jedno słowo: machine learning. I interaktywne dashboardy."

> "Dziś nie będziemy teoretyzować o sieciach neuronowych. Pokażę Wam dwa konkretne algorytmy, które można użyć w pracy w poniedziałek: segmentację klientów (KMeans) i prognozowanie sprzedaży (regresja liniowa). Plus wykresy, które klient może klikać — Plotly."

> "Po wykładzie na labie sami to zbudujecie. Zaczynamy."

---

### 0:05-0:25 — MATERIAŁ 1: scikit-learn — KMeans clustering

> "scikit-learn to najważniejsza biblioteka ML w Pythonie. Ponad 15 lat rozwoju, miliony użytkowników, standardowy interfejs. Każdy algorytm działa tak samo: stwórz obiekt, `fit`, `predict`. Trzy linijki."

> "Pierwszy problem: segmentacja klientów. Wyobraźcie sobie: pracujecie w e-commerce, macie bazę 300 klientów. Dla każdego znacie średnią wartość zamówienia i liczbę zamówień w roku. Pytanie od szefa: 'Podziel mi tych klientów na grupy, chcę wysyłać im różne kampanie marketingowe.'"

> "Nie macie etykiet — nikt nie powiedział Wam które klasy istnieją. To jest uczenie nienadzorowane — unsupervised learning. K-Means to odkryje za Was."

**[Komórka — generowanie danych i import]**

```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n = 300
klienci = pd.DataFrame({
    'srednia_wartosc': np.concatenate([
        np.random.normal(500, 80, 100),   # okazjonalni
        np.random.normal(1200, 150, 100), # standard
        np.random.normal(2500, 200, 100)  # premium
    ]),
    'zamowienia_rok': np.concatenate([
        np.random.normal(2, 0.5, 100),
        np.random.normal(8, 1.5, 100),
        np.random.normal(20, 3, 100)
    ])
})
klienci.describe().round(1)
```

> "Celowo budujemy dane z trzema skupiskami. W prawdziwych danych tego nie wiemy — ale K-Means to znajdzie."

**[StandardScaler]**

> "Zanim puścimy algorytm — musimy znormalizować dane. Dlaczego? Wartość zamówienia to setki i tysiące złotych. Liczba zamówień to 2-20. Bez normalizacji K-Means będzie zdominowany przez kolumnę z większymi liczbami."

> "`StandardScaler`: odejmuje średnią, dzieli przez odchylenie standardowe. Obie kolumny dostaną średnią 0 i odchylenie 1. Porównywalne."

```python
scaler = StandardScaler()
X = scaler.fit_transform(klienci[['srednia_wartosc', 'zamowienia_rok']])
print(f"Przed: srednia_wartosc mean={klienci['srednia_wartosc'].mean():.0f}")
print(f"Po:    X[:,0] mean={X[:,0].mean():.2f}, std={X[:,0].std():.2f}")
```

> "`fit_transform` robi dwie rzeczy naraz: `fit` oblicza średnią i odchylenie, `transform` aplikuje skalowanie. Ważna zasada: na zbiorze testowym zawsze tylko `transform`, nigdy `fit_transform` — inaczej 'zaglądacie' do danych testowych."

**[KMeans — fit i labels]**

```python
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)
klienci['segment'] = kmeans.labels_

print("Rozkład klientów:")
print(klienci['segment'].value_counts().sort_index())
print()
print("Charakterystyka segmentów:")
print(klienci.groupby('segment')[['srednia_wartosc', 'zamowienia_rok']].mean().round(0))
```

> "Trzy linijki. Tworzę model z k=3 klastrami. `fit` uczy model na danych. `labels_` — etykiety: który klient trafił do którego klastra."

> "`random_state=42` — ta sama 'losowość' za każdym razem. Reprodukowalność wyników."

> "Patrzcie na średnie. Jeden klaster ma niskie wartości i rzadkie zakupy — to klienci okazjonalni. Inny ma wysokie wartości i częste — premium. Trzeci jest pośrodku — standard. To jest gotowy wynik biznesowy: trzy grupy, trzy różne kampanie marketingowe."

**[Wizualizacja Matplotlib — szybki rzut oka]**

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 6))
for seg in sorted(klienci['segment'].unique()):
    dane = klienci[klienci['segment'] == seg]
    ax.scatter(dane['srednia_wartosc'], dane['zamowienia_rok'],
               alpha=0.6, label=f'Segment {seg}')
ax.set_xlabel('Srednia wartosc zamowienia [PLN]')
ax.set_ylabel('Zamowienia / rok')
ax.set_title('Segmentacja klientow — KMeans k=3')
ax.legend()
plt.tight_layout()
plt.show()
```

> "Trzy wyraźne grupy. Za chwilę ten sam wykres zrobimy w Plotly i zobaczycie różnicę."

---

### 0:25-0:42 — MATERIAŁ 2: scikit-learn — regresja liniowa

> "Drugi algorytm: regresja liniowa. Tym razem supervised learning — mamy zmienną celu, chcemy ją przewidywać."

> "Przypadek biznesowy: masz dane o wydatkach reklamowych (TV i radio) i sprzedaży w 200 regionach. Pytanie: 'Jeśli zwiększę budżet na TV o 10 tysięcy, to ile zyskam na sprzedaży?'"

**[Generowanie danych]**

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

> "Celowo budujemy dane z prawdziwą zależnością: TV ma wpływ 0.05, radio 0.10. Model powinien to 'odkryć' z samych danych."

**[train_test_split]**

```python
X = df_reklama[['tv', 'radio']]
y = df_reklama['sprzedaz']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Trening: {len(X_train)} probek, Test: {len(X_test)} probek")
```

> "80/20 — standardowy podział. Model uczy się na 160 próbkach, potem piszemy mu 'sprawdzian' na 40 próbkach, których nie widział. Uczciwa ocena."

**[Trening i ocena]**

```python
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R²  = {r2:.4f}")
print(f"RMSE = {rmse:.4f}")
print(f"Wspolczynniki: TV={model.coef_[0]:.4f}, Radio={model.coef_[1]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
```

> "R² — współczynnik determinacji. Ile procent zmienności sprzedaży wyjaśnia nasz model? R²=0.95 oznacza: 95%. To bardzo dużo."

> "RMSE — Root Mean Squared Error. Średni błąd predykcji w jednostkach zmiennej celu. Jeśli RMSE wynosi 2.1, to nasze prognozy błądzą średnio o 2.1 jednostki sprzedaży."

> "Współczynniki — model odtworzył prawdziwą zależność: TV wyszło blisko 0.05, radio blisko 0.10. Intercept blisko 5. Model działa."

> "Zwróćcie uwagę na API. Trzy linijki: `model = LinearRegression()`, `model.fit(X_train, y_train)`, `model.predict(X_test)`. Identyczny interfejs dla każdego algorytmu w scikit-learn — `fit`, `predict`, `score`. Zmieniacie algorytm, nie zmieniacie kodu."

---

### 0:42-0:50 — PRZERWA

> "Osiem minut przerwy. Po przerwie: Plotly — wykresy interaktywne."

---

### 0:50-1:10 — MATERIAŁ 3: Plotly Express — interaktywne wykresy

> "Wracamy. Plotly. Znacie Matplotlib — działa świetnie do raportów PDF, do publikacji naukowych. Ale jeśli robicie prezentację dla zarządu albo dashboard w przeglądarce, potrzebujecie czegoś, co klient może klikać."

> "Plotly Express — jeden import, jedna funkcja, pełna interaktywność. Porównajmy."

**[px.scatter — segmentacja interaktywna]**

```python
import plotly.express as px

fig = px.scatter(
    klienci,
    x='srednia_wartosc',
    y='zamowienia_rok',
    color='segment',
    title='Segmentacja klientow — KMeans k=3',
    labels={
        'srednia_wartosc': 'Srednia wartosc zamowienia [PLN]',
        'zamowienia_rok': 'Liczba zamowien w roku'
    },
    color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96']
)
fig.show()
```

> "Uruchomcie to u siebie. Najedźcie myszą na punkt — widzicie wszystkie wartości. Kliknijcie na legendę — ukrywacie/pokazujecie segment. Zaznaczcie prostokąt — zoom. Podwójne kliknięcie — reset."

> "Ten sam wykres co przed chwilą w Matplotlib — ale teraz jest interaktywny. HTML z JavaScriptem pod spodem. W Jupyter działa natywnie."

> "I jeszcze jedno: `fig.write_html('wykres.html')` — plik HTML który otworzy się w każdej przeglądarce. Możecie wysłać klientowi. Nie musi mieć Pythona."

**[px.bar — porównanie segmentów]**

```python
srednie_seg = klienci.groupby('segment')[['srednia_wartosc', 'zamowienia_rok']].mean().reset_index()
srednie_seg['nazwa'] = ['Okazjonalni', 'Standard', 'Premium']

fig_bar = px.bar(
    srednie_seg,
    x='nazwa',
    y='srednia_wartosc',
    color='nazwa',
    title='Srednia wartosc zamowienia per segment',
    labels={'srednia_wartosc': 'Srednia wartosc [PLN]', 'nazwa': 'Segment'},
    text_auto='.0f'
)
fig_bar.update_layout(showlegend=False)
fig_bar.show()
```

> "`text_auto='.0f'` — automatyczne etykiety na słupkach. Jeden parametr zamiast pętli `ax.text()` w Matplotlib."

**[px.line — trend]**

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
    x='miesiac', y='sprzedaz', color='produkt',
    title='Trend sprzedazy 2024 — Porownanie produktow',
    labels={'miesiac': 'Miesiac', 'sprzedaz': 'Sprzedaz [tys. PLN]'},
    markers=True
)
fig_line.show()
```

> "Hover na linii — wartość dla każdego miesiąca i produktu. Kliknięcie na legendę — porównanie z jednym produktem. W Matplotlib: `plt.plot()` razy dwa, `xlabel`, `ylabel`, `title`, `legend`, `xticks`. I zero interaktywności."

**[Plotly vs Matplotlib — tabelka]**

> "Kiedy co?"

| Cecha | Matplotlib | Plotly |
|-------|-----------|--------|
| Statyczne wykresy, PDF, publikacje | **TAK** | nie |
| Interaktywność, hover, zoom | nie | **TAK** |
| Dashboardy w przeglądarce | nie | **TAK** |
| Customizacja detali (fonty, tiksy) | **TAK** | ograniczona |
| Eksport do PNG/PDF | **TAK** | wymaga kaleido |
| Eksport do HTML | nie | **TAK** |
| Wymagane zależności | minimalne | JavaScript engine |

> "Krótko: raporty statyczne — Matplotlib. Prezentacje interaktywne — Plotly. W praktyce używacie obu. Matplotlib do eksploracji, Plotly do prezentacji."

**[Scatter z size — 3 wymiary informacji]**

```python
fig_custom = px.scatter(
    klienci,
    x='srednia_wartosc',
    y='zamowienia_rok',
    color='segment',
    size='srednia_wartosc',
    hover_data=['srednia_wartosc', 'zamowienia_rok'],
    title='Segmentacja klientow — rozmiar punktu = wartosc zamowienia',
)
fig_custom.update_traces(marker=dict(opacity=0.7))
fig_custom.update_layout(plot_bgcolor='white', paper_bgcolor='white')
fig_custom.show()
```

> "Trzy wymiary informacji w jednym wykresie: x, y i rozmiar punktu. Plus kolor na segment. Taki wykres w prezentacji dla zarządu robi bardzo dobre wrażenie."

---

### 1:10-1:20 — MATERIAŁ 4: Polars — brief mention

> "Ostatni temat, krótko: Polars. Nie będziemy dzisiaj pisać w nim kodu. Chcę żebyście wiedzieli że istnieje i kiedy po to sięgnąć."

> "Polars to biblioteka do pracy z danymi, jak Pandas. Ale napisana w Rust. Co to znaczy w praktyce? Jest znacznie szybsza."

**[Benchmark]**

```python
import time

np.random.seed(42)
n_rows = 1_000_000
df_big = pd.DataFrame({
    'id': range(n_rows),
    'wartosc': np.random.normal(1000, 200, n_rows),
    'kategoria': np.random.choice(['A', 'B', 'C'], n_rows)
})

start = time.time()
wynik_pandas = df_big.groupby('kategoria')['wartosc'].mean()
czas_pandas = time.time() - start
print(f"Pandas: {czas_pandas:.3f}s")

try:
    import polars as pl
    df_polars = pl.from_pandas(df_big)
    start = time.time()
    wynik_polars = df_polars.group_by('kategoria').agg(pl.col('wartosc').mean())
    czas_polars = time.time() - start
    print(f"Polars: {czas_polars:.3f}s")
    print(f"Polars {czas_pandas/czas_polars:.1f}x szybszy")
except ImportError:
    print("Polars nie zainstalowany — pip install polars")
    print("Na 1M wierszy Polars jest typowo 5-20x szybszy")
```

> "Kiedy użyć Polars?"

| Sytuacja | Wybór |
|----------|-------|
| Dane < 1M wierszy, szybki prototyp | Pandas |
| Dane > 1M wierszy, przetwarzanie wsadowe | Polars |
| Praca z CSV/Parquet w pipeline'ach | Polars |
| Integracja z scikit-learn, istniejący kod | Pandas |
| Nowy projekt data engineering | Polars |

> "Polars ma inną składnię niż Pandas — nie identyczną, ale podobną. Zamiast `df['kolumna']` mamy `pl.col('kolumna')`. Zamiast `groupby` mamy `group_by`. Zamiast `apply` mamy wyrażenia."

> "Na rynku pracy: znajomość Polars to atut, nie wymóg. Znajomość Pandas — wymóg. Ale warto wiedzieć że Polars istnieje, bo coraz więcej firm przechodzi na Polars dla dużych danych."

> "Dokumentacja: polars.rs — bardzo dobra, z wieloma przykładami."

---

### 1:20-1:30 — PODSUMOWANIE i zapowiedź laba

> "Podsumujmy."

> "Trzy nowe narzędzia dzisiaj:"

> "Pierwsze — scikit-learn. Standardowy interfejs: `fit`, `predict`, `score`. KMeans do segmentacji bez etykiet. LinearRegression do prognozowania wartości liczbowej. StandardScaler przed klastrowaniem. `train_test_split` przed regresją. R² i RMSE do oceny modelu."

> "Drugie — Plotly Express. `px.scatter`, `px.bar`, `px.line`. Jedna funkcja, jeden call — interaktywny wykres z hover, zoom, legendą. `color` i `size` kodują dodatkowe informacje. `fig.write_html()` eksportuje do pliku, który otworzy się w każdej przeglądarce."

> "Trzecie — Polars. Szybszy Pandas. Na duże dane (powyżej miliona wierszy). Warto znać że istnieje."

> "Najważniejsze: te narzędzia się łączą. Segmentacja KMeans plus wizualizacja Plotly plus eksport HTML to pełny pipeline analityczny w 30 linijkach kodu."

> "Za chwilę na labie zrobicie to sami: segmentację klientów, regresję liniową, interaktywne wykresy Plotly, i na koniec mini-projekt z commitem do gita."

---

## Materiały do przygotowania

- [ ] Zainstaluj scikit-learn i plotly w venv przed zajęciami
- [ ] Otwórz notebook demo, przetestuj od góry do dołu
- [ ] Przygotuj ewentualny backup (gotowe rozwiązania ćwiczeń na wypadek wolniejszych studentów)

## Typowe problemy techniczne

| Problem | Rozwiązanie |
|---------|-------------|
| `ModuleNotFoundError: sklearn` | `%pip install scikit-learn` w notebooku lub `uv pip install scikit-learn` w terminalu |
| `ModuleNotFoundError: plotly` | `%pip install plotly` w notebooku lub `uv pip install plotly` w terminalu |
| Wykres Plotly nie wyświetla się w Jupyter | Sprawdź: `pip install "plotly>=5.0" nbformat`, zrestartuj kernel |
| KMeans labels inne niż w przykładzie | Normalne — kolejność klastrów nie jest deterministyczna, ale zawartość jest ta sama |
| `fig.show()` otwiera przeglądarkę zamiast Jupyter | Zainstaluj: `pip install jupyter nbformat`, zrestartuj kernel |
| R² ujemne | Model gorszy niż baseline — sprawdź czy nie zamieniłeś X i y |
