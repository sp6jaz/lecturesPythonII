# L15 — Plan laboratorium dla prowadzącego

## Temat: Prezentacje mini-projektów + zaliczenie laboratoriów

**Programowanie w Pythonie II** | Laboratorium 15
**Czas:** 90 min | **Forma:** prezentacje studenckie + weryfikacja portfolio
**Prowadzący:** doktorant (laboratoria prowadzone samodzielnie)

---

## Efekty uczenia się (Bloom poziom 4-5)

Po tych zajęciach osoba studiująca:
1. **Prezentuje** samodzielną analizę danych w formie krótkiego wystąpienia z notebookiem Jupyter (Bloom 5)
2. **Ocenia** prezentacje kolegów stosując zdefiniowane kryteria: kompletność analizy, czytelność wizualizacji, trafność wniosków (Bloom 4)
3. **Weryfikuje** kompletność własnego portfolio na GitHubie: notebooki z L01-L14, historia commitów, dokumentacja (Bloom 4)

---

## Przydatne linki dla prowadzącego

- [GitHub — Viewing your repos](https://docs.github.com/en/repositories)
- [Pandas — Cheat Sheet (PDF)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Matplotlib — Cheat Sheets](https://matplotlib.org/cheatsheets/)

## Plan minutowy

| Czas | Etap | Opis | Uwagi |
|------|------|------|-------|
| 0:00-0:05 | Organizacja | Sprawdzenie listy, kolejność prezentacji, rozdanie rubryk | Wylosuj kolejność |
| 0:05-0:55 | Prezentacje | ~7 prezentacji × 7 min (5 min + 2 min pytania) | Runda 1 |
| 0:55-1:05 | Przerwa | 10 minut | — |
| 1:05-1:25 | Prezentacje | Pozostałe prezentacje + weryfikacja spóźnionych | Runda 2 |
| 1:25-1:35 | Portfolio | Weryfikacja GitHub: notebooki, commity, README | Indywidualnie |
| 1:35-1:45 | Zamknięcie | Podsumowanie, oceny, wpisy | Dyskusja |

---

## Organizacja sali

- Komputer z projektorem podłączony do internetu
- Student podchodzi do komputera, otwiera swój notebook z GitHuba
- Alternatywa: student prezentuje ze swojego laptopa (podłączenie HDMI)
- Rubryki oceny koleżeńskiej wydrukowane (1 na studenta)

### Format prezentacji
- Student otwiera notebook `.ipynb` i przechodzi przez komórki
- NIE robimy slajdów PowerPoint — pokazujemy żywy notebook
- Jeśli ktoś przygotował slajdy — może je pokazać jako uzupełnienie, ale notebook jest obowiązkowy

### Ewentualne problemy
- Student nie ma notebooka → pyta o termin uzupełnienia (max +1 tydzień)
- Student nie ma GitHuba → natychmiast zakładamy konto i pushujemy (5 min)
- Internet nie działa → studenci prezentują z lokalnego pliku na pendrive

---

## INSTRUKCJA DLA PROWADZĄCEGO

### Przed zajęciami (15 min wcześniej)
- [ ] Przygotuj listę studentów do prezentacji
- [ ] Wydrukuj rubryki oceny (plik cwiczenia.md — sekcja rubryk)
- [ ] Sprawdź projektor i połączenie HDMI
- [ ] Miej przygotowany timer na telefonie (5 min countdown)
- [ ] Otwórz GitHuba — będziesz weryfikować repozytoria studentów

### Podczas prezentacji

**Twoja rola: moderator + egzaminator**

Na co zwracać uwagę:
1. **Kompletność pipeline'u:** dane → czyszczenie → wizualizacja → wnioski
2. **Czy student rozumie własny kod:** zadaj 1 pytanie weryfikujące
3. **Czy wizualizacje mają etykiety, tytuły, legendę**
4. **Czy wnioski są poparte liczbami z analizy**
5. **Czy jest historia commitów na GitHubie** (nie jeden commit z wszystkim)

**Pytania do zadania (wybierz 1-2 na prezentację):**
- "Co było najtrudniejsze?"
- "Dlaczego wybrałeś ten typ wykresu?"
- "Co oznacza ta liczba dla biznesu?"
- "Jak poradziłeś sobie z brakującymi danymi?"
- "Pokaż git log — ile commitów?"
- "Gdybyś powtórzył projekt — co zrobiłbyś inaczej?"

**Ocenianie:**
- Prezentacja: 0-10 pkt (patrz rubryka w cwiczenia.md)
- Portfolio GitHub: 0-5 pkt (patrz sekcja weryfikacji)
- Razem: max 15 pkt za L15

### Weryfikacja portfolio (0:25-0:35)

Po prezentacjach — przejdź po sali i sprawdź GitHuba każdego studenta:

```
CHECKLIST PORTFOLIO:
□ Repozytorium istnieje i jest publiczne (lub prowadzący ma dostęp)
□ Minimum 5 notebooków z laboratoriów
□ Historia commitów (>10 commitów w semestrze)
□ README.md w repozytorium
□ Notebook z mini-projektem (prezentacja)
```

| Kryterium | 0 pkt | 1 pkt | 2 pkt |
|-----------|-------|-------|-------|
| Repo + README | Brak repo | Repo bez README | Repo + README |
| Notebooki lab | <3 | 3-7 | 8+ |
| Historia commitów | <5 | 5-10 | 11+ |

### Pair programming
- Studenci mogą pracować w parach: **pilot** (pisze kod) + **navigator** (czyta instrukcję, podpowiada, sprawdza)
- Co 15-20 minut zamiana ról
- Pair programming zmniejsza frustrację i przyspiesza naukę — zachęcaj, ale nie wymuszaj

---

## Tabela rozwiązywania problemów (Troubleshooting)

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| Student nie przygotował prezentacji | Nie zrobił projektu | Daj termin +1 tydzień, obniżona ocena |
| Notebook nie otwiera się | Brakuje bibliotek na komputerze sali | Otwórz przez GitHub (podgląd .ipynb online) |
| Student nie ma konta GitHub | Nie założył wcześniej | Pomóż założyć teraz (2 min) + git push |
| Prezentacja trwa >7 min | Zbyt dużo treści | Przerwij po 5 min, pytania po 6:30 |
| Nikt nie zadaje pytań z sali | Nieśmiałość grupy | Ty zadaj 2 pytania, potem zachęć |
| Internet nie działa | Awaria sieci | Prezentacje z lokalnych plików |
| Student prezentuje slajdy zamiast notebooka | Nie zrozumiał formatu | Poproś o otwarcie notebooka |
| Wszystkie prezentacje zajmą <60 min | Mało studentów | Poświęć więcej czasu na portfolio review i dyskusję |

---

## Podsumowanie i wpisy

> "Dziękuję za wszystkie prezentacje. Widać progres — od pierwszego laboratorium, gdzie instalowaliście Pythona, do dzisiaj, gdzie robicie samodzielne analizy i prezentujecie wyniki. To jest dokładnie to, o co chodziło."

> "Oceny z L15 + podsumowanie laboratoriów wpiszę do systemu do [data]. Sprawdźcie oceny i jeśli coś się nie zgadza — piszcie na maila."

> "Powodzenia na egzaminie!"
