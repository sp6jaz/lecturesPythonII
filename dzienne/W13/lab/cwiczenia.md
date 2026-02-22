# L13 — Ćwiczenia: Zaawansowane biblioteki

**Programowanie w Pythonie II** | Laboratorium 13
**Czas:** 90 min | Notebook: `lab13_advanced_libs.ipynb`

---

## Przygotowanie — uruchom PRZED ćwiczeniami

Utwórz nowy notebook `lab13_advanced_libs.ipynb` i jako **pierwszą komórkę** wpisz:

```python
# Instalacja bibliotek (uruchom raz na początku)
%pip install scikit-learn plotly -q

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

print("Wszystkie biblioteki załadowane poprawnie!")
print(f"scikit-learn wersja: {__import__('sklearn').__version__}")
print(f"plotly wersja: {__import__('plotly').__version__}")
```

---

## Ćwiczenie 1: KMeans — segmentacja klientów (20 min)

**Poziom Blooma: 3 — Stosuje**

**Cel:** Osoba studiująca stosuje KMeans do podziału klientów e-commerce na segmenty i interpretuje każdy segment biznesowo.

### Kontekst
Jesteś analitykiem danych w firmie e-commerce. Masz dane 300 klientów: średnią wartość zamówienia (PLN) i liczbę zamówień w roku. Chcesz podzielić ich na 3 segmenty, żeby móc kierować do nich różne kampanie marketingowe.

### Krok 1 — Generowanie danych

```python
np.random.seed(42)

klienci = pd.DataFrame({
    'srednia_wartosc': np.concatenate([
        np.random.normal(400, 60, 100),    # segment 0
        np.random.normal(1100, 120, 100),  # segment 1
        np.random.normal(2400, 180, 100)   # segment 2
    ]),
    'zamowienia_rok': np.concatenate([
        np.random.normal(2, 0.5, 100),
        np.random.normal(7, 1.2, 100),
        np.random.normal(18, 2.5, 100)
    ])
})

# Usuń wartości ujemne (mogą wystąpić przy małych średnich)
klienci = klienci.clip(lower=0)
klienci.describe().round(2)
```

### Krok 2 — Skalowanie i klastrowanie

Uzupełnij kod:

```python
# TODO: Stwórz obiekt StandardScaler
scaler = ___

# TODO: Zastosuj fit_transform na obu kolumnach
X_scaled = ___

# TODO: Stwórz KMeans z k=3, random_state=42, n_init=10
kmeans = ___

# TODO: Dopasuj model do danych
___

# TODO: Przypisz etykiety klastrów do DataFrame
klienci['segment'] = ___

print("Rozkład klientów per segment:")
print(klienci['segment'].value_counts().sort_index())
```

### Krok 3 — Analiza segmentów

```python
# TODO: Oblicz średnie wartości per segment
srednie = klienci.groupby('segment')[['srednia_wartosc', 'zamowienia_rok']].mean().round(1)
print(srednie)
```

### Krok 4 — Wizualizacja (matplotlib na razie)

```python
fig, ax = plt.subplots(figsize=(10, 6))
kolory = {0: 'blue', 1: 'orange', 2: 'green'}
for seg in [0, 1, 2]:
    dane_seg = klienci[klienci['segment'] == seg]
    ax.scatter(dane_seg['srednia_wartosc'], dane_seg['zamowienia_rok'],
               c=kolory[seg], label=f'Segment {seg}', alpha=0.7)
ax.set_xlabel('Średnia wartość zamówienia [PLN]')
ax.set_ylabel('Liczba zamówień w roku')
ax.set_title('Segmentacja klientów — KMeans k=3')
ax.legend()
plt.tight_layout()
plt.show()
```

### Krok 5 — Interpretacja biznesowa

Na podstawie wartości średnich z Kroku 3, przypisz nazwy do segmentów:

```python
# TODO: Wpisz nazwy segmentów na podstawie wartości średnich
# Przykład: klienci 0 to 'Okazjonalni' bo...
nazwy_segmentow = {
    0: '___',  # dlaczego?
    1: '___',  # dlaczego?
    2: '___',  # dlaczego?
}
klienci['nazwa_segmentu'] = klienci['segment'].map(nazwy_segmentow)
print(klienci.groupby('nazwa_segmentu')[['srednia_wartosc', 'zamowienia_rok']].mean().round(1))
```

