import unicodedata

from yomigana_ebook.constants import ALL_HIRA, ALL_KATA, ALL_LATIN


def is_unknown(surface: str, reading: str) -> bool:
    return "、" in surface or reading in (None, "*")


def is_kana_only(text: str) -> bool:
    return all((is_hira(char) or is_kata(char)) for char in text)


def is_kanji_only(text: str) -> bool:
    return all(is_kanji(char) for char in text)


def is_latin_only(text: str) -> bool:
    return all(is_latin(char) for char in text)


def is_hira(char: str) -> bool:
    return char in ALL_HIRA


def is_kata(char: str) -> bool:
    return char in ALL_KATA


def is_kanji(char: str) -> bool:
    unicode_name = unicodedata.name(char)

    if "CJK UNIFIED IDEOGRAPH" in unicode_name:
        return True

    if "IDEOGRAPHIC ITERATION MARK" in unicode_name:
        return True

    if char in ALL_KATA:
        return True

    return False


def is_latin(char: str) -> bool:
    return char in ALL_LATIN
