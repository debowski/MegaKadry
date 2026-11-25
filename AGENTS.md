# ZADANIE DLA AGENTA AI
## Kompleksowa rozbudowa repozytorium MegaKadry

Repozytorium: https://github.com/debowski/MegaKadry

## 1. Cel projektu

Twoim zadaniem jest kompleksowa analiza, rozbudowa i uporządkowanie repozytorium MegaKadry.

Projekt ma stanowić kompletny, praktyczny i uporządkowany zestaw dokumentacji wspierającej nowego pracownika zajmującego się kadrami w Zakładzie Gospodarki Komunalnej w Orzeszu.

Nie twórz wyłącznie katalogów, pustych plików ani ogólnych opisów.

Opracuj rzeczywistą dokumentację, która pozwoli pracownikowi:

- zrozumieć zakres obowiązków kadrowych,
- samodzielnie wykonywać typowe zadania,
- przygotowywać dokumenty kadrowe,
- kontrolować terminy i kompletność dokumentacji,
- prawidłowo prowadzić procesy zatrudnienia,
- obsługiwać zmiany w zatrudnieniu,
- rozliczać czas pracy i urlopy,
- współpracować z działem płac, BHP, księgowością i kierownictwem,
- przygotowywać dokumentację przy zakończeniu zatrudnienia,
- kontrolować zgodność dokumentacji z obowiązującymi przepisami.

Projekt ma być przyjazny dla osoby, która nie musi znać struktury repozytorium ani Markdown.

## 2. Zasady pracy z repozytorium

Przed rozpoczęciem modyfikacji:

1. Przeanalizuj całe repozytorium.
2. Zapoznaj się z README.md.
3. Sprawdź wszystkie katalogi i pliki.
4. Przeczytaj istniejące instrukcje, procedury, wzory i checklisty.
5. Zidentyfikuj dokumenty niekompletne, nieaktualne, powielone lub wymagające weryfikacji.
6. Ustal, które materiały można zachować, rozwinąć, połączyć lub przenieść.
7. Przygotuj plan zmian, ale nie kończ pracy na samym planie.

Następnie wykonaj wszystkie możliwe prace bezpośrednio w repozytorium.

### Zasady bezwzględne

- Nie usuwaj wartościowych istniejących dokumentów bez uzasadnienia.
- Nie zastępuj istniejących opracowań pustymi szablonami.
- Nie twórz kilku dokumentów zawierających tę samą treść.
- Nie zmieniaj nazw istniejących plików bez aktualizacji wszystkich odwołań.
- Nie zakładaj, że ZGK w Orzeszu jest jednostką budżetową, zakładem budżetowym lub spółką prawa handlowego, jeśli nie potwierdzisz tego w wiarygodnym źródle.
- Nie wymyślaj regulaminów, zasad wynagradzania ani wewnętrznych procedur ZGK.
- Nie przedstawiaj niezweryfikowanych informacji prawnych jako obowiązujących.
- Nie umieszczaj rzeczywistych danych osobowych pracowników.
- Nie ograniczaj się do przygotowania raportu. Wykonaj zmiany w plikach.

Jeżeli nie masz dostępu do konkretnej informacji dotyczącej ZGK, oznacz ją jako wymagającą uzupełnienia przez pracodawcę.

## 3. Analiza prawna i organizacyjna

Przed opracowaniem dokumentacji ustal możliwie dokładnie:

- formę prawną pracodawcy,
- zasady zatrudniania pracowników,
- zakres zastosowania ustawy o pracownikach samorządowych,
- obowiązujące regulaminy pracy i wynagradzania,
- zasady funkcjonowania ZFŚS,
- zasady organizacji czasu pracy,
- sposób prowadzenia dokumentacji pracowniczej,
- zakres odpowiedzialności działu kadr,
- zakres współpracy z działem płac,
- zakres współpracy ze służbą BHP,
- stosowane systemy informatyczne, o ile są znane.

