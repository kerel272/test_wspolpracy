# Instrukcja obsługi programu **Pogoda**

## 1. Opis programu

Program **Pogoda** to aplikacja napisana w języku Python, która umożliwia sprawdzanie aktualnej temperatury oraz prędkości wiatru dla wybranego miasta. Dane pogodowe pobierane są z serwisu **wttr.in**, bez konieczności używania klucza API.

Program może działać w dwóch trybach:

* **tekstowym (CLI)** – obsługa z linii poleceń,
* **graficznym (GUI)** – proste okno aplikacji (Tkinter).

Instrukcja została przetestowana dla miasta **Katowice**.

---

## 2. Wymagania systemowe

Aby uruchomić program, potrzebne są:

* Python **3.8 lub nowszy**
* Dostęp do Internetu
* Zainstalowane biblioteki:

  * `requests`
  * `tkinter` (zwykle jest domyślnie zainstalowany z Pythonem)

Instalacja biblioteki `requests`:

```bash
pip install requests
```

---

## 3. Uruchamianie programu

Program uruchamiamy z poziomu terminala w folderze, w którym znajduje się plik z kodem (np. `pogoda.py`).

### 3.1. Tryb graficzny (GUI)

Aby uruchomić aplikację w oknie graficznym, użyj polecenia:

```bash
python pogoda.py --gui
```

Po uruchomieniu pojawi się okno programu.

---

## 4. Obsługa trybu graficznego

1. W polu **Miasto** wpisz nazwę miasta, np.:

   ```
   Katowice
   ```
2. W polu **Kraj** wpisz kod kraju (opcjonalnie), np.:

   ```
   PL
   ```
3. Wybierz jednostki:

   * **Europejskie** – stopnie Celsjusza (°C) i metry na sekundę (m/s)
   * **Amerykańskie** – stopnie Fahrenheita (°F) i mile na godzinę (mph)
4. Kliknij przycisk **„Pokaż pogodę”**.

Po chwili wyświetlą się aktualne dane pogodowe.

---

## 5. Tryb tekstowy (CLI)

Program można uruchomić również bez interfejsu graficznego.

### 5.1. Przykład dla miasta Katowice

```bash
python pogoda.py --city Katowice --country PL --units metric
```

Parametry:

* `--city` – nazwa miasta
* `--country` – kod kraju (opcjonalny)
* `--units` – system jednostek (`metric` lub `imperial`)

---

## 6. Wyświetlane dane

Program pokazuje:

* **Temperaturę powietrza**
* **Prędkość wiatru**

Jednostki zależą od wybranego systemu:

* `metric` → °C, m/s
* `imperial` → °F, mph

---

## 7. Obsługa błędów

* Jeśli pole **Miasto** jest puste – pojawi się komunikat ostrzegawczy.
* Jeśli podano nieprawidłową nazwę miasta lub brak Internetu – program wyświetli komunikat o błędzie.

---

## 8. Uwagi końcowe

* Program nie wymaga klucza API.
* Dane pogodowe są pobierane w czasie rzeczywistym.
* Aplikacja idealnie nadaje się do nauki obsługi argumentów CLI oraz prostych interfejsów GUI w Pythonie.

---

**Autor:** Paweł
**Miasto testowe:** Katowice
