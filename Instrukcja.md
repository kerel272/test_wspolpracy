# Instrukcja obsługi -- Program Pogoda

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
   1. [System metryczny](#71-system-metryczny)
   2. [System imperialny](#72-system-imperialny)
8. [Źródło danych pogodowych](#8-źródło-danych-pogodowych)
9. [Obsługa błędów i komunikaty](#9-obsługa-błędów-i-komunikaty)
10. [Najczęstsze problemy (FAQ)](#10-najczęstsze-problemy-faq)
11. [Licencja i przeznaczenie](#11-licencja-i-przeznaczenie)
12. [Podsumowanie](#12-podsumowanie)

------------------------------------------------------------------------

## 1. Wprowadzenie

Program **Pogoda** jest narzędziem napisanym w języku
Python, służącym do sprawdzania aktualnych warunków pogodowych dla
wybranego miasta na świecie.  
Aplikacja została zaprojektowana tak, aby: - **nie wymagać klucza
API**,
- być **prosta w obsłudze**,
- działać zarówno w **trybie konsolowym (CLI)**, jak i **graficznym
(GUI)**.

Źródłem danych pogodowych jest publiczny serwis **wttr.in**, który
udostępnia aktualne informacje pogodowe w formacie JSON.

------------------------------------------------------------------------

## 2. Funkcjonalności programu

Program umożliwia: - sprawdzanie **aktualnej temperatury powietrza**, -
sprawdzanie **prędkości wiatru**, - wybór **jednostek metrycznych lub
imperialnych**, - podanie miasta wraz z **opcjonalnym kodem kraju**, -
obsługę zarówno przez **interfejs graficzny**, jak i **linię
poleceń**, - czytelne komunikaty błędów w języku polskim.

------------------------------------------------------------------------

## 3. Wymagania systemowe

### 3.1. Oprogramowanie

-   Python **3.8 lub nowszy**
-   System operacyjny:
    -   Windows
    -   Linux
    -   macOS

### 3.2. Wymagane biblioteki

-   `requests` -- do pobierania danych z internetu\
-   `tkinter` -- do obsługi interfejsu graficznego (zazwyczaj
    instalowana razem z Pythonem)

Instalacja biblioteki `requests`:

``` bash
pip install requests
```

------------------------------------------------------------------------

## 4. Struktura programu

Program składa się z następujących elementów: - funkcji `get_weather()`
-- pobieranie i przeliczanie danych pogodowych, - funkcji `show_gui()`
-- obsługa interfejsu graficznego, - funkcji `main()` -- obsługa
argumentów wiersza poleceń, - sekcji startowej
`if __name__ == "__main__":`.

------------------------------------------------------------------------

## 5. Sposoby uruchamiania programu

### 5.1. Tryb graficzny (GUI)

Uruchomienie:

``` bash
python pogoda.py --gui
```

Po uruchomieniu pojawi się okno aplikacji.

#### Elementy okna:

1.  **Pole „Miasto"** -- wymagane pole tekstowe
2.  **Pole „Kraj"** -- opcjonalny kod kraju (np. `PL`, `DE`, `US`)
3.  **Wybór jednostek**:
    -   Europejskie (°C, m/s)
    -   Amerykańskie (°F, mph)
4.  **Przycisk „Pokaż pogodę"**
5.  **Pole wyników** -- wyświetlanie temperatury i wiatru

------------------------------------------------------------------------

### 5.2. Tryb tekstowy (CLI)

Tryb tekstowy pozwala na szybkie użycie programu w terminalu lub w
skryptach automatyzujących.

#### Przykłady użycia

Podanie tylko miasta:

``` bash
python pogoda.py --city Warszawa
```

Podanie miasta i kraju:

``` bash
python pogoda.py --city Berlin --country DE
```

Jednostki imperialne:

``` bash
python pogoda.py --city NewYork --country US --units imperial
```

------------------------------------------------------------------------

## 6. Argumenty wiersza poleceń

  Argument      Opis                      Wymagany
  ------------- ------------------------- -----------
  `--city`      Nazwa miasta              Tak (CLI)
  `--country`   Kod kraju (ISO)           Nie
  `--units`     `metric` lub `imperial`   Nie
  `--gui`       Uruchamia GUI             Nie

------------------------------------------------------------------------

## 7. Jednostki miar

### 7.1. System metryczny

-   Temperatura: stopnie Celsjusza (°C)
-   Prędkość wiatru: metry na sekundę (m/s)

### 7.2. System imperialny

-   Temperatura: stopnie Fahrenheita (°F)
-   Prędkość wiatru: mile na godzinę (mph)

------------------------------------------------------------------------

## 8. Źródło danych pogodowych

Program korzysta z: - **https://wttr.in**

Dane pobierane są w formacie JSON i obejmują aktualne
warunki pogodowe.

Uwaga: - dostępność usługi zależy od serwisu wttr.in, - dane mogą być
opóźnione lub niedokładne.

------------------------------------------------------------------------

## 9. Obsługa błędów i komunikaty

Program wyświetli komunikat błędu w przypadku: - braku połączenia z
internetem, - nieprawidłowej nazwy miasta, - pustego pola miasta w
GUI, - problemów z odpowiedzią serwera.

Komunikaty błędów są prezentowane: - w GUI -- w oknie dialogowym, - w
CLI -- w standardowym wyjściu błędów.

------------------------------------------------------------------------

## 10. Najczęstsze problemy (FAQ)

### Program nie uruchamia się

-   Sprawdź wersję Pythona:

``` bash
python --version
```

### Brak biblioteki `requests`

``` bash
pip install requests
```

### Nie działa GUI

-   Upewnij się, że `tkinter` jest zainstalowany
-   Na Linuxie może być wymagane:

``` bash
sudo apt install python3-tk
```

------------------------------------------------------------------------
