# Instrukcja aktualizacji dokumentacji i zgłaszania błędów

*Dokument ROBOCZY — niezatwierdzony przez ZGKiM w Orzeszu.*

---

## 1. Cel

Instrukcja opisuje, co zrobić, gdy pracownik kadr zauważy nieaktualny przepis, błędną podstawę prawną albo brakującą informację o ZGKiM. Celem jest, aby poprawki trafiały do plików w sposób uporządkowany: z weryfikacją w źródle urzędowym, zmianą wersji, wpisem do rejestrów i wnioskiem o zatwierdzenie.

## 2. Zakres

Instrukcję stosuje się przy:

- wykryciu błędu w treści dokumentu (np. zły artykuł, literówka w nazwie aktu),
- wejściu w życie nowelizacji wpływającej na dokumentację,
- uzyskaniu od pracodawcy danych, które były oznaczone jako DO UZUPEŁNIENIA,
- zmianie nazwy pliku albo przeniesieniu dokumentu,
- zgłoszeniu błędu przez inną komórkę (kadry, płace, BHP, księgowość, IOD).

Instrukcji nie stosuje się do zmian w umowach i aktach osobowych konkretnych pracowników — tam obowiązują odrębne procedury i przepisy o ochronie danych osobowych.

## 3. Odpowiedzialność

| Rola | Obowiązek |
| --- | --- |
| Zgłaszający (dowolny pracownik) | Zgłasza błąd z podaniem pliku, fragmentu i przyczyny wątpliwości. |
| Specjalista ds. kadr | Weryfikuje zgłoszenie, poprawia plik, aktualizuje rejestry. |
| Księgowość / dział płac | Potwierdza dane dotyczące rozliczeń, ZUS, PFRON, PIT, ZFŚS. |
| Służba BHP | Potwierdza dane o badaniach, uprawnieniach i ryzyku zawodowym. |
| Inspektor ochrony danych (jeśli wyznaczony) | Opiniuje zmiany dotyczące przetwarzania danych osobowych. |
| Obsługa prawna (do uzupełnienia) | Rozstrzyga wątpliwość interpretacyjną. |
| Dyrektor Zakładu | Zatwierdza zaktualizowany dokument. Bez jego potwierdzenia status pozostaje ROBOCZY. |

## 4. Dokumenty i informacje wejściowe

- Plik, który ma zostać poprawiony.
- Link do źródła urzędowego z [Wykazu źródeł urzędowych](Wykaz_zrodel_urzedowych.md).
- [Rejestr zmian prawnych](Rejestr_zmian_prawnych.md) — czy zmiana już jest wpisana.
- [Rejestr weryfikacji dokumentów](Rejestr_weryfikacji_dokumentow.md) — aktualna wersja i status pliku.
- [Lista najczęstszych błędów kadrowych](../10_Kontrole_i_Audyt/Lista_najczestszych_bledow_kadrowych.md) — czy błąd już został opisany.
- Potwierdzenie od pracodawcy (jeśli uzupełniasz dane ZGKiM).

## 5. Procedura postępowania

### Krok 1 — Rozpoznaj, co jest nieaktualne

Sygnały ostrzegawcze:

- w dokumencie widnieje stary numer pozycji Dz.U. (np. „Dz.U. 2024 poz. 535" zamiast „tekst jedn. Dz.U. 2026 poz. 474"),
- podano artykuł, który nie dotyczy opisywanej czynności (np. pkt 4a zamiast pkt 4b w ogłoszeniu o naborze),
- dokument używa nazwy formularza, którego już nie ma (PIT-4) albo starego oznaczenia (DEK-I-0),
- treść mówi o „Kierowniku" tam, gdzie obowiązujący statut używa „Dyrektora",
- w pliku jest adnotacja DO UZUPEŁNIENIA PRZEZ PRACODAWCĘ i pracodawca przekazał już dane,
- zmiana przepisu wpłynęła na termin, wymiar albo dokument wynikowy.

Zapisz: nazwę pliku, numer sekcji lub wiersza, fragment, który budzi wątpliwość, i datę wykrycia.

