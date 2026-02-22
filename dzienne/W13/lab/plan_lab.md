# L13 — Plan laboratorium dla prowadzącego

## Temat: Zaawansowane biblioteki — scikit-learn, Plotly, mini-projekt

**Programowanie w Pythonie II** | Laboratorium 13
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne przy komputerze
**Prowadzący:** doktorant (laboratoria prowadzone samodzielnie)

---

## Efekty uczenia się (Bloom poziom 3-5)

Po tych zajęciach osoba studiująca:
1. **Stosuje** `KMeans` i `StandardScaler` do segmentacji klientów na syntetycznych danych, interpretując każdy klaster biznesowo (Bloom 3)
2. **Projektuje** pipeline regresji liniowej: generowanie danych → podział train/test → trening → ocena R² i RMSE → interpretacja (Bloom 4)
3. **Tworzy** interaktywny dashboard Plotly z wykresami scatter, bar i line, kodując informacje przez kolor, rozmiar i hover (Bloom 5)
4. **Integruje** segmentację KMeans z wizualizacją Plotly w spójny mini-projekt analityczny, zatwierdzany przez git commit (Bloom 5)

---

## Plan minutowy

| Czas | Etap | Opis | Uwagi |
|------|------|------|-------|
| 0:00-0:05 | Organizacja | Sprawdzenie listy, aktywacja venv, instalacja scikit-learn + plotly | Otwierają VS Code |
| 0:05-0:10 | Wprowadzenie | Kontekst: "budujemy pipeline od danych do interaktywnej prezentacji" | Bez live coding |
| 0:10-0:30 | Ćwiczenie 1 | KMeans — segmentacja klientów (20 min) | Samodzielnie / pary |
| 0:30-0:50 | Ćwiczenie 2 | Regresja liniowa — prognoza sprzedaży (20 min) | Samodzielnie |
| 0:50-1:20 | Ćwiczenie 3 | Plotly — interaktywny dashboard (30 min) | Samodzielnie |
| 1:20-1:35 | Ćwiczenie 4 | Mini-projekt: segmentacja + Plotly + commit (15 min) | Samodzielnie |
| 1:35-1:45 | Podsumowanie | Omówienie wyników, zapowiedź L14 | Dyskusja |

---

## Organizacja sali

- Studenci pracują samodzielnie lub w parach (Ćwiczenie 1 polecane w parach)
- Tworzą własny notebook `.ipynb`
- Notebook nazywają: `lab13_advanced_libs.ipynb`
- Commit na koniec zajęć (Ćwiczenie 4)

### Środowisko — WAŻNE: scikit-learn i plotly mogą nie być zainstalowane

```bash
# Aktywacja środowiska
cd ~/python2_projekt
source .venv/bin/activate   # Linux/Mac
# lub
.venv\Scripts\activate      # Windows

# Instalacja brakujących bibliotek
uv pip install scikit-learn plotly

# Weryfikacja
python -c "import sklearn; print('sklearn', sklearn.__version__)"
python -c "import plotly; print('plotly', plotly.__version__)"

# Otwarcie VS Code
code .
```

### Pierwsza komórka notebooka

Powiedz studentom żeby jako **pierwszą komórkę** w notebooku wpisali:

```python
%pip install scikit-learn plotly -q
```

To zainstaluje brakujące pakiety bez wychodzenia z notebooka, cicho (`-q`).

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przed zajęciami (10 min wcześniej)
- [ ] Sprawdź scikit-learn: `python -c "import sklearn; print(sklearn.__version__)"`
- [ ] Sprawdź plotly: `python -c "import plotly; print(plotly.__version__)"`
- [ ] Miej gotowy notebook z przykładowymi rozwiązaniami (do podglądu gdy student utknął)
- [ ] Upewnij się że numpy, pandas, matplotlib są dostępne

### Podczas zajęć
- Pierwsze 5 min: sprawdź czy wszyscy mają `sklearn` i `plotly` dostępne
- Ćwiczenie 3 (Plotly dashboard) — najtrudniejsze, 30 minut może nie wystarczyć wolniejszym studentom
- Kluczowe naprowadzenia:
  - "Pamiętasz o `StandardScaler` przed KMeans? Bez niego skala danych zaburzy wyniki"
  - "Jaki feature dasz na `color=` w Plotly scatter? Który parametr koduje segment?"
  - "Co mówi R²=0.95 dla Twojego modelu? Czy to dobry wynik?"
- Nie dawaj gotowego kodu — naprowadzaj pytaniami
- Przy Ćwiczeniu 4: commit musi zawierać plik `.ipynb`

### Tempo grup
- Szybcy studenci: Ćwiczenie 3 rozszerzenie (wielopanelowy subplot Plotly) + fig.write_html()
- Wolni studenci: Ćwiczenia 1 + 2 + podstawowy wykres scatter z Plotly wystarczają

