# Pogoda – Instrukcja użytkownika

## Spis treści
1. [Opis programu](#opis-programu)
2. [Wymagania](#wymagania)
3. [Tryb graficzny (GUI)](#tryb-graficzny-gui)
4. [Tryb tekstowy (CLI)](#tryb-tekstowy-cli)
5. [Prezentowane dane](#prezentowane-dane)
6. [Obsługa błędów](#obsługa-błędów)

---

## Opis programu

**Pogoda** to prosty program w Pythonie, który pozwala szybko sprawdzić aktualną temperaturę i prędkość wiatru dla wybranego miasta. Dane pobierane są z serwisu **wttr.in*. 

Program działa w dwóch trybach:

- **CLI** – obsługa z poziomu terminala  
- **GUI** – okienkowy interfejs graficzny (Tkinter)

---

## Wymagania

- Python **3.8+**
- Internet
- Biblioteki:
  - `requests`
  - `tkinter` (standardowo w Pythonie)

Instalacja biblioteki `requests`:

```bash
pip install requests
```

---

## Tryb graficzny (GUI)

### Uruchomienie

```bash
python pogoda.py --gui
```

### Instrukcja obsługi

1. Wpisz **Miasto** (np. `Katowice`)  
2. Opcjonalnie podaj **Kraj** (np. `PL`)  
3. Wybierz jednostki:
   - **Europejskie**: °C, m/s
   - **Amerykańskie**: °F, mph
4. Kliknij **„Pokaż pogodę”**  
5. Dane pojawią się w dolnej części okna  

---

## Tryb tekstowy (CLI)

### Przykład

```bash
python pogoda.py --city Katowice --country PL --units metric
```

Parametry:

- `--city` – nazwa miasta
- `--country` – kod kraju (opcjonalny)
- `--units` – `metric` lub `imperial`

**Przykładowy wynik:**

```
Temperatura: 7.3°C
Prędkość wiatru: 2.8 m/s
```

---

## Prezentowane dane

Program pokazuje:

| Dane | Jednostki metryczne | Jednostki amerykańskie |
|------|-------------------|------------------------|
| Temperatura | °C | °F |
| Wiatr | m/s | mph |

---

## Obsługa błędów

- Brak miasta → komunikat ostrzegawczy
- Nieprawidłowa lokalizacja lub brak internetu → komunikat o błędzie

---
