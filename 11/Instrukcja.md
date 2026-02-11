# Aplikacja „Pogoda”

Aplikacja do sprawdzania aktualnej temperatury i prędkości wiatru dla dowolnego miasta. Dane pobierane są z serwisu **wttr.in**.

---
# Spis treści
- [Aplikacja „Pogoda”](#aplikacja-pogoda)
  - [Funkcje aplikacji](#funkcje-aplikacji)
  - [Wymagania](#wymagania)
  - [Uruchamianie](#uruchamianie)
    - [Uruchamianie w trybie graficznym (GUI)](#uruchamianie-w-trybie-graficznym-gui)
    - [Uruchamianie w trybie terminalowym (CLI)](#uruchamianie-w-trybie-terminalowym-cli)
  - [Jak działa aplikacja](#jak-działa-aplikacja)
    - [1. Pobieranie danych pogodowych](#1-pobieranie-danych-pogodowych)
    - [2. Przeliczanie jednostek](#2-przeliczanie-jednostek)
    - [3. Obsługa trybu CLI](#3-obsługa-trybu-cli)
    - [4. Obsługa trybu GUI](#4-obsługa-trybu-gui)
    - [5. Obsługa błędów](#5-obsługa-błędów)
  - [Struktura programu](#struktura-programu)
  - [Najważniejsze cechy aplikacji](#najważniejsze-cechy-aplikacji)
---
## Funkcje aplikacji

- Pobieranie aktualnej pogody z wttr.in  
- Obsługa **CLI** (terminal)  
- Obsługa **GUI** (interfejs graficzny Tkinter)  
- Wybór jednostek:  
  - `metric` → °C i m/s  
  - `imperial` → °F i mph  

---

## Wymagania

- Python 3.7+
- Biblioteki:
  - `requests`
  - `tkinter` (zwykle dostępny domyślnie)

Instalacja brakujących pakietów:

```bash
pip install requests
```
---

## Uruchamianie

Aplikację można uruchomić na dwa sposoby: w trybie graficznym (GUI) lub terminalowym (CLI).

---

### Uruchamianie w trybie graficznym (GUI)

Aby uruchomić interfejs graficzny:

```bash
python app.py --gui
```

---
#### Po uruchomieniu GUI możesz:
- wpisać miasto
- opcjonalnie podać kod kraju (np. PL, US)
- wybrać jednostki (metric lub imperial)
- kliknąć Pokaż pogodę, aby wyświetlić temperaturę i prędkość wiatr

---

### Uruchamianie w trybie terminalowym (CLI)

Aby pobrać pogodę bez GUI, użyj argumentów:
|Argument   |Opis              |
|-----------|------------------|
|`--city`   |Nazwa miasta (wymagane w trybie CLI)|
|`--country`|Kod kraju, np. PL, US (opcjonalne)|
|`--units`  |`metric` lub `imperial`|
|`--gui`    |Uruchamia tryb graficzny|

```bash
python app.py --city <miasto> [--country <kod>] [--units metric|imperial]
```
#### Przykłady:
Pogoda dla Krakowa:
```bash
python app.py --city Kraków
```
Pogoda dla Londynu z podaniem kraju:
```bash
python app.py --city London --country UK
```
Jednostki amerykańskie:
```bash
python app.py --city Chicago --units imperial
```
Wyświetlenie pomocy:
```bash
python app.py --help
```

---

## Jak działa aplikacja?

Aplikacja korzysta z publicznego serwisu pogodowego **wttr.in**, który udostępnia dane w formacie JSON. Logika działania składa się z kilku etapów:

---

### 1. Pobieranie danych pogodowych

Za pobieranie informacji odpowiada funkcja:

```python
get_weather(city, country="", units="metric")
```
#### Jej działanie:
- Buduje lokalizację w formacie `miasto,kraj` (jeśli kraj został podany).
- Wysyła zapytanie HTTP do:
   ```code
   https://wttr.in/<lokalizacja>?format=j1
   ```
- Odbiera dane w formacie JSON.
- Odczytuje:
  - aktualną temperaturę (`temp_C`)
  - prędkość wiatru (`windspeedKmph`)

### 2. Przeliczanie jednostek
W zależności od wybranych ustawień:
- metric
  - temperatura: °C
  - wiatr: km/h → m/s
- imperial
  - temperatura: °F
  - wiatr: km/h → mph

Przeliczenia wykonywane są ręcznie w kodzie.
### 3. Obsługa trybu CLI
W trybie terminalowym aplikacja:
- odczytuje argumenty (`--city`, `--country`, `--units`)
- wywołuje `get_weather()`
- wyświetla wynik w konsoli

Jeśli nie podano miasta, wyświetlana jest pomoc (`--help`).
### 4. Obsługa trybu GUI
Po uruchomieniu z parametrem `--gui`:
- Tworzony jest interfejs Tkinter
- Użytkownik wpisuje miasto, opcjonalnie kraj i wybiera jednostki
- Po kliknięciu Pokaż pogodę:
  - wywoływana jest funkcja `get_weather()`
  - wynik pojawia się w etykiecie pod przyciskiem
- Błędy (np. brak internetu lub złe miasto) wyświetlane są w oknach dialogowych
### 5. Obsługa błędów
Aplikacja przechwytuje typowe problemy:
- brak połączenia z internetem
- nieistniejące miasto
- błędny format odpowiedzi

W takich przypadkach użytkownik otrzymuje komunikat:
> „Nie udało się pobrać pogody dla `<miasto>`. Sprawdź nazwę lub połączenie.”

---
## Struktura programu
- **get_weather** – pobieranie i przetwarzanie danych
- **show_gui** – interfejs graficzny
- **main** – obsługa argumentów i logika uruchamiania

---

## Najważniejsze cechy aplikacji:

- działa bez konfiguracji i bez rejestracji w zewnętrznych usługach  
- obsługuje dwa tryby pracy: **CLI** i **GUI**  
- umożliwia wybór jednostek (metric / imperial)  
- wyświetla temperaturę oraz prędkość wiatru  
- informuje o błędach, gdy lokalizacja jest nieprawidłowa lub brak połączenia 
