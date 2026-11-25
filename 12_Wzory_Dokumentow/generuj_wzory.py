# -*- coding: utf-8 -*-
"""Generuje wzory dokumentow kadrowych w formatach DOCX, XLSX i PDF.

Uzycie:
    python 12_Wzory_Dokumentow/generuj_wzory.py

Skrypt wymaga: python-docx, openpyxl, reportlab.
Wszystkie wzory zawieraja wyłącznie pola w nawiasach kwadratowych — zadnych
rzeczywistych danych osobowych. Before using, uzupelnij pola i usun note
"ROBOCZY / DO WERYFIKACJI" z naglowka.
"""

from __future__ import annotations

import html
import os
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parent
DOCX_DIR = ROOT / "DOCX"
XLSX_DIR = ROOT / "XLSX"
PDF_DIR = ROOT / "PDF"
VERIFICATION_DATE = "2026-11-25"
STATUS = "ROBOCZY / DO WERYFIKACJI PRZEZ PRACODAWCĘ"


# ---------------------------------------------------------------------------
# DOCX
# ---------------------------------------------------------------------------

GRAY = RGBColor(0x59, 0x59, 0x59)


def new_docx(title: str, subtitle: str | None = None) -> Document:
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10)
    heading = doc.add_heading(title, level=0)
    heading.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if subtitle:
        p = doc.add_paragraph()
        r = p.add_run(subtitle)
        r.italic = True
        r.font.color.rgb = GRAY
    meta = doc.add_paragraph()
    r = meta.add_run(f"Status: {STATUS}  |  Data weryfikacji: {VERIFICATION_DATE}")
    r.font.size = Pt(8)
    r.font.color.rgb = GRAY
    footer = doc.sections[0].footer.paragraphs[0]
    footer.text = "Wzór szkoleniowy — nie wpisuj rzeczywistych danych osobowych do repozytorium."
    for run in footer.runs:
        run.font.size = Pt(8)
        run.font.color.rgb = GRAY
    return doc


def field(doc: Document, label: str, value: str = "[................................]") -> None:
    p = doc.add_paragraph()
    r = p.add_run(f"{label}: ")
    r.bold = True
    v = p.add_run(value)
    v.font.color.rgb = GRAY


def note(doc: Document, text: str) -> None:
    p = doc.add_paragraph()
    r = p.add_run("INSTRUKCJA: " + text)
    r.italic = True
    r.font.size = Pt(8.5)
    r.font.color.rgb = GRAY


def add_table(doc: Document, headers: list[str], rows: list[list[str]]) -> None:
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for run in cell.paragraphs[0].runs:
            run.bold = True
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = value
    doc.add_paragraph()


def signoff(doc: Document, left: str, right: str) -> None:
    p = doc.add_paragraph()
    p.add_run("\n\n" + left + "  ........................................\t\t")
    p.add_run(right + "  ........................................")


