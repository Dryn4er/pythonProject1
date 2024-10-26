import pandas as pd


def read_csv(file_name: str) -> list:
    """Функция возвращает список словарей из файла csv"""
    try:
        reader_csv = pd.read_csv(file_name, delimiter=";")
    except FileNotFoundError:
        return []
    return reader_csv.to_dict(orient="records")


def read_xlsx(file_name: str) -> list:
    """Функция возвращает список словарей из файла xlsx"""
    try:
        reader_xlsx = pd.read_excel(file_name)
    except FileNotFoundError:
        return []
    return reader_xlsx.to_dict(orient="records")


# if __name__ == "__main__":

#    print(read_csv("../transactions.csv"))
#    print(read_xlsx('../transactions_excel (1).xlsx'))
