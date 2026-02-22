# L10 — Plan laboratorium dla prowadzącego

## Temat: Matplotlib + Seaborn — wizualizacja zaawansowana

**Programowanie w Pythonie II** | Laboratorium 10
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne przy komputerze
**Prowadzący:** doktorant (laboratoria prowadzone samodzielnie)

---

## Efekty uczenia się (Bloom poziom 3-4)

Po tych zajęciach osoba studiująca:
1. **Tworzy** wykresy kategoryczne i macierzowe w Seaborn (`barplot`, `boxplot`, `violinplot`, `heatmap`) dobierając typ do charakteru danych (Bloom 3)
2. **Konstruuje** siatkę subplotów za pomocą `plt.subplots()` i `GridSpec` z kontrolą rozmiaru paneli (Bloom 3)
3. **Projektuje** wielopanelowy dashboard analityczny z datasetu tips, łącząc minimum 4 typy wykresów (Bloom 4)
4. **Analizuje** wzorce w danych restauracji i opisuje wnioski biznesowe do każdego wykresu (Bloom 4)
5. **Eksportuje** gotową wizualizację do pliku PNG z właściwym DPI i bez obcinania elementów (Bloom 3)

---

## Plan minutowy

| Czas | Etap | Opis | Uwagi |
|------|------|------|-------|
| 0:00-0:05 | Organizacja | Sprawdzenie listy, weryfikacja środowiska | Otwierają VS Code + .venv |
| 0:05-0:10 | Wprowadzenie | Krótki kontekst: Seaborn = piękno, dashboard = historia | Bez live coding |
| 0:10-0:30 | Ćwiczenie 1 | Wykresy Seaborn: barplot, boxplot, heatmap (20 min) | Para lub samodzielnie |
| 0:30-0:50 | Ćwiczenie 2 | Subplots i GridSpec — siatki wykresów (20 min) | Samodzielnie |
| 0:50-1:20 | Ćwiczenie 3 | Pełny dashboard z tips — samodzielna praca (30 min) | Samodzielnie |
| 1:20-1:35 | Ćwiczenie 4 | Szlif, eksport, commit (15 min) | Samodzielnie |
| 1:35-1:45 | Podsumowanie | Omówienie dashboardów, zapowiedź L11 | Dyskusja |

---

## Organizacja sali

- Studenci pracują w parach lub samodzielnie — do wyboru (Ćwiczenie 1 polecane w parach)
- Tworzą własny notebook `.ipynb`
- Notebook nazywają: `lab10_seaborn_dashboard.ipynb`
- Commit na koniec zajęć (Ćwiczenie 4)

### Środowisko
```bash
# Aktywacja środowiska
cd ~/python2_projekt
source .venv/bin/activate   # Linux/Mac
# lub
.venv\Scripts\activate      # Windows

# Weryfikacja
python -c "import seaborn; print(seaborn.__version__)"

# Otwarcie VS Code
code .
```

