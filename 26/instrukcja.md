# Instrukcja obsługi programu **Pogoda**

Program **Pogoda** to prosta aplikacja w Pythonie umożliwiająca sprawdzenie aktualnej temperatury i prędkości wiatru dla wybranego miasta. Dane pogodowe pobierane są z serwisu **wttr.in**. Program może działać w trybie **konsolowym (CLI)** lub **graficznym (GUI)**.

---

## Wymagania

* Python **3.8+**
* Dostęp do Internetu
* Zainstalowane biblioteki:

  * `requests`
  * `tkinter` (zwykle wbudowany w Pythona)

Instalacja biblioteki `requests`:

```bash
pip install requests
```

---

## Uruchamianie programu

Plik programu:

```bash
pogoda.py
```

---

## Tryb graficzny (GUI)

Aby uruchomić aplikację w trybie okienkowym:

```bash
python pogoda.py --gui
```

### Obsługa GUI

1. Wpisz nazwę miasta (np. **Katowice**)
2. Opcjonalnie wpisz kod kraju (np. `PL`)
3. Wybierz jednostki:

   * **Europejskie** – stopnie Celsjusza (°C) i m/s
   * **Amerykańskie** – stopnie Fahrenheita (°F) i mph
4. Kliknij **„Pokaż pogodę”**
5. Wynik pojawi się w oknie aplikacji

---

## Tryb konsolowy (CLI)

### Składnia

```bash
python pogoda.py --city <miasto> [--country <kod_kraju>] [--units metric|imperial]
```

### Dostępne parametry

* `--city` – **(wymagane)** nazwa miasta
* `--country` – kod kraju (np. `PL`, `US`) – opcjonalnie
* `--units` – jednostki:

  * `metric` (domyślne) → °C, m/s
  * `imperial` → °F, mph

---

## Przykład testowy – miasto Katowice

### Tryb konsolowy

```bash
python pogoda.py --city Katowice --country PL --units metric
```

Przykładowy wynik:

```
Temperatura: 18.4°C
Prędkość wiatru: 3.2 m/s
```

### Tryb graficzny

```bash
python pogoda.py --gui
```

Następnie w oknie:

* Miasto: **Katowice**
* Kraj: **PL**
* Jednostki: **Europejskie (°C, m/s)**

---

## Obsługa błędów

* Brak miasta → komunikat ostrzegawczy
* Błędna nazwa miasta lub brak Internetu → komunikat o błędzie
* Program nie wymaga klucza API

---

## Uwagi końcowe

* Program korzysta z publicznego serwisu **wttr.in**
* Dane mają charakter informacyjny
* Aplikacja nadaje się do prostych testów i nauki Pythona (CLI + GUI)

---

**Autor:** *xyz*
