from yomigana_ebook.analyzer import Analyzer
from yomigana_ebook.converter import kata2hira
from yomigana_ebook.checking import is_mark, is_hira_only, is_kata_only, is_kanji_only


def yomituki_sentence(sentence: str) -> str:
    result = ""
    analyzer = Analyzer()

    for morpheme in analyzer.analyze(sentence):
        result += yomituki_word(morpheme.surface, morpheme.reading)

    return result


def yomituki_word(surface: str, kata: str) -> str:
    hira = kata2hira(kata)

    if is_mark(kata):
        return surface
    if is_hira_only(surface, hira):
        return surface
    if is_kata_only(surface, kata):
        return surface
    if is_kanji_only(surface):
        return ruby_wrap(surface, hira)

    # TODO:
    # deal with compound word

    return ""


def ruby_wrap(kanji: str, hira: str) -> str:
    return f"<ruby>{kanji}<rt>{hira}</rt></ruby>"