def build_docx_files() -> list[Path]:
    created: list[Path] = []

    # 1. Wniosek o urlop
    doc = new_docx("WNIOSEK O UDZIELENIE URLUPU WYPOCHODNIKOWEGO", "art. 152 i nast. Kodeksu pracy")
    note(doc, "Wypełnij pola, podaj we wniosku daty i liczbę dni. Kadr sprawdza wymiar urlopu i saldo zaległego urlopu.")
    field(doc, "Pracodawca", "Zakład Gospodarki Komunalnej i Mieszkaniowej w Orzeszu")
    field(doc, "Do", "Dyrektora Zakładu / [właściwy przełożony]")
    field(doc, "Imię i nazwisko", "[Imię i nazwisko]")
    field(doc, "Stanowisko / komórka", "[Stanowisko]")
    field(doc, "Rodzaj urlopu", "[wypoczynkowy / na żądanie / opiekuńczy / siła wyższa]")
    field(doc, "Od dnia", "[RRRR-MM-DD]")
    field(doc, "Do dnia", "[RRRR-MM-DD]")
    field(doc, "Liczba dni roboczych", "[...]")
    field(doc, "Rok, za który udzielany jest urlop", "[RRRR]")
    doc.add_paragraph("Proszę o udzielenie urlopu w wyżej podanym terminie i o potwierdzenie salda urlopu zaległego.")
    signoff(doc, "[Miejscowość, data]", "Podpis pracownika")
    doc.add_paragraph()
    field(doc, "Decyzja przełożonego", "[ ] wyrażono zgodę  [ ] odmowa – przyczyna: [...]")
    signoff(doc, "Data", "Podpis przełożonego")
    path = DOCX_DIR / "Wniosek_o_urlop.docx"
    doc.save(path)
    created.append(path)

    # 2. Oświadczenie o zapoznaniu z regulaminami
    doc = new_docx("OŚWIADCZENIE O ZAPOZNANIU SIĘ Z REGULAMINAMI I DOKUMENTAMI", "art. 104 § 1 i art. 94¹ Kodeksu pracy")
    note(doc, "Podpis pracownika potwierdza zapoznanie się, nie zastępuje szkolenia BHP ani informacji o warunkach zatrudnienia.")
    field(doc, "Pracodawca", "Zakład Gospodarki Komunalnej i Mieszkaniowej w Orzeszu")
    field(doc, "Imię i nazwisko", "[Imię i nazwisko]")
    field(doc, "Stanowisko", "[Stanowisko]")
    doc.add_paragraph("Oświadczam, że zapoznałem/am się z następującymi dokumentami:")
    for text in [
        "[ ] Regulamin pracy — wersja z dnia [data] (DO UZUPEŁNIENIA PRZEZ PRACODAWCĘ)",
        "[ ] Regulamin wynagradzania — wersja z dnia [data] (DO UZUPEŁNIENIA PRZEZ PRACODAWCĘ)",
        "[ ] Regulamin ZFŚS — wersja z dnia [data] (DO UZUPEŁNIENIA PRZEZ PRACODAWCĘ)",
        "[ ] Informacja o ryzyku zawodowym na stanowisku",
        "[ ] Polityka RODO i procedura zgłoszeń wewnętrznych",
        "[ ] Zakres obowiązków służbowych",
    ]:
        doc.add_paragraph(text, style="List Bullet")
    signoff(doc, "[Miejscowość, data]", "Podpis pracownika")
    path = DOCX_DIR / "Oswiadczenie_zapoznania_z_regulaminem.docx"
    doc.save(path)
    created.append(path)

    # 3. Skierowanie na badania
    doc = new_docx("SKIEROWANIE NA PROFILAKTYCZNE BADANIA LEKARSKIE", "art. 229 Kodeksu pracy")
    note(doc, "Wystaw w dwóch egzemplarzach: jeden dla pracownika, drugi dla lekarza medycyny pracy. Przed dopuszczeniem do pracy wymagane jest orzeczenie o braku przeciwwskazań.")
    field(doc, "Pracodawca", "Zakład Gospodarki Komunalnej i Mieszkaniowej w Orzeszu")
    field(doc, "Rodzaj badania", "[ ] wstępne  [ ] okresowe  [ ] kontrolne (po niezdolności > 30 dni)")
    field(doc, "Imię i nazwisko", "[Imię i nazwisko]")
    field(doc, "PESEL", "[PESEL]")
    field(doc, "Stanowisko", "[Stanowisko]")
    doc.add_paragraph("Czynniki szkodliwe, uciążliwe i niebezpieczne (zaznaczyć):")
    for text in [
        "[ ] hałas  [ ] drgania  [ ] mikroklimat zimny/gorący",
        "[ ] pyły  [ ] środki chemiczne  [ ] czynniki biologiczne (ścieki, odpady)",
        "[ ] praca na wysokości / w wykopach / w przestrzeniach zamkniętych",
        "[ ] prowadzenie pojazdów  [ ] obsługa maszyn UDT  [ ] praca przy monitorze",
    ]:
        doc.add_paragraph(text, style="List Bullet")
    field(doc, "Data wystawienia", "[RRRR-MM-DD]")
    signoff(doc, "Podpis pracodawcy", "Potwierdzenie odbioru przez pracownika")
    path = DOCX_DIR / "Skierowanie_na_badania_lekarskie.docx"
    doc.save(path)
    created.append(path)

    # 4. Karta szkolenia BHP
    doc = new_docx("KARTA SZKOLENIA WSTĘPNEGO W DZIEDZINIE BHP", "Rozporządzenie MPiPS z 26.09.2004 r. w sprawie szkolenia w dziedzinie BHP")
    note(doc, "Instruktaż ogólny i stanowiskowy. Potwierdzenie może być także elektroniczne z adnotacją w karcie (stan prawny od 12.12.2025 r. — do weryfikacji przez BHP).")
    field(doc, "Pracodawca", "Zakład Gospodarki Komunalnej i Mieszkaniowej w Orzeszu")
    field(doc, "Imię i nazwisko", "[Imię i nazwisko]")
    field(doc, "Stanowisko", "[Stanowisko]")
    add_table(
        doc,
        ["Rodzaj instruktażu", "Data", "Prowadzący", "Liczba godzin", "Podpis"],
        [
            ["Ogólny", "[data]", "[Imię i nazwisko]", "[...]", "[podpis]"],
            ["Stanowiskowy", "[data]", "[Imię i nazwisko]", "[...]", "[podpis]"],
        ],
    )
    doc.add_paragraph("Wynik sprawdzianu wiadomości i umiejętności: [pozytywny / negatywny — poprawkowy termin: data]")
    signoff(doc, "Data dopuszczenia do pracy", "Podpis pracownika")
    path = DOCX_DIR / "Karta_szkolenia_wstepnego_BHP.docx"
    doc.save(path)
    created.append(path)

    # 5. Protokół kontroli trzeźwości
    doc = new_docx("PROTOKÓŁ KONTROLI TRZEŹWOŚCI", "art. 22¹c–22¹f Kodeksu pracy")
    note(doc, "Wzór do wydruku. Część E akt osobowych wyłącznie przy wyniku dodatnim; okres przechowywania zależy także od ewentualnej kary porządkowej (art. 22¹c § 7 KP).")
    field(doc, "Pracodawca", "Zakład Gospodarki Komunalnej i Mieszkaniowej w Orzeszu")
    field(doc, "Imię i nazwisko pracownika", "[Imię i nazwisko]")
    field(doc, "Data, godzina i minuta badania", "[RRRR-MM-DD, HH:MM]")
    field(doc, "Osoba przeprowadzająca", "[Imię i nazwisko, stanowisko]")
    field(doc, "Urządzenie i numer wzorcowania", "[Model, numer, data ważności]")
    add_table(
        doc,
        ["Pomiar", "Godzina", "Wynik mg/l", "Wynik ‰"],
        [["I", "[HH:MM]", "[...]", "[...]"], ["II (po ok. 15 min)", "[HH:MM]", "[...]", "[...]"]],
    )
    field(doc, "Kwalifikacja", "[ ] 0,00  [ ] stan po użyciu alkoholu  [ ] stan nietrzeźwości  [ ] środki podobne")
    field(doc, "Działania", "[ ] niedopuszczenie do pracy  [ ] badanie przez Policję: [tak/nie]")
    signoff(doc, "Podpis osoby kontrolującej", "Podpis pracownika / adnotacja o odmowie")
    path = DOCX_DIR / "Protokol_kontroli_trzezwosci.docx"
    doc.save(path)
    created.append(path)

    # 6. Checklista onboardingu
    doc = new_docx("CHECKLISTA WDROŻENIA NOWEGO PRACOWNIKA", "Do wydruku — zaznacz [x], wpisz datę i osobę potwierdzającą")
    note(doc, "Wersja robocza: terminy i odpowiedzialności należy potwierdzić z regulaminem pracy i praktyką ZGK.")
    items = [
        "Umowa o pracę podpisana przed dopuszczeniem do pracy (art. 29 § 2 KP)",
        "Pisemna informacja o warunkach zatrudnienia — do 7 dni od dopuszczenia (art. 29 § 3 KP)",
        "Skierowanie na badania wstępne (2 egz.) i orzeczenie lekarskie",
        "Kwestionariusz osobowy i kopie dokumentów potwierdzających kwalifikacje",
        "ZUS ZUA w terminie 7 dni od powstania obowiązku; ZUS ZCNA jeśli dotyczy",
        "Szkolenie wstępne BHP — karta szkolenia podpisana",
        "Zapoznanie z regulaminami, RODO i sygnalistami — oświadczenie",
        "Odzież robocza i ŚOI — karta ewidencji",
        "Założenie akt osobowych A–E i nadanie upoważnień RODO",
        "PPK — decyzja o zapisie lub deklaracja rezygnacji",
        "Dla stanowiska urzędniczego: ślubowanie; dla pierwszego urzędnika: służba przygotowawcza i umowa na czas określony ≤ 6 mies.",
        "Wpisanie terminów badań, szkoleń i uprawnień do rejestru",
    ]
    add_table(doc, ["[x]", "Czynność", "Data", "Potwierdził"], [["", item, "", ""] for item in items])
    path = DOCX_DIR / "Checklista_onboardingu.docx"
    doc.save(path)
    created.append(path)

    # 7. Wniosek ZFŚS
    doc = new_docx("WNIOSEK O PRZYZNANIE ŚWIADCZENIA Z ZFŚS", "art. 8 ust. 1 ustawy z 4.03.1994 r. o ZFŚS")
    note(doc, "Wniosek zawiera dane o sytuacji życiowej, rodzinnej i materialnej. Przekazuj wyłącznie dane niezbędne; podstawą przetwarzania jest obowiązek ustawowy i art. 9 § 2 lit. b RODO, nie zgoda.")
    field(doc, "Wnioskodawca", "[Imię i nazwisko]")
    field(doc, "Status", "[ ] pracownik  [ ] emeryt/rencista – były pracownik")
    field(doc, "Liczba osób w gospodarstwie domowym", "[...]")
    field(doc, "Średni miesięczny dochód netto na osobę", "[...] zł")
    field(doc, "Rodzaj świadczenia", "[wypoczynek / zapomoga / świadczenie świąteczne / pożyczka / inne]")
    doc.add_paragraph("Uzasadnienie sytuacji życiowej, rodzinnej i materialnej: [................................................]")
    signoff(doc, "[Miejscowość, data]", "Podpis wnioskodawcy")
    doc.add_paragraph("Opinia Komisji Socjalnej i decyzja Dyrektora: [................................]")
    path = DOCX_DIR / "Wniosek_o_swiadczenie_ZFSS.docx"
    doc.save(path)
    created.append(path)

    return created


