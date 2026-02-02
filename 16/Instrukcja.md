````md
# 🌤️ Program Pogoda

Program **Pogoda** to prosta aplikacja napisana w języku Python, służąca do sprawdzania aktualnej temperatury oraz prędkości wiatru dla wybranego miasta.  
Dane pogodowe pobierane są z serwisu **wttr.in** i **nie wymagają klucza API**.

Program działa w dwóch trybach:
- tryb konsolowy (CLI)
- tryb graficzny (GUI – Tkinter)

---

## 📦 Wymagania

- Python 3.8 lub nowszy
- Dostęp do internetu
- Biblioteki:
  - `requests`
  - `tkinter` (zwykle dostępny domyślnie)

Instalacja biblioteki `requests`:
```bash
pip install requests
````

---

## 🚀 Uruchomienie programu

```bash
python3 pogoda.py
```

---

## 🖥️ Tryb konsolowy (CLI)

### Składnia:

```bash
python3 pogoda.py --city MIASTO [--country KOD_KRAJU] [--units metric|imperial]
```

### Parametry:

* `--city` – nazwa miasta (wymagane)
* `--country` – kod kraju, np. `PL`, `US` (opcjonalne)
* `--units` – jednostki:

  * `metric` – stopnie Celsjusza (°C) i m/s
  * `imperial` – stopnie Fahrenheita (°F) i mph

---

### ✅ Przykład testowy – Katowice

```bash
python3 pogoda.py --city Katowice --country PL
```

Przykładowy wynik:

```
Temperatura: 18.4°C
Prędkość wiatru: 3.2 m/s
```

---

### 🇺🇸 Jednostki amerykańskie

```bash
python3 pogoda.py --city Katowice --country PL --units imperial
```

Przykładowy wynik:

```
Temperatura: 65.1°F
Prędkość wiatru: 7.1 mph
```

---

## 🪟 Tryb graficzny (GUI)

Uruchomienie trybu graficznego:

```bash
python3 pogoda.py --gui
```

### Obsługa GUI:

1. Wpisz miasto (np. Katowice)
2. Opcjonalnie wpisz kod kraju (PL)
3. Wybierz jednostki (europejskie lub amerykańskie)
4. Kliknij przycisk **„Pokaż pogodę”**

Wynik zostanie wyświetlony w oknie aplikacji.

---

## ⚠️ Obsługa błędów

Program wyświetla komunikaty błędów w przypadku:

* braku nazwy miasta
* braku połączenia z internetem
* nieprawidłowej nazwy miasta

---

## ℹ️ Informacje dodatkowe

* Źródło danych pogodowych: [https://wttr.in](https://wttr.in)
* Program nie wymaga rejestracji ani klucza API
* Projekt edukacyjny w Pythonie
* Testowane dla miasta **Katowice**

```
