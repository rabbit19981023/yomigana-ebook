import pytest

from yomigana_ebook.constants import ALL_HIRA, ALL_KATA
from yomigana_ebook.yomituki import yomituki, yomituki_word


@pytest.mark.parametrize(
    "test_case, sentence, expected",
    [
        (
            "common sentence",
            "月が綺麗ですね！",
            "<ruby>月<rt>つき</rt></ruby>が<ruby>綺麗<rt>きれい</rt></ruby>ですね！",
        ),
        (
            "sentence with whitespaces 01",
            "This project is aimed at making Japanese eBooks more friendly to those who are learning Japanese now by adding readings for every Kanji in the eBooks.",
            "This project is aimed at making Japanese eBooks more friendly to those who are learning Japanese now by adding readings for every Kanji in the eBooks.",
        ),
        (
            "sentence with whitespaces 02 (even with full whitespaces)",
            "本好きの下剋上 〜司書になるためには手段を選んでいられません〜 第一部　兵士の娘Ｉ",
            "<ruby>本好<rt>ほんず</rt></ruby>きの<ruby>下剋上<rt>げこくじょう</rt></ruby> 〜<ruby>司書<rt>ししょ</rt></ruby>になるためには<ruby>手段<rt>しゅだん</rt></ruby>を<ruby>選<rt>えら</rt></ruby>んでいられません〜 <ruby>第<rt>だい</rt></ruby><ruby>一<rt>いっ</rt></ruby><ruby>部<rt>ぶ</rt></ruby>　<ruby>兵士<rt>へいし</rt></ruby>の<ruby>娘<rt>むすめ</rt></ruby>Ｉ",
        ),
    ],
)
def test_yomituki(test_case: str, sentence: str, expected: str):
    assert "".join(yomituki(sentence)) == expected


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
        ("all kanji contains `々`", "日々", "ヒビ", "<ruby>日々<rt>ひび</rt></ruby>"),
        ("all latin", "right", "ライト", "right"),
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
        ("special: old word 01", "間違へ", "マチガエ", "<ruby>間違へ<rt>まちがえ</rt></ruby>"),
        ("special: old word 02", "教へる", "オシエル", "<ruby>教へる<rt>おしえる</rt></ruby>"),
        ("special: old word 03", "思ひ出せ", "オモイダセ", "<ruby>思ひ出せ<rt>おもいだせ</rt></ruby>"),
        ("special: old word 04", "づゝ", "ヅツ", "づゝ"),
        ("special: old word 05", "かゝはら", "カカワラ", "かゝはら"),
    ],
)
def test_yomituki_word(test_case: str, surface: str, kata: str, expected: str):
    assert yomituki_word(surface, kata) == expected