### Pair programming
- Studenci mogą pracować w parach: **pilot** (pisze kod) + **navigator** (czyta instrukcję, podpowiada, sprawdza)
- Co 15-20 minut zamiana ról
- Pair programming zmniejsza frustrację i przyspiesza naukę — zachęcaj, ale nie wymuszaj

### Typowe błędy koncepcyjne (poprawiaj natychmiast)
- Brak `StandardScaler` przed KMeans — pytaj "czy Twoje cechy są w tej samej skali?"
- Używanie `fit_transform` na zbiorze testowym — zawsze tylko `transform`
- Mylenie R² i RMSE — R² bezwymiarowe (0-1), RMSE w jednostkach zmiennej celu
- Interpretacja klastrów po numerach (0, 1, 2) bez analizy co one znaczą — pytaj "jak nazwałbyś ten segment?"

---

## Tabela rozwiązywania problemów (Troubleshooting)

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `ModuleNotFoundError: sklearn` | Brak scikit-learn w venv | `uv pip install scikit-learn` lub `%pip install scikit-learn` w notebooku |
| `ModuleNotFoundError: plotly` | Brak plotly w venv | `uv pip install plotly` lub `%pip install plotly` |
| `fig.show()` nie wyświetla wykresu | Problem z renderowaniem w Jupyter | Sprawdź: `uv pip install "plotly>=5.0" nbformat`, zrestartuj kernel |
| KMeans daje inne klastry niż przykład | Różne `random_state` lub kolejność klastrów | Normalne — sprawdź `random_state=42`, ale kolejność etykiet może się różnić |
| R² ujemne lub bardzo niskie | Model gorszy niż baseline (średnia) | Sprawdź `X_train` i `y_train` — czy nie zamieniłeś features z target? |
| `ValueError: could not convert string to float` | Dane kategoryczne w X | Encode kategoryczne: `pd.get_dummies()` lub `LabelEncoder` |
| `ConvergenceWarning: KMeans nie osiągnął zbieżności` | Za mało iteracji lub zły init | Zwiększ `max_iter=500` lub `n_init=20` |
| Wykres Plotly otwiera się w przeglądarce zamiast w Jupyter | Brak `nbformat` lub stary Jupyter | `uv pip install nbformat`, zrestartuj kernel |
| `fig.write_html()` — FileNotFoundError | Zły path lub brak uprawnień | Użyj `fig.write_html('wykres.html')` — bez ścieżki → aktualny katalog |
| Scatter plot wszystkie punkty jednego koloru | `color=` przyjmuje numeryczną kolumnę zamiast kategorycznej | Zamień: `klienci['segment'] = klienci['segment'].astype(str)` |

---

## Weryfikacja wyników — klucz odpowiedzi

### Ćwiczenie 1 (KMeans segmentacja)
- Z `seed=42`, n=300, k=3: trzy czytelne klastry widoczne na scatter plotcie
- `klienci.groupby('segment').mean()` — różne średnie wartości dla każdego segmentu
- Clusterhead powinny odpowiadać segmentom: niski/średni/wysoki wartość + częstotliwość
- Inertia (koszt): `kmeans.inertia_` — mniejsza = lepszy podział

### Ćwiczenie 2 (Regresja liniowa)
- R² na zbiorze testowym ≥ 0.95 (dane syntetyczne z wyraźną zależnością)
- RMSE ≈ 2-3 (szum `np.random.normal(0, 2)`)
- Współczynniki: TV ≈ 0.05, Radio ≈ 0.10, Intercept ≈ 5
- `model.predict([[200, 30]])` → sprzedaż ≈ 5 + 0.05×200 + 0.10×30 = 18

### Ćwiczenie 3 (Plotly dashboard)
- 3 wykresy: scatter z segmentami, bar ze średnimi, line z trendem
- Każdy wykres ma `title`, `labels`, `color`
- Hover pokazuje wartości

### Ćwiczenie 4 (Mini-projekt + commit)
- Plik `lab13_advanced_libs.ipynb` widoczny w `git log`
- Commit message opisuje co zostało zrobione
- Notebook zawiera przynajmniej: KMeans, scatter Plotly, interpretację segmentów

---

## Zapowiedź L14

> "Na kolejnych zajęciach: LLM i AI API. Nauczymy się wywoływać GPT-4 lub Claude przez Python — automatyczne generowanie tekstów, klasyfikacja, streszczenia. Kto chce się przygotować — rejestracja na platform.openai.com i zapoznanie się z Python SDK: `pip install openai`. Będziemy potrzebować klucza API (możecie użyć darmowego kredytu próbnego)."
