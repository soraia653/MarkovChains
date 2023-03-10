import pytest
from mark_chains_prj.main import prepare_data, beginnings, ngrams


# test beginnings using different ORDER values
def test_beginnings() -> None:
    test_data = ["Avatar", "Aviso", "Autora"]
    expected_beginnings = ["Av", "Av", "Au"]

    prepare_data(test_data)
    assert beginnings == expected_beginnings


class TestGrams:
    def test_ngrams_keys(self):
        expected_grams = [
            "Av",
            "va",
            "at",
            "ta",
            "ar",
            "vi",
            "is",
            "so",
            "Au",
            "ut",
            "to",
            "or",
            "ra",
        ]
        assert list(ngrams.keys()) == expected_grams

    def test_ngrams_possibilities(self) -> None:
        expected_possibilities = {
            "Av": ["a", "i"],
            "va": ["t"],
            "at": ["a"],
            "ta": ["r"],
            "ar": [],
            "vi": ["s"],
            "is": ["o"],
            "so": [],
            "Au": ["t"],
            "ut": ["o"],
            "to": ["r"],
            "or": ["a"],
            "ra": [],
        }

        assert ngrams == expected_possibilities
