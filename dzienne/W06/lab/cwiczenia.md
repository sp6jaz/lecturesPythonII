# L06 — Ćwiczenia laboratoryjne

## Temat: Pandas — selekcja, filtrowanie, sortowanie

**Programowanie w Pythonie II** | Laboratorium 6
**Czas:** 90 min | **Forma:** ćwiczenia praktyczne

---

## Ćwiczenie 1: loc i iloc — selekcja (20 min)

### Cel
Naucz się precyzyjnie wybierać wiersze i kolumny z DataFrame.

### Dane

```python
import pandas as pd
import numpy as np

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
```

### Zadania iloc (pozycja)

**Zadanie 1a:**
```python
# 1. Wyświetl wiersz nr 10 (iloc)
# 2. Wyświetl wiersze 5-9 i kolumny 0-2
# 3. Wyświetl ostatnie 3 wiersze
# 4. Wyświetl co 10-ty wiersz
```

### Zadania loc (etykieta/warunek)

**Zadanie 1b:**
```python
# 1. Wyświetl kolumnę 'total_bill' za pomocą loc (wszystkie wiersze)
# 2. Wyświetl kolumny 'total_bill' i 'tip' za pomocą loc (pierwsze 5 wierszy)
# 3. Wyświetl wiersze, gdzie total_bill > 40 (za pomocą loc + warunek)
# 4. Wyświetl wiersze, gdzie day == 'Sun', tylko kolumny 'total_bill' i 'tip'
```

### DataFrame z własnym indeksem

**Zadanie 1c:**
```python
produkty = pd.DataFrame({
    'cena': [3500, 1800, 2500, 350, 2200],
    'magazyn': [45, 120, 200, 500, 75],
    'kategoria': ['Komputery', 'Mobilne', 'Mobilne', 'Akcesoria', 'Komputery']
}, index=['Laptop', 'Tablet', 'Smartfon', 'Słuchawki', 'Monitor'])

# 1. Wyświetl cenę Laptopa (loc)
# 2. Wyświetl cenę i magazyn dla Tablet i Monitor
# 3. Wyświetl produkty z kategorii 'Mobilne'
```

### Sprawdzenie ✅

- 1a: Wiersz 10 → total_bill = 10.27
- 1b: Wiersze z total_bill > 40 → 10 wierszy
- 1c: Cena Laptopa = 3500

---

## Ćwiczenie 2: Filtrowanie z warunkami logicznymi (20 min)

### Cel
Filtruj dane odpowiadając na precyzyjne pytania biznesowe.

### Dane

```python
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
```

### Zadania

**Zadanie 2a — Filtry proste:**
```python
# 1. Rachunki od kobiet (sex == 'Female')
# 2. Rachunki z obiadu (time == 'Dinner')
# 3. Rachunki z grupami >= 4 osób
# Dla każdego: ile wierszy?
```

**Zadanie 2b — AND (oba warunki):**
```python
# 1. Kobiety + niepalaczki — ile?
# 2. Sobota + obiad + rachunek > 20$ — ile?
# 3. Duże grupy (4+) + napiwek > 15% — ile?
```

**Zadanie 2c — OR, isin, between:**
```python
# 1. Piątek LUB sobota (użyj isin)
# 2. Rachunki między 10 a 20 dolarów (użyj between)
# 3. Grupy 2 lub 3 osoby (użyj isin)
```

**Zadanie 2d — query():**
```python
# Przepisz filtr z 2b.2 używając query():
# Sobota + obiad + rachunek > 20$
```

### Sprawdzenie ✅

- 2a: Kobiety: 87; Obiad: 176; Grupy ≥ 4: 46
- 2b: Kobiety niepalaczki: 54; Sob+obiad+>20$: 38; Duże grupy + napiwek >15%: 17
- 2c: Pt lub Sob: 106; Rachunki 10-20$: 130; Grupy 2 lub 3: 194

---

## Ćwiczenie 3: Analiza danych — samodzielna praca (30 min)

### Cel
Odpowiedz na pytania biznesowe łącząc filtrowanie, sortowanie i agregację.

### Dane

```python
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
```

### Pytania

**Zadanie 3a: Rankingi**
```python
# 1. TOP-5 najdroższych rachunków (nlargest)
# 2. TOP-5 najhojniejszych (wg tip_pct, nlargest)
# 3. 5 najniższych rachunków od palaczy
```

**Zadanie 3b: Porównania dzień po dniu**
```python
# Dla każdego dnia oblicz: liczbę rachunków, średni rachunek, średni napiwek %
# Wskazówka: pętla for + filtrowanie
for day in tips['day'].unique():
    subset = tips[tips['day'] == day]
    # ... oblicz statystyki
```

**Zadanie 3c: Pytania biznesowe**
```python
# 1. Czy niepalacze dają wyższy napiwek (%) niż palacze? O ile?
# 2. Czy na obiedzie (Dinner) rachunki są wyższe niż na lunchu?
# 3. Jaki jest średni rachunek dla grup 2-osobowych vs 4-osobowych?
# 4. Znajdź "VIP-ów": rachunek > 40$ i napiwek > 15%. Ilu ich jest?
```

**Zadanie 3d: Odkryj anomalię**
```python
# Kto dał napiwek powyżej 50%? Wyświetl pełne dane tych wierszy.
# Co ciekawego widzisz? (podpowiedź: porównaj total_bill z tip)
```

### Sprawdzenie ✅

- 3a: Najdroższy rachunek = 50.81$
- 3b: Sob — 87 rachunków, śr. ~20.4$
- 3c: Niepalacze: ~15.9%, palacze: ~16.3% (różnica minimalna); Dinner ~20.8$ > Lunch ~17.2$; Grupy 2: ~16.4$, grupy 4: ~28.6$
- 3d: Osoba z tip > 50%: wiersz 172 (rachunek 7.25$, napiwek 5.15$ = 71%) — niski rachunek, wysoki napiwek

---

## Ćwiczenie 4: Segmentacja + commit (15 min)

### Cel
Utwórz segmenty klientów i zapisz pracę.

### Zadanie

```python
# Segmentacja klientów wg rachunku
tips['segment_rachunek'] = np.where(
    tips['total_bill'] > 30, 'Premium',
    np.where(tips['total_bill'] > 15, 'Standard', 'Economy')
)

# 1. Ile klientów w każdym segmencie? (value_counts)
# 2. Jaki jest średni napiwek (%) w każdym segmencie?
# 3. Który segment ma najhojniejszych klientów?
```

### Commit

```bash
git add lab06_pandas_selection.ipynb
git commit -m "L06: Pandas — loc/iloc, filtrowanie, segmentacja"
git push
```

---

## Podsumowanie

Po dzisiejszych zajęciach umiesz:
- ✅ Używać iloc (pozycja) i loc (etykieta/warunek) do selekcji
- ✅ Filtrować dane z &, |, isin, between, query
- ✅ Tworzyć rankingi (sort_values, nlargest, nsmallest)
- ✅ Odpowiadać na precyzyjne pytania o danych
- ✅ Segmentować dane na grupy biznesowe

**Na następnych zajęciach:** Czyszczenie danych — brakujące wartości, duplikaty, konwersja typów. Poznasz jak wygląda "brudny" dataset i jak go naprawić.
