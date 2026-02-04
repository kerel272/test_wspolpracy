# Instrukcja obsługi – Program Pogoda

**Testowana lokalizacja przykładowa: Katowice (PL)**

## Spis treści

1. [Wprowadzenie](#1-wprowadzenie)
2. [Funkcjonalności programu](#2-funkcjonalności-programu)
3. [Wymagania systemowe](#3-wymagania-systemowe)
4. [Struktura programu](#4-struktura-programu)
5. [Sposoby uruchamiania programu](#5-sposoby-uruchamiania-programu)
6. [Argumenty wiersza poleceń](#6-argumenty-wiersza-poleceń)
7. [Jednostki miar](#7-jednostki-miar)
8. [Przykład działania dla miasta Katowice](#8-przyklad-dzialania-dla-miasta-katowice)
9. [Obsługa błędów](#9-obsluga-bledow)
10. [Najczęstsze problemy](#10-najczestsze-problemy)

---

## 1. Wprowadzenie

Program **Pogoda** to aplikacja napisana w języku Python umożliwiająca sprawdzanie aktualnej temperatury oraz prędkości wiatru dla dowolnego miasta.
Aplikacja:

* nie wymaga klucza API,
* korzysta z darmowego serwisu **wttr.in**,
* działa w trybie tekstowym (CLI) oraz graficznym (GUI).

---

## 2. Funkcjonalności programu

Program pozwala na:

* pobranie aktualnej temperatury powietrza,
* odczyt prędkości wiatru,
* wybór jednostek: metrycznych lub imperialnych,
* podanie miasta z opcjonalnym kodem kraju,
* obsługę przez okno graficzne lub terminal.

---

## 3. Wymagania systemowe

### 3.1 Oprogramowanie

* Python 3.8+
* system Windows / Linux / macOS
* dostęp do internetu

### 3.2 Wymagane biblioteki

* requests
* tkinter (standardowo z Pythonem)

Instalacja biblioteki:

```
pip install requests
```

---

## 4. Struktura programu

Najważniejsze elementy kodu:

* `get_weather()` – pobiera dane z serwisu wttr.in i przelicza jednostki,
* `show_gui()` – tworzy interfejs graficzny,
* `main()` – obsługuje argumenty wiersza poleceń.

---

## 5. Sposoby uruchamiania programu

### 5.1 Tryb graficzny (GUI)

Uruchomienie:

```
python pogoda.py --gui
```

W oknie należy:

1. wpisać nazwę miasta (np. Katowice),
2. opcjonalnie kod kraju (PL),
3. wybrać jednostki,
4. kliknąć **Pokaż pogodę**.

### 5.2 Tryb tekstowy (CLI)

Przykładowe uruchomienia:

```
python pogoda.py --city Katowice
```

```
python pogoda.py --city Katowice --country PL
```

```
python pogoda.py --city Katowice --units imperial
```

---

## 6. Argumenty wiersza poleceń

| Argument  | Opis              | Przykład |
| --------- | ----------------- | -------- |
| --city    | nazwa miasta      | Katowice |
| --country | kod kraju         | PL       |
| --units   | metric / imperial | metric   |
| --gui     | uruchom GUI       | –        |

---

## 7. Jednostki miar

**Metric:**

* temperatura – °C
* wiatr – m/s

**Imperial:**

* temperatura – °F
* wiatr – mph

---

## 8. Przykład działania dla miasta Katowice

Polecenie:

```
python pogoda.py --city Katowice --country PL
```

Przykładowy wynik:

```
Temperatura: 7.2°C  
Prędkość wiatru: 3.5 m/s
```

W GUI należy wpisać:

* Miasto: *Katowice*
* Kraj: *PL*

---

## 9. Obsługa błędów

Program wyświetli komunikat gdy:

* brak internetu,
* wpisano błędną nazwę miasta,
* pole miasta jest puste (GUI),
* serwis wttr.in nie odpowiada.

W CLI błędy pojawiają się w terminalu, w GUI – w oknie dialogowym.

---

## 10. Najczęstsze problemy

### Brak biblioteki requests

```
pip install requests
```

### GUI nie uruchamia się

* sprawdzić czy zainstalowany jest tkinter,
* na Linux:

```
sudo apt-get install python3-tk
```

### Nie znaleziono miasta

* spróbować z kodem kraju: `Katowice --country PL`.

---

**Autor instrukcji:** użytkownik programu
**Źródło danych:** [https://wttr.in](https://wttr.in)
**Miasto testowe:** Katowice

