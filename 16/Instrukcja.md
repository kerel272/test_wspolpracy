# Instrukcja obsługi – Pogoda (bez klucza API)

## Opis programu
Program **Pogoda (bez klucza!)** to aplikacja napisana w języku Python, która umożliwia sprawdzanie aktualnej temperatury oraz prędkości wiatru dla wybranego miasta.  
Dane pogodowe pobierane są z serwisu **wttr.in**, dzięki czemu **nie jest wymagany żaden klucz API**.

Program może działać:
- w **trybie konsolowym (CLI)**,
- w **trybie graficznym (GUI)** opartym o bibliotekę `tkinter`.

---

## Wymagania
Aby uruchomić program, wymagane są:

- Python **3.8 lub nowszy**
- Dostęp do internetu
- Zainstalowane biblioteki:
  - `requests`
  - `tkinter` (zwykle dostępna domyślnie w Pythonie)

### Instalacja wymaganych bibliotek
Jeśli biblioteka `requests` nie jest zainstalowana, należy ją dodać poleceniem:
```bash
pip install requests
````

---

## Uruchamianie programu

Plik programu należy uruchamiać z poziomu terminala / wiersza poleceń:

```bash
python pogoda.py [opcje]
```

---

## Tryb graficzny (GUI)

Aby uruchomić aplikację w trybie graficznym, należy użyć flagi:

```bash
python pogoda.py --gui
```

### Obsługa GUI

1. Wpisz **nazwę miasta** (np. `Katowice`).
2. Opcjonalnie wpisz **kod kraju** (np. `PL`).
3. Wybierz jednostki:

   * Europejskie: °C i m/s
   * Amerykańskie: °F i mph
4. Kliknij przycisk **„Pokaż pogodę”**.
5. Wynik zostanie wyświetlony w oknie aplikacji.

---

## Tryb konsolowy (CLI)

### Podstawowe użycie

```bash
python pogoda.py --city Katowice
```

### Z kodem kraju

```bash
python pogoda.py --city Katowice --country PL
```

### Jednostki amerykańskie

```bash
python pogoda.py --city Katowice --country PL --units imperial
```

### Dostępne argumenty

| Argument    | Opis                               |
| ----------- | ---------------------------------- |
| `--city`    | Nazwa miasta                       |
| `--country` | Kod kraju (np. PL, DE, US)         |
| `--units`   | `metric` (domyślne) lub `imperial` |
| `--gui`     | Uruchamia interfejs graficzny      |

---

## Wyświetlane dane

Program wyświetla:

* **Temperaturę**

  * °C w trybie `metric`
  * °F w trybie `imperial`
* **Prędkość wiatru**

  * m/s w trybie `metric`
  * mph w trybie `imperial`

---

## Obsługa błędów

Program wyświetli komunikat błędu w następujących przypadkach:

* nie podano nazwy miasta,
* podano nieistniejące miasto,
* brak połączenia z internetem,
* serwis `wttr.in` jest chwilowo niedostępny.

W trybie graficznym błędy pojawiają się w oknach dialogowych,
natomiast w trybie konsolowym jako komunikaty w terminalu.

---

## Uwagi techniczne

* Program korzysta z publicznego API serwisu `wttr.in` w formacie JSON.
* Dane pogodowe są aktualne, jednak nie stanowią oficjalnej prognozy meteorologicznej.
* Aplikacja nie zapisuje żadnych danych lokalnie.

---
