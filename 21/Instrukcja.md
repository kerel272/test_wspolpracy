# Instrukcja obsługi programu „Pogoda”

## Opis programu
Program **Pogoda** służy do sprawdzania aktualnej temperatury oraz prędkości wiatru
dla wybranego miasta. Dane pogodowe pobierane są z serwisu **wttr.in** i nie wymagają
klucza API.

Program może działać w dwóch trybach:
- tekstowym (w konsoli)
- graficznym (GUI)

---

## Wymagania
- Python 3
- Biblioteki:
  - requests
  - tkinter (standardowo w Pythonie)

Instalacja biblioteki `requests` (jeśli nie jest zainstalowana):
```bash
pip install requests
```

---

## Uruchamianie programu

Plik programu:
```bash
pogoda.py
```

### 1. Tryb konsolowy

Aby uruchomić program w trybie tekstowym, należy podać nazwę miasta:

```bash
python pogoda.py --city Katowice
```

Opcjonalnie można podać:

* kraj (np. PL)
* jednostki miary

Przykład:

```bash
python pogoda.py --city Katowice --country PL --units metric
```

Dostępne jednostki:

* `metric` – stopnie Celsjusza (°C) i m/s
* `imperial` – stopnie Fahrenheita (°F) i mph

---

### 2. Tryb graficzny (GUI)

Aby uruchomić wersję z interfejsem graficznym:

```bash
python pogoda.py --gui
```

W oknie programu należy:

1. Wpisać nazwę miasta (np. **Katowice**)
2. Opcjonalnie wpisać kod kraju (PL)
3. Wybrać system jednostek
4. Kliknąć przycisk **„Pokaż pogodę”**

Wynik zostanie wyświetlony w oknie aplikacji.

---

## Test programu

Program został przetestowany dla miasta:

```text
Katowice
```

Program poprawnie wyświetla:

* aktualną temperaturę
* prędkość wiatru

---

## Obsługa błędów

* Jeśli miasto nie zostanie podane, program wyświetli komunikat o błędzie
* W przypadku braku połączenia z internetem pojawi się komunikat o niepowodzeniu pobierania danych

---

## Autor

Imię i nazwisko: **Oliwier Stawowczyk**
Numer z dziennika: **21**