### Pytania do przemyślenia
1. Dlaczego używamy `StandardScaler` przed KMeans? Co by się stało bez skalowania?
2. Jak dobierasz liczbę klastrów k? Co to jest metoda łokcia (elbow method)?
3. Który segment warto obsłużyć priorytetowo z perspektywy biznesowej?

---

## Ćwiczenie 2: Regresja liniowa — prognoza sprzedaży (20 min)

**Poziom Blooma: 4 — Projektuje**

**Cel:** Osoba studiująca projektuje pipeline regresji liniowej do przewidywania sprzedaży na podstawie wydatków reklamowych i ocenia jakość modelu.

### Kontekst
Masz dane z 200 regionów sprzedaży. Dla każdego regionu znasz wydatki na reklamę TV i radio (w tys. PLN) oraz osiągniętą sprzedaż. Chcesz zbudować model, który przewidzi sprzedaż na podstawie budżetu reklamowego.

### Krok 1 — Generowanie danych

```python
np.random.seed(42)
n = 200

reklama_tv = np.random.uniform(10, 300, n)
reklama_radio = np.random.uniform(5, 50, n)
szum = np.random.normal(0, 1.5, n)

# Prawdziwa zależność: sprzedaz = 5 + 0.05*tv + 0.12*radio + szum
sprzedaz = 5 + 0.05 * reklama_tv + 0.12 * reklama_radio + szum

df_reklama = pd.DataFrame({
    'tv': reklama_tv,
    'radio': reklama_radio,
    'sprzedaz': sprzedaz
})

print(df_reklama.describe().round(2))
```

### Krok 2 — Podział na zbiory treningowy i testowy

```python
X = df_reklama[['tv', 'radio']]
y = df_reklama['sprzedaz']

# TODO: Podziel dane na train/test
# test_size=0.2, random_state=42
X_train, X_test, y_train, y_test = ___

print(f"Zbiór treningowy: {len(X_train)} próbek")
print(f"Zbiór testowy: {len(X_test)} próbek")
```

### Krok 3 — Trening modelu

```python
# TODO: Stwórz model LinearRegression
model = ___

# TODO: Wytrenuj model na danych treningowych
___

print(f"Intercept (wyraz wolny): {model.intercept_:.3f}")
print(f"Współczynnik TV: {model.coef_[0]:.4f}  (prawdziwy: 0.05)")
print(f"Współczynnik Radio: {model.coef_[1]:.4f}  (prawdziwy: 0.12)")
```

Czy współczynniki są zbliżone do prawdziwych wartości (0.05 i 0.12)?

### Krok 4 — Ocena modelu

```python
# TODO: Wykonaj predykcje na zbiorze testowym
y_pred = ___

# TODO: Oblicz R² i RMSE
r2 = ___
rmse = ___

print(f"R² = {r2:.4f}")
print(f"RMSE = {rmse:.4f}")
```

### Krok 5 — Wykres predykcji vs rzeczywistość

```python
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolors='black', linewidths=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         'r--', lw=2, label='Idealna predykcja')
plt.xlabel('Sprzedaż rzeczywista')
plt.ylabel('Sprzedaż przewidywana')
plt.title(f'Regresja liniowa — predykcja vs rzeczywistość\nR²={r2:.3f}, RMSE={rmse:.3f}')
plt.legend()
plt.tight_layout()
plt.show()
```

### Krok 6 — Predykcja dla nowych danych

```python
# TODO: Przewidź sprzedaż dla budżetu TV=200 tys, Radio=30 tys
nowe_dane = pd.DataFrame({'tv': [200], 'radio': [30]})
prognoza = ___

print(f"Prognoza sprzedaży dla TV=200, Radio=30: {prognoza[0]:.1f} tys. PLN")
# Sprawdzenie ręczne: 5 + 0.05*200 + 0.12*30 = ?
```

### Pytania do przemyślenia
1. Co oznacza R² = 0.97? Ile procent zmienności sprzedaży wyjaśnia nasz model?
2. Jak interpretujesz RMSE w kontekście prognozowania sprzedaży?
3. Dlaczego NIE stosujemy `fit_transform` na X_test? Co by się stało gdybyśmy tak zrobili?

---

## Ćwiczenie 3: Plotly — interaktywny dashboard (30 min)

**Poziom Blooma: 5 — Tworzy**

