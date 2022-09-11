#!/usr/bin/env python
# coding: utf-8

# [家計目標達成シート](https://docs.google.com/spreadsheets/d/10Klr0er2jXVqGIzVU84E_24OkZDYWvRGXZBpJhznim0/edit#gid=0)

# In[27]:


import logging
from pathlib import Path

import logzero
import pandas as pd
from logzero import logger

INPUT_PATH = Path("./data/input/")
file_name = "収入・支出詳細_2022-09-01_2022-09-30.csv"
logzero.loglevel(20)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
logzero.formatter(formatter)


def get_expense(df: pd.DataFrame) -> dict:
    return (
        df[(df["振替"] == 0) & (df["大項目"] != "収入")].groupby("内容").sum()["金額（円）"].to_dict()
    )


def main():
    df = pd.read_csv(INPUT_PATH / file_name, encoding="shiftjis")
    logger.info(f"""This week expense{get_expense(df)}""")


if __name__ == "__main__":
    main()
