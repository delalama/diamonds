import os
import pandas as pd


def get_csv(rows):
    if rows is None:
        rows = 50
    assets_folder = os.path.join(os.getcwd(), 'assets')
    csv_file_path = os.path.join(assets_folder, 'diamonds.csv')

    # Read the CSV file and discard the 'id' column
    df = pd.read_csv(csv_file_path, usecols=lambda col: col.lower() != 'id', nrows=rows)

    return df
