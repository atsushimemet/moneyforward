from src.config import weeknum
from src.load import Loader
from src.paths import INPUT_PATH
from src.utils import get_file_name


def test_loader():
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    rows = bool(len(loader.run()))
    assert rows
