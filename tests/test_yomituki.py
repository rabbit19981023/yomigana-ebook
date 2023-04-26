import pytest

from yomigana_ebook.yomituki import yomituki_sentence


@pytest.mark.parametrize(
    "test_case, sentence, expected",
    [
        ("common sentence", "月が綺麗ですね！ ", "<ruby>月<rt>つき</rt></ruby>が<ruby>綺麗<rt>きれい</rt></ruby>ですね！"),
    ]
)
def test_yomituki_sentence(test_case: str, sentence: str, expected: str):
    assert yomituki_sentence(sentence) == expected
