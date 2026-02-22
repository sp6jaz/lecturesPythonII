# S08 — Ćwiczenia laboratoryjne: scikit-learn, Plotly, mini-projekt

**Programowanie w Pythonie II** | Spotkanie 8 (zaoczne) — Laboratorium
**Czas:** 90 min | Notebook: `s08_advanced_libs.ipynb`

---

## Przydatne materiały

| Temat | Link |
|-------|------|
| scikit-learn — Getting Started | https://scikit-learn.org/stable/getting_started.html |
| scikit-learn — KMeans | https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html |
| scikit-learn — LinearRegression | https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html |
| Plotly — Python Quick Start | https://plotly.com/python/getting-started/ |
| Plotly — Scatter plots | https://plotly.com/python/line-and-scatter/ |

---

## Przygotowanie — uruchom PRZED ćwiczeniami

Utwórz nowy notebook `s08_advanced_libs.ipynb` i jako **pierwszą komórkę** wpisz:

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

print("Wszystkie biblioteki zaladowane!")
print(f"scikit-learn: {__import__('sklearn').__version__}")
print(f"plotly: {__import__('plotly').__version__}")
```

**Sprawdzenie:** Powinien się wyświetlić komunikat z wersjami obu bibliotek. Jeśli jest błąd, uruchom w terminalu: `uv pip install scikit-learn plotly`

---

## Ćwiczenie 1: KMeans — segmentacja klientów (25 min)

**Poziom Blooma: 3 — Stosuje**

**Cel:** Osoba studiująca stosuje KMeans do podziału klientów e-commerce na 3 segmenty i interpretuje każdy segment biznesowo.

### Kontekst
Jesteś analitykiem danych w firmie e-commerce. Masz dane 300 klientów: średnią wartość zamówienia (PLN) i liczbę zamówień w roku. Szef chce podzielić klientów na segmenty i kierować do nich różne kampanie marketingowe.

### Krok 1 — Generowanie danych

```python
np.random.seed(42)

klienci = pd.DataFrame({
    'srednia_wartosc': np.concatenate([
        np.random.normal(400, 60, 100),    # segment okazjonalny
        np.random.normal(1100, 120, 100),  # segment standardowy
        np.random.normal(2400, 180, 100)   # segment premium
    ]),
    'zamowienia_rok': np.concatenate([
        np.random.normal(2, 0.5, 100),
        np.random.normal(7, 1.2, 100),
        np.random.normal(18, 2.5, 100)
    ])
})

# Usuń wartości ujemne
klienci = klienci.clip(lower=0)
print(f"Liczba klientow: {len(klienci)}")
klienci.describe().round(1)
```

### Krok 2 — Skalowanie danych

Uzupełnij brakujące fragmenty kodu:

```python
# Stwórz obiekt StandardScaler
scaler = ___

# Zastosuj fit_transform na obu kolumnach
X_scaled = scaler.fit_transform(klienci[['srednia_wartosc', 'zamowienia_rok']])

# Sprawdź że skalowanie zadziałało
print(f"Srednia po skalowaniu: {X_scaled.mean(axis=0).round(4)}")
print(f"Std po skalowaniu:     {X_scaled.std(axis=0).round(4)}")
```

**Sprawdzenie:** Srednia powinna byc bliska [0, 0], a odchylenie blisko [1, 1].

### Krok 3 — KMeans clustering

```python
# Stwórz KMeans z k=3, random_state=42, n_init=10
kmeans = ___

# Dopasuj model do danych
kmeans.fit(___)

# Przypisz etykiety klastrów do DataFrame
klienci['segment'] = ___

# Wyświetl rozkład
print("Rozklad klientow per segment:")
print(klienci['segment'].value_counts().sort_index())
```

**Sprawdzenie:** Każdy segment powinien mieć w okolicach 100 klientów (bo dane generowaliśmy po 100 na grupę).

### Krok 4 — Analiza i interpretacja segmentów

```python
# Oblicz średnie per segment
srednie = klienci.groupby('segment')[['srednia_wartosc', 'zamowienia_rok']].mean().round(1)
print("Charakterystyka segmentow:")
print(srednie)
```

Na podstawie wyników uzupełnij:

```python
# Nadaj nazwy segmentom na podstawie wartości średnich
# Segment z najniższymi wartościami to "Okazjonalni"
# Segment ze średnimi wartościami to "Standardowi"
# Segment z najwyższymi wartościami to "Premium"