### Krok 2 — Zweryfikuj w źródle urzędowym

1. Otwórz ISAP albo Dziennik Ustaw (linki w [Wykazie źródeł](Wykaz_zrodel_urzedowych.md)).
2. Sprawdź, czy masz **tekst jednolity obowiązujący w dniu weryfikacji**.
3. Odczytaj datę wejścia w życie i przepisy przejściowe.
4. Porównaj treść przepisu z opisem w dokumencie — nie kopiuj przepisu, sformułuj własną instrukcję.
5. Jeśli przepis jest niejednoznaczny — wpisz status DO WERYFIKACJI i zapytaj obsługę prawną. **Nie zgaduj.**

W dokumencie podaj zawsze: pełną nazwę aktu, artykuł/paragraf/punkt, link, datę weryfikacji i status (ROBOCZY / DO WERYFIKACJI).

### Krok 3 — Zdecyduj o zmianie

| Sytuacja | Decyzja |
| --- | --- |
| Błąd literacki albo zły numer pozycji | Poprawka w miejscu, wersja +0.1. |
| Zmiana przepisu wpływa na instrukcję | Nowa wersja (np. 1.1), aktualizacja podstawy prawnej i terminów. |
| Zmiana całej procedury | Nowa wersja główna (np. 2.0), wpis do rejestru zmian prawnych. |
| Brak danych o ZGKiM | Pozostaw adnotację DO UZUPEŁNIENIA; po otrzymaniu danych uzupełnij z potwierdzeniem. |
| Dokument zastąpiony innym | Status ARCHIWALNY, zachowanie historii, aktualizacja odnośników. |

### Krok 4 — Popraw plik

- Użyj narzędzia do edycji pliku; nie twórz duplikatu pod inną nazwą.
- Jeśli zmieniasz nazwę pliku, zaktualizuj **wszystkie** odnośniki w repozytorium.
- Zachowaj historię zmian w pliku (tabela na końcu).
- Sprawdź polskie znaki i spójność nazewnictwa (ASCII w nazwach plików).
- Nie wprowadzaj do pliku danych osobowych ani niepotwierdzonych faktów o ZGKiM.

### Krok 5 — Zaktualizuj rejestry

1. [Rejestr zmian prawnych](Rejestr_zmian_prawnych.md) — dodaj wpis z datą wejścia w życie i listą plików do poprawy.
2. [Rejestr weryfikacji dokumentów](Rejestr_weryfikacji_dokumentow.md) — zwiększ wersję, wpisz datę weryfikacji, opisz zmianę w historii.
3. [Lista najczęstszych błędów kadrowych](../10_Kontrole_i_Audyt/Lista_najczestszych_bledow_kadrowych.md) — jeśli błąd się powtarzał, dopisz go do listy.
4. Jeśli zmiana dotyczy wzoru DOCX/XLSX — uzupełnij metrykę wzoru (nawet jeśli plik jest w innym folderze).

### Krok 6 — Sprawdź odnośniki i strukturę

Uruchom [skrypt kontroli repozytorium](skrypt_kontroli.py):

```
python skrypt_kontroli.py
```

Skrypt sprawdza istnienie wymaganych plików, puste pliki, lokalne odnośniki Markdown i obecność nagłówka. Popraw zgłoszone błędy w swoich plikach; błędy w plikach innych komórek zgłoś zgodnie z krokiem 8.

### Krok 7 — Wnieś o zatwierdzenie

Przygotuj krótką notatkę dla Dyrektora:

- nazwa pliku i nowa wersja,
- co się zmieniło i dlaczego,
- podstawa prawna z linkiem i datą weryfikacji,
- informacja o tym, czy zmiana wymaga decyzji (np. przyjęcie regulaminu, zmiana wzoru umowy),
- miejsce na podpis i datę zatwierdzenia.

Do czasu otrzymania potwierdzenia dokument pozostaje **ROBOCZY**. Nie wpisuj statusu ZATWIERDZONY na podstawie domniemania.

### Krok 8 — Zgłoś błąd

