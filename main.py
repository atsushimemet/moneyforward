#!/usr/bin/env python
# coding: utf-8

# [家計目標達成シート](https://docs.google.com/spreadsheets/d/10Klr0er2jXVqGIzVU84E_24OkZDYWvRGXZBpJhznim0/edit#gid=0)

import logging

# from pathlib import Path
from pprint import pformat

import logzero
from logzero import logger

from src.config import weeknum
from src.load import Loader
from src.paths import INPUT_PATH
from src.preprocess import Preprocessor
from src.utils import get_file_name

logzero.loglevel(20)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
logzero.formatter(formatter)


def main():
    file_name = get_file_name(weeknum)
    loader = Loader(INPUT_PATH, file_name)
    df = loader.run()
    preprocessor = Preprocessor(df)
    logger.info(f"1週間あたりの支出: {sum(t[1] / 3 for t in preprocessor.agg_sorted()):,}")
    logger.info("1週間あたりの大項目別支出")
    # TODO: Refactored
    for v in preprocessor.agg_sorted():
        logger.info(pformat((v[0], round(v[1] / 3))))


if __name__ == "__main__":
    main()