nazwy = {
    ___: 'Okazjonalni',   # segment z najnizsza srednia_wartosc
    ___: 'Standardowi',   # segment ze srednia srednia_wartosc
    ___: 'Premium',       # segment z najwyzsza srednia_wartosc
}
klienci['nazwa_segmentu'] = klienci['segment'].map(nazwy)

print("\nSegmenty z nazwami:")
print(klienci.groupby('nazwa_segmentu')[['srednia_wartosc', 'zamowienia_rok']].mean().round(1))
```

### Krok 5 — Wizualizacja (Matplotlib)

```python
fig, ax = plt.subplots(figsize=(9, 6))
kolory = {0: 'blue', 1: 'orange', 2: 'green'}
for seg in sorted(klienci['segment'].unique()):
    dane = klienci[klienci['segment'] == seg]
    ax.scatter(dane['srednia_wartosc'], dane['zamowienia_rok'],
               c=kolory[seg], alpha=0.6, label=f'Segment {seg}')
ax.set_xlabel('Srednia wartosc zamowienia [PLN]')
ax.set_ylabel('Liczba zamowien w roku')
ax.set_title('Segmentacja klientow — KMeans k=3')
ax.legend()
plt.tight_layout()
plt.show()
```

**Sprawdzenie:**
- Na wykresie powinny być widoczne 3 wyraźne skupiska punktów
- Kolory powinny odpowiadać segmentom
- Segment "Okazjonalni" powinien być w lewym dolnym rogu (niska wartość, mało zamówień)
- Segment "Premium" powinien być w prawym górnym rogu (wysoka wartość, dużo zamówień)

---

## Ćwiczenie 2: Regresja liniowa — prognoza sprzedaży (20 min)

**Poziom Blooma: 4 — Projektuje**

**Cel:** Osoba studiująca projektuje pipeline regresji liniowej do przewidywania sprzedaży na podstawie wydatków reklamowych i ocenia jakość modelu.

### Kontekst
Masz dane z 200 regionów sprzedaży. Dla każdego znasz wydatki na reklamę TV i radio (tys. PLN) oraz sprzedaż. Chcesz zbudować model prognostyczny.

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

### Krok 2 — Podział train/test

```python
X = df_reklama[['tv', 'radio']]
y = df_reklama['sprzedaz']

# Podziel dane: 80% trening, 20% test, random_state=42
X_train, X_test, y_train, y_test = train_test_split(
    ___, ___, test_size=___, random_state=___
)

print(f"Zbior treningowy: {len(X_train)} probek")
print(f"Zbior testowy:    {len(X_test)} probek")
```

**Sprawdzenie:** Trening: 160 probek, Test: 40 probek.

### Krok 3 — Trening modelu

```python
# Stwórz i wytrenuj model
model = ___
model.fit(___, ___)

print(f"Intercept (wyraz wolny): {model.intercept_:.3f}")
print(f"Wspolczynnik TV:    {model.coef_[0]:.4f}  (prawdziwy: 0.0500)")
print(f"Wspolczynnik Radio: {model.coef_[1]:.4f}  (prawdziwy: 0.1200)")
```

**Sprawdzenie:** Intercept powinien byc bliski 5. Wspolczynniki powinny byc bliskie prawdziwym wartosciom.

### Krok 4 — Ocena modelu

```python
# Predykcja na zbiorze testowym
y_pred = model.predict(___)

# Oblicz metryki
r2 = r2_score(___, ___)
rmse = np.sqrt(mean_squared_error(___, ___))