Korzystaj z oficjalnych źródeł:

- ISAP: https://isap.sejm.gov.pl/
- Dziennik Ustaw: https://dziennikustaw.gov.pl/
- ZUS: https://www.zus.pl/
- Państwowa Inspekcja Pracy: https://www.pip.gov.pl/
- Portal PPK: https://www.mojeppk.pl/

W dokumentach prawnych podawaj:

- pełną nazwę aktu prawnego,
- właściwy artykuł, paragraf lub punkt,
- link do źródła,
- datę weryfikacji,
- informację, czy dokument wymaga dodatkowej weryfikacji.

Jeżeli nie możesz zweryfikować aktualnego stanu prawnego, nie zgaduj. Oznacz dokument jako wymagający sprawdzenia.

Nie kopiuj obszernych fragmentów aktów prawnych. Twórz własne instrukcje i odsyłaj do oficjalnych źródeł.

## 4. Docelowa struktura repozytorium

Rozbuduj repozytorium do następującej struktury, zachowując istniejące materiały i ich historię:

MegaKadry/
├── 00_Start/
│   ├── README.md
│   ├── Instrukcja_dla_nowego_kadrowca.md
│   ├── Mapa_obowiazkow_kadrowych.md
│   ├── Najczestsze_zadania.md
│   ├── Kontakty_i_odpowiedzialnosci.md
│   ├── Slownik_pojec_kadrowych.md
│   └── Konfiguracja_ZGK_Orzesze.md
│
├── 01_Akta_Osobowe/
│
├── 02_Rekrutacja_i_Zatrudnienie_Samorzadowe/
│
├── 03_Czas_Pracy_i_Urlopy/
│
├── 04_Wynagrodzenia_i_Swiadczenia/
│
├── 05_BHP_Badania_i_Uprawnienia_ZGK/
│
├── 06_Regulaminy_i_Procedury_Zakladowe/
│
├── 07_Kalendarz_i_Checklisty_Kadrowca/
│
├── 08_Zmiany_w_zatrudnieniu/
│
├── 09_Zakonczenie_zatrudnienia/
│
├── 10_Kontrole_i_Audyt/
│
├── 11_Aktualizacje_i_Zrodla/
│
├── 12_Wzory_Dokumentow/
│   ├── DOCX/
│   ├── XLSX/
│   └── PDF/
│
├── .gitignore
├── README.md
└── LICENSE

Nie twórz na siłę pustych katalogów. Każdy katalog powinien zawierać rzeczywiste opracowania lub uzasadnioną strukturę przygotowaną do dalszego rozwoju.

Jeżeli istniejące katalogi mają inną nazwę, zachowaj spójność z repozytorium i unikaj niepotrzebnych zmian.

## 5. Opracowanie katalogu 00_Start

Katalog 00_Start ma być punktem wejścia dla nowego pracownika.

Opracuj:

### Instrukcja_dla_nowego_kadrowca.md

Dokument powinien zawierać:

- opis roli pracownika kadr,
- zakres typowych obowiązków,
- sposób korzystania z repozytorium,
- opis struktury katalogów,
- instrukcję odnajdywania wzorów dokumentów,
- instrukcję realizacji najczęstszych zadań,
- zasady współpracy z innymi komórkami,
- zasady ochrony danych osobowych,
- sposób postępowania w sytuacjach nietypowych.

### Mapa_obowiazkow_kadrowych.md

Przedstaw procesy kadrowe w sposób uporządkowany.

Uwzględnij:

- zatrudnienie,
- prowadzenie akt osobowych,
- czas pracy,
- urlopy,
- wynagrodzenia,
- badania i uprawnienia,
- zmiany w zatrudnieniu,
- zakończenie zatrudnienia,
- obowiązki okresowe i roczne.

### Najczestsze_zadania.md

Przygotuj praktyczne instrukcje typu:

