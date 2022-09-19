from dataclasses import dataclass
from typing import List, Tuple

import pandas as pd


@dataclass
class Preprocessor:
    df: pd.DataFrame

    def _prep(self) -> pd.DataFrame:
        _df = self.df.copy()
        _df = _df[_df["振替"] == 0].copy()
        _df = _df[(_df["大項目"] != "収入") & (_df["大項目"] != "現金・カード")].copy()
        return _df

    def agg_sorted(self) -> List[Tuple[str, int]]:
        _df = self._prep()
        return sorted(
            _df.groupby("大項目").sum()["金額（円）"].to_dict().items(), key=lambda x: x[1]
        )