Jeśli nie możesz sam poprawić dokumentu (np. plik należy do innej komórki albo potrzebna jest decyzja prawna), zgłoś:

| Pole | Co wpisać |
| --- | --- |
| Data zgłoszenia | data wykrycia |
| Zgłaszający | rola / stanowisko (bez danych osobowych w repozytorium) |
| Plik i sekcja | np. `07_Kalendarz...md`, sekcja I, pozycja „PIT-4" |
| Opis błędu | konkretny fragment i dlaczego jest błędny |
| Źródło weryfikacji | link do ISAP/Dz.U./gov.pl |
| Proponowana poprawka | propozycja nowego brzmienia |
| Priorytet | wysoki (błędny termin / przepis) / średni / niski (literówka) |
| Status zgłoszenia | nowe / w toku / poprawione / odrzucone (z uzasadnieniem) |

Zgłoszenie przekazuj drogą służbową do specjalisty ds. kadr i — jeśli dotyczy rozliczeń — do księgowości. Nie umieszczaj treści zgłoszenia z danymi pracowników w repozytorium.

## 6. Zasady wersjonowania

| Zmiana | Wersja |
| --- | --- |
| Pierwsze opracowanie | 1.0 |
| Poprawka redakcyjna, link, data weryfikacji | 1.1, 1.2 … |
| Zmiana jednego przepisu albo terminu | 1.x → 1.x+1 |
| Zmiana struktury, celu albo całej procedury | 2.0, 3.0 … |
| Wycofanie dokumentu | status ARCHIWALNY, nowy plik dostaje wersję 1.0 |

W każdej wersji aktualizuj datę ostatniej weryfikacji — wersja bez daty weryfikacji jest bezwartościowa.

## 7. Kontrola poprawności

- Czy poprawka wynika z źródła urzędowego, a nie z intuicji?
- Czy podano pełną nazwę aktu, przepis, link, datę weryfikacji i status?
- Czy zmieniono wersję i historię zmian?
- Czy zaktualizowano oba rejestry?
- Czy odnośniki do pliku działają (skrypt kontroli)?
- Czy nie powstał duplikat dokumentu?
- Czy status dokumentu nie sugeruje zatwierdzenia przez ZGK bez potwierdzenia?

## 8. Terminy

| Rodzaj zadania | Termin (do ustalenia przez ZGKiM) |
| --- | --- |
| Weryfikacja po wejściu w życie zmiany | Przed pierwszym zastosowaniem nowej zasady. |
| Aktualizacja dokumentacji | Nie zwlekaj dłużej niż do najbliższego okresu rozliczeniowego. |
| Odpowiedź na zgłoszenie błędu | 5 dni roboczych (termin roboczy — do potwierdzenia). |
| Zatwierdzenie przez Dyrektora | Przed wdrożeniem nowej wersji jako obowiązującej. |

## 9. Podstawa prawna

| Pełna nazwa aktu prawnego | Przepis | Źródło oficjalne | Status |
| --- | --- | --- | --- |
| Ustawa z dnia 20 lipca 2000 r. o ogłaszaniu aktów normatywnych i niektórych innych aktów prawnych | art. 16 (ogłaszanie tekstów jednolitych) | [ELI — Dz.U. 2019 poz. 1461](https://eli.gov.pl/eli/DU/2019/1461/ogl) | DO WERYFIKACJI |
| Rozporządzenie Ministra Rodziny, Pracy i Polityki Społecznej z dnia 10 grudnia 2018 r. w sprawie dokumentacji pracowniczej | § 3, § 4 | [ELI — tekst jedn. Dz.U. 2026 poz. 474](https://eli.gov.pl/eli/DU/2026/474/ogl) | ROBOCZY |

**Data weryfikacji: 2026-11-25.** Status dokumentu: ROBOCZY.

## 10. Historia zmian

| Data | Wersja | Opis zmiany |
| --- | --- | --- |
| 2026-11-25 | 1.0 | Opracowanie instrukcji: wykrywanie nieaktualności, weryfikacja, poprawa pliku, aktualizacja rejestrów, wniosek o zatwierdzenie, zgłoszenie błędu, wersjonowanie. |
