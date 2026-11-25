# Standard opracowania procedur i checklist

Dokument porządkuje formę nowych i aktualizowanych instrukcji w repozytorium. Nie zmienia treści merytorycznej istniejących procedur — opisuje **jak je pisać, żeby były spójne i używalne**.

**Status:** ROBOCZY · **Data opracowania i weryfikacji:** 2026-11-25 · **Wersja:** 1.0

---

## 1. Cel

Ujednolicić układ dokumentów tak, aby nowy kadrowca od razu wiedział, gdzie w procedurze szukać odpowiedzialności, terminów i podstawy prawnej, a kontrolujący — jak udokumentować wykonanie.

## 2. Zasady ogólne

1. **Jeden plik = jeden problem pracownika.** Nie łącz niepowiązanych procesów ani nie powielaj treści z innego pliku — użyj odnośnika.
2. **Tytuł opisuje zadanie**, np. `Procedura wypłaty dodatkowego wynagrodzenia rocznego.md`, nie `Dokument 12.md`.
3. **Nazwy plików bez polskich znaków**, z polskimi znakami w treści.
4. Metryka na początku każdego dokumentu: nazwa, wersja, data opracowania, data ostatniej weryfikacji, rola odpowiedzialna, status, zakład.
5. Statusy zgodne z [`Rejestrem weryfikacji dokumentów`](Rejestr_weryfikacji_dokumentow.md): ROBOCZY, DO WERYFIKACJI, ZATWIERDZONY, ARCHIWALNY.
6. **Nie oznaczaj dokumentu jako ZATWIERDZONY** bez potwierdzenia przez Dyrektora ZGKiM.
7. Każdy przepis: pełna nazwa aktu, artykuł/paragraf, link do źródła urzędowego, data weryfikacji i informacja o konieczności dalszego sprawdzenia.
8. Nie wpisuj rzeczywistych danych pracowników — używaj `[Imię i nazwisko]`, `[Pracownik A]`, `[PESEL]`.

## 3. Standardowa struktura procedury / instrukcji

| Nr | Sekcja | Co wpisać |
| --- | --- | --- |
| 1 | Cel | Jedno zdanie: jaki problem rozwiązuje dokument. |
| 2 | Zakres | Kiedy stosować, kogo dotyczy, czego nie obejmuje. |
| 3 | Odpowiedzialność | Tabela ról: kto wykonuje, kto zatwierdza, kto jest konsultowany. |
| 4 | Dokumenty i informacje wejściowe | Co trzeba mieć przed rozpoczęciem. |
| 5 | Procedura postępowania | Numerowane kroki, każdy z wynikiem i punktem kontrolnym. |
| 6 | Wzory dokumentów | Odnośniki do plików DOCX/XLSX/MD — bez kopiowania ich treści. |
| 7 | Kontrola poprawności | Lista pytań weryfikacyjnych. |
| 8 | Terminy | Tabela: termin, obowiązek, podstawa. |
| 9 | Podstawa prawna | Akty, artykuły, linki, data weryfikacji, status. |
| 10 | Historia zmian | Wersja, data, opis zmiany. |

Układ nie jest sztywny: prostą checklistę lub krótki wzór można zapisać zwięźle, ale zachowaj czytelność i metrykę.

## 4. Standard checklisty

- Tytuł z czasem trwania lub celem, np. `Checklista cyklicznych obowiązków kadrowych`.
- Metryka jak w procedurze.
- Tabela z kolumnami statusu: **W** (wykonano), **NW** (nie wykonano), **ND** (nie dotyczy), **WY** (wymaga wyjaśnienia).
- Każdy wiersz: zadanie, termin, podstawa, rola odpowiedzialna, dokument wynikowy, sposób potwierdzenia.
- Terminy zdarzeniowe (np. 7 dni od zatrudnienia) nie mogą być wpisywane jako stały dzień miesiąca.
- Na końcu: podpis/ data kontroli i odnośnik do dokumentu źródłowego.

## 5. Standard odnośników

- Odnośniki względne: `[Opis](../03_Czas_Pracy_i_Urlopy/Instrukcja_ustalania_wymiaru_urlopu.md)`.
- Linki zewnętrzne prowadzą do ISAP, Dz.U., ELI, gov.pl, ZUS, PIP, PFRON, mojeppk.pl lub EUR-Lex.
- Po utworzeniu pliku uruchom [`skrypt_kontroli.py`](skrypt_kontroli.py) — wykryje brakujące odnośniki i puste pliki.
- Po dodaniu nowego pliku zaktualizuj [`INDEKS_DOKUMENTACJI.md`](../INDEKS_DOKUMENTACJI.md) poleceniem z [`generuj_indeks.py`](generuj_indeks.py).

## 6. Kontrola przed publikacją

- [ ] Czy plik ma metrykę, status i datę weryfikacji?
- [ ] Czy treść rozwiązuje konkretny problem i nie powtarza innego dokumentu?
- [ ] Czy wszystkie odnośniki działają (skrypt kontroli)?
- [ ] Czy przepisy mają pełną nazwę, artykuł, link i datę weryfikacji?
- [ ] Czy nie ma rzeczywistych danych osobowych ani niepotwierdzonych ustaleń ZGKiM?
- [ ] Czy wpisano zmianę do [`Rejestru weryfikacji dokumentów`](Rejestr_weryfikacji_dokumentow.md)?

## 7. Podstawa i metryka

Podstawa: [AGENTS.md](../AGENTS.md) (zasady pracy z repozytorium), [`Instrukcja aktualizacji i zgłaszania błędów`](Instrukcja_aktualizacji_i_zglaszania_bledow.md), [`Wykaz źródeł urzędowych`](Wykaz_zrodel_urzedowych.md).

| Wersja | Data | Opis |
| --- | --- | --- |
| 1.0 | 2026-11-25 | Ustanowienie standardu procedur i checklist. |
