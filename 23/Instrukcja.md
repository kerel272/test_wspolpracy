# Instrukcja obsługi programu Pogoda

Program służy do sprawdzania aktualnej temperatury i prędkości wiatru dla wybranego miasta.

Dane pogodowe pobierane są z serwisu **wttr.in**, dlatego nie jest wymagany klucz API.

---

## Wymagania systemowe

- **Python 3.7** lub nowszy
- Dostęp do internetu
- Zainstalowanie biblioteki
    - **`requests`**
    - `tkinter` (wbudowany)

```bash
pip install requests
```

---

## Uruchomienie programu

Uruchomienie bez argumentów wyświetli pomoc.

```bash
python pogoda.py
```

---

## Dostępne parametry

- --city - Nazwa miasta
- --country - Kod kraju (np. PL)
- --units - metric lub imperial
- --gui - uruchamia GUI

---

## Tryb CLI (jednostki europejskie)

### Sprawdzenie pogody dla Katowic

```bash
python pogoda.py --city Katowice --country PL
```

### Wynik

```text
Temperatura: X°C
Prędkość wiatru: Y m/s
```

---

## Tryb CLI (jednostki amerykańskie)

### Sprawdzenie pogody dla Katowic

```bash
python pogoda.py --city Katowice --country PL --units imperial
```

### Wynik

```text
Temperatura: X°F
Prędkość wiatru: Y mph
```

---

## Tryb GUI

### Uruchamianie GUI

```bash
python pogoda.py --gui
```

### Obsługa okna

1. W pole **Miasto** wpisz np. "Katowice"
2. W pole **Kraj** wpisz np. "PL"
3. Wybierz jednostki
    - Europejskie
    - Amerykańskie
4. Kliknij **Pokaż pogodę**
5. Wynik zostanie wyświetlony w oknie

---

## Obsługa błędów

- **Brak miasta** (komunikat „Wprowadź miasto!”) - Należy wpisać wybrane miasto w pole **Miasto**
- **Błędna nazwa miasta lub brak Internetu** (komunikat "Nie udało się pobrać pogody dla *lokacja*. Sprawdź nazwę lub połączenie.") - Należy sprawdzić czy nazwa miasta jest prawidłowa lub czy jest połączenie z internetem.