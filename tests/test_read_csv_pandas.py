from unittest.mock import patch

from src.read_csv_pandas import read_csv, read_xlsx
from tests.conftest import test_df_csv_xlsx


@patch("src.read_csv_pandas.pd.read_csv")
def test_read_csv(mock_read, test_df_csv_xlsx):
    mock_read.return_value = test_df_csv_xlsx
    assert read_csv("../transactions.csv") == test_df_csv_xlsx.to_dict(orient="records")
    mock_read.assert_called_once_with("../transactions.csv", delimiter=";")


@patch("src.read_csv_pandas.pd.read_excel")
def test_read_xlsx(mock_read, test_df_csv_xlsx):
    mock_read.return_value = test_df_csv_xlsx
    result = read_xlsx("../transactions_excel (1).xlsx")
    assert result == test_df_csv_xlsx.to_dict(orient="records")
    mock_read.assert_called_once_with("../transactions_excel (1).xlsx")
