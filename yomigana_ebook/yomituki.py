from typing import Tuple, Generator
from os.path import commonprefix

from yomigana_ebook.analyzer import Analyzer
from yomigana_ebook.converter import kata2hira
from yomigana_ebook.checking import (
    is_unknown,
    is_kana_only,
    is_kanji_only,
    is_latin_only,
    is_hira,
    is_kanji,
)


analyzer = Analyzer()


def yomituki_sentence(sentence: str) -> Generator[str, None, None]:
    for morpheme in analyzer.analyze(sentence):
        yield yomituki_word(morpheme.surface, morpheme.reading)


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

    try:
        # yomituki for
        # normal compound word: 思い出した
        # triple compound word: 引っ繰り返って
        return f"{prefix}{yomituki_compound(mid_text, mid_hira)}{suffix}"
    except:
        # yomituki for
        # old word: 間違へ(まちがえ), 教へる(おしえる), づゝ(ずつ)
        return ruby_wrap(surface, kata2hira(kata))


def yomituki_compound(surface: str, hira: str) -> str:
    hira_in_surface_reversed = ""

    for char in surface[::-1]:
        if is_hira(char):
            hira_in_surface_reversed += char

        if is_kanji(char) and hira_in_surface_reversed:
            break

    if not hira_in_surface_reversed:
        return ruby_wrap(surface, hira)

    hira_in_surface = hira_in_surface_reversed[::-1]
    hira_index_in_surface, hira_index_in_hira = (
        surface.rindex(hira_in_surface),
        hira.rindex(hira_in_surface),
    )

    left_surface, left_hira = surface[:hira_index_in_surface], hira[:hira_index_in_hira]
    right_surface, right_hira = (
        surface[hira_index_in_surface + len(hira_in_surface) :],
        hira[hira_index_in_hira + len(hira_in_surface) :],
    )

    return (
        yomituki_compound(left_surface, left_hira)
        + hira_in_surface
        + ruby_wrap(right_surface, right_hira)
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
