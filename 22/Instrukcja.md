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
8. [Przykład działania dla miasta Katowice](#katowice)
9. [Obsługa błędów](#bledy)
10. [Najczęstsze problemy](#problemy)

---

## 1. Wprowadzenie

Program **Pogoda** jest narzędziem napisanym w języku Python, służącym do sprawdzania aktualnych warunków pogodowych dla wybranego miasta na świecie.
Aplikacja została zaprojektowana tak, aby:

* nie wymagać klucza API,
* być prosta w obsłudze,
* działać w trybie konsolowym (CLI) oraz graficznym (GUI).

Źródłem danych jest publiczny serwis **wttr.in**, udostępniający informacje pogodowe w formacie JSON.

---

## 2. Funkcjonalności programu

Program umożliwia:

* sprawdzanie aktualnej temperatury powietrza,
* sprawdzanie prędkości wiatru,
* wybór jednostek metrycznych lub imperialnych,
* podanie miasta wraz z opcjonalnym kodem kraju,
* obsługę przez interfejs graficzny lub linię poleceń,
* wyświetlanie komunikatów błędów w języku polskim.

---

## 3. Wymagania systemowe

### 3.1 Oprogramowanie

* Python 3.8 lub nowszy
* Windows / Linux / macOS
* dostęp do internetu

### 3.2 Wymagane biblioteki

* requests
* tkinter

Instalacja:

```
pip install requests
```

---

## 4. Struktura programu

Program zawiera:

* funkcję `get_weather()` – pobieranie danych z wttr.in,
* funkcję `show_gui()` – obsługa interfejsu graficznego,
* funkcję `main()` – obsługa argumentów CLI,
* blok startowy `if __name__ == "__main__":`.

---

## 5. Sposoby uruchamiania programu

### 5.1 Tryb graficzny (GUI)

Uruchomienie:

```
python pogoda.py --gui
```

Elementy okna:

1. Pole „Miasto” – wymagane
2. Pole „Kraj” – opcjonalne (np. PL)
3. Wybór jednostek
4. Przycisk „Pokaż pogodę”
5. Pole z wynikami

### 5.2 Tryb tekstowy (CLI)

Przykłady:

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

| Argument  | Opis              |
| --------- | ----------------- |
| --city    | nazwa miasta      |
| --country | kod kraju         |
| --units   | metric / imperial |
| --gui     | uruchom GUI       |

---

## 7. Jednostki miar

**System metryczny**

* temperatura: °C
* wiatr: m/s

**System imperialny**

* temperatura: °F
* wiatr: mph

---

<a id="katowice"></a>

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

* Miasto: Katowice
* Kraj: PL

---

<a id="bledy"></a>

## 9. Obsługa błędów

Program wyświetli komunikat gdy:

* brak połączenia z internetem,
* podano nieprawidłową nazwę miasta,
* pole miasta jest puste,
* serwer wttr.in nie odpowiada.

W CLI błędy pojawiają się w terminalu, a w GUI – w oknie dialogowym.

---

<a id="problemy"></a>

## 10. Najczęstsze problemy

### Brak biblioteki requests

```
pip install requests
```

### GUI nie uruchamia się

Na Linuxie:

```
sudo apt-get install python3-tk
```

### Nie znaleziono miasta

Użyć kodu kraju:

```
python pogoda.py --city Katowice --country PL
```

---

**Źródło danych:** [https://wttr.in](https://wttr.in)
**Miasto testowe:** Katowice
