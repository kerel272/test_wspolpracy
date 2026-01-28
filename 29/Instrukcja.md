Instrukcja obsługi programu „Pogoda (bez klucza API)” – przykład: Katowice
1. Opis programu

Program umożliwia sprawdzenie aktualnej temperatury oraz prędkości wiatru dla wybranego miasta.
Dane pobierane są z serwisu wttr.in, bez konieczności używania klucza API.

Program działa w dwóch trybach:

graficznym (GUI)

konsolowym (terminal)

2. Wymagania

Python 3.x

dostęp do Internetu

biblioteki:

requests

tkinter

3. Uruchamianie programu
🔹 Tryb graficzny (GUI)

Uruchomienie programu:

python pogoda.py --gui


Instrukcja krok po kroku:

W polu Miasto wpisz:

Katowice


W polu Kraj wpisz (opcjonalnie):

PL


Wybierz system jednostek:

Europejskie (°C, m/s) – domyślny

Amerykańskie (°F, mph)

Kliknij przycisk „Pokaż pogodę”

Program wyświetli aktualną temperaturę i prędkość wiatru dla Katowic.

🔹 Tryb konsolowy (terminal)

Podstawowe uruchomienie dla Katowic:

python pogoda.py --city Katowice


Z podanym krajem:

python pogoda.py --city Katowice --country PL


Z jednostkami amerykańskimi:

python pogoda.py --city Katowice --country PL --units imperial

4. Przykładowy wynik w konsoli
Temperatura: 12.4°C
Prędkość wiatru: 3.1 m/s


(lub w jednostkach amerykańskich):

Temperatura: 54.3°F
Prędkość wiatru: 6.9 mph

5. Obsługa błędów

Program wyświetli komunikat błędu, gdy:

nie zostanie wpisana nazwa miasta

podane miasto nie istnieje

brak połączenia z Internetem
