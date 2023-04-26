from yomigana_ebook.constants import ALL_HIRA, ALL_KATA

hira2kata_table = str.maketrans(ALL_HIRA, ALL_KATA)
kata2hira_table = str.maketrans(ALL_KATA, ALL_HIRA)


def hira2kata(hira: str) -> str:
    return hira.translate(hira2kata_table)


def kata2hira(kata: str) -> str:
    return kata.translate(kata2hira_table)