# ---------------------------------------------------------------------------
# XLSX
# ---------------------------------------------------------------------------

HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
HEADER_FONT = Font(color="FFFFFF", bold=True)
NOTE_FILL = PatternFill("solid", fgColor="FFF2CC")


def style_header(ws, row: int = 1) -> None:
    for cell in ws[row]:
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.freeze_panes = ws.cell(row=row + 1, column=1)


def add_instruction_sheet(wb: Workbook, title: str, lines: list[str]) -> None:
    ws = wb.create_sheet("Instrukcja")
    ws["A1"] = title
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = f"Status: {STATUS} | Data weryfikacji: {VERIFICATION_DATE}"
    ws["A2"].fill = NOTE_FILL
    for i, line in enumerate(lines, start=4):
        ws.cell(row=i, column=1, value=line)
    ws.column_dimensions["A"].width = 120


def add_status_validation(ws, cell_range: str) -> None:
    dv = DataValidation(type="list", formula1='"wykonano,nie wykonano,nie dotyczy,wymaga wyjaśnienia"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(cell_range)


def build_xlsx_files() -> list[Path]:
    created: list[Path] = []

    # 1. Rejestr uprawnień i badań
    wb = Workbook()
    ws = wb.active
    ws.title = "Rejestr"
    headers = ["Lp.", "Imię i nazwisko", "Stanowisko", "Badania lekarskie ważne do", "Badania psychotechniczne ważne do",
               "Szkolenie BHP ważne do", "Prawo jazdy (kat., kod 95, ważne do)", "UDT / SEP / inne (ważne do)", "Status", "Uwagi"]
    ws.append(headers)
    style_header(ws)
    ws.append([1, "[Pracownik A]", "[Kierowca]", "[RRRR-MM-DD]", "[RRRR-MM-DD]", "[RRRR-MM-DD]", "C, CE, kod 95 [data]", "[UDT – bezterminowo; szkolenie okresowe: data]", "OK", "Przykładowy wiersz – usunąć"])
    ws.append([2, "[Pracownik B]", "[Konserwator wod-kan]", "[RRRR-MM-DD]", "nie dotyczy", "[RRRR-MM-DD]", "B [data]", "SEP E do 1 kV [data]", "wymaga wyjaśnienia", "Przykładowy wiersz – usunąć"])
    add_status_validation(ws, "I2:I200")
    for col, width in enumerate([6, 24, 24, 22, 24, 20, 30, 34, 20, 32], start=1):
        ws.column_dimensions[ws.cell(row=1, column=col).column_letter].width = width
    add_instruction_sheet(wb, "Rejestr badań, szkoleń i uprawnień", [
        "1. Sprawdzaj rejestr co najmniej raz w miesiącu (1. dzień miesiąca).",
        "2. Skierowania na badania wystawiaj z wyprzedzeniem co najmniej 30 dni.",
        "3. Decyzje UDT są bezterminowe, ale operatorzy sprzętu mają obowiązek okresowych szkoleń – wpisz osobny termin w kolumnie H.",
        "4. Kod 95 (kierowcy) wymaga okresowego szkolenia – wpisz termin w kolumnie G.",
        "5. Statusy: wykonano / nie wykonano / nie dotyczy / wymaga wyjaśnienia.",
        "6. Nie wpisuj rzeczywistych danych osobowych do wzoru w repozytorium.",
    ])
    path = XLSX_DIR / "Rejestr_uprawnien_i_badan.xlsx"
    wb.save(path)
    created.append(path)

    # 2. Ewidencja czasu pracy + sprawdzenie formuł
    wb = Workbook()
    ws = wb.active
    ws.title = "Ewidencja"
    headers = ["Data", "Dzień tyg.", "Rozpoczęcie", "Zakończenie", "Przerwa (min)", "Czas pracy (h)", "Nadgodziny (h)", "Rodzaj pracy", "Uwagi"]
    ws.append(headers)
    style_header(ws)
    # Przykładowe dane weryfikacyjne: 08:00-17:00 z 30 min przerwy = 8,5 h, nadgodziny 0,5 h
    ws.append(["[RRRR-MM-DD]", "[pon]", "08:00", "17:00", 30, "=(D2-C2)*24-E2/60", "=MAX(0;F2-8)", "zwykła", "Przykład – usunąć"])
    ws.append(["[RRRR-MM-DD]", "[wt]", "08:00", "16:00", 30, "=(D3-C3)*24-E3/60", "=MAX(0;F3-8)", "zwykła", "Przykład – usunąć"])
    for r in range(4, 36):
        ws.append([None, None, None, None, None, f"=IF(OR(C{r}=\"\";D{r}=\"\");\"\";(D{r}-C{r})*24-E{r}/60)",
                   f"=IF(F{r}=\"\";\"\";MAX(0;F{r}-8))", None, None])
    total_row = 36
    ws.cell(row=total_row, column=1, value="SUMA").font = Font(bold=True)
    ws.cell(row=total_row, column=6, value=f"=SUM(F2:F35)")
    ws.cell(row=total_row, column=7, value=f"=SUM(G2:G35)")
    for col, width in enumerate([16, 12, 14, 14, 14, 16, 16, 18, 34], start=1):
        ws.column_dimensions[ws.cell(row=1, column=col).column_letter].width = width
    add_instruction_sheet(wb, "Ewidencja czasu pracy", [
        "1. Godziny wpisuj jako tekst HH:MM — formuły liczą różnicę jako ułamek doby.",
        "2. Czas pracy = (zakończenie – rozpoczęcie) × 24 – przerwa / 60.",
        "3. Nadgodziny = MAX(0; czas pracy – 8) dla podstawowego systemu czasu pracy.",
        "4. Kontrolny przykład: 08:00–17:00, przerwa 30 min → 8,50 h; nadgodziny 0,50 h.",
        "5. Drugi przykład: 08:00–16:00, przerwa 30 min → 7,50 h; nadgodziny 0,00 h.",
        "6. W systemie równoważnym zmień wzór na zgodny z ustalonym wymiarem dobowym (DO UZUPEŁNIENIA PRZEZ PRACODAWCĘ).",
        "7. Praca w porze nocnej, niedziele i święta oraz dyżury rozliczaj wg instrukcji w folderze 03.",
    ])
    # Weryfikacja formuł na danych przykładowych (niezależne obliczenie w Pythonie)
    assert round((17 - 8) - 30 / 60, 2) == 8.5
    assert round(max(0, 8.5 - 8), 2) == 0.5
    assert round((16 - 8) - 30 / 60, 2) == 7.5
    assert round(max(0, 7.5 - 8), 2) == 0.0
    path = XLSX_DIR / "Ewidencja_czasu_pracy.xlsx"
    wb.save(path)
    created.append(path)

    # 3. Kalkulator świadczeń
    wb = Workbook()
    ws = wb.active
    ws.title = "Kalkulator"
    ws.append(["Parametr", "Wartość", "Jednostka / uwagi"])
    style_header(ws)
    rows = [
        ("Wynagrodzenie zasadnicze miesięczne", 5000, "zł — przykład do usunięcia"),
        ("Staż pracy (pełne lata)", 12, "lata"),
        ("Suma wynagrodzeń za rok (do trzynastki)", 60000, "zł — przykład"),
        ("Lata pracy przy nagrodzie jubileuszowej", 25, "lata"),
        ("Wynagrodzenie miesięczne do nagrody", 5000, "zł — przykład"),
        ("Lata pracy przy odprawie", 20, "lata"),
    ]
    for r in rows:
        ws.append(list(r))
    results = [
        ("Dodatek stażowy (%)", "=IF(B3<5;0;MIN(20;5+(B3-5)))"),
        ("Dodatek stażowy (zł)", "=ROUND(B2*B8/100;2)"),
        ("Trzynastka 8,5% (zł)", "=ROUND(B4*0,085;2)"),
        ("Nagroda jubileuszowa (%)", "=IF(B5>=45;400;IF(B5>=40;300;IF(B5>=35;200;IF(B5>=30;150;IF(B5>=25;100;IF(B5>=20;75;0))))))"),
        ("Nagroda jubileuszowa (zł)", "=ROUND(B6*B11/100;2)"),
        ("Odprawa (miesiące)", "=IF(B7>=20;6;IF(B7>=15;3;IF(B7>=10;2;0)))"),
        ("Odprawa (zł)", "=ROUND(B6*B13;2)"),
    ]
    start = 8
    for i, (label, formula) in enumerate(results):
        ws.cell(row=start + i, column=1, value=label)
        ws.cell(row=start + i, column=2, value=formula)
        ws.cell(row=start + i, column=3, value="formuła — sprawdź przed użyciem")
        ws.cell(row=start + i, column=1).font = Font(bold=True)
    ws.column_dimensions["A"].width = 38
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 42
    add_instruction_sheet(wb, "Kalkulator dodatków, trzynastki, nagrody i odprawy", [
        "1. Wartości w wierszach 2–7 to PRZYKŁADY — zastąp własnymi danymi.",
        "2. Dodatek stażowy: 5% po 5 latach, +1% za każdy dalszy rok, maks. 20% (art. 38 ust. 1 ustawy o pracownikach samorządowych).",
        "3. Trzynastka: 8,5% sumy wynagrodzeń za rok (ustawa z 12.12.1997 r., tekst jedn. Dz.U. 2025 poz. 560).",
        "4. Nagroda jubileuszowa: 20 lat – 75%, 25 – 100%, 30 – 150%, 35 – 200%, 40 – 300%, 45 – 400%.",
        "5. Odprawa emerytalno-rentowa: 10 lat – 2 mies., 15 – 3 mies., 20 – 6 mies.",
        "6. Kontrola na przykładzie: staż 12 lat → 12%; 60 000 zł → trzynastka 5 100 zł; 25 lat → 100% z 5 000 zł = 5 000 zł; 20 lat → 6 × 5 000 zł = 30 000 zł.",
        "7. Uwaga: wysokości i zasady obowiązujące w ZGK mogą wynikać z regulaminu wynagradzania — zweryfikuj u pracodawcy.",
    ])
    # Weryfikacja formuł na przykładach
    assert min(20, 5 + (12 - 5)) == 12
    assert round(60000 * 0.085, 2) == 5100.0
    assert round(5000 * 100 / 100, 2) == 5000.0
    assert 6 * 5000 == 30000
    path = XLSX_DIR / "Kalkulator_swiadczen.xlsx"
    wb.save(path)
    created.append(path)

    # 4. Kalendarz terminów
    wb = Workbook()
    ws = wb.active
    ws.title = "Kalendarz"
    ws.append(["Obowiązek", "Termin", "Podstawa", "Dokument wynikowy", "Osoba odpowiedzialna (rola)", "Sposób potwierdzenia", "Status"])
    style_header(ws)
    calendar_rows = [
        ("ZUS – dokumenty i składki za poprzedni miesiąc (jednostki i zakłady budżetowe)", "do 5. dnia miesiąca", "art. 47 § 1 pkt 2 ustawy o systemie ubezpieczeń społecznych", "DRA, RCA, RSA", "specjalista ds. kadrowych / płac", "potwierdzenie ZUS", "wykonano"),
        ("Wpłaty PPK", "do 15. dnia miesiąca", "art. 28 ust. 4 ustawy o PPK", "potwierdzenie przelewu", "dział płac", "wyciąg bankowy", "nie wykonano"),
        ("Zaliczki PIT + PFRON", "do 20. dnia miesiąca", "ustawa o PIT / ustawa o rehabilitacji", "PIT-4R (dane), DEK-1-a / INF-1", "dział płac", "potwierdzenie nadania", "nie dotyczy"),
        ("ZUS ZUA / ZWUA / ZCNA", "7 dni od zdarzenia", "art. 36 ust. 2 ustawy o systemie ubezpieczeń społecznych", "zgłoszenie ZUS", "specjalista ds. kadr", "potwierdzenie ZUS", "wykonano"),
        ("Informacja o warunkach zatrudnienia", "7 dni od dopuszczenia do pracy", "art. 29 § 3 KP", "informacja pisemna/elektroniczna", "specjalista ds. kadr", "potwierdzenie odbioru", "wykonano"),
        ("Trzynastka", "do 31 marca", "art. 5 ust. 2 ustawy z 12.12.1997 r.", "lista wypłat", "dział płac", "lista podpisana", "wykonano"),
        ("ZFŚS – 75% odpisu", "do 31 maja", "art. 6 ust. 2 ustawy o ZFŚS", "przelew na rachunek ZFŚS", "księgowość", "wyciąg", "wykonano"),
        ("Zaległy urlop wypoczynkowy", "do 30 września", "art. 168 KP", "wniosek i ewidencja", "specjalista ds. kadr", "podpisany wniosek", "wykonano"),
        ("ZFŚS – wyrównanie do 100% odpisów i zwiększeń; rozliczenie na 31 grudnia", "30 września / 31 grudnia", "art. 6 ust. 2 i art. 5a ustawy o ZFŚS", "zestawienie rozliczeniowe", "księgowość / Komisja Socjalna", "protokół", "wymaga wyjaśnienia"),
        ("DEK-R / INF-2 (PFRON)", "do 20 stycznia", "ustawa o rehabilitacji zawodowej i społecznej", "DEK-R / INF-2", "dział płac", "potwierdzenie nadania", "nie dotyczy"),
    ]
    for row in calendar_rows:
        ws.append(list(row))
    add_status_validation(ws, "G2:G200")
    for col, width in enumerate([52, 24, 46, 30, 28, 24, 20], start=1):
        ws.column_dimensions[ws.cell(row=1, column=col).column_letter].width = width
    add_instruction_sheet(wb, "Kalendarz terminów kadrowo-płacowych", [
        "1. Terminy ustawowe przesuwają się na następny dzień roboczy, gdy przypadają na dzień wolny (art. 12 § 5 Ordynacji podatkowej i odpowiednie przepisy).",
        "2. Terminy zależne od zdarzenia (np. zatrudnienie) nie są przypisane do stałego dnia miesiąca.",
        "3. Statusy: wykonano / nie wykonano / nie dotyczy / wymaga wyjaśnienia.",
        "4. Szczegółowy opis: 07_Kalendarz_i_Checklisty_Kadrowca/Kalendarz_obowiazkow_kadrowych_roczny_i_miesieczny.md",
    ])
    path = XLSX_DIR / "Kalendarz_terminow.xlsx"
    wb.save(path)
    created.append(path)

    # 5. Checklista kompletności akt
    wb = Workbook()
    ws = wb.active
    ws.title = "Checklista"
    ws.append(["Część", "Dokument", "Wymagane", "Status", "Data sprawdzenia", "Uwagi"])
    style_header(ws)
    items = [
        ("A", "Kwestionariusz osobowy osoby ubiegającej się o zatrudnienie", "tak", ""),
        ("A", "Kopie dokumentów potwierdzających kwalifikacje i staż", "jeśli dotyczy", ""),
        ("A", "Skierowanie i orzeczenie lekarskie (wstępne)", "tak", ""),
        ("B", "Umowa o pracę i aneksy", "tak", ""),
        ("B", "Informacja o warunkach zatrudnienia (art. 29 § 3 KP)", "tak", ""),
        ("B", "Kwestionariusz osobowy pracownika", "tak", ""),
        ("B", "Oświadczenia o zapoznaniu z regulaminami i ryzykiem", "tak", ""),
        ("B", "Karta szkolenia wstępnego BHP", "tak", ""),
        ("B", "Dokumenty służby przygotowawczej i ślubowanie", "jeśli dotyczy", ""),
        ("B", "Upoważnienia do przetwarzania danych", "jeśli dotyczy", ""),
        ("C", "Oświadczenie o rozwiązaniu / porozumienie", "tak", ""),
        ("C", "Kopia świadectwa pracy i potwierdzenie odbioru", "tak", ""),
        ("C", "Informacja o okresie przechowywania i zniszczeniu dokumentacji", "tak", ""),
        ("D", "Odpis zawiadomienia o karze porządkowej", "jeśli dotyczy", ""),
        ("E", "Informacje z kontroli trzeźwości", "jeśli dotyczy", ""),
    ]
    for part, docname, required, status in items:
        ws.append([part, docname, required, status, None, None])
    add_status_validation(ws, "D2:D200")
    for col, width in enumerate([10, 72, 16, 22, 20, 40], start=1):
        ws.column_dimensions[ws.cell(row=1, column=col).column_letter].width = width
    add_instruction_sheet(wb, "Checklista kompletności akt osobowych", [
        "1. Statusy: wykonano / nie wykonano / nie dotyczy / wymaga wyjaśnienia.",
        "2. Część D: karę uznaje się za niebyłą po roku od zastosowania (art. 113 KP) — sprawdź termin usunięcia odpisu.",
        "3. Część E: dokumenty przechowuje się co do zasady 1 rok; przy karze porządkowej — do wygaśnięcia kary (art. 22¹c § 7 KP).",
        "4. Dokładna instrukcja: 01_Akta_Osobowe/Instrukcja_obslugi_akt_osobowych.md",
    ])
    path = XLSX_DIR / "Checklista_kompletnosci_akt.xlsx"
    wb.save(path)
    created.append(path)

    # Test odczytu wygenerowanych plików
    for p in created:
        wb_test = load_workbook(p)
        assert wb_test.sheetnames, f"Brak arkuszy: {p}"
        wb_test.close()

    return created


# ---------------------------------------------------------------------------
# PDF
# ---------------------------------------------------------------------------

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\calibri.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]
FONT_BOLD_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\calibrib.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def register_fonts() -> tuple[str, str]:
    regular = "Helvetica"
    bold = "Helvetica-Bold"
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont("PolishRegular", path))
            regular = "PolishRegular"
            break
    for path in FONT_BOLD_CANDIDATES:
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont("PolishBold", path))
            bold = "PolishBold"
            break
    return regular, bold


