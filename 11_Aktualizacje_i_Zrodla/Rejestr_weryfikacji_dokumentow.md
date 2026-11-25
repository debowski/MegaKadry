# Rejestr weryfikacji dokumentów

*Dokument ROBOCZY. Rejestr ewidencjonuje metrykę i status każdego opracowania w repozytorium.*

---

## 1. Cel

Rejestr odpowiada na pytania: kto opracował dany plik, kiedy był ostatnio sprawdzany, na jakiej podstawie prawnej i czy został zatwierdzony. Dzięki temu nowy pracownik kadr nie stosuje dokumentu sprzed zmiany przepisów w przekonaniu, że jest on aktualny.

## 2. Zakres

Rejestr obejmuje wszystkie pliki Markdown w repozytorium, które są instrukcjami, procedurami, checklistami, rejestrami albo wzorami. Wzory DOCX/XLSX/PDF również powinny mieć wpis po ich opracowaniu.

## 3. Statusy dokumentów

| Status | Znaczenie | Kto może nadać |
| --- | --- | --- |
| **ROBOCZY** | Dokument nadaje się do użytku wewnętrznego, ale nie jest zatwierdzony przez pracodawcę. | Opracujący (specjalista ds. kadr). |
| **DO WERYFIKACJI** | Treść wymaga sprawdzenia w źródle urzędowym albo uzupełnienia danymi ZGKiM. Nie należy jej stosować bez weryfikacji. | Opracujący; wpisuje powód w uwagach. |
| **ZATWIERDZONY** | Dokument zatwierdzony przez Dyrektora Zakładu. | **Wyłącznie Dyrektor** — na podstawie pisemnego potwierdzenia. |
| **ARCHIWALNY** | Dokument wycofany z użytku, zachowany jako historia zmian. | Specjalista ds. kadr po decyzji Dyrektora. |

> **Zasada bezwzględna:** żadnego dokumentu w tym repozytorium nie wolno oznaczyć jako **ZATWIERDZONY** ani „zatwierdzony przez ZGK", jeżeli nie ma potwierdzenia zatwierdzenia od pracodawcy. Wszystkie obecne opracowania są **ROBOCZE** albo **DO WERYFIKACJI**.

## 4. Wzór metryki pojedynczego dokumentu

```
Nazwa dokumentu:      [tytuł pliku]
Wersja:               1.0
Data opracowania:     RRRR-MM-DD
Data ostatniej weryfikacji: RRRR-MM-DD
Rola odpowiedzialna:  specjalista ds. kadr / księgowość / BHP / obsługa prawna
Status:               ROBOCZY | DO WERYFIKACJI | ZATWIERDZONY | ARCHIWALNY
Podstawa prawna:      [pełna nazwa aktu, art./§, link do źródła oficjalnego]
Historia zmian:       RRRR-MM-DD, wersja X.Y — [opis]
Uwagi:                [co wymaga uzupełnienia przez pracodawcę]
```

## 5. Rejestr dokumentów