- Jak zatrudnić nowego pracownika?
- Jak przygotować umowę o pracę?
- Jak obsłużyć wniosek urlopowy?
- Jak rozliczyć nadgodziny?
- Jak skierować pracownika na badania?
- Jak przygotować dokumenty przy zmianie stanowiska?
- Jak przygotować dokumenty przy zakończeniu zatrudnienia?

### Kontakty_i_odpowiedzialnosci.md

Nie wpisuj wymyślonych nazwisk, numerów telefonów ani adresów.

Przygotuj tabelę do uzupełnienia:

- stanowisko lub komórka organizacyjna,
- zakres odpowiedzialności,
- sposób kontaktu,
- zastępstwo,
- uwagi.

### Slownik_pojec_kadrowych.md

Przygotuj słownik najważniejszych pojęć kadrowych, prawnych i płacowych.

Wyjaśnienia mają być proste, praktyczne i zrozumiałe dla nowego pracownika.

### Konfiguracja_ZGK_Orzesze.md

Przygotuj dokument zawierający informacje wymagające potwierdzenia przez pracodawcę.

Nie uzupełniaj nieznanych informacji fikcyjnymi danymi.

## 6. Rozbudowa akt osobowych

W katalogu 01_Akta_Osobowe opracuj lub uzupełnij:

- instrukcję prowadzenia akt osobowych,
- zasady podziału dokumentacji na części A, B, C, D i E,
- checklistę kompletności akt,
- procedurę zakładania akt osobowych,
- procedurę numerowania dokumentów,
- procedurę włączania dokumentów do akt,
- procedurę przenoszenia dokumentów między częściami,
- procedurę prowadzenia dokumentacji elektronicznej,
- procedurę udostępniania dokumentacji,
- procedurę wydawania kopii dokumentów,
- zasady przechowywania dokumentacji,
- procedurę obsługi dokumentacji po zakończeniu zatrudnienia.

Przygotuj dokument:

Instrukcja_obslugi_akt_osobowych.md

Powinien prowadzić pracownika krok po kroku przez obsługę dokumentów.

## 7. Rozbudowa rekrutacji i zatrudnienia

W katalogu 02_Rekrutacja_i_Zatrudnienie_Samorzadowe opracuj:

- procedurę zatrudnienia pracownika na stanowisku urzędniczym,
- procedurę zatrudnienia pracownika na stanowisku pomocniczym lub obsługi,
- procedurę zatrudnienia pracownika fizycznego,
- checklistę dokumentów przed zatrudnieniem,
- instrukcję przygotowania umowy o pracę,
- instrukcję przygotowania informacji o warunkach zatrudnienia,
- procedurę skierowania na badania wstępne,
- procedurę zgłoszenia pracownika do ZUS,
- procedurę przygotowania dokumentów na pierwszy dzień pracy,
- procedurę wdrożenia pracownika,
- procedurę obsługi służby przygotowawczej, jeżeli ma zastosowanie,
- procedurę przygotowania dokumentacji do rozpoczęcia pracy.

Przygotuj główną procedurę:

Procedura_zatrudnienia_pracownika.md

Dokument powinien przedstawiać cały proces od decyzji o zatrudnieniu do zakończenia formalności związanych z rozpoczęciem pracy.

## 8. Rozbudowa czasu pracy i urlopów

W katalogu 03_Czas_Pracy_i_Urlopy opracuj:

- instrukcję prowadzenia ewidencji czasu pracy,
- przykładową ewidencję dla pracownika administracyjnego,
- przykładową ewidencję dla pracownika fizycznego,
- przykładową ewidencję dla pracownika zmianowego,
- procedurę rozliczania nadgodzin,
- procedurę rozliczania pracy w niedziele i święta,
- procedurę rozliczania dyżurów i gotowości do usuwania awarii,
- instrukcję rozliczania nieobecności,
- instrukcję ustalania wymiaru urlopu,
- procedurę udzielania urlopu na żądanie,
- procedurę rozliczania urlopu zaległego,
- instrukcję ustalania wymiaru czasu pracy,
- procedurę rozliczania czasu pracy w różnych okresach rozliczeniowych.