**Cel:** Osoba studiująca tworzy interaktywny dashboard Plotly z trzema wykresami prezentującymi wyniki segmentacji i trendów sprzedaży.

**Uwaga:** To ćwiczenie korzysta z danych z Ćwiczenia 1 (`klienci` z kolumną `nazwa_segmentu`).

### Krok 1 — Interaktywny scatter plot segmentacji

```python
# TODO: Stwórz interaktywny scatter plot
# x='srednia_wartosc', y='zamowienia_rok'
# color='nazwa_segmentu'
# size='srednia_wartosc' (rozmiar punktu proporcjonalny do wartości)
# title='Segmentacja klientów — KMeans k=3'
# Ustaw odpowiednie labels

fig_scatter = px.scatter(
    klienci,
    x=___,
    y=___,
    color=___,
    size=___,
    title=___,
    labels={
        'srednia_wartosc': ___,
        'zamowienia_rok': ___,
        'nazwa_segmentu': 'Segment'
    },
    hover_data=['srednia_wartosc', 'zamowienia_rok']
)
fig_scatter.show()
```

Sprawdź interaktywność:
- Najedź myszą na punkt — czy widzisz wszystkie wartości?
- Kliknij na segment w legendzie — czy ukrywa/pokazuje punkty?
- Zaznacz obszar — czy zoom działa?

### Krok 2 — Bar chart: średnie wartości per segment

```python
# Przygotowanie danych
srednie_seg = (klienci.groupby('nazwa_segmentu')
               [['srednia_wartosc', 'zamowienia_rok']]
               .mean()
               .reset_index()
               .round(1))

# TODO: Stwórz bar chart
# x='nazwa_segmentu', y='srednia_wartosc'
# color='nazwa_segmentu'
# title='Średnia wartość zamówienia per segment'
# text_auto=':.0f' (etykiety na słupkach)

fig_bar = ___
fig_bar.update_layout(showlegend=False)
fig_bar.show()
```

### Krok 3 — Line chart: trend sprzedaży miesięcznej

```python
# Generuj dane trendu
np.random.seed(42)
miesiace = list(range(1, 13))
nazwy_miesiecy = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze',
                  'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']

sprzedaz_2023 = [80 + i*4 + np.random.normal(0, 5) for i in miesiace]
sprzedaz_2024 = [100 + i*6 + np.random.normal(0, 7) for i in miesiace]

df_trend = pd.DataFrame({
    'miesiac': nazwy_miesiecy * 2,
    'sprzedaz': sprzedaz_2023 + sprzedaz_2024,
    'rok': ['2023'] * 12 + ['2024'] * 12
})

# TODO: Stwórz line chart
# x='miesiac', y='sprzedaz'
# color='rok'
# markers=True
# title='Trend sprzedaży 2023 vs 2024'

fig_line = ___
fig_line.show()
```

### Krok 4 — Wielopanelowy dashboard (rozszerzenie)

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Tworzenie siatki 2x2 wykresów
fig_dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=[
        'Segmentacja klientów',
        'Średnie wartości per segment',
        'Trend sprzedaży',
        'Rozkład wartości zamówień'
    ]
)

# Panel 1: Scatter segmentacji
for seg_name in klienci['nazwa_segmentu'].unique():
    dane_seg = klienci[klienci['nazwa_segmentu'] == seg_name]
    fig_dashboard.add_trace(
        go.Scatter(
            x=dane_seg['srednia_wartosc'],
            y=dane_seg['zamowienia_rok'],
            mode='markers',
            name=seg_name,
            marker=dict(opacity=0.7)
        ),
        row=1, col=1
    )

# Panel 2: Bar chart
fig_dashboard.add_trace(
    go.Bar(
        x=srednie_seg['nazwa_segmentu'],
        y=srednie_seg['srednia_wartosc'],
        showlegend=False,
        marker_color=['#636EFA', '#EF553B', '#00CC96']
    ),
    row=1, col=2
)

# Panel 3: Line chart trendu
for rok_val in ['2023', '2024']:
    dane_rok = df_trend[df_trend['rok'] == rok_val]
    fig_dashboard.add_trace(
        go.Scatter(
            x=dane_rok['miesiac'],
            y=dane_rok['sprzedaz'],
            mode='lines+markers',
            name=f'Sprzedaż {rok_val}',
            showlegend=False
        ),
        row=2, col=1
    )

