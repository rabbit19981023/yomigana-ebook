import pytest

from yomigana_ebook.constants import ALL_HIRA, ALL_KATA, ALL_NUMBER
from yomigana_ebook.yomituki import yomituki_sentence, yomituki_word


@pytest.mark.parametrize(
    "test_case, sentence, expected",
    [
        ("common sentence", "月が綺麗ですね！ ", "<ruby>月<rt>つき</rt></ruby>が<ruby>綺麗<rt>きれい</rt></ruby>ですね！"),
    ]
)
def test_yomituki_sentence(test_case: str, sentence: str, expected: str):
    assert yomituki_sentence(sentence) == expected


@pytest.mark.parametrize(
    "test_case, surface, kata, expected",
    [
        ("mark", "。", "*", "。"),
        ("all hira", ALL_HIRA, ALL_KATA, ALL_HIRA),
        ("all kata", ALL_KATA, ALL_KATA, ALL_KATA),
        ("all kanji", "漢字", "カンジ", "<ruby>漢字<rt>かんじ</rt></ruby>"),
        ("all number", ALL_NUMBER, "dummy kata", ALL_NUMBER),
        ("kanji + hira", "見上げて", "ミアゲテ", "<ruby>見上<rt>みあ</rt></ruby>げて"),
        ("hira + kanji", "うれし涙", "ウレシナミダ", "うれし<ruby>涙<rt>なみだ</rt></ruby>"),
        ("kanji + hira + kanji + hira", "思い出した", "オモイダシタ", "<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>した"),
    ]
)
def test_yomituki_word(test_case: str, surface: str, kata: str, expected: str):
    assert yomituki_word(surface, kata) == expected
