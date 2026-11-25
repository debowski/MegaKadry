# Wzory dokumentów do wydruku i edycji

Katalog zawiera gotowe pliki w trzech formatach. Wszystkie są **wzorami roboczymi** — przed użyciem uzupełnij pola w nawiasach kwadratowych i usuń oznaczenie statusu z nagłówka.

Status: **ROBOCZY / DO WERYFIKACJI PRZEZ PRACODAWCĘ** · Data weryfikacji: **2026-11-25**

---

## Jak wybrać format

| Format | Kiedy użyć | Uwaga |
| --- | --- | --- |
| `DOCX/` | Wniosek, oświadczenie, skierowanie, protokół, checklista do wydruku | Otwórz w Wordzie, uzupełnij pola `[ ]`, wydrukuj |
| `XLSX/` | Rejestr, ewidencja, kalkulator, kalendarz terminów | Otwórz w Excelu; przed użyciem formuł przeczytaj arkusz „Instrukcja" |
| `PDF/` | Podgląd, wydruk, materiał szkoleniowy | Nie edytuj — to wersja do wyświetlania i druku |

---

## Pliki

### DOCX

| Plik | Zastosowanie |
| --- | --- |
| `Wniosek_o_urlop.docx` | Wniosek o urlop wypoczynkowy, na żądanie, opiekuńczy lub z powodu siły wyższej |
| `Oswiadczenie_zapoznania_z_regulaminem.docx` | Potwierdzenie zapoznania z regulaminami, ryzykiem i polityką RODO |
| `Skierowanie_na_badania_lekarskie.docx` | Skierowanie na badania wstępne, okresowe lub kontrolne (2 egzemplarze) |
| `Karta_szkolenia_wstepnego_BHP.docx` | Instruktaż ogólny i stanowiskowy |
| `Protokol_kontroli_trzezwosci.docx` | Protokół badania z części E akt osobowych |
| `Checklista_onboardingu.docx` | checklista wdrożenia nowego pracownika do wydruku |
| `Wniosek_o_swiadczenie_ZFSS.docx` | Wniosek o świadczenie z zakładowego funduszu świadczeń socjalnych |

### XLSX

| Plik | Zastosowanie |
| --- | --- |
| `Rejestr_uprawnien_i_badan.xlsx` | Terminy badań, szkoleń BHP, UDT, SEP, prawa jazdy i kodów 95 |
| `Ewidencja_czasu_pracy.xlsx` | Miesięczna ewidencja z formułami czasu pracy i nadgodzin |
| `Kalkulator_swiadczen.xlsx` | Dodatek stażowy, trzynastka, nagroda jubileuszowa i odprawa |
| `Kalendarz_terminow.xlsx` | Obowiązki miesięczne i roczne ze statusem wykonania |
| `Checklista_kompletnosci_akt.xlsx` | Kontrola kompletności akt osobowych A–E |

### PDF

| Plik | Zastosowanie |
| --- | --- |
| `Instrukcja_uzytkowania_wzorow.pdf` | Jak wypełniać i sprawdzać wzory |
| `Podglad_checklisty_onboardingu.pdf` | Wersja do wydruku |
| `Material_szkoleniowy_kadry.pdf` | Szkolenie wstępne dla nowego pracownika kadr |

---

## Regeneracja wzorów

Pliki zostały wygenerowane skryptem [`generuj_wzory.py`](generuj_wzory.py). Jeśli zmienisz treść wzoru w skrypcie, uruchom:

```powershell
python 12_Wzory_Dokumentow/generuj_wzory.py
```

Wymagane pakiety: `python-docx`, `openpyxl`, `reportlab`. Skrypt sprawdza formuły w kalkulatorze i ewidencji na przykładowych danych (12 lat stażu → 12%; 60 000 zł → 5 100 zł trzynastki; 08:00–17:00 z 30-min przerwą → 8,50 h).

---

## Bezpieczeństwo danych

We wzorach nie ma rzeczywistych danych pracowników — są tylko pola w nawiasach i fikcyjne przykłady. Nie wpisuj tu PESEL-i, adresów, danych o zdrowiu ani wynagrodzeń konkretnych osób. Zasady wykluczania takich plików z repozytorium opisuje [`../.gitignore`](../.gitignore).

Podstawa prawna użytych wzorów i terminy są podane w dokumentach źródłowych w folderach `01`–`11`, w szczególności w [`../11_Aktualizacje_i_Zrodla/Wykaz_zrodel_urzedowych.md`](../11_Aktualizacje_i_Zrodla/Wykaz_zrodel_urzedowych.md).
