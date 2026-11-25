#!/usr/bin/env python3
"""Monitor aktualnosci dokumentow MegaKadry (bez zaleznosci zewnetrznych).

Uzycie:
    python 11_Aktualizacje_i_Zrodla/monitor_aktualnosci.py
    python 11_Aktualizacje_i_Zrodla/monitor_aktualnosci.py --date 2027-01-31 --months 12

Sprawdza date weryfikacji wpisana w metryce dokumentu i wskazuje pliki,
ktorych weryfikacja jest starsza niz podana liczba miesiecy. Domyslnie
porownuje z data zbiorczej weryfikacji repozytorium (2026-11-25).

Skrypt nie sprawdza merytorycznej poprawnosci przepisow — do tego sluza
zrodla urzedowe i Rejestr zmian prawnych. Nie modyfikuje plikow.
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATE = date(2026, 11, 25)
EXCLUDED = {"AGENTS.md", "INDEKS_DOKUMENTACJI.md"}
DATE_RE = re.compile(
    r"(?:data\s+(?:ostatniej\s+)?weryfikacj\w*|weryfikacj\w*)[^\d]{0,60}(\d{4}-\d{2}-\d{2})",
    re.IGNORECASE,
)
ANY_DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


def verification_date(text: str) -> date | None:
    """Zwraca date weryfikacji z metryki, a gdy jej nie ma — najpóźniejszą date w pliku."""
    found = DATE_RE.findall(text)
    candidates = found or ANY_DATE_RE.findall(text)
    dates = []
    for raw in candidates:
        try:
            dates.append(date.fromisoformat(raw))
        except ValueError:
            continue
    return max(dates) if dates else None


def months_between(start: date, end: date) -> int:
    return (end.year - start.year) * 12 + end.month - start.month - (1 if end.day < start.day else 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Monitor aktualności dokumentacji MegaKadry")
    parser.add_argument("--date", default=DEFAULT_DATE.isoformat(), help="data porównania (RRRR-MM-DD)")
    parser.add_argument("--months", type=int, default=12, help="maksymalny wiek weryfikacji w miesiącach")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    today = date.fromisoformat(args.date)
    files = sorted(
        p for p in ROOT.rglob("*.md")
        if p.name not in EXCLUDED and ".git" not in p.parts
    )
    overdue: list[tuple[str, int]] = []
    missing: list[str] = []
    fresh = 0

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        verified = verification_date(text)
        if verified is None:
            missing.append(path.relative_to(ROOT).as_posix())
            continue
        age = months_between(verified, today)
        if age > args.months:
            overdue.append((path.relative_to(ROOT).as_posix(), age))
        else:
            fresh += 1

    print(f"Data porównania: {today.isoformat()} | limit: {args.months} miesięcy")
    print(f"Sprawdzono plików .md: {len(files)}")
    print(f"Aktualne: {fresh} | Przeterminowane: {len(overdue)} | Bez daty weryfikacji: {len(missing)}")
    if overdue:
        print("\nPRZETERMINOWANE:")
        for name, age in overdue:
            print(f" - {name} ({age} mies.)")
    if missing:
        print("\nBRAK DATY WERYFIKACJI:")
        for name in missing:
            print(f" - {name}")
    if not overdue and not missing:
        print("\nOK: wszystkie dokumenty mają aktualną datę weryfikacji.")
    raise SystemExit(1 if overdue or missing else 0)


if __name__ == "__main__":
    main()
