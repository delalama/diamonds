import os
import csv
from typing import Optional, List
from project.utils.diamond import Diamond


def get_diamonds(how: Optional[int]) -> List[Diamond]:
    assets_folder = os.path.join(os.getcwd(), 'assets')
    csv_file_path = os.path.join(assets_folder, 'diamonds.csv')

    diamonds = []

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        row_count = 0

        for row in csv_reader:
            row_count += 1
            # Create a Diamond object
            diamond_example = Diamond(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10])

            # Append the Diamond object to the list
            diamonds.append(diamond_example)

            # Break out of the loop if the specified number of rows is reached
            if row_count == how:
                break

    return diamonds