# Panel 4: Histogram wartości zamówień
fig_dashboard.add_trace(
    go.Histogram(
        x=klienci['srednia_wartosc'],
        nbinsx=30,
        showlegend=False,
        marker_color='#AB63FA',
        opacity=0.8
    ),
    row=2, col=2
)

fig_dashboard.update_layout(
    height=800,
    title_text='Dashboard Analityczny — Segmentacja Klientów 2024',
    title_font_size=16
)
fig_dashboard.show()

# Eksport do HTML
fig_dashboard.write_html('dashboard_klienci.html')
print("Dashboard zapisany jako dashboard_klienci.html")
```

### Pytania do przemyślenia
1. Jakie są różnice między `plotly.express` (px) a `plotly.graph_objects` (go)?
2. Kiedy użyłbyś wielopanelowego dashboardu zamiast oddzielnych wykresów?
3. `fig.write_html()` zapisuje plik HTML — co możesz z nim zrobić? Komu możesz go wysłać?

---

## Ćwiczenie 4: Mini-projekt — segmentacja + wizualizacja + commit (15 min)

**Poziom Blooma: 5 — Tworzy**

**Cel:** Osoba studiująca integruje KMeans i Plotly w samodzielny mini-projekt analityczny i zatwierdza pracę przez git commit.

### Zadanie

Masz swobodę w doborze danych i parametrów. Wymagania:

**Wymaganie minimalne (10 pkt):**
1. Wygeneruj nowy zbiór danych klientów z `np.random.seed(123)` i k=4 segmentami
   - Dwie cechy do wyboru: np. `wiek` (18-70 lat) i `wydatki_miesiac` (PLN)
2. Zastosuj KMeans z k=4 (pamiętaj o StandardScaler)
3. Stwórz scatter plot Plotly z `color='segment'`
4. Opisz każdy segment jednym zdaniem w komentarzu

**Wymaganie rozszerzone (+ 5 pkt):**
5. Dodaj `size='wydatki_miesiac'` do scatter plotu
6. Stwórz bar chart pokazujący liczebność każdego segmentu (`klienci['segment'].value_counts()`)
7. Wyeksportuj jeden wykres jako HTML: `fig.write_html('segmentacja_4_klastry.html')`

### Commit

Po zakończeniu:

```bash
cd ~/python2_projekt
git add lab13_advanced_libs.ipynb
# Jeśli zapisałeś HTML:
git add segmentacja_4_klastry.html
git add dashboard_klienci.html
git commit -m "L13: KMeans segmentacja + Plotly dashboard"
git log --oneline -3
```

### Szablon do wypełnienia

```python
# ============================================================
# MINI-PROJEKT: Segmentacja klientów z wizualizacją Plotly
# Imię i nazwisko: [TWOJE DANE]
# Data: 2025-01-XX
# ============================================================

np.random.seed(123)
n = 200

# TODO: Wygeneruj dane z 4 segmentami
# Sugestia: wiek (18-70) i wydatki_miesiac (100-5000 PLN)
# Każdy segment powinien mieć inny zakres wartości

klienci_mp = pd.DataFrame({
    'wiek': ___,
    'wydatki_miesiac': ___
})

# TODO: StandardScaler + KMeans(k=4, random_state=42)
scaler_mp = ___
X_mp = ___
kmeans_mp = ___
___
klienci_mp['segment'] = ___

# TODO: Analiza — średnie per segment
print("Charakterystyka segmentów:")
print(___)

# TODO: Scatter plot Plotly
fig_mp = px.scatter(
    ___
)
fig_mp.show()

# TODO: Opisz segmenty
"""
Segment 0: [opis]
Segment 1: [opis]
Segment 2: [opis]
Segment 3: [opis]

Rekomendacja marketingowa:
- Dla segmentu 0: [propozycja]
- Dla segmentu 1: [propozycja]
"""
```

---

## Podsumowanie zajęć

Co zrobiłeś na tych laboratoriach:
- KMeans clustering z StandardScaler — segmentacja bez etykiet (unsupervised)
- Pipeline regresji: `fit` → `predict` → `r2_score` + `mean_squared_error`
- Plotly Express: `px.scatter`, `px.bar`, `px.line` z pełną interaktywnością
- Dashboard wielopanelowy z `make_subplots` i `graph_objects`
- Commit wyników do git

Następne laboratoria (L14): LLM i AI API — wywołania GPT-4/Claude przez Python, automatyzacja tekstu.
