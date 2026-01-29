Oto instrukcja obsługi przygotowana zgodnie z Twoimi wytycznymi usunięto ikony, zachowano strukturę podanego przykładu, a w przykładach użycia zastosowano miasto Katowice.
Instrukcja obsługi -- Program Pogoda
Spis treści

    Wprowadzenie

    Funkcjonalności programu

    Wymagania systemowe

        Oprogramowanie

        Wymagane biblioteki

    Struktura programu

    Sposoby uruchamiania programu

        Tryb graficzny (GUI)

        Tryb tekstowy (CLI) i testowanie

    Argumenty wiersza poleceń

    Jednostki miar

        System metryczny

        System imperialny

    Źródło danych pogodowych

    Obsługa błędów i komunikaty

    Najczęstsze problemy (FAQ)

    Licencja i przeznaczenie

    Podsumowanie

1. Wprowadzenie

Program Pogoda jest narzędziem napisanym w języku Python, służącym do sprawdzania aktualnych warunków pogodowych dla wybranego miasta na świecie.

Aplikacja została zaprojektowana tak, aby

    nie wymagać klucza API,

    być prosta w obsłudze,

    działać zarówno w trybie konsolowym (CLI), jak i graficznym (GUI).

Źródłem danych pogodowych jest publiczny serwis wttr.in, który udostępnia aktualne informacje pogodowe w formacie JSON.
2. Funkcjonalności programu

Program umożliwia

    sprawdzanie aktualnej temperatury powietrza,

    sprawdzanie prędkości wiatru,

    wybór jednostek metrycznych lub imperialnych,

    podanie miasta wraz z opcjonalnym kodem kraju,

    obsługę zarówno przez interfejs graficzny, jak i linię poleceń,

    czytelne komunikaty błędów.

3. Wymagania systemowe
3.1. Oprogramowanie

    Python 3.6 lub nowszy

    System operacyjny

        Windows

        Linux

        macOS

3.2. Wymagane biblioteki

    requests -- do pobierania danych z internetu

    tkinter -- do obsługi interfejsu graficznego (biblioteka standardowa)

Instalacja biblioteki requests
Bash

pip install requests

4. Struktura programu

Program składa się z następujących elementów logicznych

    funkcja get_weather(city, country, units) -- pobiera dane JSON i przelicza jednostki,

    funkcja show_gui() -- buduje okno aplikacji przy użyciu biblioteki tkinter,

    funkcja main() -- przetwarza argumenty startowe przy użyciu biblioteki argparse,

    blok if __name__ == __main__ -- punkt wejścia programu.

5. Sposoby uruchamiania programu
5.1. Tryb graficzny (GUI)

Uruchomienie interfejsu okienkowego następuje poprzez dodanie flagi --gui.

Polecenie
Bash

python pogoda.py --gui

Po uruchomieniu pojawi się okno z polami do wpisania miasta (np. Katowice), kraju (np. PL) oraz opcją wyboru jednostek.
5.2. Tryb tekstowy (CLI) i testowanie

Tryb tekstowy pozwala na szybkie użycie programu w terminalu. Poniżej przedstawiono scenariusze testowe dla miasta Katowice.

Test 1 Podstawowe sprawdzenie pogody (Katowice)
Bash

python pogoda.py --city Katowice

Oczekiwany wynik Wyświetlenie temperatury w °C i wiatru w ms.

Test 2 Precyzowanie kraju (Katowice, Polska)
Bash

python pogoda.py --city Katowice --country PL

Test 3 Zmiana jednostek na imperialne (Katowice)
Bash

python pogoda.py --city Katowice --units imperial

Oczekiwany wynik Wyświetlenie temperatury w °F i wiatru w mph.
6. Argumenty wiersza poleceń

Poniższa tabela opisuje dostępne flagi przy uruchamianiu skryptu z konsoli
Argument	Opis	Wymagany	Domyślnie
--city	Nazwa miasta	Tak (w trybie CLI)	brak
--country	Kod kraju (np. PL, US)	Nie	pusty ciąg
--units	Jednostki (metricimperial)	Nie	metric
--gui	Uruchamia tryb graficzny	Nie	False

Jeśli program zostanie uruchomiony bez żadnych argumentów, wyświetli pomoc (help).
7. Jednostki miar

Program obsługuje dwa systemy jednostek, kontrolowane przez parametr units.
7.1. System metryczny (domyślny)

    Temperatura stopnie Celsjusza (°C)

    Prędkość wiatru metry na sekundę (ms) (przeliczane z kmh wartość  3.6)

7.2. System imperialny

    Temperatura stopnie Fahrenheita (°F) (przeliczane z °C)

    Prędkość wiatru mile na godzinę (mph) (przeliczane z kmh)

8. Źródło danych pogodowych

Program wysyła zapytania HTTP GET do serwisu

    Adres httpswttr.in{lokalizacja}format=j1

Odpowiedź serwera jest w formacie JSON, z którego skrypt wyciąga klucze temp_C oraz windspeedKmph.
9. Obsługa błędów i komunikaty

Program posiada wbudowaną obsługę wyjątków (try...except).

Sytuacje awaryjne

    Brak połączenia z siecią.

    Błędna nazwa miasta (kod HTTP inny niż 200).

    Timeout (przekroczenie czasu oczekiwania 10s).

W trybie GUI błędy wyświetlane są jako wyskakujące okno (MessageBox) z tytułem Błąd. W trybie CLI komunikat błędu wypisywany jest na standardowe wyjście błędów (sys.stderr).
