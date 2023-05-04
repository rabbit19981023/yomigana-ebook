from typing import Tuple
from os.path import commonprefix

from yomigana_ebook.analyzer import Analyzer
from yomigana_ebook.converter import kata2hira
from yomigana_ebook.checking import (
    is_unknown,
    is_kana_only,
    is_kanji_only,
    is_latin_only,
    is_kanji,
)


analyzer = Analyzer()


def yomituki_sentence(sentence: str) -> str:
    result = ""

    for morpheme in analyzer.analyze(sentence):
        result += yomituki_word(morpheme.surface, morpheme.reading)

    return result


def yomituki_word(surface: str, kata: str) -> str:
    # this checking is for `Mecab` only
    if is_unknown(surface, kata):
        return surface

    if is_kana_only(surface):
        return surface
    if is_kanji_only(surface):
        return ruby_wrap(surface, kata2hira(kata))
    if is_latin_only(surface):
        # add space for separating every latin word
        return " " + surface

    # yomituki for:
    # hira + kanji: うれし涙
    # kanji + hira: 見上げて
    (prefix, (mid_text, mid_hira), suffix) = cut_by_hira(surface, kata2hira(kata))
    if is_kanji_only(mid_text):
        return f"{prefix}{ruby_wrap(mid_text, mid_hira)}{suffix}"

    # yomituki for
    # kanji + hira + kanji + hira: 思い出した
    return f"{prefix}{yomituki_compound(mid_text, mid_hira)}{suffix}"


def yomituki_compound(surface: str, hira: str) -> str:
    hira_in_surface = "".join(char for char in surface if not is_kanji(char))
    hira_index_in_surface = surface.index(hira_in_surface)
    hira_index_in_hira = hira.rindex(hira_in_surface)

    return "{}{}{}".format(
        ruby_wrap(surface[:hira_index_in_surface], hira[:hira_index_in_hira]),
        hira_in_surface,
        ruby_wrap(
            surface[hira_index_in_surface + len(hira_in_surface) :],
            hira[hira_index_in_hira + len(hira_in_surface) :],
        ),
    )


def ruby_wrap(kanji: str, hira: str) -> str:
    return f"<ruby>{kanji}<rt>{hira}</rt></ruby>"


def cut_by_hira(surface: str, hira: str) -> Tuple[str, Tuple[str, str], str]:
    prefix = find_common_prefix(surface, hira)
    suffix = find_common_suffix(surface, hira)
    middle = (
        surface.removeprefix(prefix).removesuffix(suffix),
        hira.removeprefix(prefix).removesuffix(suffix),
    )
    return (prefix, middle, suffix)


def find_common_prefix(str1: str, str2: str) -> str:
    return commonprefix((str1, str2))


def find_common_suffix(str1: str, str2: str) -> str:
    return commonprefix((str1[::-1], str2[::-1]))[::-1]
