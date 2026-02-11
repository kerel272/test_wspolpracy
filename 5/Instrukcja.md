# Instrukcja obsługi programu „Pogoda”

## Opis programu
Program **Pogoda** służy do sprawdzania aktualnej temperatury powietrza oraz prędkości wiatru dla wybranego miasta.  
Dane pobierane są z serwisu **wttr.in** i nie wymagają klucza API.

Program można uruchomić:
- w **trybie tekstowym (terminal)**  
- w **trybie graficznym (GUI)**

Test działania należy wykonać dla miasta **Katowice**.

---

## Wymagania
Aby uruchomić program, potrzebne są:

- Python 3
- biblioteka `requests`
- biblioteka `tkinter` (zwykle zainstalowana razem z Pythonem)

Instalacja brakującej biblioteki:

```bash
pip install requests
```

---

## Uruchomienie programu w terminalu

### 1. Sprawdzenie pogody dla Katowic (jednostki europejskie)
```bash
python3 pogoda.py --city Katowice --country PL
```

Wyświetlone zostaną:
- temperatura w °C  
- prędkość wiatru w m/s  

---

### 2. Jednostki amerykańskie
```bash
python3 pogoda.py --city Katowice --country PL --units imperial
```

Wyświetlone zostaną:
- temperatura w °F  
- prędkość wiatru w mph  

---

## Uruchomienie programu w trybie graficznym (GUI)

```bash
python3 pogoda.py --gui
```

### Obsługa okna:
1. W polu **Miasto** wpisz: `Katowice`
2. W polu **Kraj** wpisz: `PL`
3. Wybierz jednostki:
   - Europejskie (°C, m/s)  
   - Amerykańskie (°F, mph)
4. Kliknij przycisk **„Pokaż pogodę”**

W dolnej części okna pojawi się:
- temperatura  
- prędkość wiatru  

---

## Możliwe błędy
Program może wyświetlić komunikat błędu, gdy:

- brak połączenia z internetem  
- podano niepoprawną nazwę miasta  
- serwis wttr.in jest chwilowo niedostępny  

---

## Autor
Karol Grot