# Instrukcja obsługi programu Pogoda

## Opis programu

Program **Pogoda** to aplikacja umożliwiająca sprawdzanie aktualnych warunków pogodowych dla wybranego miasta. Program działa bez konieczności posiadania klucza API, korzystając z usługi wttr.in.

### Możliwości programu:
- Sprawdzanie temperatury i prędkości wiatru dla dowolnego miasta
- Obsługa jednostek metrycznych (°C, m/s) i imperialnych (°F, mph)
- Dwa tryby pracy: linia poleceń (CLI) oraz interfejs graficzny (GUI)
- Możliwość precyzyjnego określenia lokalizacji przez podanie kodu kraju

---

## Wymagania systemowe

### Wymagane oprogramowanie:
- Python 3.6 lub nowszy
- Połączenie z internetem

### Wymagane biblioteki Python:
```bash
pip install requests
```

**Uwaga:** Biblioteka `tkinter` jest zazwyczaj instalowana domyślnie z Pythonem. Jeśli jej brakuje:
- **Windows:** Zainstaluj ponownie Pythona z opcją "tcl/tk and IDLE"
- **Linux:** `sudo apt-get install python3-tk`
- **macOS:** tkinter powinien być dostępny domyślnie

---

## Instalacja

1. Zapisz kod programu do pliku `pogoda.py`
2. Zainstaluj wymagane zależności:
   ```bash
   pip install requests
   ```
3. (Opcjonalnie) Nadaj uprawnienia wykonywania (Linux/macOS):
   ```bash
   chmod +x pogoda.py
   ```

---

## Tryb CLI (linia poleceń)

### Podstawowe użycie

Aby sprawdzić pogodę dla miasta, użyj argumentu `--city`:

```bash
python pogoda.py --city Katowice
```

**Wynik:**
```
Temperatura: 5.0°C
Prędkość wiatru: 3.2 m/s
```

### Określenie kraju

Aby uniknąć niejednoznaczności (np. miasta o tej samej nazwie), podaj kod kraju:

```bash
python pogoda.py --city Katowice --country PL
```

### Jednostki imperialne

Aby wyświetlić temperaturę w °F i prędkość wiatru w mph:

```bash
python pogoda.py --city Katowice --units imperial
```

**Wynik:**
```
Temperatura: 41.0°F
Prędkość wiatru: 2.0 mph
```

### Wyświetlenie pomocy

```bash
python pogoda.py --help
```

---

## Tryb GUI (interfejs graficzny)

### Uruchomienie

Aby uruchomić aplikację w trybie okienkowym:

```bash
python pogoda.py --gui
```

### Obsługa interfejsu

Po uruchomieniu pojawi się okno z następującymi elementami:

