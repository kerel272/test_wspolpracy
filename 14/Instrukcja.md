# Instrukcja obsługi programu Pogoda

Program służy do sprawdzania pogody (temperatura i wiatr) w konsoli lub w oknie graficznym.

## 1. Przygotowanie
Upewnij się, że masz zainstalowaną bibliotekę `requests`. Wpisz w terminalu:
pip install requests

## 2. Test dla miasta Katowice
Zgodnie z poleceniem, aby sprawdzić pogodę dla Katowic, wpisz komendę:

python pogoda.py --city Katowice

## 3. Tryb graficzny (Okienko)
Aby uruchomić program w wersji okienkowej, wpisz:

python pogoda.py --gui

W oknie wpisz "Katowice" i kliknij przycisk "Pokaż pogodę".

## 4. Dostępne opcje
* `--city [Miasto]` - Wybór miasta (np. Katowice)
* `--units imperial` - Zmiana na stopnie Fahrenheita
* `--gui` - Uruchomienie interfejsu graficznego