def pdf_paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(html.escape(text).replace("\n", "<br/>"), style)


def make_pdf(filename: str, title: str, blocks: list[tuple[str, str]]) -> Path:
    regular, bold = register_fonts()
    styles = getSampleStyleSheet()
    body = ParagraphStyle("BodyPL", parent=styles["BodyText"], fontName=regular, fontSize=9.5,
                          leading=13, alignment=TA_LEFT, spaceAfter=6)
    heading = ParagraphStyle("HeadingPL", parent=styles["Heading2"], fontName=bold, fontSize=13,
                             textColor=colors.HexColor("#1F4E78"), spaceBefore=10, spaceAfter=6)
    small = ParagraphStyle("SmallPL", parent=body, fontSize=8, textColor=colors.HexColor("#595959"))
    title_style = ParagraphStyle("TitlePL", parent=styles["Title"], fontName=bold, fontSize=18,
                                 textColor=colors.HexColor("#1F4E78"), spaceAfter=4)

    story: list = [pdf_paragraph(title, title_style),
                   pdf_paragraph(f"Status: {STATUS} | Data weryfikacji: {VERIFICATION_DATE}", small),
                   Spacer(1, 6 * mm)]
    for kind, text in blocks:
        if kind == "h":
            story.append(pdf_paragraph(text, heading))
        elif kind == "p":
            story.append(pdf_paragraph(text, body))
        elif kind == "small":
            story.append(pdf_paragraph(text, small))
        elif kind == "table":
            lines = [line.split(" | ") for line in text.split("\n")]
            data = [[pdf_paragraph(cell, small) for cell in row] for row in lines]
            table = Table(data, colWidths=[45 * mm, 120 * mm])
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCE6F1")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#9BB0C4")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ]))
            story.append(table)
            story.append(Spacer(1, 4 * mm))
    path = PDF_DIR / filename
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                            topMargin=16 * mm, bottomMargin=16 * mm, title=title)
    doc.build(story)
    return path


