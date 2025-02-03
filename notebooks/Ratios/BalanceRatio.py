import pandas as pd
from Data.DataFetcher import DataFetcher

class BalanceRatio:
    def __init__(self, economies, start_year, end_year, indicators):
        self.data_fetcher = DataFetcher(economies, start_year, end_year, indicators)
        self.data = None

    def fetch_data(self):
        self.data = self.data_fetcher.fetch_data()
        return self.data_fetcher.data
    
    def calculate_balance_ratio(self):
        if self.data is None:
            return ValueError("data not loaded")
        
        if len(self.data_fetcher.indicators) == 2:
            revenue_col = self.data_fetcher.indicators[0]
            expense_col = self.data_fetcher.indicators[1]
        else:
            raise ValueError("Only two indicators are supported for balance ratio calculation")
        self.data['Balance_ratio'] = self.data.apply(
            lambda row: row[revenue_col] / row[expense_col] if row[expense_col] != 0 else None,
            axis=1
        )
        return self.data
    
    def display_results(self):
        if self.data is None:
            return ValueError("data not loaded")
        print(self.data)