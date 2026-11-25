"""Shared loader for pipeline/tts/respell.json (single source of truth for EN/number/brand respellings & STT aliases)."""
import json
from pathlib import Path

_DATA = json.loads((Path(__file__).resolve().parent / "respell.json").read_text(encoding="utf-8"))

EN_TO_VI: dict[str, str] = dict(_DATA["en_to_vi"])
VI_TO_EN: list[tuple[str, str]] = [tuple(x) for x in _DATA["vi_to_en"]]
STT_ALIASES: list[tuple[str, str]] = [tuple(x) for x in _DATA["stt_aliases"]]
STT_ALIAS_MAP: dict[str, str] = {k: v for k, v in STT_ALIASES}


def unrespell(text: str) -> str:
    for a, b in VI_TO_EN:
        text = text.replace(a, b)
    return text


def respell_word(word: str) -> str:
    return EN_TO_VI.get(word.lower(), word)
