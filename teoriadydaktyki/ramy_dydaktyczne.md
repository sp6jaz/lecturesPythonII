# Ramy dydaktyczne kursu — synteza z E-dydaktyki PO

## Źródła
- Kurs E-dydaktyka PO (Moodle Politechnika Opolska)
- "17 elementów dobrego kursu online" (Doug Madden / PUW)
- "Cele i efekty uczenia się — zacznij od końca" (E-dydaktyka PO)
- "Wzorcowa struktura jednostki dydaktycznej" (E-dydaktyka PO)

---

## 1. Backward Design — projektuj od końca

Nie zaczynamy od "co powiedzieć", ale od:
1. **Efekty uczenia się** — co student będzie potrafił zrobić?
2. **Weryfikacja** — po czym poznamy, że to umie?
3. **Aktywności** — co musi zrobić, żeby się tego nauczyć?
4. **Materiały** — co musi przeczytać/obejrzeć, żeby wykonać aktywność?

## 2. Cel zajęć vs efekt uczenia się

| | Cel zajęć | Efekt uczenia się |
|---|-----------|-------------------|
| **Perspektywa** | prowadzącego | osoby studiującej |
| **Forma** | "Po co realizujemy temat" | "Osoba studiująca **potrafi** zrobić X" |
| **Wymóg** | ogólny | **operacyjny** — konkretne zachowanie |

## 3. Taksonomia Blooma — czasowniki działania

| Poziom | Czasowniki | Weryfikacja |
|--------|-----------|-------------|
| 1. Pamiętanie/Rozumienie | rozpoznaje, definiuje, wyjaśnia, opisuje | quiz, krótka odpowiedź |
| 2. Zastosowanie | stosuje, oblicza, wykonuje, używa | zadanie praktyczne |
| 3. Analiza | analizuje, porównuje, rozróżnia, wskazuje zależności | forum problemowe, analiza case'u |
| 4. Ocena | ocenia, uzasadnia, weryfikuje, krytykuje | ocena z uzasadnieniem |
| 5. Tworzenie | projektuje, konstruuje, opracowuje, tworzy rozwiązanie | projekt + rubryka |

**Szybka korekta sylabusowych sformułowań:**
- "zna" → "wyjaśnia", "wskazuje"
- "rozumie" → "uzasadnia", "interpretuje"
- "zapoznaje się" → "analizuje", "porównuje"

## 4. Warunki poprawnego efektu uczenia się

1. **Opisuje działanie osoby studiującej** (nie "zapoznanie z...")
2. **Odpowiedni poziom Blooma** (czasownik określa czynność)
3. **Przypisana forma weryfikacji** (efekt i weryfikacja muszą się "zgrywać")
4. **Możliwość weryfikacji** (quiz, zadanie, forum, projekt, portfolio)

## 5. Wzorcowa struktura jednostki dydaktycznej (90 min)

Oparta na czterech filarach:
- Backward Design
- Cykl uczenia się Kolba
- Zasady poznawcze Mayera
- Dobre praktyki MAKRO (organizacja, multimedialność, aktywizacja, refleksyjność)

### Etap 1: WPROWADZENIE — orientacja i bezpieczeństwo poznawcze
- Temat jednostki
- Cele zapisane językiem studenta ("Po tym temacie będziesz potrafić...")
- Instrukcja krok po kroku (co, w jakiej kolejności, ile czasu)
- Informacja o sposobie sprawdzenia pracy
- **Efekt:** student wie gdzie jest, po co tu jest i co ma zrobić

### Etap 2: MATERIAŁY DYDAKTYCZNE — eksploracja treści
- Student zdobywa wiedzę potrzebną do **wykonania zadania** (nie "poznania wszystkiego")
- Krótsze materiały (5-12 min) skuteczniejsze niż długie wykłady
- Jeden materiał = jedno zagadnienie
- Łączenie form (tekst, schemat, kod, diagram) — każda ma określoną funkcję
- **Efekt:** student eksploruje treści świadomie i w swoim tempie

### Etap 3: AKTYWNOŚCI — aplikacja i działanie
- Student przestaje być odbiorcą, zaczyna **działać** (cykl Kolba)
- Kolba: doświadczenie → refleksja → teoria → ponowne działanie
- Materiał **nie zastępuje aktywności**, tylko ją wspiera
- Jedna aktywność = jeden efekt uczenia się
- Jasne kryteria i instrukcje
- **Efekt:** student uczy się przez działanie, nie przez czytanie

### Etap 4: PODSUMOWANIE I WERYFIKACJA — konsolidacja
- Krótka synteza najważniejszych treści
- Zadanie punktowane lub quiz weryfikujący
- Forum lub pytanie refleksyjne
- **Efekt:** student wie czego się nauczył i co może poprawić

### Dlaczego ta struktura działa
Stała, powtarzalna struktura:
- obniża obciążenie poznawcze
- zwiększa poczucie bezpieczeństwa
- ułatwia samoregulację uczenia się

## 6. 17 elementów dobrego kursu (wybór kluczowych dla nas)

1. **Wstępne informacje dostępne online** — sylabus, wymagania, kontakt
2. **Szkolenie z nawigacji** — pierwszy wykład: Git, VS Code, workflow
3. **Sylabus na pierwszych zajęciach** — KOP, zasady, harmonogram
4. **Materiały atrakcyjne** — grafika, multimedia, nie ściana tekstu
5. **Odnośniki do zasobów** — linki do dokumentacji, tutoriali
6. **W pełni funkcjonalny** — testowany kod, działające przykłady
7. **Różne style uczenia** — tekst + schemat + kod + video
8. **Logiczna nawigacja** — spójna struktura każdej jednostki
9. **Szybki kontakt z prowadzącym** — odpowiedź < 24h
10. **Podtrzymywanie uwagi** — aktywności, quizy, unikanie ściany tekstu
11. **Poprawny język** — profesjonalne materiały, sprawdzone
12. **Szybkie ładowanie** — lekkie pliki, nie gigantyczne PDF-y

## 7. Zastosowanie w naszym kursie Python II

Każda jednostka (wykład + lab) powinna mieć strukturę:

```
1. WPROWADZENIE (5 min)
   - Temat i cele ("Po tym wykładzie potrafisz...")
   - Co będziemy robić i w jakiej kolejności
   - Powiązanie z poprzednimi zajęciami

2. MATERIAŁ (30-40 min wykład / 15 min lab)
   - Krótkie bloki 5-12 min, nie monolog
   - Kod na żywo, nie slajdy ze zrzutami
   - Diagramy Mermaid zamiast statycznych obrazków
   - Przykłady z danych biznesowych

3. AKTYWNOŚĆ (10-15 min wykład / 60 min lab)
   - Wykład: mini-zadanie, quiz, dyskusja
   - Lab: praktyczne ćwiczenie z danymi
   - Jasne kryteria oceny

4. PODSUMOWANIE (5 min)
   - Co dzisiaj zrobiliśmy (3 bullet points)
   - Co będzie następnym razem
   - Zadanie do samodzielnej pracy
```
