from pathlib import Path

import pandas as pd

app_dir = Path(__file__).parent

weights = pd.read_csv(app_dir / "weights.csv", index_col=False)
