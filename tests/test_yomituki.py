import pytest

from yomigana_ebook.constants import ALL_HIRA, ALL_KATA
from yomigana_ebook.yomituki import yomituki_sentence, yomituki_word


@pytest.mark.parametrize(
    "test_case, sentence, expected",
    [
        (
            "common sentence",
            "月が綺麗ですね！",
            "<ruby>月<rt>つき</rt></ruby>が<ruby>綺麗<rt>きれい</rt></ruby>ですね！",
        ),
    ],
)
def test_yomituki_sentence(test_case: str, sentence: str, expected: str):
    assert yomituki_sentence(sentence) == expected


ANYTHING_UNKNOWN = "anything whose reading is unknown"


@pytest.mark.parametrize(
    "test_case, surface, kata, expected",
    [
        ("for `Mecab` only: unknown 01", ANYTHING_UNKNOWN, "*", ANYTHING_UNKNOWN),
        ("for `Mecab` only: unknown 02", ANYTHING_UNKNOWN, None, ANYTHING_UNKNOWN),
        ("all hira", ALL_HIRA, ALL_KATA, ALL_HIRA),
        ("all kata", ALL_KATA, ALL_KATA, ALL_KATA),
        ("all kata contains mark 01", "チュー", "チュウ", "チュー"),
        ("all kata contains mark 02", "アルフレッド・チャニング", "アルフレッド・チャニング", "アルフレッド・チャニング"),
        ("all kanji", "漢字", "カンジ", "<ruby>漢字<rt>かんじ</rt></ruby>"),
        # need to add space for separating every latin word
        ("all latin", "right", "ライト", " right"),
        ("kanji + hira", "見上げて", "ミアゲテ", "<ruby>見上<rt>みあ</rt></ruby>げて"),
        (
            "hira + kanji",
            "うれし涙",
            "ウレシナミダ",
            "うれし<ruby>涙<rt>なみだ</rt></ruby>",
        ),
        (
            "kanji + hira + kanji + hira",
            "思い出した",
            "オモイダシタ",
            "<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>した",
        ),
        ("special: hira/kata compound", "ッつい", "ッツイ", "ッつい"),
        (
            "special: all kanji contains kata 01",
            "カ月",
            "カゲツ",
            "<ruby>カ月<rt>かげつ</rt></ruby>",
        ),
        (
            "special: all kanji contains kata 02",
            "掛ケ",
            "カケ",
            "<ruby>掛ケ<rt>かけ</rt></ruby>",
        ),
        (
            "special: all kanji contains kata 03",
            "雑司ヶ谷",
            "ゾウシガヤ",
            "<ruby>雑司ヶ谷<rt>ぞうしがや</rt></ruby>",
        ),
        ("special: numbers contain mark", "二、三", "ニサン", "二、三"),
        (
            "special: triple compound kanji",
            "引っ繰り返って",
            "ヒックリカエッテ",
            "<ruby>引<rt>ひ</rt></ruby>っ<ruby>繰<rt>く</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>って",
        ),
        ("special: old word 01", "間違へ", "まちがえ", "<ruby>間違へ<rt>まちがえ</rt></ruby>"),
        ("special: old word 02", "教へる", "おしえる", "<ruby>教へる<rt>おしえる</rt></ruby>"),
        ("special: old word 03", "思ひ出せ", "オモイダセ", "<ruby>思ひ出せ<rt>おもいだせ</rt></ruby>"),
        ("special: old word 04", "づゝ", "ずつ", "<ruby>づゝ<rt>ずつ</rt></ruby>"),
        ("special: old word 05", "かゝはら", "カカワラ", "<ruby>かゝはら<rt>かかわら</rt></ruby>"),
    ],
)
def test_yomituki_word(test_case: str, surface: str, kata: str, expected: str):
    assert yomituki_word(surface, kata) == expected
