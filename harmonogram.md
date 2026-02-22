# Harmonogram kursu — Programowanie w języku Python II

## Studia dzienne — 15 tygodni (wykład 2h + lab 2h)

| Tydz. | Wykład | Laboratorium | Bloom |
|-------|--------|-------------|-------|
| **W01** | **Warsztat pracy analityka** — Git, GitHub, Markdown, Mermaid, VS Code, uv, venv, zasady kodu | Instalacja narzędzi, pierwsze repo na GitHub, README.md, commit | 1-2 |
| **W02** | **Wprowadzenie do analizy danych** — pipeline analityczny, Jupyter Notebook, typy danych, źródła danych w biznesie | Jupyter w VS Code, pierwszy notebook, eksploracja przykładowego datasetu biznesowego | 1-2 |
| **W03** | **NumPy — podstawy** — ndarray, tworzenie tablic, indeksowanie, slicing, typy danych | Ćwiczenia z tablicami, operacje na danych sprzedażowych, benchmarki lista vs ndarray | 2 |
| **W04** | **NumPy — zaawansowane** — broadcasting, operacje wektorowe, algebra liniowa, generowanie danych | Analiza danych finansowych z NumPy, macierze, statystyki opisowe na tablicach | 2-3 |
| **W05** | **Pandas — Series i DataFrame** — tworzenie, wczytywanie CSV/Excel, podstawowe atrybuty, dtypes | Wczytanie prawdziwego datasetu biznesowego, info(), describe(), head(), eksploracja | 2 |
| **W06** | **Pandas — selekcja i filtrowanie** — loc/iloc, warunki logiczne, sortowanie, query() | Filtrowanie danych sprzedażowych, ranking produktów, segmentacja klientów | 2-3 |
| **W07** | **Pandas — czyszczenie danych** — brakujące wartości, duplikaty, konwersja typów, string operations | Czyszczenie "brudnego" datasetu — realne problemy: NaN, literówki, formaty dat | 3 |
| **W08** | **Pandas — łączenie i agregacja** — merge, join, concat, groupby, pivot_table, crosstab | Łączenie tabel (zamówienia + klienci + produkty), raporty agregowane, KPI | 3-4 |
| **W09** | **Matplotlib — podstawy** — Figure, Axes, line/bar/scatter/histogram, etykiety, legendy | Wizualizacja danych sprzedażowych: trendy, porównania, rozkłady | 2 |
| **W10** | **Matplotlib + Seaborn — zaawansowane** — subplots, style, heatmapy, pairploty, eksport | Dashboard analityczny: 4-6 wykresów na jednym rysunku, raport wizualny | 3-4 |
| **W11** | **Statystyka opisowa w Pythonie** — miary tendencji centralnej, rozproszenia, korelacja, scipy.stats | Analiza statystyczna datasetu HR: wynagrodzenia, rotacja, korelacje | 2-3 |
| **W12** | **Statystyka — rozkłady i testy** — rozkład normalny, t-test, chi-kwadrat, p-value, przedziały ufności | A/B testing: kampania marketingowa, testowanie hipotez na danych biznesowych | 3-4 |
| **W13** | **Zaawansowane biblioteki** — scikit-learn (intro), plotly (interaktywne wykresy), polars (szybki Pandas) | Mini-projekt: klasteryzacja klientów (K-means) + interaktywna wizualizacja | 3-5 |
| **W14** | **LLM i AI w analizie danych** — API (OpenAI/Anthropic), prompty, agenty, automatyzacja analiz | Praktyczne użycie API: generowanie kodu, interpretacja wyników, czyszczenie danych z AI | 4-5 |
| **W15** | **Podsumowanie** — przegląd kursu, best practices, co dalej, przygotowanie do egzaminu | Prezentacja mini-projektów, zaliczenia, wpisy | 4-5 |

---

## Studia zaoczne — 10 spotkań (wykład + lab w bloku)

