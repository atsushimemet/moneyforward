from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class Loader:
    path: Path
    file_name: str

    def run(self) -> pd.DataFrame:
        return pd.read_csv(self.path / self.file_name, encoding="shiftjis")