print(f"R²   = {r2:.4f}")
print(f"RMSE = {rmse:.4f}")
```

**Sprawdzenie:**
- R² powinno byc >= 0.95 (dane syntetyczne z wyrazna zaleznoscia)
- RMSE powinno byc w okolicach 1.5 (zblizone do szumu)

### Krok 5 — Wykres predykcji vs rzeczywistość

```python
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolors='black', linewidths=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         'r--', lw=2, label='Idealna predykcja')
plt.xlabel('Sprzedaz rzeczywista')
plt.ylabel('Sprzedaz przewidywana')
plt.title(f'Regresja liniowa\nR²={r2:.3f}, RMSE={rmse:.3f}')
plt.legend()
plt.tight_layout()
plt.show()
```

**Sprawdzenie:** Punkty powinny lezec blisko czerwonej linii przerywanej (idealna predykcja). Im blizej — tym lepszy model.

### Krok 6 — Predykcja dla nowych danych

```python
# Przewidź sprzedaż dla: TV=200 tys, Radio=30 tys
nowe = pd.DataFrame({'tv': [200], 'radio': [30]})
prognoza = model.predict(nowe)

print(f"Prognoza sprzedazy: {prognoza[0]:.1f} tys. PLN")
# Weryfikacja reczna: 5 + 0.05*200 + 0.12*30 = 5 + 10 + 3.6 = 18.6
```

**Sprawdzenie:** Prognoza powinna byc bliska 18.6 (wartosc obliczona recznie z prawdziwych wspolczynnikow). Model daje przyblizone wspolczynniki, wiec wynik bedzie zblizona, ale nie identyczna.

---

## Ćwiczenie 3: Plotly — interaktywny scatter + bar chart (20 min)

**Poziom Blooma: 5 — Tworzy**

**Cel:** Osoba studiująca tworzy interaktywne wykresy Plotly Express prezentujące wyniki segmentacji klientów.

**Uwaga:** To ćwiczenie korzysta z DataFrame `klienci` z Ćwiczenia 1 (z kolumnami `segment` i `nazwa_segmentu`).

### Krok 1 — Interaktywny scatter plot segmentacji

```python
# Stwórz scatter plot Plotly
fig_scatter = px.scatter(
    klienci,
    x=___,                    # 'srednia_wartosc'
    y=___,                    # 'zamowienia_rok'
    color=___,                # 'nazwa_segmentu'
    size=___,                 # 'srednia_wartosc' — rozmiar punktu
    title='Segmentacja klientow — KMeans k=3',
    labels={
        'srednia_wartosc': 'Srednia wartosc zamowienia [PLN]',
        'zamowienia_rok': 'Liczba zamowien w roku',
        'nazwa_segmentu': 'Segment'
    },
    hover_data=['srednia_wartosc', 'zamowienia_rok']
)
fig_scatter.show()
```

Sprawdź interaktywność:
- Najedź myszą na punkt — czy widzisz wartości w tooltip?
- Kliknij na segment w legendzie — czy ukrywa punkty?
- Zaznacz prostokąt myszą — czy zoom działa?
- Podwójne kliknięcie — czy resetuje widok?

**Sprawdzenie:** Wykres powinien pokazywac 3 grupy punktow w roznych kolorach, z tooltipami wyswietlajacymi wartosci przy najechaniu myszka.

### Krok 2 — Bar chart: porównanie segmentów

```python
# Przygotowanie danych
srednie_seg = (klienci.groupby('nazwa_segmentu')
               [['srednia_wartosc', 'zamowienia_rok']]
               .mean()
               .reset_index()
               .round(1))

