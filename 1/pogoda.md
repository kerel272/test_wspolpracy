# Instrukcja obsługi – Pogoda (bez klucza API)

## Opis programu
Program **Pogoda (bez klucza!)** to aplikacja napisana w Pythonie, która umożliwia sprawdzanie aktualnej temperatury oraz prędkości wiatru dla wybranego miasta.  
Dane pogodowe są pobierane z serwisu **wttr.in**, co oznacza, że **nie jest wymagany żaden klucz API**.

Program może działać:
- w **trybie konsolowym (CLI)**,
- w **trybie graficznym (GUI)** opartym o bibliotekę `tkinter`.

---

## Wymagania
Aby uruchomić program, potrzebujesz:

- Python **3.8 lub nowszy**
- Dostęp do internetu
- Zainstalowane biblioteki:
  - `requests`
  - `tkinter` (zwykle dostępna domyślnie w Pythonie)

### Instalacja wymaganych bibliotek
Jeśli nie masz biblioteki `requests`, zainstaluj ją poleceniem:
```bash
pip install requests
```

---

## Uruchamianie programu

Plik programu należy uruchamiać z poziomu terminala / wiersza poleceń:

```bash
python pogoda.py [opcje]
```

---

## Tryb graficzny (GUI)

Aby uruchomić aplikację z interfejsem graficznym, użyj flagi:

```bash
python pogoda.py --gui
```

### Obsługa GUI
1. Wpisz **nazwę miasta** (np. `Warszawa`).
2. Opcjonalnie wpisz **kod kraju** (np. `PL`, `US`).
3. Wybierz jednostki:
   - Europejskie: °C i m/s
   - Amerykańskie: °F i mph
4. Kliknij **„Pokaż pogodę”**.
5. Wynik pojawi się w oknie aplikacji.

---

## Tryb konsolowy (CLI)

### Podstawowe użycie
```bash
python pogoda.py --city Warszawa
```

### Z kodem kraju
```bash
python pogoda.py --city Berlin --country DE
```

### Jednostki amerykańskie
```bash
python pogoda.py --city New York --country US --units imperial
```

### Dostępne argumenty
| Argument | Opis |
|--------|------|
| `--city` | Nazwa miasta |
| `--country` | Kod kraju (np. PL, DE, US) |
| `--units` | `metric` (domyślne) lub `imperial` |
| `--gui` | Uruchamia interfejs graficzny |

---

## Wyświetlane dane
Program pokazuje:
- **Temperaturę**
  - °C (tryb metric)
  - °F (tryb imperial)
- **Prędkość wiatru**
  - m/s (tryb metric)
  - mph (tryb imperial)

---

## Obsługa błędów
Program wyświetli komunikat błędu, gdy:
- nie podano nazwy miasta,
- miasto nie istnieje,
- brak połączenia z internetem,
- serwis wttr.in jest niedostępny.

W trybie GUI błędy pojawiają się w oknach dialogowych,  
w trybie CLI – jako komunikaty w terminalu.

---

## Uwagi techniczne
- Program korzysta z publicznego API `wttr.in` w formacie JSON.
- Dane pogodowe są aktualne, ale nie gwarantują dokładności meteorologicznej.
- Aplikacja nie zapisuje żadnych danych lokalnie.

---

## Autor
Program i instrukcja – użytkowe narzędzie edukacyjne w Pythonie.

