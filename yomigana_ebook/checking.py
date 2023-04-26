import unicodedata


def is_mark(char: str) -> bool:
    return char == "*"


def is_hira_only(text: str, hira: str) -> bool:
    return text == hira


def is_kata_only(text: str, kata: str) -> bool:
    return text == kata


def is_kanji_only(text: str) -> bool:
    for char in text:
        if not is_kanji(char):
            return False

    return True


def is_kanji(char: str) -> bool:
    unicode_name = unicodedata.name(char)

    if "CJK UNIFIED IDEOGRAPH" in unicode_name:
        return True

    if "IDEOGRAPHIC ITERATION MARK" in unicode_name:
        return True

    return False
