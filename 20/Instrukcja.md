# Instrukcja obsługi programu **Pogoda**

Program **Pogoda** służy do pobierania aktualnej temperatury oraz prędkości wiatru dla wybranego miasta. Dane pogodowe pobierane są z serwisu **wttr.in** .

Instrukcja została przetestowana dla miasta **Katowice (PL)**.

---

## 1. Wymagania

Do poprawnego działania programu wymagane są:

* Python **3.x**
* Biblioteki Pythona:

  * `requests`
  * `tkinter` (zwykle dostępna domyślnie)

Instalacja biblioteki `requests` (jeśli nie jest zainstalowana):

```bash
pip install requests
```

---

## 2. Uruchamianie programu

Program można uruchomić w **trybie tekstowym (CLI)** lub w **trybie graficznym (GUI)**.

Plik programu powinien mieć prawa do uruchamiania:

```bash
chmod +x pogoda.py
```

lub można go uruchamiać poleceniem:

```bash
python3 pogoda.py
```

---

## 3. Tryb tekstowy (CLI)

### Składnia polecenia

```bash
python3 pogoda.py --city MIASTO [--country KOD_KRAJU] [--units metric|imperial]
```

### Dostępne parametry

* `--city` – nazwa miasta (wymagana w trybie CLI)
* `--country` – kod kraju, np. `PL`, `US` (opcjonalny)
* `--units` – system jednostek:

  * `metric` – stopnie Celsjusza (°C) i m/s *(domyślne)*
  * `imperial` – stopnie Fahrenheita (°F) i mph

### Przykład (Katowice)

```bash
python3 pogoda.py --city Katowice --country PL
```

Przykładowy wynik:

```
Temperatura: 18.4°C
Prędkość wiatru: 3.2 m/s
```

### Przykład z jednostkami amerykańskimi

```bash
python3 pogoda.py --city Katowice --country PL --units imperial
```

---

## 4. Tryb graficzny (GUI)

Aby uruchomić program w trybie okienkowym, użyj parametru `--gui`:

```bash
python3 pogoda.py --gui
```

### Obsługa GUI

1. W polu **Miasto** wpisz nazwę miasta (np. `Katowice`)
2. W polu **Kraj** wpisz kod kraju (np. `PL`)
3. Wybierz system jednostek:

   * Europejskie (°C, m/s)
   * Amerykańskie (°F, mph)
4. Kliknij przycisk **Pokaż pogodę**

Wynik zostanie wyświetlony w oknie programu.

---

## 5. Obsługa błędów

Program wyświetla komunikaty o błędach w następujących sytuacjach:

* brak podanej nazwy miasta
* nieprawidłowa nazwa miasta lub kraju
* brak połączenia z Internetem
* problem z serwisem wttr.in

W trybie GUI błędy pokazywane są w oknie dialogowym, a w trybie CLI – w konsoli.

---

## 6. Informacje dodatkowe

* Program pobiera aktualne dane pogodowe
* Działa na systemach Linux, Windows i macOS

---
****
