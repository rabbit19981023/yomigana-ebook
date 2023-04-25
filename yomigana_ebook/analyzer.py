from typing import Generator

from fugashi import Tagger


class Morpheme:
    def __init__(self, surface: str, reading: str):
        self.surface = surface
        self.reading = reading


class Analyzer:
    def __init__(self):
        self._analyzer = Tagger()

    def analyze(self, text: str) -> Generator[Morpheme, None, None]:
        for token in self._analyzer(text):
            yield Morpheme(token.surface, token.feature.kana)
