from src.config import weeknum
from src.load import Loader
from src.paths import INPUT_PATH
from src.preprocess import Preprocessor
from src.utils import get_file_name


def test_not_furikae_rec():
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    df = loader.run()
    preprocessor = Preprocessor(df)
    preprocessed = preprocessor._prep()
    actual = preprocessed["振替"].unique().tolist()
    expected = [0]
    assert actual == expected


def test_not_syunyu_rec():
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    df = loader.run()
    preprocessor = Preprocessor(df)
    preprocessed = preprocessor._prep()
    actual = preprocessed["大項目"].unique().tolist()
    assert "収入" not in actual


def test_not_cash_and_card_rec():
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    df = loader.run()
    preprocessor = Preprocessor(df)
    preprocessed = preprocessor._prep()
    actual = preprocessed["大項目"].unique().tolist()
    assert "現金・カード" not in actual


def test_aggregated_key_types():
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    df = loader.run()
    preprocessor = Preprocessor(df)
    actual = all([isinstance(t[0], str) for t in preprocessor.agg_sorted()])
    expected = True
    assert actual == expected


def test_aggregated_value_types():
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    df = loader.run()
    preprocessor = Preprocessor(df)
    actual = all([isinstance(t[1], int) for t in preprocessor.agg_sorted()])
    expected = True
    assert actual == expected


def test_aggregated_value_sorted():
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    df = loader.run()
    preprocessor = Preprocessor(df)
    actual = [t[1] for t in preprocessor.agg_sorted()]
    expected = sorted(actual, reverse=False)  # NOTE: negative values
    assert actual == expected
