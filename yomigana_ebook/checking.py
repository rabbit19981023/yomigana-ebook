import unicodedata

from yomigana_ebook.constants import ALL_NUMBER


def is_unknown(char: str) -> bool:
    return char in (None, "*")


def is_hira_only(text: str, hira: str) -> bool:
    return text == hira


def is_kata_only(text: str, kata: str) -> bool:
    return text == kata


def is_kanji_only(text: str) -> bool:
    for char in text:
        if not is_kanji(char):
            return False

    return True


def is_number_only(text: str) -> bool:
    for char in text:
        if not is_number(char):
            return False

    return True


def is_kanji(char: str) -> bool:
    unicode_name = unicodedata.name(char)

    if "CJK UNIFIED IDEOGRAPH" in unicode_name:
        return True

    if "IDEOGRAPHIC ITERATION MARK" in unicode_name:
        return True

    return False


def is_number(char: str) -> bool:
    return char in ALL_NUMBER