| Nazwa dokumentu | Wersja | Data opracowania | Data ostatniej weryfikacji | Rola odpowiedzialna | Status | Podstawa prawna | Historia zmian |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10_Kontrole_i_Audyt/Instrukcja_kontroli_wewnetrznej.md` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | ROBOCZY | Kodeks pracy art. 94 pkt 9a–9b, 94⁶, 22¹c § 6–9; rozporządzenie MRPiPS z 10.12.2018 r. (tekst jedn. Dz.U. 2026 poz. 474) | 2026-11-25 — opracowanie |
| `10_Kontrole_i_Audyt/Checklista_kontroli_akt_osobowych.md` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | ROBOCZY | § 3, § 4 rozporządzenia MRPiPS z 10.12.2018 r.; art. 113 i 22¹c § 6–9 KP | 2026-11-25 — opracowanie |
| `10_Kontrole_i_Audyt/Checklista_kontroli_czasu_pracy_i_urlopow.md` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | ROBOCZY | art. 149, 151–151⁴, 168, 171 KP; § 6 rozporządzenia MRPiPS z 10.12.2018 r. | 2026-11-25 — opracowanie |
| `10_Kontrole_i_Audyt/Lista_najczestszych_bledow_kadrowych.md` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | DO WERYFIKACJI | akty wymienione w poszczególnych wierszach tabeli (każdy z własnym linkiem) | 2026-11-25 — opracowanie; część wpisów wymaga potwierdzenia zakresu obowiązków ZGKiM |
| `11_Aktualizacje_i_Zrodla/Wykaz_zrodel_urzedowych.md` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | ROBOCZY | ustawa o pracownikach samorządowych art. 13 ust. 1; ustawa o ochronie sygnalistów; RODO | 2026-11-25 — opracowanie |
| `11_Aktualizacje_i_Zrodla/Rejestr_zmian_prawnych.md` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | ROBOCZY | Dz.U. 2023 poz. 471; 2025 poz. 335; 2026 poz. 474; 2024 poz. 928 | 2026-11-25 — opracowanie |
| `11_Aktualizacje_i_Zrodla/Rejestr_weryfikacji_dokumentow.md` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | ROBOCZY | — (rejestr metryk, nie przepis) | 2026-11-25 — opracowanie |
| `11_Aktualizacje_i_Zrodla/Instrukcja_aktualizacji_i_zglaszania_bledow.md` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | ROBOCZY | ustawa o ogłaszaniu aktów normatywnych art. 16 | 2026-11-25 — opracowanie |
| `11_Aktualizacje_i_Zrodla/skrypt_kontroli.py` | 1.0 | 2026-11-25 | 2026-11-25 | specjalista ds. kadr | ROBOCZY | — (narzędzie techniczne, nie przepis) | 2026-11-25 — opracowanie |

**Pozostałe dokumenty repozytorium** (foldery `01_`–`07_`): ich metrykę i status należy uzupełnić w miarę weryfikacji. Do czasu wpisu traktuj je jako **ROBOCZE / DO WERYFIKACJI** — nigdy jako zatwierdzone przez ZGKiM.

## 6. Tryb aktualizacji wpisu

1. Otwórz plik, który chcesz zweryfikować.
2. Sprawdź przepisy w źródłach z [Wykazu źródeł urzędowych](Wykaz_zrodel_urzedowych.md).
3. Jeśli zmienił się przepis — wykonaj czynności z [Instrukcji aktualizacji i zgłaszania błędów](Instrukcja_aktualizacji_i_zglaszania_bledow.md).
4. Zwiększ wersję: `1.0 → 1.1` przy drobnej poprawce, `1.x → 2.0` przy zmianie merytorycznej.
5. Wpisz datę weryfikacji i krótki opis w historii zmian.
6. Zmień status wyłącznie na podstawie decyzji Dyrektora (dla ZATWIERDZONY) albo decyzji o wycofaniu (dla ARCHIWALNY).

## 7. Kontrola poprawności

- Czy każdy plik w repozytorium ma wpis albo jest wyraźnie objęty adnotacją zbiorczą?
- Czy żaden wpis nie ma statusu ZATWIERDZONY bez potwierdzenia Dyrektora?
- Czy data ostatniej weryfikacji nie jest starsza niż data wejścia w życie ostatniej zmiany przepisu?
- Czy podstawa prawna zawiera pełną nazwę aktu i link?
- Czy historia zmian opisuje co się zmieniło, a nie tylko datę?

## 8. Podstawa prawna i metryka

| Pełna nazwa aktu prawnego | Przepis | Źródło oficjalne | Status |
| --- | --- | --- | --- |
| Ustawa z dnia 20 lipca 2000 r. o ogłaszaniu aktów normatywnych i niektórych innych aktów prawnych | art. 16 | [ELI — Dz.U. 2019 poz. 1461](https://eli.gov.pl/eli/DU/2019/1461/ogl) | DO WERYFIKACJI |

**Data weryfikacji: 2026-11-25.** Status dokumentu: ROBOCZY.

## 9. Historia zmian

| Data | Wersja | Opis zmiany |
| --- | --- | --- |
| 2026-11-25 | 1.0 | Utworzenie rejestru; wpisanie metryk dokumentów folderów `10_` i `11_`; zawarcie zasady o zakazie oznaczania dokumentów jako ZATWIERDZONE bez potwierdzenia pracodawcy. |