# Stwórz bar chart
fig_bar = px.bar(
    srednie_seg,
    x=___,              # 'nazwa_segmentu'
    y=___,              # 'srednia_wartosc'
    color=___,          # 'nazwa_segmentu'
    title='Srednia wartosc zamowienia per segment',
    labels={'srednia_wartosc': 'Srednia wartosc [PLN]', 'nazwa_segmentu': 'Segment'},
    text_auto='.0f'     # etykiety na słupkach
)
fig_bar.update_layout(showlegend=False)
fig_bar.show()
```

**Sprawdzenie:** Powinny byc 3 slupki (Okazjonalni, Premium, Standardowi) z etykietami liczbowymi na kazdym slupku. Slupek Premium powinien byc najwyzszy.

### Krok 3 — Eksport do HTML

```python
# Zapisz scatter plot jako HTML
fig_scatter.write_html('segmentacja_klienci.html')
print("Wykres zapisany jako segmentacja_klienci.html")
print("Otworz ten plik w przegladarce — dziala bez Pythona!")
```

**Sprawdzenie:** Plik `segmentacja_klienci.html` powinien istniec w katalogu roboczym. Otworz go w przegladarce — wykres powinien byc w pelni interaktywny.

### Krok 4 — Porównanie Plotly vs Matplotlib

Odpowiedz na pytania (komentarz w notebooku):

```python
"""
Porównanie Plotly vs Matplotlib:

1. Kiedy użyłbym Matplotlib?
   Odpowiedź: ___

2. Kiedy użyłbym Plotly?
   Odpowiedź: ___

3. Czy mogę używać obu w jednym projekcie?
   Odpowiedź: ___
"""
```

---

## Ćwiczenie 4: Mini-projekt — segmentacja + wizualizacja Plotly + commit (25 min)

**Poziom Blooma: 5 — Tworzy**

**Cel:** Osoba studiująca samodzielnie integruje KMeans i Plotly w mini-projekt analityczny i zatwierdza pracę przez git commit.

### Zadanie

Zbuduj kompletny pipeline analityczny dla nowego zbioru danych:

### Krok 1 — Nowe dane (4 segmenty)

```python
np.random.seed(123)
n = 200

# 4 segmenty klientów: młodzi/oszczędni, młodzi/rozrzutni,
# dojrzali/oszczędni, dojrzali/rozrzutni
klienci_mp = pd.DataFrame({
    'wiek': np.concatenate([
        np.random.normal(25, 3, 50),    # mlodzi
        np.random.normal(28, 4, 50),    # mlodzi
        np.random.normal(50, 5, 50),    # dojrzali
        np.random.normal(55, 6, 50)     # dojrzali
    ]),
    'wydatki_miesiac': np.concatenate([
        np.random.normal(800, 150, 50),   # oszczedni
        np.random.normal(3500, 400, 50),  # rozrzutni
        np.random.normal(1200, 200, 50),  # oszczedni
        np.random.normal(4500, 500, 50)   # rozrzutni
    ])
})

# Usuń wartości ujemne
klienci_mp = klienci_mp.clip(lower=0)
print(f"Liczba klientow: {len(klienci_mp)}")
klienci_mp.describe().round(1)
```

### Krok 2 — StandardScaler + KMeans z k=4

```python
# TODO: Skaluj dane
scaler_mp = ___
X_mp = scaler_mp.fit_transform(klienci_mp[['wiek', 'wydatki_miesiac']])

# TODO: KMeans z k=4, random_state=42
kmeans_mp = ___
kmeans_mp.fit(___)
klienci_mp['segment'] = kmeans_mp.labels_

# Analiza segmentów
print("Charakterystyka segmentow:")
print(klienci_mp.groupby('segment')[['wiek', 'wydatki_miesiac']].mean().round(1))
print()
print("Liczebnosc:")
print(klienci_mp['segment'].value_counts().sort_index())
```

**Sprawdzenie:** Powinny powstac 4 segmenty. Kazdy powinien miec okolo 50 klientow. Srednie wartosci powinny pokazywac 4 rozne profile: mlody+oszczedny, mlody+rozrzutny, dojrzaly+oszczedny, dojrzaly+rozrzutny.

### Krok 3 — Interpretacja segmentów

```python
# Na podstawie średnich wartości nadaj nazwy
# Segment z młodymi + niskimi wydatkami = "Mlodzi oszczedni"
# Segment z młodymi + wysokimi wydatkami = "Mlodzi premium"
# Segment z dojrzałymi + niskimi wydatkami = "Dojrzali oszczedni"
# Segment z dojrzałymi + wysokimi wydatkami = "Dojrzali premium"

