from unicodedata import name as get_unicode_name


def is_unknown(surface: str, reading: str) -> bool:
    return reading in (None, "*") or "、" in surface


def is_kana_only(text: str) -> bool:
    return all((is_hira(char) or is_kata(char)) for char in text)


def is_kanji_only(text: str) -> bool:
    return all(is_kanji(char) for char in text)


def is_latin_only(text: str) -> bool:
    return all(is_latin(char) for char in text)


def is_hira(char: str) -> bool:
    return "HIRAGANA" in get_unicode_name(char)


def is_kata(char: str) -> bool:
    return "KATAKANA" in get_unicode_name(char)


def is_kanji(char: str) -> bool:
    unicode_name = get_unicode_name(char)

    if "CJK UNIFIED IDEOGRAPH" in unicode_name:
        return True

    if "IDEOGRAPHIC ITERATION MARK" in unicode_name:
        return True

    return False


def is_latin(char: str) -> bool:
    return "LATIN" in get_unicode_name(char)
