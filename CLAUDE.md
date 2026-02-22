# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**lecturesPythonII** — materiały do wykładów z Pythona (część II). Katalog w monorepo `~/agent/`.

## Repository Layout

This project lives inside the `~/agent/` git repo (branch: `master`, remote: `github.com/sp6jaz/systemopt`). It is a subdirectory alongside `systemopt/` (Linux optimization toolkit).

## Bootstrap

```bash
./go.sh   # uruchamia claude --dangerously-skip-permissions
```

## Zasady pracy

### NIGDY nie pytaj użytkownika
- Masz pełne uprawnienia do wszystkich operacji
- Jeśli coś nie działa — szukaj rozwiązania sam, nie pytaj
- Jeśli potrzebujesz podjąć decyzję — podejmij ją sam
- Użytkownik chce zostawić cię samego i wrócić do gotowego wyniku

### Logowanie — NA BIEŻĄCO, od razu, nie na przypomnienie
- Polecenia użytkownika → `logwr.md`
- Twoje czynności → `logdone.md`
- Format: `| Nr | Data | Godzina | Treść |`

### Konwencje
- Język komunikacji: **polski**
- Mermaid: **ZAWSZE układ pionowy (TD)**, max 3 bloczki w rzędzie
- Działaj autonomicznie, raportuj wyniki

### Przy każdym starcie sesji
- Wczytaj `wytycznepodstawowe.md` — główne zasady projektu i dydaktyki
- Wczytaj `teoriadydaktyki/ramy_dydaktyczne.md` — struktura jednostki dydaktycznej, Backward Design, Bloom