| Spotk. | Wykład (część 1) | Laboratorium (część 2) | Odpowiednik dziennych |
|--------|-----------------|----------------------|----------------------|
| **S01** | Warsztat pracy + Wprowadzenie do analizy danych | Instalacja, Git, Jupyter, pierwszy notebook | W01 + W02 |
| **S02** | NumPy — pełny przegląd (podstawy + zaawansowane) | Ćwiczenia z tablicami, operacje wektorowe | W03 + W04 |
| **S03** | Pandas — Series, DataFrame, wczytywanie danych | Eksploracja datasetu, info/describe, selekcja | W05 + W06 |
| **S04** | Pandas — czyszczenie, merge, groupby, pivot | Czyszczenie brudnych danych + raporty agregowane | W07 + W08 |
| **S05** | Matplotlib + Seaborn — od podstaw po dashboard | Wizualizacja danych: wykresy + dashboard | W09 + W10 |
| **S06** | Statystyka opisowa — miary, korelacja | Analiza statystyczna datasetu biznesowego | W11 |
| **S07** | Statystyka — rozkłady, testy hipotez | A/B testing na danych marketingowych | W12 |
| **S08** | Zaawansowane biblioteki (scikit-learn, plotly) | Mini-projekt: klasteryzacja + wizualizacja | W13 |
| **S09** | LLM i AI w analizie danych | Praktyczne użycie API AI | W14 |
| **S10** | Podsumowanie, przegląd, przygotowanie do egzaminu | Prezentacja projektów, zaliczenia, wpisy | W15 |

---

## Rozkład godzin na bloki tematyczne

| Blok | Dzienne (wykł./lab) | Zaoczne (w+l) | Waga |
|------|-------------------|---------------|------|
| Warsztat + Intro | 4h / 4h | 1 spotkanie | 13% |
| NumPy | 4h / 4h | 1 spotkanie | 13% |
| **Pandas** | **8h / 8h** | **2 spotkania** | **27%** |
| Matplotlib + Seaborn | 4h / 4h | 1 spotkanie | 13% |
| Statystyka | 4h / 4h | 2 spotkania | 13% |
| Zaawansowane + AI | 4h / 4h | 2 spotkania | 13% |
| Podsumowanie | 2h / 2h | 1 spotkanie | 7% |

**Pandas ma największą wagę (27%)** — bo to kluczowe narzędzie analityka danych.

---

## Projekt przewodni — "Analiza firmy X"

Propozycja: **jeden spójny dataset biznesowy przewija się przez cały kurs**.

Np. fikcyjna firma e-commerce z tabelami:
- `zamowienia.csv` — id, data, klient_id, produkt_id, kwota, status
- `klienci.csv` — id, imie, miasto, wiek, segment, data_rejestracji
- `produkty.csv` — id, nazwa, kategoria, cena, koszt
- `kampanie.csv` — id, typ, budzet, klikniecia, konwersje

Każdy tydzień dodaje nową warstwę analizy tych samych danych:
- W03-04: NumPy na surowych wartościach
- W05-08: Pandas — ładowanie, czyszczenie, merge, raporty
- W09-10: Wizualizacja trendów, dashboard
- W11-12: Testy statystyczne (A/B test kampanii)
- W13: Klasteryzacja klientów
- W14: AI interpretuje wyniki

**Efekt:** student buduje kompletną analizę portfolio-ready.

---

## Pomysły dodatkowe

### Mini-quizy na początku każdego wykładu (5 min)
- 3-5 pytań z poprzedniego tygodnia (spaced repetition)
- Nieoceniane, ale budują nawyk powtarzania
- Można przez Moodle quiz lub Mentimeter (live)

### "Wyzwanie tygodnia" (opcjonalne)
- Jedno dodatkowe zadanie dla ambitnych
- Rozwiązanie omawiane na następnym wykładzie
- Buduje zaangażowanie najlepszych studentów

### Peer review (2× w semestrze)
- Studenci przeglądają kod kolegów na GitHub
- Buduje kompetencje społeczne (K1_K04 z sylabusa)
- Uczy czytania cudzego kodu — kluczowa umiejętność w pracy
