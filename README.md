# Programowanie w Pythonie II — materiały dydaktyczne

**Politechnika Opolska, WEAiI**
**Kierunek:** Analityka danych w biznesie, semestr 2
**Prowadzący:** dr hab. inż. Jarosław Zygarlicki

## O kursie

Kurs uczy praktycznego wykorzystania Pythona w analizie danych biznesowych. Obejmuje pełny pipeline analityka: od przygotowania środowiska, przez NumPy/Pandas/Matplotlib/Seaborn, statystykę, aż po scikit-learn, Plotly i API modeli LLM.

## Narzędzia kursu

| Narzędzie | Zastosowanie |
|-----------|-------------|
| Python 3.10+ | Język programowania |
| uv | Menedżer pakietów i środowisk wirtualnych |
| VS Code | Edytor kodu + Jupyter + Git |
| Git + GitHub | Kontrola wersji, portfolio studenta |

## Struktura repozytorium

```
dzienne/                      ← studia stacjonarne (15 tygodni)
  W01/ .. W15/
    wyklad/                   ← plan zajęć, quizy, demo notebooki
    lab/                      ← plan lab (dla prowadzącego), ćwiczenia

zaoczne/                      ← studia niestacjonarne (10 zjazdów)
  S01/ .. S10/
    wyklad/                   ← plan zajęć ze stenogramem
    lab/                      ← ćwiczenia

skryptdlastudentow/           ← skrypt do samodzielnej nauki (8 rozdziałów)
teoriadydaktyki/              ← ramy dydaktyczne (Bloom, Backward Design)
publikacja/                   ← skrypty do publikacji materiałów
```

## Harmonogram — studia dzienne

| Tydz. | Temat |
|-------|-------|
| W01 | Warsztat pracy — Git, Markdown, VS Code, uv |
| W02 | Wprowadzenie do analizy danych — pipeline, Jupyter |
| W03 | NumPy — podstawy |
| W04 | NumPy — zaawansowane |
| W05 | Pandas — Series i DataFrame |
| W06 | Pandas — selekcja i filtrowanie |
| W07 | Pandas — czyszczenie danych |
| W08 | Pandas — łączenie i agregacja |
| W09 | Matplotlib — podstawy |
| W10 | Matplotlib + Seaborn — zaawansowane |
| W11 | Statystyka opisowa |
| W12 | Statystyka — rozkłady i testy hipotez |
| W13 | Zaawansowane biblioteki — scikit-learn, Plotly |
| W14 | LLM i AI w analizie danych |
| W15 | Podsumowanie i prezentacje |

## Harmonogram — studia zaoczne

| Zjazd | Temat |
|-------|-------|
| S01 | Warsztat pracy + pipeline analityka |
| S02 | NumPy — od podstaw do zaawansowanych |
| S03 | Pandas — Series, DataFrame, selekcja |
| S04 | Pandas — czyszczenie, łączenie, agregacja |
| S05 | Matplotlib + Seaborn — wizualizacja |
| S06 | Statystyka opisowa |
| S07 | Statystyka — testy hipotez |
| S08 | scikit-learn, Plotly, Polars |
| S09 | LLM i AI w analizie danych |
| S10 | Prezentacje mini-projektów |

## Struktura materiałów na każdy tydzień

Każdy tydzień zawiera do 5 plików:

| Plik | Przeznaczenie |
|------|--------------|
| `plan_zajec.md` | Scenariusz wykładu ze stenogramem (dla prowadzącego) |
| `quiz_wXX.md` | Quiz 5 pytań (spaced repetition na początku kolejnych zajęć) |
| `plan_lab.md` | Scenariusz laboratorium (dla doktoranta) |
| `cwiczenia.md` | Ćwiczenia krok po kroku (dla studentów) |
| `*_demo.ipynb` | Notebook demonstracyjny |

## Zasady dydaktyczne

- **Backward Design** — od efektów uczenia się do materiałów
- **Taksonomia Blooma** — od zapamiętania (poziom 1) do tworzenia (poziom 6)
- **Struktura 4-częściowa** — Wprowadzenie, Materiał, Aktywność, Podsumowanie
- **Kontekst biznesowy** — dane sprzedażowe, HR, logistyka, finanse
- **Pair programming** — zachęcane na laboratoriach

## Repo studenckie

Materiały widoczne dla studentów (bez planów prowadzącego):
https://github.com/sp6jaz/python2-materialy

## Stan projektu

- Dzienne W01-W15: kompletne
- Zaoczne S01-S10: kompletne
- Skrypt studenta: 8 rozdziałów (~2300 linii)
- Audyt jakości: 3 rewizje przeprowadzone
