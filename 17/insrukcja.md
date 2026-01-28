# Instrukcja obsługi programu Pogoda

## 1. Informacje ogólne
Program **Pogoda** jest aplikacją napisaną w języku Python, która umożliwia sprawdzenie aktualnych warunków pogodowych dla wybranego miasta. Program pobiera dane z serwisu **wttr.in**, dzięki czemu nie wymaga użycia klucza API ani zakładania konta w zewnętrznym serwisie.

Program został przetestowany dla miasta **Katowice (Polska)** i działa zarówno w trybie tekstowym, jak i graficznym.

---

## 2. Funkcje programu
Program umożliwia:
- sprawdzenie aktualnej temperatury powietrza,
- sprawdzenie prędkości wiatru,
- wybór jednostek europejskich (°C, m/s),
- wybór jednostek amerykańskich (°F, mph),
- uruchomienie programu w trybie tekstowym (CLI),
- uruchomienie programu w trybie graficznym (GUI).

---

## 3. Wymagania systemowe
Do poprawnego działania programu wymagane są:
- Python w wersji 3.x,
- biblioteka `requests`,
- biblioteka `tkinter` (standardowo dostępna w Pythonie).

Instalacja biblioteki `requests`:
pip install requests

---

## 4. Uruchamianie programu
Program uruchamia się z poziomu terminala poleceniem:
python3 pogoda.py

Jeżeli nie zostaną podane żadne argumenty, program wyświetli pomoc dotyczącą dostępnych opcji.

---

## 5. Tryb tekstowy (CLI)

### 5.1 Sprawdzenie pogody dla Katowic
Aby sprawdzić pogodę dla Katowic, należy wpisać:
python3 pogoda.py --city Katowice --country PL

Program wyświetli aktualną temperaturę oraz prędkość wiatru.

### 5.2 Jednostki miary
Domyślnie program korzysta z jednostek europejskich:
- temperatura w stopniach Celsjusza (°C),
- prędkość wiatru w metrach na sekundę (m/s).

Aby użyć jednostek amerykańskich, należy wpisać:
python3 pogoda.py --city Katowice --country PL --units imperial

---

## 6. Tryb graficzny (GUI)
Program może zostać uruchomiony w trybie graficznym za pomocą polecenia:
python3 pogoda.py --gui

Po uruchomieniu pojawi się okno programu.

### 6.1 Obsługa okna
1. W polu **Miasto** wpisz: Katowice  
2. W polu **Kraj** wpisz: PL  
3. Wybierz system jednostek:
   - Europejskie (°C, m/s)
   - Amerykańskie (°F, mph)
4. Kliknij przycisk **Pokaż pogodę**

Wynik zostanie wyświetlony w dolnej części okna.

---

## 7. Obsługa błędów
Program posiada podstawową obsługę błędów. Komunikat błędu pojawi się w następujących sytuacjach:
- nie podano nazwy miasta,
- podano nieprawidłową nazwę miasta,
- brak połączenia z Internetem,
- problem z pobraniem danych z serwera.

W trybie graficznym błąd zostanie pokazany w oknie dialogowym, natomiast w trybie tekstowym w konsoli.

---

## 8. Przykład użycia
Przykład sprawdzenia pogody dla miasta Katowice:
python3 pogoda.py --city Katowice --country PL

Program zwróci informacje o aktualnej temperaturze oraz prędkości wiatru.

---

## 9. Podsumowanie
Program **Pogoda** jest prostym i intuicyjnym narzędziem do sprawdzania aktualnych danych pogodowych. Dzięki wykorzystaniu serwisu wttr.in nie wymaga klucza API, a możliwość wyboru trybu pracy (tekstowy lub graficzny) sprawia, że jest wygodny w użyciu.
