# Instrukcja użytkowania programu „Pogoda”

### Informacje o programie

Aplikacja „Pogoda” umożliwia sprawdzanie bieżącej temperatury oraz siły wiatru dla wybranego miasta. Dane meteorologiczne są pobierane ze strony wttr.in, dlatego nie jest potrzebny żaden klucz API.
Program może być uruchamiany zarówno w wersji tekstowej, jak i z interfejsem graficznym.

---

### Wymagania systemowe

Do poprawnego działania programu potrzebne są:

* Python w wersji 3
* aktywne połączenie z internetem
* biblioteki:

  * `requests`
  * `tkinter`

Jeżeli biblioteka `requests` nie jest zainstalowana, można ją dodać poleceniem:

```
pip install requests
```

---

### Uruchamianie programu

Program startuje z poziomu wiersza poleceń za pomocą komendy:

```
python pogoda.py
```

---

## Tryb graficzny (GUI)

### Start programu

Aby włączyć wersję z oknem graficznym, należy użyć polecenia:

```
python pogoda.py --gui
```

### Korzystanie z aplikacji

1. Wpisz nazwę miasta (np. Katowice).
2. Opcjonalnie podaj kod państwa (np. PL).
3. Wybierz system jednostek:

   * europejski (°C, m/s),
   * amerykański (°F, mph).
4. Kliknij przycisk **„Pokaż pogodę”**.
5. Sprawdź wyświetlone dane pogodowe.

---

## Tryb tekstowy (konsola)

### Przykład użycia

```
python pogoda.py --city Katowice --country PL
```

### Jednostki imperialne

```
python pogoda.py --city Katowice --country PL --units imperial
```

---

### Dostępne parametry

| Parametr    | Znaczenie                  |
| ----------- | -------------------------- |
| `--city`    | nazwa miasta               |
| `--country` | kod kraju                  |
| `--units`   | metric lub imperial        |
| `--gui`     | uruchamia wersję graficzną |
| `--help`    | wyświetla pomoc            |

---

### Przykładowy wynik działania

Temperatura: 18.2°C
Prędkość wiatru: 3.5 m/s

---

## Obsługa błędów

Podczas działania programu mogą wystąpić różne problemy. Każdy z nich jest sygnalizowany odpowiednim komunikatem.

### Niepodana miejscowość

**Opis:** użytkownik nie wpisał miasta
**Komunikat:** prośba o podanie nazwy miasta
**Rozwiązanie:** wpisać nazwę i spróbować ponownie

### Nieprawidłowa nazwa miasta

**Opis:** miasto nie istnieje lub zostało źle zapisane
**Komunikat:** błąd pobierania danych
**Rozwiązanie:** poprawić nazwę miasta lub dodać kod kraju

### Brak internetu

**Opis:** program nie może połączyć się z siecią
**Komunikat:** informacja o braku dostępu do danych
**Rozwiązanie:** sprawdzić połączenie i ponownie uruchomić program

### Niedostępny serwis pogodowy

**Opis:** strona wttr.in chwilowo nie działa
**Komunikat:** błąd odczytu danych
**Rozwiązanie:** odczekać kilka minut i spróbować ponownie

### Brak biblioteki `requests`

**Opis:** brak wymaganej biblioteki w systemie
**Objaw:** program się nie uruchamia
**Rozwiązanie:** zainstalować bibliotekę poleceniem:

```
pip install requests
```

Program nie zamyka się automatycznie i umożliwia użytkownikowi poprawienie błędnych danych.

---

## Słowniczek

**GUI** – graficzny interfejs użytkownika umożliwiający obsługę programu za pomocą okna.

**Konsola** – tryb tekstowy, w którym program uruchamiany jest przy pomocy poleceń.

**API** – sposób komunikacji z usługami internetowymi (w tym programie nie jest wymagany klucz).

**Jednostki metryczne** – stopnie Celsjusza (°C) oraz metry na sekundę (m/s).

**Jednostki imperialne** – stopnie Fahrenheita (°F) oraz mile na godzinę (mph).

**Kod kraju** – dwuliterowy skrót państwa, np. PL (Polska), SK (Słowacja), DK (Dania).

 
