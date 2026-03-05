# Instrukcja obsługi programu do sprawdzania pogody

## Spis treści
1. [Opis programu](#opis-programu)
2. [Wymagania techniczne](#wymagania-techniczne)
3. [Funkcje programu](#funkcje-programu)
4. [Działanie programu](#działanie-programu)
5. [Tryb graficzny](#tryb-graficzny)
6. [Tryb konsolowy](#tryb-konsolowy)

## Opis Programu
Program pozwala na sprawdzenie temperatury i prędkości wiatru dla wybranego miasta korzystając z serwisu [wttr.in](wttr.in).

## Wymagania techniczne
- Python 3.X
- Dostęp do internetu
- Zainstalowana biblioteka Python `requests` i `tkinter`
Jeśli wymagana biblioteka nie jest zainstalowana, można to zrobić wpisując poniższą komendę w wierszu poleceń:
```bash
pip install requests
```
Komendę należy poprzedzić słowem `python`, `python3` lub `py` w zależności od zainstalowanego systemu.

---------------------------------

## Funkcje programu
- Wybór miasta dla którego chce się sprawdzić pogodę
- Wybór jednostek metrycznych lub imperialnych
- Wyświetlanie w trybie konsolowym lub graficznym

---------------------------------

## Działanie programu
Dla pliku programu o nazwie `pogoda.py`, można program uruchomić w następujący sposób:
```bash
py Ścieżka/do/pliku/pogoda.py --flagi
```

Uruchomienie programu bez żadnych flag lub z flagą `-h` lub `--help` wyświetla instrukcje korzystania z programu.  
Gdy sprawdzenie pogody się nie powiedzie, program wyświetli komunikat z typem błędu.

---------------------------------

### Tryb konsolowy

#### Flagi
| Flaga | Opis |
| -------------------| ----------------- |
| `--city [Nazwa miasta]` | Wybór miasta dla którego sprawdza się pogodę. Nie jest wymagana pełna nazwa, gdy miast jest określone jednoznacznie. |
| `--country [Kod kraju]` | Wybór kraju. Wymagana do poprawnego wyniku, gdy istnieją takie same nazwy miast w kilku krajach. |
| `--units [metric/imperial]` | Wybór jednostek, w których pokazany będzie wynik. Podstawowo są użyte jednostki metryczne. |
| `--gui` | Uruchomienie graficznym trybie programu. Inne flagi są wtedy ignorowane. |
| `-h` / `--help` | Wyświetlenie instrukcji programu. |

#### Przykładowe użycie w trybie konsolowym
```bash
py pogoda.py --country PL --city Katowice --units metric
```
**Przykładowy wynik:**  
```bash
Temperatura: 0.0°C
Prędkość wiatru: 3.9 m/s
```

---------------------------------

### Tryb graficzny
Po uruchomieniu z flagą `--gui` program otworzy się w trybie graficznym.  
W trybie graficznym są dwa pola tekstowe (`Miasto` i `Kraj`) i Przełącznik do wybierania jednostek.

#### Przykładowe użycie w trybie graficznym
Po wpisanie do pola tekstowego `Miasto` - `Katowice`, wpisaniu do pola `Kraj` - `PL` i naciśnięciu przycisku `Pokaż pogodę`, zostanie pod przyciskiem wyświetlony wynik.  

**Przykładowy wynik:**  
Temperatura: -1.0°C  
Wiatr 4.7 m/s  

---------------------------------


