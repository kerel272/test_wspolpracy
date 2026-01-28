# Aplikacja „Pogoda bez klucza API”

Prosta aplikacja do sprawdzania aktualnej temperatury i prędkości wiatru dla dowolnego miasta — bez konieczności używania klucza API. Dane pobierane są z serwisu **wttr.in**.

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

Aplikacja korzysta z publicznego serwisu pogodowego **wttr.in**, który udostępnia dane w formacie JSON bez konieczności używania klucza API. Logika działania składa się z kilku etapów:

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
## Podsumowanie

Aplikacja „Pogoda bez klucza API” to proste i wygodne narzędzie do szybkiego sprawdzania aktualnych warunków pogodowych. Działa zarówno w terminalu, jak i w intuicyjnym interfejsie graficznym, a dzięki wykorzystaniu serwisu wttr.in nie wymaga żadnego klucza API.

Najważniejsze cechy aplikacji:

- działa bez konfiguracji i bez rejestracji w zewnętrznych usługach  
- obsługuje dwa tryby pracy: **CLI** i **GUI**  
- umożliwia wybór jednostek (metric / imperial)  
- wyświetla temperaturę oraz prędkość wiatru  
- informuje o błędach, gdy lokalizacja jest nieprawidłowa lub brak połączenia  