![Interfejs programu](https://via.placeholder.com/320x220?text=GUI+Pogoda)

1. **Pole "Miasto":** Wpisz nazwę miasta (np. `Katowice`)
2. **Pole "Kraj":** (Opcjonalne) Wpisz kod kraju (np. `PL`)
3. **Opcje jednostek:**
   - **Europejskie (°C, m/s)** - temperatura w stopniach Celsjusza, wiatr w metrach na sekundę
   - **Amerykańskie (°F, mph)** - temperatura w stopniach Fahrenheita, wiatr w milach na godzinę
4. **Przycisk "Pokaż pogodę":** Kliknij, aby pobrać dane

### Przykład użycia dla Katowic

1. Uruchom program: `python pogoda.py --gui`
2. W polu "Miasto" wpisz: **Katowice**
3. W polu "Kraj" wpisz: **PL**
4. Wybierz "Europejskie (°C, m/s)"
5. Kliknij "Pokaż pogodę"

Program wyświetli aktualne dane pogodowe:
```
Temperatura: 5.0°C
Wiatr: 3.2 m/s
```

---

## Przykłady użycia

### Przykład 1: Katowice (Polska)
```bash
python pogoda.py --city Katowice --country PL
```

### Przykład 2: Warszawa (jednostki metryczne)
```bash
python pogoda.py --city Warszawa --country PL --units metric
```

### Przykład 3: Nowy Jork (jednostki imperialne)
```bash
python pogoda.py --city "New York" --country US --units imperial
```

### Przykład 4: Londyn (GUI)
```bash
python pogoda.py --gui
```
Następnie w oknie wpisz: **London** i **GB**

---

## Kody krajów

Program obsługuje międzynarodowe kody krajów (ISO 3166-1 alpha-2):

| Kraj | Kod |
|------|-----|
| Polska | PL |
| Niemcy | DE |
| Wielka Brytania | GB |
| Stany Zjednoczone | US |
| Francja | FR |
| Czechy | CZ |
| Słowacja | SK |

Pełna lista: [Wikipedia - ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

---

## Jednostki miary

### Jednostki metryczne (metric)
- **Temperatura:** °C (stopnie Celsjusza)
- **Wiatr:** m/s (metry na sekundę)

### Jednostki imperialne (imperial)
- **Temperatura:** °F (stopnie Fahrenheita)
- **Wiatr:** mph (mile na godzinę)

**Konwersja:**
- °F = °C × 9/5 + 32
- mph = km/h × 0.621371

---

## Rozwiązywanie problemów

### Problem: "Nie udało się pobrać pogody"

**Przyczyny i rozwiązania:**

1. **Brak połączenia z internetem**
   - Sprawdź połączenie internetowe
   - Spróbuj otworzyć stronę https://wttr.in w przeglądarce

2. **Nieprawidłowa nazwa miasta**
   - Sprawdź pisownię miasta
   - Spróbuj użyć angielskiej nazwy (np. `Warsaw` zamiast `Warszawa`)
   - Dodaj kod kraju: `--country PL`

3. **Timeout (zbyt długi czas odpowiedzi)**
   - Spróbuj ponownie za chwilę
   - Usługa wttr.in może być tymczasowo niedostępna

### Problem: "ModuleNotFoundError: No module named 'requests'"

**Rozwiązanie:**
```bash
pip install requests
```

### Problem: "ModuleNotFoundError: No module named 'tkinter'"

**Rozwiązanie:**
- **Windows:** Przeinstaluj Pythona z zaznaczoną opcją "tcl/tk and IDLE"
- **Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Fedora:** `sudo dnf install python3-tkinter`

### Problem: Okno GUI się nie pojawia

**Rozwiązanie:**
- Upewnij się, że używasz flagi `--gui`
- Sprawdź, czy tkinter jest zainstalowany
- Uruchom w trybie CLI, aby wykluczyć problemy z połączeniem

---

## Test dla miasta Katowice

### Test 1: CLI z jednostkami metrycznymi
```bash
python pogoda.py --city Katowice --country PL --units metric
```
**Oczekiwany wynik:**
```
Temperatura: [aktualna wartość]°C
Prędkość wiatru: [aktualna wartość] m/s
```

### Test 2: CLI z jednostkami imperialnymi
```bash
python pogoda.py --city Katowice --country PL --units imperial
```
**Oczekiwany wynik:**
```
Temperatura: [aktualna wartość]°F
Prędkość wiatru: [aktualna wartość] mph
```

### Test 3: GUI
```bash
python pogoda.py --gui
```
1. Wpisz "Katowice" w pole miasto
2. Wpisz "PL" w pole kraj
3. Wybierz "Europejskie (°C, m/s)"
4. Kliknij "Pokaż pogodę"

**Oczekiwany wynik:** Wyświetlenie aktualnej temperatury i prędkości wiatru w oknie aplikacji

---

## Często zadawane pytania (FAQ)

### 1. Czy program wymaga klucza API?
Nie, program korzysta z darmowej usługi wttr.in, która nie wymaga rejestracji ani klucza API.

### 2. Jak często aktualizują się dane?
Dane są pobierane w czasie rzeczywistym z serwisu wttr.in przy każdym wywołaniu.

### 3. Czy mogę sprawdzić prognozę na kolejne dni?
Obecna wersja programu pokazuje tylko aktualne warunki pogodowe.

### 4. Dlaczego wiatr jest w m/s, a nie w km/h?
W trybie metrycznym program konwertuje prędkość wiatru z km/h na m/s, która jest bardziej powszechna w prognozach pogody w Polsce.

### 5. Czy program działa offline?
Nie, program wymaga połączenia z internetem do pobierania danych z wttr.in.

---

## Informacje techniczne

- **Źródło danych:** wttr.in API
- **Timeout połączenia:** 10 sekund
- **Format danych:** JSON
- **Licencja:** Brak informacji (określ samodzielnie)

---

## Autor i wsparcie

W przypadku pytań lub problemów:
1. Sprawdź sekcję "Rozwiązywanie problemów"
2. Upewnij się, że masz najnowszą wersję programu
3. Sprawdź dostępność usługi wttr.in: https://wttr.in

---

**Data ostatniej aktualizacji:** Styczeń 2026