Przygotuj praktyczne checklisty i przykłady obliczeń.

Jeżeli tworzysz kalkulator lub arkusz Excel, sprawdź poprawność formuł na przykładowych danych.

Nie zakładaj, że wszyscy pracownicy ZGK pracują w tym samym systemie czasu pracy.

## 9. Rozbudowa wynagrodzeń i świadczeń

W katalogu 04_Wynagrodzenia_i_Swiadczenia opracuj:

- instrukcję ustalania stażu pracy do poszczególnych uprawnień,
- procedurę naliczania dodatku za wieloletnią pracę,
- procedurę ustalania prawa do nagrody jubileuszowej,
- procedurę obsługi odpraw,
- procedurę obsługi potrąceń,
- procedurę obsługi zajęć komorniczych,
- instrukcję przekazywania danych do płac,
- procedurę korekty błędnie naliczonego wynagrodzenia,
- instrukcję obsługi PPK,
- instrukcję obsługi ZFŚS,
- procedurę rozliczania ekwiwalentu za niewykorzystany urlop.

Wyraźnie rozdziel zadania kadrowe od zadań płacowych.

Nie twórz niepotwierdzonych zasad wynagradzania obowiązujących w ZGK.

## 10. Rozbudowa BHP, badań i uprawnień

W katalogu 05_BHP_Badania_i_Uprawnienia_ZGK opracuj:

- procedurę kierowania na badania wstępne,
- procedurę kierowania na badania okresowe,
- procedurę kierowania na badania kontrolne,
- instrukcję monitorowania terminów badań,
- procedurę monitorowania uprawnień zawodowych,
- instrukcję obsługi uprawnień UDT,
- instrukcję obsługi uprawnień SEP,
- instrukcję obsługi prawa jazdy i badań psychotechnicznych, jeśli wymagane,
- checklistę dopuszczenia pracownika do pracy,
- procedurę ewidencjonowania odzieży roboczej,
- procedurę ewidencjonowania środków ochrony indywidualnej,
- procedurę współpracy z BHP,
- procedurę dokumentacji kadrowej po wypadku przy pracy.

Przygotuj przykładowe profile stanowisk:

- kierowca,
- operator sprzętu,
- pracownik wod-kan,
- pracownik utrzymania zieleni,
- pracownik oczyszczania miasta,
- konserwator,
- pracownik administracyjny.

Dla każdego profilu określ, jakie dokumenty i terminy należy sprawdzić.

## 11. Rozbudowa regulaminów i procedur zakładowych

W katalogu 06_Regulaminy_i_Procedury_Zakladowe opracuj:

- rejestr obowiązujących regulaminów,
- instrukcję weryfikacji aktualności regulaminów,
- procedurę konsultowania zmian,
- procedurę zapoznawania pracowników z regulaminami,
- wzór potwierdzenia zapoznania się z regulaminem,
- procedurę obsługi oświadczeń pracowników,
- instrukcję obsługi zgłoszeń wewnętrznych dotyczących sygnalistów,
- procedurę współpracy z inspektorem ochrony danych,
- instrukcję obsługi żądań pracowników dotyczących danych osobowych.

Nie twórz fikcyjnych regulaminów zakładowych.

Jeżeli przygotowujesz wzór regulaminu, wyraźnie oznacz go jako projekt wymagający dostosowania i zatwierdzenia przez pracodawcę.

## 12. Rozbudowa kalendarza i checklist

W katalogu 07_Kalendarz_i_Checklisty_Kadrowca opracuj:

- checklistę rozpoczęcia pracy nowego kadrowca,
- checklistę obowiązków codziennych,
- checklistę obowiązków tygodniowych,
- checklistę obowiązków miesięcznych,
- checklistę obowiązków kwartalnych,
- checklistę obowiązków rocznych,
- checklistę końca roku,
- checklistę zakończenia zatrudnienia,
- checklistę przekazania obowiązków,
- checklistę kontroli kompletności dokumentacji.

