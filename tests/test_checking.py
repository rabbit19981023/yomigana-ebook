import pytest
import unicodedata

from yomigana_ebook.constants import ALL_HIRA, ALL_KATA
from yomigana_ebook.checking import is_hira_only, is_kata_only, is_kanji_only


def test_is_hira_only():
    for char in ALL_HIRA:
        if not "HIRAGANA" in unicodedata.name(char):
            assert False
    assert is_hira_only(ALL_HIRA, ALL_HIRA)


def test_is_kata_only():
    for char in ALL_KATA:
        if not "KATAKANA" in unicodedata.name(char):
            assert False
    assert is_kata_only(ALL_KATA, ALL_KATA)


@pytest.mark.parametrize(
    "test_case, kanji, expected",
    [
        ("common", "漢字", True),
        ("all hira", ALL_HIRA, False),
        ("all kata", ALL_KATA, False),
        ("contains hira", "感じ", False),
        ("contains `々`", "時々", True),
        ("contains mark", "漢字。", False)
    ]
)
def test_is_kanji_only(test_case: str, kanji: str, expected: bool):
    assert is_kanji_only(kanji) == expected
