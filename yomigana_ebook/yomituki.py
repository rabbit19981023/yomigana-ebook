from typing import Tuple
from os.path import commonprefix

from yomigana_ebook.analyzer import Analyzer, Morpheme
from yomigana_ebook.converter import kata2hira
from yomigana_ebook.checking import (
    is_unknown,
    is_hira_only,
    is_kata_only,
    is_kanji_only,
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
    if is_unknown(kata):
        return surface

    hira = kata2hira(kata)

    if is_hira_only(surface, hira):
        return surface
    if is_kata_only(surface, kata):
        return surface
    if is_kanji_only(surface):
        return ruby_wrap(surface, hira)

    # yomituki for:
    # hira + kanji: うれし涙
    # kanji + hira: 見上げて
    (prefix, middle, suffix) = cut_by_hira(surface, hira)
    if is_kanji_only(middle.surface):
        return f"{prefix}{ruby_wrap(middle.surface, middle.reading)}{suffix}"

    # yomituki for
    # kanji + hira + kanji + hira: 思い出した
    hira_index_surface = 0
    hira_in_surface = ""
    for i, char in enumerate(middle.surface[::-1]):
        if not is_kanji(char):
            hira_index_surface = -i - 1
            hira_in_surface = middle.surface[hira_index_surface]

    hira_index_reading = 0
    for i, char in enumerate(middle.reading[::-1]):
        if char == hira_in_surface:
            hira_index_reading = -i - 1

    return (
        f"{prefix}"
        f"{ruby_wrap(middle.surface[:hira_index_surface], middle.reading[:hira_index_reading])}"
        f"{hira_in_surface}"
        f"{ruby_wrap(middle.surface[hira_index_surface+1:], middle.reading[hira_index_reading+1:])}"
        f"{suffix}"
    )


def ruby_wrap(kanji: str, hira: str) -> str:
    return f"<ruby>{kanji}<rt>{hira}</rt></ruby>"


def cut_by_hira(surface: str, hira: str) -> Tuple[str, Morpheme, str]:
    prefix = find_common_prefix(surface, hira)
    suffix = find_common_suffix(surface, hira)
    middle = Morpheme(
        surface.removeprefix(prefix).removesuffix(suffix),
        hira.removeprefix(prefix).removesuffix(suffix),
    )
    return (prefix, middle, suffix)


def find_common_prefix(str1: str, str2: str) -> str:
    return commonprefix((str1, str2))


def find_common_suffix(str1: str, str2: str) -> str:
    return commonprefix((str1[::-1], str2[::-1]))[::-1]