Kalendarz powinien wskazywać:

- zadanie,
- termin,
- podstawę prawną lub organizacyjną,
- osobę odpowiedzialną,
- dokument wynikowy,
- sposób potwierdzenia wykonania.

Nie przypisuj wszystkich obowiązków do stałego dnia miesiąca, jeżeli termin zależy od konkretnego zdarzenia.

## 13. Opracowanie zmian w zatrudnieniu

W katalogu 08_Zmiany_w_zatrudnieniu przygotuj:

- procedurę zmiany stanowiska,
- procedurę zmiany wynagrodzenia,
- procedurę zmiany wymiaru etatu,
- procedurę zmiany miejsca pracy,
- procedurę przedłużenia umowy,
- procedurę powierzenia innej pracy,
- procedurę zmiany danych pracownika.

Każda procedura powinna zawierać:

- warunki rozpoczęcia procesu,
- wymagane informacje,
- wymagane dokumenty,
- kolejne kroki,
- osoby odpowiedzialne,
- terminy,
- dokumenty wynikowe,
- kontrolę poprawności.

## 14. Opracowanie zakończenia zatrudnienia

W katalogu 09_Zakonczenie_zatrudnienia przygotuj:

- procedurę rozwiązania umowy,
- procedurę wypowiedzenia umowy,
- procedurę rozwiązania umowy za porozumieniem stron,
- procedurę przygotowania świadectwa pracy,
- procedurę rozliczenia urlopu,
- procedurę zwrotu mienia,
- procedurę wyrejestrowania z ZUS,
- checklistę odejścia pracownika,
- procedurę zakończenia zatrudnienia w przypadkach szczególnych.

Uwzględnij również sytuacje wymagające odrębnego postępowania, takie jak wygaśnięcie umowy czy śmierć pracownika.

Nie twórz jednego uniwersalnego wzoru dla wszystkich przypadków, jeżeli przepisy wymagają odmiennego postępowania.

## 15. Opracowanie kontroli i audytu

W katalogu 10_Kontrole_i_Audyt przygotuj:

- checklistę kontroli akt osobowych,
- checklistę kontroli ewidencji czasu pracy,
- checklistę kontroli terminów badań,
- checklistę kontroli dokumentacji zatrudnienia,
- checklistę kontroli obowiązków rocznych,
- listę najczęstszych błędów kadrowych,
- instrukcję przeprowadzania wewnętrznej kontroli dokumentacji.

Każda lista kontrolna powinna umożliwiać zaznaczenie:

- wykonano,
- nie wykonano,
- nie dotyczy,
- wymaga wyjaśnienia.

## 16. Opracowanie aktualizacji i źródeł

W katalogu 11_Aktualizacje_i_Zrodla przygotuj:

- rejestr zmian prawnych,
- rejestr weryfikacji dokumentów,
- wykaz oficjalnych źródeł prawnych,
- instrukcję aktualizacji dokumentacji,
- instrukcję zgłaszania błędów i nieaktualnych informacji.

Każdy dokument prawny powinien mieć metrykę:

- nazwa dokumentu,
- wersja,
- data opracowania,
- data ostatniej weryfikacji,
- osoba odpowiedzialna lub rola odpowiedzialna,
- status dokumentu,
- podstawa prawna,
- historia zmian.

Zastosuj statusy:

- ROBOCZY,
- DO WERYFIKACJI,
- ZATWIERDZONY,
- ARCHIWALNY.

Nie oznaczaj dokumentu jako zatwierdzonego przez ZGK, jeżeli nie masz potwierdzenia zatwierdzenia przez pracodawcę.

## 17. Przygotowanie wzorów dokumentów

W katalogu 12_Wzory_Dokumentow przygotuj praktyczne wzory w formatach DOCX, XLSX i PDF, zgodnie z ich przeznaczeniem.

