# Harmonogram projektu – aplikacja pogodowa w Pythonie

## 1. Analiza wymagań
**Czas:** [??]

**Zadania:**
- określenie funkcjonalności aplikacji (pobieranie pogody dla miasta)
- ustalenie obsługi kraju (opcjonalnie)
- wybór jednostek (metric / imperial)
- określenie trybów działania: CLI oraz GUI
- wybór technologii i bibliotek (`requests`, `tkinter`, `argparse`)
- zaplanowanie ogólnej struktury programu

---

## 2. Projektowanie aplikacji
**Czas:** [??]

**Zadania:**
- zaprojektowanie struktury programu
- określenie głównych funkcji:
  - `get_weather()`
  - `show_gui()`
  - `main()`
- zaplanowanie przepływu działania aplikacji
- zaprojektowanie interfejsu GUI (pola tekstowe, przycisk, wynik)

---

## 3. Implementacja pobierania danych pogodowych
**Czas:** [??]

**Zadania:**
- napisanie funkcji `get_weather()`
- wysyłanie zapytania HTTP do serwisu `wttr.in`
- przetwarzanie danych w formacie JSON
- pobieranie temperatury i prędkości wiatru
- konwersja jednostek (°C ↔ °F, km/h → m/s lub mph)
- obsługa błędów (np. brak połączenia lub błędne miasto)

---

## 4. Implementacja trybu CLI
**Czas:** [??]

**Zadania:**
- konfiguracja `argparse`
- obsługa argumentów:
  - `--city`
  - `--country`
  - `--units`
  - `--gui`
- wyświetlanie wyników w terminalu
- obsługa komunikatów błędów

---

## 5. Implementacja GUI
**Czas:** [??]

**Zadania:**
- utworzenie okna aplikacji w `tkinter`
- dodanie elementów interfejsu:
  - pole tekstowe – miasto
  - pole tekstowe – kraj
  - wybór jednostek
  - przycisk pobierania pogody
  - pole wyświetlania wyniku
- połączenie GUI z funkcją `get_weather()`

---

## 6. Testowanie aplikacji
**Czas:** [??]

**Zadania:**
- testowanie poprawnych i błędnych nazw miast
- testowanie działania w różnych jednostkach
- sprawdzenie działania CLI i GUI
- sprawdzenie obsługi błędów
- poprawa znalezionych problemów

---

## 7. Dokumentacja projektu
**Czas:** [??]

**Zadania:**
- opis działania aplikacji
- opis użycia argumentów CLI
- komentarze w kodzie
- przygotowanie instrukcji dla użytkownika