nazwy_mp = {
    ___: '___',
    ___: '___',
    ___: '___',
    ___: '___',
}
klienci_mp['nazwa'] = klienci_mp['segment'].map(nazwy_mp)

print("Segmenty z nazwami:")
print(klienci_mp.groupby('nazwa')[['wiek', 'wydatki_miesiac']].mean().round(1))
```

### Krok 4 — Scatter plot Plotly z 4 segmentami

```python
fig_mp = px.scatter(
    klienci_mp,
    x='wiek',
    y='wydatki_miesiac',
    color='nazwa',
    size='wydatki_miesiac',
    title='Segmentacja klientow — 4 grupy (wiek vs wydatki)',
    labels={
        'wiek': 'Wiek klienta',
        'wydatki_miesiac': 'Wydatki miesieczne [PLN]',
        'nazwa': 'Segment'
    },
    hover_data=['wiek', 'wydatki_miesiac']
)
fig_mp.update_traces(marker=dict(opacity=0.7))
fig_mp.update_layout(plot_bgcolor='white', paper_bgcolor='white')
fig_mp.show()
```

**Sprawdzenie:** Wykres powinien pokazywac 4 wyrazne grupy punktow. Mlodzi po lewej stronie, dojrzali po prawej. Oszczedni na dole, premium na gorze.

### Krok 5 — Bar chart: liczebność segmentów

```python
# Policz klientów per segment
liczebnosc = klienci_mp['nazwa'].value_counts().reset_index()
liczebnosc.columns = ['segment', 'liczba']

fig_bar_mp = px.bar(
    liczebnosc,
    x='segment',
    y='liczba',
    color='segment',
    title='Liczebnosc segmentow',
    text_auto=True
)
fig_bar_mp.update_layout(showlegend=False)
fig_bar_mp.show()
```

### Krok 6 — Eksport i rekomendacja

```python
# Eksport do HTML
fig_mp.write_html('segmentacja_4_grupy.html')
print("Dashboard zapisany jako segmentacja_4_grupy.html")
```

Dodaj komentarz z rekomendacjami:

```python
"""
REKOMENDACJE MARKETINGOWE:

Segment 'Mlodzi oszczedni':
- Strategia: ___
- Przyklad kampanii: ___

Segment 'Mlodzi premium':
- Strategia: ___
- Przyklad kampanii: ___

Segment 'Dojrzali oszczedni':
- Strategia: ___
- Przyklad kampanii: ___

Segment 'Dojrzali premium':
- Strategia: ___
- Przyklad kampanii: ___
"""
```

### Krok 7 — Git commit

```bash
cd ~/python2_projekt
git add s08_advanced_libs.ipynb
git add segmentacja_klienci.html
git add segmentacja_4_grupy.html
git commit -m "S08: KMeans segmentacja + Plotly interaktywne wykresy"
git log --oneline -3
```

**Sprawdzenie:**
- `git log` powinien pokazac nowy commit z wiadomoscia "S08: KMeans segmentacja..."
- Pliki `.ipynb` i `.html` powinny byc w commitcie
- Sprawdz: `git status` — powinno byc czysto (nothing to commit)

---

## Podsumowanie zajęć

Co zrobiłeś na tych laboratoriach:

1. **KMeans clustering** — segmentacja klientów bez etykiet (unsupervised), StandardScaler, interpretacja biznesowa klastrów
2. **Regresja liniowa** — pipeline `train_test_split` -> `fit` -> `predict` -> ocena R² i RMSE
3. **Plotly Express** — interaktywne scatter i bar chart z hover, color, size, eksport HTML
4. **Mini-projekt** — pełny pipeline: dane -> segmentacja -> wizualizacja -> interpretacja -> commit

### Kluczowe wzorce do zapamiętania

```python
# scikit-learn — zawsze ten sam schemat:
model = AlgorytmML(parametry)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Plotly Express — jeden call = interaktywny wykres:
fig = px.scatter(df, x='kol1', y='kol2', color='kategoria')
fig.show()
fig.write_html('wykres.html')
```

Następne spotkanie (S09): LLM i AI API w Pythonie — wywoływanie modeli AI z poziomu kodu.