DOCX:

- wnioski pracowników,
- oświadczenia,
- wzory pism,
- wzory dokumentów kadrowych,
- checklisty przeznaczone do wydruku.

XLSX:

- rejestry,
- ewidencje,
- kalkulatory,
- zestawienia kontrolne,
- kalendarze terminów.

PDF:

- wersje dokumentów przeznaczone do podglądu lub wydruku,
- instrukcje użytkownika,
- materiały szkoleniowe.

Wzory mają być estetyczne, czytelne i gotowe do praktycznego wykorzystania.

Stosuj:

- czytelne nagłówki,
- logiczny układ sekcji,
- pola do wypełnienia,
- instrukcje dla użytkownika,
- prawidłowe polskie znaki,
- odpowiednie marginesy,
- spójne nazewnictwo.

Nie generuj dokumentów zawierających niepotwierdzone dane pracodawcy.

## 18. Standard opracowania dokumentów Markdown

Każda instrukcja lub procedura powinna mieć możliwie spójny układ:

# Nazwa procedury

## 1. Cel
Wyjaśnienie, czego dotyczy procedura.

## 2. Zakres
Kiedy należy ją stosować.

## 3. Odpowiedzialność
Kto wykonuje zadanie i kto je zatwierdza.

## 4. Dokumenty i informacje wejściowe
Co należy przygotować przed rozpoczęciem.

## 5. Procedura postępowania
Kolejne kroki opisane prostym językiem.

## 6. Wzory dokumentów
Linki do odpowiednich plików DOCX lub XLSX.

## 7. Kontrola poprawności
Co należy sprawdzić przed zakończeniem procesu.

## 8. Terminy
Terminy ustawowe lub organizacyjne.

## 9. Podstawa prawna
Akty prawne i oficjalne źródła.

## 10. Historia zmian
Data, wersja i opis zmiany.

Nie stosuj tego układu sztywno, jeżeli dany dokument jest prostą checklistą lub krótką instrukcją. Zachowaj jednak spójność i czytelność.

## 19. Poprawa README.md

Zaktualizuj główne README.md.

Powinno zawierać:

- opis celu projektu,
- informację dla kogo jest przeznaczony,
- opis struktury katalogów,
- instrukcję korzystania z dokumentacji,
- link do instrukcji dla nowego kadrowca,
- opis formatów plików,
- zasady aktualizacji,
- zasady ochrony danych osobowych,
- informacje o statusie dokumentacji,
- zastrzeżenie dotyczące konieczności dostosowania dokumentów do konkretnego pracodawcy.

README ma być czytelne dla osoby nietechnicznej.

Dodaj odnośniki do najważniejszych dokumentów.

## 20. Bezpieczeństwo danych

Sprawdź repozytorium pod kątem danych osobowych i informacji poufnych.

Nie umieszczaj w repozytorium:

- rzeczywistych akt osobowych,
- list płac,
- danych o wynagrodzeniach konkretnych pracowników,
- numerów PESEL,
- adresów zamieszkania,
- danych dotyczących zdrowia,
- dokumentacji sytuacji rodzinnej i socjalnej,
- rzeczywistych wniosków pracowników,
- poufnych dokumentów zakładowych.

Przygotuj lub popraw plik .gitignore.

Uwzględnij w nim odpowiednie wzory nazw plików i katalogów zawierających dokumentację roboczą lub dane osobowe.

Nie usuwaj istniejących reguł .gitignore bez sprawdzenia ich znaczenia.

Jeżeli znajdziesz rzeczywiste dane osobowe, nie kopiuj ich do nowych dokumentów ani raportów. Zgłoś problem i wskaż plik wymagający interwencji.

## 21. Jakość i czytelność dokumentacji

Wszystkie dokumenty powinny być:

