


# Instrukcja użytkownika – Program „Pogoda”

**Wersja:** 1.0  
**Autor:** Bartłomiej Kozieł  
**Data opracowania:** 2026-02-08  
**Grupa docelowa:** Użytkownicy końcowi (osoby chcące sprawdzić aktualną pogodę w danym mieście)

---

## Spis treści
1. [Wprowadzenie](#wprowadzenie)  
2. [Instalacja i uruchomienie](#instalacja-i-uruchomienie)  
3. [Opis interfejsu użytkownika](#opis-interfejsu-użytkownika)  
4. [Instrukcje krok po kroku – podstawowe funkcje](#instrukcje-krok-po-kroku--podstawowe-funkcje)  
5. [Częste problemy i rozwiązania (FAQ)](#częste-problemy-i-rozwiązania-faq)  
6. [Dane kontaktowe / zgłaszanie błędów](#dane-kontaktowe--zgłaszanie-błędów)  
7. [Słownik pojęć (glossary)](#słownik-pojęć-glossary)

---

## Wprowadzenie

Program **Pogoda** służy do sprawdzania aktualnej temperatury oraz prędkości wiatru dla wybranego miasta.  
Aplikacja może działać w dwóch trybach:
- w trybie tekstowym (w konsoli),
- w trybie graficznym (okno aplikacji).
Dane na temat pogody zwracane są na podstawie strony **wttr.in**

### Przeznaczenie aplikacji
Aplikacja jest przeznaczona dla użytkowników, którzy chcą szybko sprawdzić aktualne warunki pogodowe dla wskazanej lokalizacji.

### Wymagania systemowe
- system operacyjny: Windows / Linux / macOS  
- zainstalowany Python 3  
- dostęp do Internetu  

### Grupa użytkowników
- użytkownicy końcowi  
- osoby korzystające z terminala lub prostych aplikacji okienkowych  

---

## Instalacja i uruchomienie

### Instalacja
1. Pobierz plik programu `pogoda.py`.
2. Upewnij się, że masz zainstalowanego Pythona w wersji 3.

### Uruchomienie w trybie tekstowym
W terminalu wpisz:
```
python pogoda.py --city NAZWA_MIASTA
````

Przykład:

```bash
python pogoda.py --city Katowice
```

### Uruchomienie w trybie graficznym

Aby uruchomić wersję z oknem:

```bash
python pogoda.py --gui
```

---

## Opis interfejsu użytkownika

### Tryb graficzny (okno programu)

Elementy interfejsu:

* **Pole „Miasto”** – służy do wpisania nazwy miasta (np. Katowice).
* **Pole „Kraj”** – opcjonalne pole do wpisania kodu kraju (np. PL, US).
* **Opcja „Europejskie (°C, m/s)”** – wybór jednostek metrycznych.
* **Opcja „Amerykańskie (°F, mph)”** – wybór jednostek imperialnych.
* **Przycisk „Pokaż pogodę”** – pobiera dane i wyświetla wynik.
* **Pole wyniku** – pokazuje temperaturę i prędkość wiatru.

---

## Instrukcje krok po kroku – podstawowe funkcje

### Sprawdzenie pogody w trybie graficznym

1. Uruchom program z opcją `--gui`.
2. W polu **Miasto** wpisz nazwę miasta.
3. (Opcjonalnie) Wpisz kod kraju w polu **Kraj**.
4. Wybierz jednostki:

   * Europejskie (°C, m/s)
   * Amerykańskie (°F, mph)
5. Kliknij przycisk **Pokaż pogodę**.
6. Na ekranie pojawi się:

   * aktualna temperatura,
   * prędkość wiatru.

**Oczekiwany rezultat:**
Wyświetlenie informacji pogodowych dla wybranego miasta.

---

### Sprawdzenie pogody w trybie tekstowym

1. Otwórz terminal.
2. Wpisz:

   ```bash
   python pogoda.py --city Katowice
   ```
3. Program wyświetli:

   * temperaturę,
   * prędkość wiatru.

Przykładowy wynik:

```
Temperatura: 12.3°C
Prędkość wiatru: 3.2 m/s
```

---

## Częste problemy i rozwiązania (FAQ)

**1. Program wyświetla komunikat o błędzie przy pobieraniu danych.**
Sprawdź:

* czy masz dostęp do Internetu,
* czy poprawnie wpisałeś nazwę miasta.

**2. Program nie uruchamia się.**
Upewnij się, że:

* masz zainstalowanego Pythona 3,
* uruchamiasz program poprawną komendą.

**3. Brak wyniku po kliknięciu przycisku.**
Sprawdź, czy pole „Miasto” nie jest puste.

---

## Dane kontaktowe / zgłaszanie błędów

W przypadku znalezienia błędu w działaniu programu należy zgłosić problem:

* poprzez system zgłoszeń (Issues) w repozytorium GitHub,
* lub mailowo na **bkoziel_221p@e.zseeim.edu.pl**

---

## Słownik pojęć (glossary)

| Pojęcie              | Definicja                                                      |
| -------------------- | -------------------------------------------------------------- |
| Użytkownik           | Osoba korzystająca z programu Pogoda.                          |
| Interfejs            | Sposób komunikacji użytkownika z aplikacją (okno lub konsola). |
| Temperatura          | Aktualna wartość ciepła powietrza w danym miejscu.             |
| Prędkość wiatru      | Szybkość poruszania się powietrza.                             |
| Jednostki metryczne  | Stopnie Celsjusza (°C) i metry na sekundę (m/s).               |
| Jednostki imperialne | Stopnie Fahrenheita (°F) i mile na godzinę (mph).              |
| Terminal             | Okno do wpisywania poleceń tekstowych.                         |
| Parametr             | Opcja przekazywana przy uruchamianiu programu (np. `--city`).  |

---
