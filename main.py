#!/usr/bin/env python
# coding: utf-8

# [家計目標達成シート](https://docs.google.com/spreadsheets/d/10Klr0er2jXVqGIzVU84E_24OkZDYWvRGXZBpJhznim0/edit#gid=0)

import logging

# from pathlib import Path
from pprint import pprint

import logzero

from src.config import weeknum
from src.load import Loader
from src.paths import INPUT_PATH
from src.preprocess import Preprocessor
from src.utils import get_file_name

# import pandas as pd
# from logzero import logger


logzero.loglevel(20)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
logzero.formatter(formatter)


# def get_expense(df: pd.DataFrame) -> dict:
#     return (
#         df[(df["振替"] == 0) & (df["大項目"] != "収入")].groupby("内容").sum()["金額（円）"].to_dict()
#     )


def main():
    # df = pd.read_csv(INPUT_PATH / file_name, encoding="shiftjis")
    # logger.info(f"""This week expense{get_expense(df)}""")
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    df = loader.run()
    preprocessor = Preprocessor(df)
    pprint(preprocessor.agg_sorted())


if __name__ == "__main__":
    main()
