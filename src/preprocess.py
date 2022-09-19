from dataclasses import dataclass

import pandas as pd


@dataclass
class Preprocessor:
    df: pd.DataFrame

    def _prep(self) -> pd.DataFrame:
        _df = self.df.copy()
        _df = _df[_df["振替"] == 0].copy()
        _df = _df[(_df["大項目"] != "収入") & (_df["大項目"] != "現金・カード")].copy()
        return _df

    def agg(self) -> dict:
        _df = self._prep()
        return _df.groupby("大項目").sum()["金額（円）"].to_dict()
