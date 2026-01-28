# Instrukcja obsługi programu „Pogoda"

Program **Pogoda** umożliwia szybkie sprawdzenie aktualnej temperatury i prędkości wiatru dla wybranego miasta, bez potrzeby posiadania klucza API. Wykorzystuje darmową usługę **wttr.in**.

## Wymagania
- Python 3.x
- Biblioteki: `requests`, `tkinter` (Tkinter zwykle jest domyślnie z Pythonem)
- Połączenie z internetem

## Uruchamianie programu

### 1. Z linii poleceń (terminal)
1. Otwórz terminal lub PowerShell.
2. Przejdź do folderu z programem (`pogoda.py`).
3. Uruchom program dla miasta Katowice w jednostkach metrycznych (°C, m/s):
   ```bash
   python pogoda.py --city Katowice
   ```
   Wyjście będzie wyglądać np. tak:
   ```
   Temperatura: 5.2°C
   Prędkość wiatru: 3.4 m/s
   ```

4. Aby sprawdzić pogodę w jednostkach imperialnych (°F, mph):
   ```bash
   python pogoda.py --city Katowice --units imperial
   ```

5. Jeśli chcesz podać kod kraju (np. Polska – `PL`):
   ```bash
   python pogoda.py --city Katowice --country PL
   ```

### 2. Z użyciem GUI (interfejs graficzny)
1. Uruchom program w trybie GUI:
   ```bash
   python pogoda.py --gui
   ```
2. W oknie programu:
   - Wprowadź miasto: `Katowice`
   - (Opcjonalnie) wprowadź kod kraju: `PL`
   - Wybierz jednostki: `Europejskie (°C, m/s)` lub `Amerykańskie (°F, mph)`
   - Kliknij **Pokaż pogodę**
3. Program wyświetli temperaturę i prędkość wiatru w oknie.

## Obsługa błędów
- Jeśli wpiszesz niepoprawną nazwę miasta, program wyświetli komunikat błędu.
- W przypadku problemów z internetem lub usługą wttr.in, program również wyświetli odpowiedni komunikat.