### Dataset (wbudowany w Seaborn — nie wymaga internetu po instalacji)
```python
import seaborn as sns
tips = sns.load_dataset('tips')
# 244 wiersze, 7 kolumn: total_bill, tip, sex, smoker, day, time, size
```

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przed zajęciami (10 min wcześniej)
- [ ] Sprawdź, czy seaborn jest zainstalowany: `python -c "import seaborn; print(seaborn.__version__)"`
- [ ] Zweryfikuj, że `sns.load_dataset('tips')` działa (wymaga dostępu do sieci przy pierwszym pobraniu — dataset cache'uje się lokalnie)
- [ ] Miej gotowy notebook z przykładowymi rozwiązaniami (do podglądu gdy student utknął)
- [ ] Jeśli nie ma internetu: tips dataset można też pobrać jako CSV z seaborn GitHub i wczytać ręcznie

### Backup datasetu (gdy brak internetu)
```python
# Alternatywne wczytanie jeśli sns.load_dataset nie działa
import pandas as pd
# CSV dostępny pod: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
# Wczytaj lokalnie jeśli masz zapisany plik:
tips = pd.read_csv('tips.csv')
```

### Podczas zajęć
- Pierwsze 5 min: sprawdź czy wszyscy mają działający `sns.load_dataset('tips')`
- Ćwiczenie 3 (dashboard) — najtrudniejsze, 30 minut może nie wystarczyć dla wolniejszych studentów
- Nie dawaj gotowego kodu — naprowadzaj: "Jakiego wykresu użyjesz? Jak umieszczasz w siatce? Co oznacza parametr `hue`?"
- Przy Ćwiczeniu 4: commit musi zawierać plik `.ipynb` — sprawdź na ekranie studenta

### Tempo grup
- Szybcy studenci: Ćwiczenie 3 rozszerzone (sekcja "Rozszerzenie") + eksport do PDF
- Wolni studenci: Ćwiczenia 1 + 2 + commit podstawowy wystarczają — 3 i 4 bonusowe

### Pair programming
- Studenci mogą pracować w parach: **pilot** (pisze kod) + **navigator** (czyta instrukcję, podpowiada, sprawdza)
- Co 15-20 minut zamiana ról
- Pair programming zmniejsza frustrację i przyspiesza naukę — zachęcaj, ale nie wymuszaj

---

## Tabela rozwiązywania problemów (Troubleshooting)

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| `ModuleNotFoundError: No module named 'seaborn'` | Seaborn nie jest zainstalowany w aktywnym venv | `uv pip install seaborn` w aktywowanym środowisku |
| `sns.load_dataset('tips')` — timeout / brak danych | Brak internetu lub cache nie istnieje | Pobierz tips.csv osobno lub użyj backupu z kodu (patrz sekcja Backup powyżej) |
| Wykresy nie wyświetlają się w VS Code | Brak `%matplotlib inline` lub nieprawidłowy backend | Dodaj `%matplotlib inline` jako pierwszą komórkę; lub użyj `plt.savefig()` i otwórz plik |
| Wykresy nachodzą na siebie / tytuł obcięty | Brak `plt.tight_layout()` lub `constrained_layout=True` | Dodaj `plt.tight_layout()` przed `plt.show()`, lub przy `subplots()` dodaj `constrained_layout=True` |
| `pairplot` nie mieści się w `ax=` | `pairplot` zwraca `PairGrid`, nie standardowy `Axes` | `sns.pairplot()` tworzy własną figurę — nie można go umieścić w `axes[i,j]`. Użyj `plt.show()` osobno. |
| `TypeError: violinplot() got an unexpected keyword argument 'split'` | Starsza wersja seaborn (< 0.12) | Zaktualizuj: `uv pip install --upgrade seaborn` lub usuń `split=True` |
| Kolory w `hue` nie działają z `violinplot` i `split=True` | `split=True` wymaga dokładnie 2 kategorii w `hue` | Upewnij się, że kolumna `hue` ma tylko 2 unikalne wartości (np. `sex`: Male/Female) |
| `KeyError: 'day'` w groupby/pivot | Błąd: `observed=False` powoduje problemy z kategoriami | Dodaj `observed=True` do `groupby()`: `tips.groupby('day', observed=True)` |
| Dashboard wychodzi za mały — wykresy nieczytelne | `figsize` za małe dla liczby paneli | Zwiększ `figsize`: dla 4 paneli minimum `(12, 8)`, dla 6 paneli `(16, 11)` |
| `AttributeError: 'AxesSubplot' object has no attribute 'bar'` | Mieszanie `plt.bar()` z `ax.bar()` | Używaj konsekwentnie `ax.bar()` gdy masz `ax` z subplots. `plt.bar()` tylko gdy jedyny wykres. |
| Legenda zasłania dane | Legenda wewnątrz wykresu przy dużej liczbie kategorii | `ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')` + `plt.tight_layout()` |
| `FutureWarning: observed=False` | Pandas ostrzega o zmianie domyślnego zachowania dla kategorii | Dodaj `observed=True` do każdego `groupby()` na kolumnach kategorycznych |
| `savefig` generuje plik z białymi marginesami | `bbox_inches` nie ustawione | Zawsze używaj `plt.savefig('plik.png', dpi=150, bbox_inches='tight', facecolor='white')` |
| Styl Seaborn nie zmienia wyglądu | `sns.set_theme()` wywołane po narysowaniu wykresu | `sns.set_theme()` musi być wywołane przed pierwszym wykresem, najlepiej na początku notebooka |

---

## Weryfikacja wyników — klucz odpowiedzi

### Ćwiczenie 1 (Wykresy Seaborn)
- `sns.barplot(data=tips, x='day', y='total_bill')` — 4 słupki (Thur, Fri, Sat, Sun), wąsy CI widoczne
- Boxplot: Sobota ma najwyższą medianę rachunku, widoczne outliers powyżej 40 USD
- Heatmap: korelacja total_bill–tip wynosi ~0.68, total_bill–size ~0.60

### Ćwiczenie 2 (Subplots i GridSpec)
- `plt.subplots(2, 2)` — 4 wykresy w siatce, dostęp przez `axes[0,0]`, `axes[0,1]` itd.
- GridSpec: górny panel `gs[0, :]` zajmuje całą szerokość — wizualnie wyróżniony
- `constrained_layout=True` — wykresy nie nachodzą na siebie

### Ćwiczenie 3 (Dashboard)
- Minimum 4 panele, każdy inny typ wykresu
- Tytuł główny figurą: `fig.suptitle()`
- Każdy panel ma tytuł i etykiety osi
- Kod wykonuje się bez błędów — `plt.show()` na końcu, `plt.close()` po show

### Ćwiczenie 4 (Eksport + commit)
- Plik PNG istnieje, rozmiar > 50 KB (świadczy o treści), DPI minimum 150
- `git log` — widoczny commit z plikiem `lab10_seaborn_dashboard.ipynb`

---

## Zapowiedź L11

> "Na kolejnych zajęciach: statystyka z SciPy — rozkłady prawdopodobieństwa, testy hipotez (t-test, chi-kwadrat), przedziały ufności. Będziemy wizualizować wyniki testów statystycznych — więc dzisiejszy Seaborn będzie potrzebny. Kto nie skończył dashboardu — dokończcie na własną rękę, przyda się jako materiał do prezentacji wyników statystycznych."
