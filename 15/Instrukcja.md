# Instrukcja do programu do sprawdzania pogody napisanego w języku Python

Dane pogodowe pobierane są z serwisu wttr.in, który nie wymagaja klucza API.

Wymagania systemowe

-Python 3.8 lub nowszy

-Dostęp do Internetu

Biblioteki do zainstalowania

-requests

-tkinter

Instalacja biblioteki requests
```
pip install requests
```

Uruchamianie programu
```
python nazwa_pliku.py
```

Obsługa

W polu Miasto wpisz nazwę miasta (np. Warszawa)

Opcjonalnie w polu Kraj wpisz kod kraju:

-PL – Polska

-US – USA

-DE – Niemcy

Wybierz system jednostek:

-Europejskie – °C, m/s

-Amerykańskie – °F, mph

Kliknij „Pokaż pogodę”

W oknie zostanie wyświetlona:

-temperatura,

-prędkość wiatru.

W przypadku błędu pojawi się komunikat dialogowy.

Tryb konsolowy (CLI)
Podstawowe użycie
```
python nazwa_pliku.py --city Warszawa
```

Dostępne argumenty:
```
--city	Nazwa miasta (wymagane)
--country	Kod kraju (opcjonalny)
--units	metric lub imperial
--gui	Uruchamia interfejs graficzny
```


Przykłady użycia:

Miasto + jednostki metryczne (domyślne)
```
python pogoda.py --city Katowice
```

Miasto + kraj
```
python pogoda.py --city Berlin --country DE
```

Jednostki amerykańskie
```
python pogoda.py --city NewYork --country US --units imperial
```

Wynik w konsoli
```
Temperatura: 21.3°C
Prędkość wiatru: 3.5 m/s
```

Program wyświetli komunikat błędu, gdy:

-nie podano miasta,

-brak połączenia z Internetem,

-podano niepoprawną nazwę miasta lub kraju.

Informacje techniczne:

-Dane pogodowe: https://wttr.in

-Brak potrzeby klucza API

-Interfejs graficzny oparty na Tkinter

-Komunikacja sieciowa przez requests
