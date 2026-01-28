# Instrukcja obsługi programu „Pogoda” 

Program „Pogoda” pobiera aktualne dane meteorologiczne z serwisu **wttr.in** i wyświetla temperaturę oraz prędkość wiatru. Aplikacja działa w dwóch trybach:
- **CLI (tekstowy)** – uruchamiany w terminalu
- **GUI (graficzny)** – prosty interfejs okienkowy (Tkinter)

---

## 1. Wymagania systemowe

### 1.1. Oprogramowanie
- **Python 3.x**
- Dostęp do Internetu (program pobiera dane online)

### 1.2. Biblioteki
- `requests` – obsługa HTTP
- `tkinter` – GUI (zwykle wbudowany w Pythona)

Instalacja `requests`:
```bash
pip install requests
```

---

## 2. Struktura programu

Plik główny:
```
pogoda.py
```

Program uruchamia się w trybie:
- GUI – jeśli podano `--gui`
- CLI – jeśli podano `--city`
- Pomoc – jeśli nie podano żadnych argumentów

---

## 3. Tryb GUI (graficzny)

### Uruchomienie:
```bash
python3 pogoda.py --gui
```

### Funkcje interfejsu:
- **Miasto** – obowiązkowe pole tekstowe
- **Kraj** – opcjonalny kod kraju (np. PL, US, DE)
- **Jednostki**:
  - Europejskie: °C i m/s
  - Amerykańskie: °F i mph
- Przycisk **„Pokaż pogodę”** – pobiera dane i wyświetla wynik

### Przykładowe dane wejściowe:
- Miasto: `Warszawa`
- Kraj: `PL`
- Jednostki: Europejskie

---

## 4. Tryb CLI (tekstowy)

### Podstawowe użycie:
```bash
python3 pogoda.py --city Warszawa
```

### Z kodem kraju:
```bash
python3 pogoda.py --city London --country GB
```

### Jednostki amerykańskie:
```bash
python3 pogoda.py --city NewYork --country US --units imperial
```

---

## 5. Dostępne argumenty

| Argument | Typ | Opis |
|---------|-----|------|
| `--city` | string | Nazwa miasta (wymagana w trybie CLI) |
| `--country` | string | Kod kraju (np. PL, US). Opcjonalny |
| `--units` | string | `metric` lub `imperial` (domyślnie `metric`) |
| `--gui` | flaga | Uruchamia interfejs graficzny |

---

## 6. Jednostki i przeliczenia

Program automatycznie przelicza:
- **temperaturę** z °C na °F (jeśli `imperial`)
- **wiatr** z km/h na mph (jeśli `imperial`)
- w trybie `metric` wiatr podawany jest w **m/s**

---

## 7. Przykładowy wynik (CLI)

```
Temperatura: 21.4°C
Prędkość wiatru: 3.2 m/s
```

---

## 8. Obsługa błędów

Program zwraca komunikat błędu, gdy:
- nazwa miasta jest pusta
- podana nazwa miasta nie istnieje
- brak połączenia z Internetem
- serwis wttr.in nie odpowiada

Przykład komunikatu:
```
Błąd: Nie udało się pobrać pogody dla 'Xyz'. Sprawdź nazwę lub połączenie.
```

---

## 9. Uwagi praktyczne

- Nazwy miast najlepiej podawać bez polskich znaków (np. `Krakow`, `Lodz`)
- Kod kraju pomaga rozróżnić miasta o tej samej nazwie
- Program nie wymaga klucza API

---

## 10. Szybka ściąga

| Cel | Polecenie |
|-----|-----------|
| GUI | `python3 pogoda.py --gui` |
| CLI (miasto) | `python3 pogoda.py --city Warszawa` |
| CLI + kraj | `python3 pogoda.py --city London --country GB` |
| CLI + imperial | `python3 pogoda.py --city NewYork --country US --units imperial` |

---

**Autor programu:** `pogoda.py`  
**Źródło danych:** https://wttr.in