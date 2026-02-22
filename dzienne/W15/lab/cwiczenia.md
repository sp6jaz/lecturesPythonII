# L15 — Prezentacje mini-projektów: rubryki i materiały

**Programowanie w Pythonie II** | Laboratorium 15
**Format:** prezentacje studenckie (5 min + 2 min pytania)

## Przydatne materiały do prezentacji

| Temat | Link |
|-------|------|
| Jak robić dobre prezentacje techniczne | https://speakerdeck.com/ (inspiracje) |
| GitHub — tworzenie README.md | https://docs.github.com/en/get-started/writing-on-github |
| Pandas — Cheat Sheet (ściąga) | https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf |
| Matplotlib — Cheat Sheets | https://matplotlib.org/cheatsheets/ |
| Seaborn — Cheat Sheet | https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf |

---

## Rubryka oceny prezentacji (dla prowadzącego)

### Ocena prezentacji — karta (0-10 pkt)

| Kryterium | 0 pkt | 1 pkt | 2 pkt |
|-----------|-------|-------|-------|
| **1. Struktura** — problem → dane → metoda → wyniki → wnioski | Brak struktury, chaotycznie | Częściowa struktura, brakuje elementów | Jasna struktura, logiczny przepływ |
| **2. Dataset i pipeline** — kompletność analizy (EDA → czyszczenie → wizualizacja → statystyka) | Tylko surowe dane lub 1 krok | 2-3 kroki pipeline'u | Pełny pipeline (4+ kroków) |
| **3. Wizualizacje** — czytelność, etykiety, tytuły, dobór typu wykresu | Brak wykresów lub nieczytelne | Wykresy są, ale brak etykiet/tytułów | Czytelne wykresy z pełnym opisem |
| **4. Wnioski** — poparte danymi, relewantne biznesowo | Brak wniosków | Wnioski ogólne, niepoparte liczbami | Konkretne wnioski z liczbami |
| **5. Rozumienie kodu** — student potrafi wyjaśnić co robi jego kod | Nie potrafi wyjaśnić | Wyjaśnia częściowo, z pomocą | Wyjaśnia samodzielnie i pewnie |

**Suma: ___ / 10 pkt**

---

### Ocena portfolio GitHub (0-5 pkt)

| Kryterium | 0 pkt | 1 pkt | 2 pkt |
|-----------|-------|-------|-------|
| **Repozytorium + README** | Brak repo | Repo bez README | Repo + README z opisem |
| **Notebooki z laboratoriów** | <3 notebooki | 3-7 notebooków | 8+ notebooków |
| **Historia commitów** | <5 commitów | 5-10 commitów | 11+ commitów (regularne) |

**Suma portfolio: ___ / 6 pkt** (max 5 — cap)

---

### Łączna ocena L15: ___ / 15 pkt

| Zakres punktów | Ocena |
|----------------|-------|
| 14-15 | 5.0 |
| 12-13 | 4.5 |
| 10-11 | 4.0 |
| 8-9 | 3.5 |
| 6-7 | 3.0 |
| <6 | 2.0 (nzal) |

---

## Rubryka oceny koleżeńskiej (dla studentów — do wydruku)

```
╔══════════════════════════════════════════════════════╗
║  OCENA KOLEŻEŃSKA — prezentacja mini-projektu       ║
║  Programowanie w Pythonie II, L15                    ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  Prezentujący/a: _______________________________     ║
║                                                      ║
║  Oceń w skali 1-5:                                   ║
║                                                      ║
║  Czy prezentacja była zrozumiała?     [ ]            ║
║  Czy wykresy były czytelne?           [ ]            ║
║  Czy wnioski były przekonujące?       [ ]            ║
║                                                      ║
║  Co było najlepsze w tej prezentacji?                 ║
║  __________________________________________________  ║
║                                                      ║
║  Co można poprawić?                                  ║
║  __________________________________________________  ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

*(Wydrukuj kilka kopii na studenta — po jednej na każdą prezentację)*

---

## Wymagania minimalne dla mini-projektu

Studenci powinni byli otrzymać te wymagania na W11-W12 (zapowiedź projektu):

```
MINI-PROJEKT — WYMAGANIA:

1. DATASET
   - Własny dataset (nie z zajęć) — min. 100 wierszy, 5+ kolumn
   - Źródło: Kaggle, UCI ML Repository, dane.gov.pl, API publiczne
   - Zapisany w repozytorium (CSV/Excel)

2. NOTEBOOK (.ipynb)
   - Komórka Markdown: tytuł, opis datasetu, pytanie badawcze
   - EDA: info(), describe(), shape, brakujące dane
   - Czyszczenie: obsługa NaN, typów, duplikatów
   - Minimum 3 wizualizacje (różne typy)
   - Minimum 1 analiza statystyczna (korelacja, test, groupby)
   - Komórka Markdown: wnioski (3 bullet points)

3. GIT
   - Notebook na GitHubie
   - Minimum 3 commity (nie jeden commit z wszystkim)
   - README.md z krótkim opisem projektu

4. PREZENTACJA
   - 5 minut: problem → dane → analiza → wykresy → wnioski
   - Prezentacja z notebooka (nie z PowerPointa)
```

---

## Studenci bez prezentacji — procedura

Jeśli student nie przygotował prezentacji na L15:

1. Daj termin dodatkowy: **+1 tydzień** na przesłanie notebooka na GitHuba
2. Student musi umówić się na krótką rozmowę (5 min) z prowadzącym
3. Obniżenie oceny: max 70% punktów za prezentację (bo brak wystąpienia publicznego)
4. Brak oddania po +1 tygodniu = 0 pkt za mini-projekt

---

## Checklist prowadzącego po L15

- [ ] Wszystkie prezentacje ocenione (karta 0-10 pkt)
- [ ] Portfolio GitHub każdego studenta sprawdzone (0-5 pkt)
- [ ] Oceny koleżeńskie zebrane (nie wpływają na ocenę, ale warto przejrzeć)
- [ ] Lista studentów z brakującymi prezentacjami — termin uzupełnienia ustalony
- [ ] Oceny końcowe z laboratoriów obliczone i gotowe do wpisania
- [ ] Studenci poinformowani o terminie egzaminu
