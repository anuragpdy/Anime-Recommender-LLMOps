import pandas as pd
from typing import Set

class AnimeDataProcessor:
    """Handles loading and processing of the anime dataset."""

    def __init__(self, raw_csv_path: str, processed_csv_path: str):
        self.raw_csv_path = raw_csv_path
        self.processed_csv_path = processed_csv_path

    def process(self) -> str:
        """
        Loads the raw CSV, cleans and combines relevant columns,
        and saves the result to a new CSV.
        """
        df = pd.read_csv(self.raw_csv_path, encoding='utf-8', on_bad_lines='skip').dropna()

        required_cols: Set[str] = {'Name', 'Genres', 'sypnopsis'}
        missing_cols = required_cols - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns in CSV file: {', '.join(missing_cols)}")

        df['combined_info'] = (
            "Title: " + df["Name"] + "; " +
            "Synopsis: " + df["sypnopsis"] + "; " +
            "Genres: " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv_path, index=False, encoding='utf-8')
        return self.processed_csv_path