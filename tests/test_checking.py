import pytest
import unicodedata

from yomigana_ebook.constants import ALL_HIRA, ALL_KATA
from yomigana_ebook.checking import is_hira_only, is_kata_only, is_kanji_only


@pytest.mark.parametrize(
    "test_case, text, hira, expected",
    [
        ("all hira", ALL_HIRA, ALL_HIRA, True),
        ("all kata", ALL_KATA, ALL_HIRA, False),
        ("all kanji", "漢字", "かんじ", False),
        ("contains kanji", "感じ", "かんじ", False),
    ],
)
def test_is_hira_only(test_case: str, text: str, hira: str, expected: bool):
    for char in ALL_HIRA:
        if not "HIRAGANA" in unicodedata.name(char):
            assert False
    assert is_hira_only(text, hira) == expected


@pytest.mark.parametrize(
    "test_case, text, kata, expected",
    [
        ("all hira", ALL_HIRA, ALL_KATA, False),
        ("all kata", ALL_KATA, ALL_KATA, True),
        ("all kanji", "漢字", "カンジ", False),
        ("contains kanji", "感じ", "カンジ", False),
    ],
)
def test_is_kata_only(test_case: str, text: str, kata: str, expected: bool):
    for char in ALL_KATA:
        if not "KATAKANA" in unicodedata.name(char):
            assert False
    assert is_kata_only(text, kata) == expected


@pytest.mark.parametrize(
    "test_case, kanji, expected",
    [
        ("common", "漢字", True),
        ("all hira", ALL_HIRA, False),
        ("all kata", ALL_KATA, False),
        ("contains hira", "感じ", False),
        ("contains `々`", "時々", True),
    ],
)
def test_is_kanji_only(test_case: str, kanji: str, expected: bool):
    assert is_kanji_only(kanji) == expected
