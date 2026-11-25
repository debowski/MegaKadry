#!/usr/bin/env python3
"""Prosty kontroler jakosci repozytorium MegaKadry (bez zaleznosci zewnetrznych).

Uzycie:
    python skrypt_kontroli.py [sciezka_do_katalogu_glównego]

Domyslnie sprawdzany jest katalog nadrzedny wzgledem tego pliku, czyli
katalog glowny repozytorium. Skrypt dziala na Windows, Linux i macOS
(wymaga wyłącznie Pythona 3 z biblioteki standardowej).

Sprawdza:
  1. istnienie wymaganych plikow i katalogow,
  2. czy pliki .md nie sa puste i maja naglowek oraz minimum tresci,
  3. czy lokalne odnosniki Markdown wskazuja na istniejace pliki/katalogi.

Wynik:
  - wypisuje liste bledow (lub komunikat o braku bledow),
  - podsumowanie liczbowe,
  - kod wyjscia 0 gdy nie ma bledow, 1 gdy chociaz jeden blad zostal znaleziony.

Uwaga: skrypt nie sprawdza poprawnosci merytorycznej przepisow prawnych
ani jakosci merytorycznej dokumentow. Nie modyfikuje plikow.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

# Wymagane elementy repozytorium (sciezki wzgledem katalogu glownego).
REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "00_Dane_pracodawcy_ZGKiM_Orzesze.md",
    "01_Akta_Osobowe",
    "01_Akta_Osobowe/00_Spis_tresci_akt_osobowych_AB_CDE.md",
    "10_Kontrole_i_Audyt",
    "10_Kontrole_i_Audyt/Instrukcja_kontroli_wewnetrznej.md",
    "10_Kontrole_i_Audyt/Checklista_kontroli_akt_osobowych.md",
    "10_Kontrole_i_Audyt/Checklista_kontroli_czasu_pracy_i_urlopow.md",
    "10_Kontrole_i_Audyt/Lista_najczestszych_bledow_kadrowych.md",
    "11_Aktualizacje_i_Zrodla",
    "11_Aktualizacje_i_Zrodla/Wykaz_zrodel_urzedowych.md",
    "11_Aktualizacje_i_Zrodla/Rejestr_zmian_prawnych.md",
    "11_Aktualizacje_i_Zrodla/Rejestr_weryfikacji_dokumentow.md",
    "11_Aktualizacje_i_Zrodla/Instrukcja_aktualizacji_i_zglaszania_bledow.md",
    "11_Aktualizacje_i_Zrodla/skrypt_kontroli.py",
]

# Odnośniki [tekst](adres) — bez zagniezdzonych nawiasow w adresie.
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+\S", re.MULTILINE)
MIN_CONTENT_LENGTH = 40

# Prefiksy oznaczajace odnosniki, ktorych nie sprawdzamy na dysku.
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:")


def configure_stdout() -> None:
    """Ustaw kodowanie UTF-8 na wypisie (wazne na Windows)."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def clean_destination(raw: str) -> str:
    """Usuwa opcjonalny tytul odnosnika, kotwice i kodowanie %XX."""
    destination = raw.strip()
    if destination.startswith("<") and ">" in destination:
        destination = destination[1 : destination.index(">")]
    else:
        # Tytul w postaci: sciezka.md "Tytul" albo sciezka.md 'Tytul'
        title_match = re.search(r'\s+["\']', destination)
        if title_match:
            destination = destination[: title_match.start()]
    destination = destination.split("#", 1)[0].strip()
    destination = unquote(destination)
    return destination


def check_required_paths(root: Path, errors: list[str]) -> None:
    """Sprawdza istnienie wymaganych plikow i katalogow."""
    for relative in REQUIRED_PATHS:
        path = root / relative
        if not path.exists():
            errors.append(f"BRAK: wymagany element nie istnieje: {relative}")


def check_markdown_files(root: Path, errors: list[str]) -> tuple[int, int]:
    """Sprawdza pliki .md oraz lokalne odnosniki. Zwraca (liczba plikow, liczba odnosnikow)."""
    files_checked = 0
    links_checked = 0

    for md_path in sorted(root.rglob("*.md")):
        # Pomijamy katalogi pomocnicze, nie bedace czescia dokumentacji.
        if any(part.startswith(".git") for part in md_path.parts):
            continue

        files_checked += 1
        relative = md_path.relative_to(root).as_posix()

        try:
            text = md_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"ODCZYT: {relative} — {exc}")
            continue

        stripped = text.strip()
        if not stripped:
            errors.append(f"PUSTY PLIK: {relative}")
            continue

        if len(stripped) < MIN_CONTENT_LENGTH:
            errors.append(
                f"ZA KROTKI: {relative} — mniej niz {MIN_CONTENT_LENGTH} znakow tresci"
            )

        if not HEADING_RE.search(text):
            errors.append(f"BRAK NAGLOWKA: {relative} — brak linii zaczynajacej sie od #")

        for match in LINK_RE.finditer(text):
            raw_destination = match.group(1)
            destination = clean_destination(raw_destination)

            if not destination or destination.startswith(EXTERNAL_PREFIXES):
                continue
            if destination.startswith("#"):
                continue

            line_number = text.count("\n", 0, match.start()) + 1
            links_checked += 1

            if destination.startswith("/"):
                target = root / destination.lstrip("/")
            else:
                target = (md_path.parent / destination).resolve()

            if not target.exists():
                errors.append(
                    f"ODNOSNIK: {relative}:{line_number} — nie istnieje: {raw_destination}"
                )

    return files_checked, links_checked


def main() -> int:
    """Punkt wejscia skryptu. Zwraca kod wyjscia 0 lub 1."""
    configure_stdout()

    if len(sys.argv) > 2:
        print("Uzycie: python skrypt_kontroli.py [sciezka_do_katalogu_glównego]")
        return 1

    if len(sys.argv) == 2:
        root = Path(sys.argv[1]).expanduser().resolve()
    else:
        root = Path(__file__).resolve().parent.parent

    if not root.is_dir():
        print(f"BLAD: katalog glowny nie istnieje: {root}")
        return 1

    errors: list[str] = []
    check_required_paths(root, errors)
    files_checked, links_checked = check_markdown_files(root, errors)

    print(f"Katalog glowny: {root}")
    print(f"Sprawdzono plikow .md: {files_checked}")
    print(f"Sprawdzono lokalnych odnosnikow: {links_checked}")
    print(f"Liczba bledow: {len(errors)}")

    if errors:
        print("\n--- Szczegoly bledow ---")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nOK: struktura, pliki .md i lokalne odnosniki sa poprawne.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
