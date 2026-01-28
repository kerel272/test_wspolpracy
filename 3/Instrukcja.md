# Instrukcja obsługi programu Pogoda

## 1. Opis programu
Program **Pogoda** umożliwia sprawdzenie aktualnej:
- temperatury powietrza  
- prędkości wiatru  
dla dowolnego miasta na świecie.

### Program korzysta z serwisy **wttr.in** i nie wymaga klucza API
Program działa w dwóch trybach:
- tekstowym (konsolowym)  
- graficznym (GUI – okno aplikacji)  

## 2. Wymagania systemowe
### Do uruchomienia programu jest potrzebne:
- Python **3**.x  
- Dostęp do Internetu  
- Biblioteka `requests`

### Instalacja wymaganej biblioteki
```python
pip install requests
```

#### Biblioteka tkinter jest standardowo dostępna w większości instalacji Pythona.
## 3. Uruchamianie programu

Program uruchamiany jest z terminala/wiersza poleceń:
```python
python pogoda.py
```

Jeżeli nie podano żadnych argumentów, program wyświetla pomoc.
## 4. Tryb tekstowy (konsola)
### Sprawdzenie pogody dla miasta
```python
python pogoda.py --city Katowice
```
#### Przykładowy wynik:

- Temperatura: 12.3°C
- Prędkość wiatru: 3.5 m/s

### Podanie kraju (opcjonalnie)

#### Jeżeli miasto występuje w wielu krajach, należy doprecyzować kod kraju:
```python
python pogoda.py --city Paris --country FR
```
### Wybór jednostek

#### Program obsługuje dwa systemy jednostek:

|System|Temperatura|	Wiatr|
|------|-------------|-------|
metric (domyślny)|	°C|	m/s|
|imperialne|°F|	mph|

#### Przykład użycia jednostek amerykańskich:
```python
python pogoda.py --city NewYork --units imperial
```
## 5. Tryb graficzny (GUI)

#### Aby uruchomić wersję okienkową programu, należy użyć flagi:
```python
python pogoda.py --gui
```
#### W oknie aplikacji należy:

- Wpisać nazwę miasta

- (Opcjonalnie) wpisać kod kraju, np. PL, US

- Wybrać system jednostek:

    - Europejski (°C, m/s)

    - Amerykański (°F, mph)

- Kliknąć przycisk Pokaż pogodę

Program wyświetli aktualną temperaturę oraz prędkość wiatru.
## 6. Obsługa błędów

#### Program może wyświetlić komunikaty o błędach w przypadku:

    nieprawidłowej nazwy miasta

    braku połączenia z Internetem

    problemów z serwisem wttr.in

#### W trybie GUI błędy pojawiają się w oknie dialogowym.
#### W trybie konsolowym błędy zostają wypisane na standardowe wyjście błędów.
## 7. Pomoc

### Aby wyświetlić pomoc i listę dostępnych opcji:
```python
python pogoda.py --help
```
### Dostępne opcje w konsoli:
```python
    --city – nazwa miasta (wymagana w trybie tekstowym)

    --country – kod kraju (opcjonalnie)

    --units – jednostki: metric lub imperial

    --gui – uruchomienie interfejsu graficznego
```      
