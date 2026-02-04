
# Instrukcja obsługi — Program Pogoda

## Spis treści

1. [Wprowadzenie](#1-wprowadzenie)
2. [Funkcjonalności programu](#2-funkcjonalności-programu)
3. [Wymagania systemowe](#3-wymagania-systemowe)
   1. [Oprogramowanie](#31-oprogramowanie)
   2. [Wymagane biblioteki](#32-wymagane-biblioteki)
4. [Struktura programu](#4-struktura-programu)
5. [Sposoby uruchamiania programu](#5-sposoby-uruchamiania-programu)
   1. [Tryb graficzny (GUI)](#51-tryb-graficzny-gui)
   2. [Tryb tekstowy (CLI)](#52-tryb-tekstowy-cli)
6. [Argumenty wiersza poleceń](#6-argumenty-wiersza-poleceń)
7. [Jednostki miar](#7-jednostki-miar)
8. [Źródło danych pogodowych](#8-źródło-danych-pogodowych)
9. [Obsługa błędów i komunikaty](#9-obsługa-błędów-i-komunikaty)
10. [Najczęstsze problemy (FAQ)](#10-najczęstsze-problemy-faq)

---

## 1. Wprowadzenie

Program **Pogoda** to aplikacja napisana w języku Python, służąca do
sprawdzania aktualnych warunków pogodowych dla wybranego miasta na świecie.

Najważniejsze cechy programu:
- brak konieczności używania klucza API,
- prosta i intuicyjna obsługa,
- możliwość pracy w trybie tekstowym (CLI) oraz graficznym (GUI).

Dane pogodowe pobierane są z publicznego serwisu **wttr.in**, który
udostępnia aktualne informacje pogodowe w formacie JSON.

---

## 2. Funkcjonalności programu

Program umożliwia:
- sprawdzanie aktualnej temperatury powietrza,
- sprawdzanie prędkości wiatru,
- wybór jednostek metrycznych lub imperialnych,
- podanie miasta wraz z opcjonalnym kodem kraju,
- obsługę poprzez interfejs graficzny lub linię poleceń,
- wyświetlanie czytelnych komunikatów błędów w języku polskim.

---

## 3. Wymagania systemowe

### 3.1. Oprogramowanie

- Python w wersji **3.8 lub nowszej**
- System operacyjny:
  - Windows
  - Linux
  - macOS

### 3.2. Wymagane biblioteki

- `requests` — pobieranie danych pogodowych z internetu
- `tkinter` — obsługa interfejsu graficznego (zwykle instalowana razem z Pythonem)

Instalacja biblioteki `requests`:

```bash
pip install requests
```

---

## 4. Struktura programu

Kod programu składa się z następujących elementów:
- `get_weather()` — pobieranie i przeliczanie danych pogodowych,
- `show_gui()` — obsługa interfejsu graficznego,
- `main()` — obsługa argumentów wiersza poleceń,
- sekcja startowa `if __name__ == "__main__":`.

---

## 5. Sposoby uruchamiania programu

### 5.1. Tryb graficzny (GUI)

Uruchomienie programu w trybie graficznym:

```bash
python pogoda.py --gui
```

Po uruchomieniu pojawi się okno aplikacji umożliwiające wprowadzenie danych.

**Elementy interfejsu:**
1. Pole *Miasto* — pole wymagane
2. Pole *Kraj* — opcjonalny kod kraju (np. `PL`, `DE`, `US`)
3. Wybór jednostek:
   - Europejskie (°C, m/s)
   - Amerykańskie (°F, mph)
4. Przycisk *Pokaż pogodę*
5. Obszar wyników z aktualną temperaturą i prędkością wiatru

---

### 5.2. Tryb tekstowy (CLI)

Tryb tekstowy umożliwia szybkie sprawdzenie pogody bez uruchamiania okna
graficznego.

**Przykłady użycia:**

Podanie samego miasta:
```bash
python pogoda.py --city Warszawa
```

Podanie miasta i kraju:
```bash
python pogoda.py --city Berlin --country DE
```

Użycie jednostek imperialnych:
```bash
python pogoda.py --city NewYork --country US --units imperial
```

---

## 6. Argumenty wiersza poleceń

| Argument     | Opis                    | Wymagany |
|-------------|-------------------------|----------|
| `--city`    | Nazwa miasta            | Tak (CLI) |
| `--country` | Kod kraju (ISO)         | Nie |
| `--units`   | `metric` lub `imperial` | Nie |
| `--gui`     | Uruchamia tryb GUI      | Nie |

---

## 7. Jednostki miar

- **System metryczny**
  - temperatura: stopnie Celsjusza (°C)
  - prędkość wiatru: metry na sekundę (m/s)

- **System imperialny**
  - temperatura: stopnie Fahrenheita (°F)
  - prędkość wiatru: mile na godzinę (mph)

---

## 8. Źródło danych pogodowych

Program korzysta z publicznego serwisu:
- **https://wttr.in**
- Testy zostały przeprowadzona dla miasta Katowice
Dane pobierane są w formacie JSON i przedstawiają aktualne warunki
pogodowe.

Uwaga:
- dostępność usługi zależy od działania serwisu wttr.in,
- dane mogą być opóźnione lub niedokładne.

---

## 9. Obsługa błędów i komunikaty

Program wyświetla komunikaty błędów w przypadku:
- braku połączenia z internetem,
- nieprawidłowej nazwy miasta,
- nieuzupełnienia pola miasta w trybie GUI,
- problemów z odpowiedzią serwera.

Komunikaty:
- w GUI — wyświetlane w oknach dialogowych,
- w CLI — wypisywane na standardowe wyjście błędów.

---

## 10. Najczęstsze problemy (FAQ)

**Program nie uruchamia się**
- Sprawdź wersję Pythona:
```bash
python --version
```

**Brak biblioteki `requests`**
```bash
pip install requests
```

**Nie działa interfejs graficzny**
- Upewnij się, że `tkinter` jest zainstalowany
- W systemach Linux może być wymagane:
```bash
sudo apt install python3-tk
```