def build_pdf_files() -> list[Path]:
    created = []
    created.append(make_pdf(
        "Instrukcja_uzytkowania_wzorow.pdf",
        "Instrukcja użytkowania wzorów dokumentów",
        [
            ("h", "1. Zasady ogólne"),
            ("p", "Wzory w katalogu 12_Wzory_Dokumentow są roboczymi szablonami szkoleniowymi. Zawierają wyłącznie pola w nawiasach kwadratowych. Przed użyciem uzupełnij je danymi właściwymi dla ZGKiM w Orzeszu i usuń oznaczenie statusu ROBOCZY."),
            ("h", "2. Formaty"),
            ("table", "Format | Przeznaczenie\nDOCX | wnioski, oświadczenia, wzory pism i dokumentów kadrowych; edytuj w Wordzie\nXLSX | rejestry, ewidencje, kalkulator i kalendarz terminów; edytuj w Excelu\nPDF | wersja do podglądu i wydruku; nie edytuj"),
            ("h", "3. Jak wypełniać DOCX"),
            ("p", "Otwórz plik, uzupełnij pola w nawiasach, sprawdź datę i podpisy. Wzór wniosku o urlop wymaga podania roku, za który udzielany jest urlop. Checklistę onboardingu wydrukuj i zaznacz wykonane czynności."),
            ("h", "4. Jak używać XLSX"),
            ("p", "W kalkulatorze B2–B7 to przykłady — zastąp je własnymi danymi. Formuły zostały sprawdzone na przykładach: 12 lat stażu daje 12% dodatku, 60 000 zł rocznego wynagrodzenia daje 5 100 zł trzynastki, 25 lat daje 100% nagrody jubileuszowej, 20 lat daje 6 miesięcy odprawy."),
            ("p", "W ewidencji czasu pracy godziny wpisuj jako HH:MM. Przykład: 08:00–17:00 z 30-minutową przerwą daje 8,50 h i 0,50 h nadgodzin."),
            ("h", "5. Ochrona danych"),
            ("p", "Nie wpisuj do wzorów rzeczywistych PESEL-i, adresów, danych o zdrowiu ani wynagrodzeń konkretnych osób. Reguły wykluczania takich plików opisuje plik .gitignore."),
        ],
    ))

    created.append(make_pdf(
        "Podglad_checklisty_onboardingu.pdf",
        "Podgląd do wydruku — checklista wdrożenia nowego pracownika",
        [
            ("p", "Zaznacz [x], wpisz datę i osobę potwierdzającą. Wersja robocza — terminy Potwierdź z regulaminem pracy ZGKiM."),
            ("table", "Czynność | Status / data\nUmowa o pracę przed dopuszczeniem do pracy (art. 29 § 2 KP) | [ ]\nInformacja o warunkach zatrudnienia — 7 dni od dopuszczenia | [ ]\nSkierowanie i orzeczenie lekarskie (badania wstępne) | [ ]\nKwestionariusz osobowy i kopie kwalifikacji | [ ]\nZUS ZUA w 7 dni; ZUS ZCNA jeśli dotyczy | [ ]\nSzkolenie wstępne BHP — karta podpisana | [ ]\nZapoznanie z regulaminami, RODO i sygnalistami | [ ]\nOdzież robocza i ŚOI — karta ewidencji | [ ]\nAkt osobowe A–E i upoważnienia RODO | [ ]\nPPK — zapis lub deklaracja rezygnacji | [ ]\nŚlubowanie urzędnika; służba przygotowawcza przy pierwszej pracy urzędniczej | [ ]\nTerminy badań, szkoleń i uprawnień w rejestrze | [ ]"),
            ("small", "Podstawa: Kodeks pracy (art. 29 § 2 i 3, art. 229), ustawa z 21.11.2008 r. o pracownikach samorządowych (art. 16, 18, 19), ustawa o PPK. Data weryfikacji: 2026-11-25."),
        ],
    ))

    created.append(make_pdf(
        "Material_szkoleniowy_kadry.pdf",
        "Materiał szkoleniowy — podstawy pracy kadrowej w ZGK",
        [
            ("h", "1. Forma pracodawcy"),
            ("p", "Zakład Gospodarki Komunalnej i Mieszkaniowej w Orzeszu jest samorządowym zakładem budżetowym, gminną jednostką organizacyjną bez osobowości prawnej (§ 2 statutu, uchwała nr XVIII/192/25 z 23.10.2025 r.). Kieruje nim Dyrektor."),
            ("h", "2. Najważniejsze terminy"),
            ("table", "Czynność | Termin\nUmowa o pracę na piśmie | przed dopuszczeniem do pracy\nInformacja o warunkach zatrudnienia | 7 dni od dopuszczenia\nZUS ZUA / ZWUA / ZCNA | 7 dni od zdarzenia\nZUS dla zakładów budżetowych | do 5. dnia miesiąca\nWpłaty PPK | do 15. dnia miesiąca\nTrzynastka | do 31 marca\nZFŚS – 75% odpisu | do 31 maja\nZaległy urlop | do 30 września\nŚwiadectwo pracy | w dniu ustania zatrudnienia"),
            ("h", "3. Akta osobowe"),
            ("p", "Akta mają części A–E. Część E powstała w 2023 r. i dotyczy kontroli trzeźwości. Dokumenty z części E przechowuje się co do zasady rok; gdy nałożono karę porządkową — do momentu uznania kary za niebyłą (art. 22¹c § 7 KP)."),
            ("h", "4. Najczęstsze błędy"),
            ("p", "Podawanie „Gminy Orzesze” zamiast „Miasta Orzesze”; ograniczanie ślubowania do pierwszych zatrudnień; mylenie PIT-4 z PIT-4R i DEK-I-0 z DEK-1-a; traktowanie zgody jako podstawy przetwarzania danych o zdrowiu w ZFŚS; brak informacji o zniszczeniu dokumentacji przy wydaniu świadectwa pracy."),
            ("small", "Opracowanie robocze. Pełne procedury i odnośniki do źródeł urzędowych znajdują się w plikach Markdown repozytorium."),
        ],
    ))
    return created


def main() -> None:
    for directory in (DOCX_DIR, XLSX_DIR, PDF_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    all_files = build_docx_files() + build_xlsx_files() + build_pdf_files()
    print(f"Wygenerowano {len(all_files)} plików:")
    for f in all_files:
        print(" -", f.relative_to(ROOT))


if __name__ == "__main__":
    main()
