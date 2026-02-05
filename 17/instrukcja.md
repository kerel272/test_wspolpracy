# Instrukcja obsługi programu Pogoda

## 1. Opis programu
Program **Pogoda** to aplikacja napisana w języku Python, która umożliwia sprawdzenie aktualnej temperatury oraz prędkości wiatru dla wybranego miasta.  
Dane pogodowe pobierane są z serwisu **wttr.in**, dzięki czemu program **nie wymaga klucza API**.

Program został przetestowany dla miasta **Katowice (PL)**.

---

## 2. Funkcjonalności programu
Program umożliwia:
- pobieranie aktualnej temperatury powietrza,
- pobieranie prędkości wiatru,
- wybór jednostek europejskich (°C, m/s),
- wybór jednostek amerykańskich (°F, mph),
- pracę w trybie tekstowym (CLI),
- pracę w trybie graficznym (GUI).

---

## 3. Wymagania
Do uruchomienia programu potrzebne są:
- Python w wersji 3.x
- biblioteka `requests`
- biblioteka `tkinter`

### Instalacja biblioteki `requests`
```bash
pip install requests
```

---

## 4. Uruchamianie programu

### Plik programu
```text
pogoda.py
```

### Podstawowe uruchomienie
```bash
python3 pogoda.py
```

Po uruchomieniu bez argumentów program wyświetli pomoc z dostępnymi opcjami.

---

## 5. Tryb tekstowy (CLI)

### Sprawdzenie pogody dla Katowic
```bash
python3 pogoda.py --city Katowice --country PL
```

### Przykładowy wynik
```text
Temperatura: 18.2°C
Prędkość wiatru: 3.4 m/s
```

### Jednostki amerykańskie
```bash
python3 pogoda.py --city Katowice --country PL --units imperial
```

---

## 6. Tryb graficzny (GUI)

### Uruchomienie trybu graficznego
```bash
python3 pogoda.py --gui
```

### Obsługa programu
1. Wpisz nazwę miasta:
```text
Katowice
```
2. Wpisz kod kraju:
```text
PL
```
3. Wybierz jednostki:
```text
Europejskie (°C, m/s) lub Amerykańskie (°F, mph)
```
4. Kliknij przycisk:
```text
Pokaż pogodę
```

Wynik zostanie wyświetlony w oknie programu.

---

## 7. Obsługa błędów
Program wyświetla komunikat błędu w następujących przypadkach:
- brak podanej nazwy miasta,
- nieprawidłowa nazwa miasta,
- brak połączenia z Internetem,
- problem z pobraniem danych pogodowych.

W trybie GUI błąd wyświetlany jest w oknie dialogowym, a w trybie CLI w terminalu.

---

## 8. Przykład pełnego użycia
```bash
python3 pogoda.py --city Katowice --country PL --units metric
```

---

## 9. Możliwości rozbudowy
Program można w przyszłości rozbudować o:
- wyświetlanie wilgotności powietrza,
- prognozę pogody na kilka dni,
- zapisywanie wyników do pliku,
- automatyczne wykrywanie kraju.

---

## 10. Podsumowanie
Program **Pogoda** jest prostym i czytelnym narzędziem do sprawdzania aktualnych warunków pogodowych. Dzięki wykorzystaniu serwisu wttr.in nie wymaga klucza API i może być używany zarówno w terminalu, jak i w trybie graficznym.
