#  Instrukcja obsługi programu Pogoda

Program **Pogoda** umożliwia sprawdzenie aktualnej temperatury oraz
prędkości wiatru dla wybranego miasta. Dane pobierane są z serwisu
**wttr.in** (bez potrzeby używania klucza API).

------------------------------------------------------------------------

##  Wymagania

-   Python 3.7 lub nowszy
-   Biblioteka `requests`

Instalacja:

    pip install requests

------------------------------------------------------------------------

##  Uruchamianie programu

### Tryb graficzny (GUI)

    python pogoda.py --gui

1.  Wpisz miasto: **Katowice**
2.  (Opcjonalnie) wpisz kraj: **PL**
3.  Wybierz jednostki
4.  Kliknij „Pokaż pogodę"

------------------------------------------------------------------------

### Tryb konsolowy (CLI)

Podstawowe użycie:

    python pogoda.py --city Katowice --country PL

Jednostki amerykańskie:

    python pogoda.py --city Katowice --country PL --units imperial

------------------------------------------------------------------------

##  Test dla miasta Katowice

    python pogoda.py --city Katowice --country PL

Przykładowy wynik:

    Temperatura: 5.2°C
    Prędkość wiatru: 3.4 m/s

------------------------------------------------------------------------

##  Dostępne argumenty

  Argument    Opis
  ----------- -----------------------------------------
  --city      Nazwa miasta
  --country   Kod kraju (np. PL, US)
  --units     metric (°C, m/s) lub imperial (°F, mph)
  --gui       Uruchamia tryb graficzny

------------------------------------------------------------------------

##  Obsługa błędów

Program wyświetli komunikat o błędzie, gdy: - nie podano miasta - brak
połączenia z internetem - podano niepoprawną nazwę miasta

------------------------------------------------------------------------

##  Jak działa program?

1.  Wysyła zapytanie do: https://wttr.in/{miasto}?format=j1
2.  Odczytuje dane JSON
3.  Wyświetla temperaturę i prędkość wiatru
