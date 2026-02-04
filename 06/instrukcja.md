# Instrukcja obsługi programu **Pogoda (bez klucza API)**

Program służy do sprawdzania aktualnej temperatury oraz prędkości wiatru dla wybranego miasta. Dane pogodowe pobierane są z serwisu **wttr.in**, bez konieczności używania klucza API.

Instrukcja poniżej opisuje użycie programu **dla miasta Katowice (Polska)**, zarówno w trybie tekstowym (terminal), jak i graficznym (okno GUI).

---

## 1. Wymagania

Aby uruchomić program, potrzebujesz:

* systemu z zainstalowanym **Pythonem 3**
* dostępu do internetu
* zainstalowanych bibliotek:

  * `requests`
  * `tkinter` (zwykle wbudowany w Pythona)

---

## 2. Uruchamianie programu

Plik programu uruchamiany jest z linii poleceń:

```bash
python3 pogoda.py
```

Jeśli plik ma prawa do uruchamiania:

```bash
./pogoda.py
```

---

## 3. Tryb graficzny (GUI) – zalecany

### Uruchomienie

```bash
python3 pogoda.py --gui
```

### Instrukcja krok po kroku (Katowice)

1. W polu **Miasto** wpisz:

   ```
   Katowice
   ```
2. W polu **Kraj** wpisz:

   ```
   PL
   ```
3. Wybierz system jednostek:

   * **Europejskie** – temperatura w °C, wiatr w m/s (zalecane)
   * **Amerykańskie** – temperatura w °F, wiatr w mph
4. Kliknij przycisk **„Pokaż pogodę”**
5. Wynik pojawi się w oknie, np.:

   ```
   Temperatura: 18.4°C
   Wiatr: 3.2 m/s
   ```

### Możliwe komunikaty

* **„Wprowadź miasto!”** – pole Miasto jest puste
* **„Nie udało się pobrać pogody”** – brak internetu lub błąd serwisu

---

## 4. Tryb tekstowy (terminal)

### Podstawowe użycie – Katowice

```bash
python3 pogoda.py --city Katowice --country PL
```

### Przykładowy wynik

```text
Temperatura: 18.4°C
Prędkość wiatru: 3.2 m/s
```

### Jednostki amerykańskie

```bash
python3 pogoda.py --city Katowice --country PL --units imperial
```

Wynik:

* temperatura w °F
* prędkość wiatru w mph

---

## 5. Parametry programu

| Parametr    | Opis                          |
| ----------- | ----------------------------- |
| `--city`    | Nazwa miasta (np. Katowice)   |
| `--country` | Kod kraju (dla Polski: PL)    |
| `--units`   | `metric` lub `imperial`       |
| `--gui`     | Uruchamia interfejs graficzny |

---

## 6. Uwagi końcowe

* Program pokazuje **aktualną pogodę**, nie prognozę
* Dane pochodzą z serwisu **wttr.in**
* Program nie zapisuje żadnych danych lokalnie
