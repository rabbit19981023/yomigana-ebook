from yomigana_ebook.constants import ALL_HIRA, ALL_KATA
from yomigana_ebook.converter import hira2kata, kata2hira


def test_converter_hira2kata():
    assert hira2kata(ALL_HIRA) == ALL_KATA


def test_converter_kata2hira():
    assert kata2hira(ALL_KATA) == ALL_HIRA
