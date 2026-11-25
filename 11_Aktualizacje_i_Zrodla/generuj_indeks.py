#!/usr/bin/env python3
"""Generuje centralny indeks dokumentacji MegaKadry (bez zaleznosci zewnetrznych).

Uzycie:
    python 11_Aktualizacje_i_Zrodla/generuj_indeks.py

Plik wyjsciowy: INDEKS_DOKUMENTACJI.md w katalogu glownym repozytorium.
Indeks jest generowany automatycznie — nie edytuj go recznie; zmien skrypt
albo zrodlowy dokument i uruchom go ponownie.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "INDEKS_DOKUMENTACJI.md"
EXCLUDED = {"INDEKS_DOKUMENTACJI.md", "AGENTS.md"}
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def clean(text: str) -> str:
    text = LINK.sub(r"\1", text)
    text = re.sub(r"[`*_>#]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def describe(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return "Dokument źródłowy."
    lines = [line.strip() for line in text.splitlines()]
    for i, line in enumerate(lines):
        if line.startswith("# "):
            for candidate in lines[i + 1:]:
                if candidate and not candidate.startswith(("#", "|", "---", ">", "*Status")):
                    desc = clean(candidate)
                    if len(desc) > 25:
                        return desc[:180] + ("…" if len(desc) > 180 else "")
            break
    return "Dokument źródłowy — otwórz plik, aby zapoznać się z treścią."


def main() -> None:
    files = sorted(
        p for p in ROOT.rglob("*.md")
        if p.name not in EXCLUDED and ".git" not in p.parts
    )
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        rel = path.relative_to(ROOT)
        group = rel.parts[0] if len(rel.parts) > 1 else "(dokumenty główne)"
        groups[group].append(path)

    lines = [
        "# Centralny indeks dokumentacji MegaKadry",
        "",
        "Automatycznie wygenerowany spis wszystkich dokumentów Markdown w repozytorium.",
        "Nie edytuj ręcznie — uruchom `python 11_Aktualizacje_i_Zrodla/generuj_indeks.py`.",
        "",
        "Status indeksu: **ROBOCZY** · Data wygenerowania: **2026-11-25**",
        "",
        f"Liczba dokumentów: **{len(files)}** · Liczba grup: **{len(groups)}**",
        "",
        "## Jak korzystać z indeksu",
        "",
        "1. Wybierz grupę (katalog) odpowiadającą potrzebie.",
        "2. Otwórz dokument ze spisu — link prowadzi bezpośrednio do pliku.",
        "3. W razie wątpliwości co do aktualności sprawdź [rejestr zmian prawnych](11_Aktualizacje_i_Zrodla/Rejestr_zmian_prawnych.md).",
        "",
        "Punkt wejścia dla nowego pracownika: [Podręcznik kadrowca](00_Start/Podrecznik_kadrowca.md).",
        "",
        "---",
        "",
    ]
    for group in sorted(groups):
        lines.append(f"## {group}")
        lines.append("")
        lines.append("| Dokument | Opis |")
        lines.append("| --- | --- |")
        for path in sorted(groups[group]):
            rel = path.relative_to(ROOT).as_posix()
            title = clean(HEADING.search(path.read_text(encoding="utf-8", errors="ignore")).group(1)) if HEADING.search(path.read_text(encoding="utf-8", errors="ignore")) else path.stem
            lines.append(f"| [{title}]({rel}) | {describe(path)} |")
        lines.append("")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wygenerowano {OUTPUT.relative_to(ROOT)}: {len(files)} dokumentow w {len(groups)} grupach.")


if __name__ == "__main__":
    main()
