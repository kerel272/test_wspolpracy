# Instrukcja obsługi programu „Pogoda”

## Opis programu

Program „Pogoda” służy do sprawdzania aktualnej temperatury oraz prędkości wiatru dla wybranego miasta. Dane pogodowe pobierane są ze strony **wttr.in**, więc program nie wymaga klucza API.   
Program może działać w trybie tekstowym lub w trybie graficznym.

## Wymagania

Do uruchomienia programu potrzebne są:
- Python 3  
- dostęp do internetu  
- biblioteki:
  - `requests`
  - `tkinter`

Jeżeli biblioteka `requests` nie jest zainstalowana, należy wpisać:

`pip install requests`

## Uruchamianie programu

Program uruchamia się z konsoli poleceniem:

`python pogoda.py`

## Tryb graficzny (GUI)

### Uruchomienie
Aby uruchomić program w oknie graficznym:

`python pogoda.py --gui`

### Obsługa programu
1. Wpisz nazwę miasta (np. Katowice)  
2. Opcjonalnie wpisz kod kraju (np. PL)  
3. Wybierz jednostki:
   - Europejskie (°C, m/s)
   - Amerykańskie (°F, mph)
4. Kliknij przycisk **„Pokaż pogodę”**  
5. Odczytaj wynik w oknie programu  

## Tryb tekstowy (konsola)

### Przykład użycia

`python pogoda.py --city Katowice --country PL`

### Jednostki amerykańskie

`python pogoda.py --city Katowice --country PL --units imperial`

## Dostępne opcje

| Opcja         | Opis                      |
|---------------|---------------------------|
| `--city`      | nazwa miasta              |
| `--country`   | kod kraju                 |
| `--units`     | metric lub imperial       |
| `--gui`       | uruchamia tryb graficzny  |
| `--help`      | wyświetla pomoc           |

## Przykładowy wynik

```text
Temperatura: 18.2°C
Prędkość wiatru: 3.5 m/s
```

## Obsługa błędów

W trakcie korzystania z programu mogą pojawić się różne błędy. Program informuje o nich w czytelny sposób.

### Brak wpisanego miasta
- **Opis:** użytkownik nie podał nazwy miasta  
- **Komunikat:** informacja o konieczności wpisania miasta  
- **Rozwiązanie:** wpisać nazwę miasta i spróbować ponownie  

### Błędna nazwa miasta
- **Opis:** podana nazwa miasta nie istnieje lub jest źle zapisana  
- **Komunikat:** błąd pobierania danych pogodowych  
- **Rozwiązanie:** sprawdzić poprawność nazwy miasta lub dodać kod kraju  

### Brak połączenia z internetem
- **Opis:** program nie ma dostępu do internetu  
- **Komunikat:** informacja o braku możliwości pobrania danych  
- **Rozwiązanie:** sprawdzić połączenie z internetem i uruchomić program ponownie  

### Problem z serwisem pogodowym
- **Opis:** serwis wttr.in jest chwilowo niedostępny  
- **Komunikat:** błąd pobierania pogody  
- **Rozwiązanie:** odczekać kilka minut i spróbować ponownie  

### Brak wymaganych bibliotek
- **Opis:** w systemie nie ma zainstalowanej biblioteki `requests`  
- **Objaw:** program nie uruchamia się  
- **Rozwiązanie:** zainstalować bibliotekę poleceniem `pip install requests`  

***Program nie zamyka się samoczynnie i pozwala użytkownikowi poprawić dane.***

## Słownik pojęć

**GUI** – okno programu, w którym użytkownik może wpisywać dane i klikać przyciski.  

**Konsola** – tryb tekstowy, w którym program uruchamia się za pomocą poleceń.  

**API** – sposób pobierania danych z internetu (w tym programie nie jest wymagany klucz).  

**Jednostki metryczne** – stopnie Celsjusza (°C) i metry na sekundę (m/s).  

**Jednostki imperialne** – stopnie Fahrenheita (°F) i mile na godzinę (mph).  

**Kod kraju** – skrót kraju, np. PL (Polska), DE (Niemcy), US (Stany Zjednoczone).