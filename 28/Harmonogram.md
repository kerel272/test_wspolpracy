## 1. Analiza wymagań [??]
- Ustalenie funkcjonalności: pobieranie danych z wttr.in, obsługa CLI i GUI.
- Sprawdzenie formatu JSON i potrzebnych pól (`temp_C`, `windspeedKmph`).
- Określenie obsługi błędów (brak miasta, brak internetu, błędny kod kraju).

## 2. Projekt struktury programu [??]
- Podział na moduły: logika pobierania, konwersje jednostek, CLI, GUI.
- Zaplanowanie funkcji: `get_weather()`, `show_gui()`, `main()`.
- Ustalenie przepływu danych między modułami.

## 3. Implementacja funkcji pobierania pogody [??]
- Wysyłanie zapytania HTTP do `wttr.in`.
- Parsowanie JSON i wyciąganie danych.
- Konwersje jednostek: °C ↔ °F, km/h ↔ mph ↔ m/s.
- Obsługa wyjątków i zwracanie czytelnych komunikatów.

## 4. Implementacja interfejsu CLI [??]
- Dodanie argumentów: `--city`, `--country`, `--units`, `--gui`.
- Formatowanie wyników w terminalu.
- Testy działania dla różnych kombinacji argumentów.

## 5. Implementacja GUI (Tkinter) [??]
- Stworzenie okna, pól tekstowych, przycisków i etykiet.
- Obsługa zdarzeń i wyświetlanie wyników.
- Komunikaty błędów w `messagebox`.
- Testy ergonomii i poprawności.

## 6. Testy całościowe [??]
- Sprawdzenie działania dla różnych miast i krajów.
- Testy offline (brak internetu).
- Testy błędnych danych wejściowych.

## 7. Dokumentacja projektu [??]
- Opis działania programu.
- Instrukcja uruchamiania CLI i GUI.
- Krótki opis architektury i użytych technologii.

## 8. Finalne poprawki i optymalizacja [??]
- Czyszczenie kodu.
- Uspójnienie komunikatów.
- Ostateczne testy przed oddaniem.