- napisane poprawną polszczyzną,
- zrozumiałe dla nowego pracownika,
- praktyczne,
- uporządkowane,
- pozbawione zbędnego języka technicznego,
- pozbawione niepotrzebnych powtórzeń,
- zgodne z terminologią prawa pracy.

Nie twórz dokumentów składających się wyłącznie z ogólnych zdań typu „należy przestrzegać przepisów”.

Zamiast tego wyjaśnij:

- co należy zrobić,
- kiedy należy to zrobić,
- kto odpowiada za wykonanie,
- jakie dokumenty są potrzebne,
- gdzie znaleźć wzór,
- jak sprawdzić poprawność.

## 22. Kontrola jakości po zakończeniu pracy

Po opracowaniu dokumentacji:

1. Sprawdź kompletność katalogów.
2. Sprawdź, czy nie pozostały puste pliki.
3. Sprawdź, czy wszystkie odnośniki Markdown działają.
4. Sprawdź, czy README prowadzi do najważniejszych dokumentów.
5. Sprawdź, czy nie powstały duplikaty.
6. Sprawdź, czy wszystkie wzory mają instrukcję użycia.
7. Sprawdź, czy dokumenty prawne mają źródła.
8. Sprawdź, czy nie ma niepotwierdzonych informacji o ZGK.
9. Sprawdź, czy nie ma danych osobowych.
10. Sprawdź, czy pliki DOCX i XLSX otwierają się poprawnie.
11. Sprawdź poprawność formuł w arkuszach.
12. Sprawdź polskie znaki w dokumentach.
13. Sprawdź spójność nazw plików.
14. Sprawdź, czy dokumentacja jest przyjazna dla osoby nietechnicznej.

Jeżeli repozytorium zawiera testy lub walidatory, uruchom je.

Jeżeli nie ma testów, przygotuj prosty skrypt kontrolujący:

- istnienie wymaganych plików,
- poprawność lokalnych odnośników Markdown,
- obecność metryk dokumentów,
- wykrywanie pustych plików,
- podstawowe błędy struktury.

Nie dodawaj zbędnych zależności programistycznych, jeśli wystarczy prosty skrypt.

## 23. Raport końcowy

Po zakończeniu pracy przygotuj raport zawierający:

### A. Wykonane zmiany

Lista najważniejszych utworzonych i zmodyfikowanych dokumentów.

### B. Nowa struktura

Opis docelowej struktury repozytorium.

### C. Dokumenty wymagające zatwierdzenia

Lista dokumentów, które wymagają weryfikacji przez:

- kierownictwo ZGK,
- kadry,
- księgowość,
- BHP,
- inspektora ochrony danych,
- obsługę prawną.

### D. Informacje wymagające uzupełnienia

Lista danych organizacyjnych, których nie udało się potwierdzić.

### E. Kontrola jakości

Wyniki sprawdzenia:

- odnośników,
- plików DOCX,
- plików XLSX,
- poprawności struktury,
- bezpieczeństwa danych.

### F. Rekomendacje dalszego rozwoju

Wskaż kolejne usprawnienia, które mogą zwiększyć praktyczną wartość projektu.

## 24. Oczekiwany rezultat

Po zakończeniu zadania repozytorium MegaKadry ma być:

- kompletnym przewodnikiem po najważniejszych procesach kadrowych,
- praktycznym narzędziem wdrożenia nowego pracownika,
- uporządkowanym zbiorem instrukcji i wzorów,
- dostosowanym do specyfiki zakładu gospodarki komunalnej,
- możliwym do dalszej aktualizacji,
- bezpiecznym pod względem danych osobowych,
- przyjaznym dla osoby nietechnicznej.

Najważniejsza zasada:

**Nie twórz dokumentacji dla samej dokumentacji. Każdy plik ma rozwiązywać konkretny problem pracownika kadr i pomagać mu wykonać rzeczywiste zadanie.**

Wykonaj zadanie kompleksowo, zachowując istniejące wartościowe opracowania i rozwijając repozytorium do postaci praktycznego systemu pracy kadrowej.