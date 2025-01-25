import pandas as pd

class EconimicGrowth:
    def __init__(self, alpha=0.3):
        self.alpha = alpha
        self.data = None
    
    def load_data(self, filename):
        self.data = pd.read_csv(filename)
    
    def get_data_for_year(self, year):
        """
        Get GDP labor and capital data
        : param year: 
        : return, A dictionary with GDP, labor, and capital data
        """
        if self.data is None:
            raise ValueError("No data loaded")
        year_data = self.data[self.data['year'] == year]
        if year_data.empty:
            raise ValueError(f"No data found for the year {year}.")
        
        return {
            'GDP': year_data['GDP'].values[0],
            'Labor': year_data['Labor'].values[0],
            'Capital': year_data['Capital'].values[0]
        }
    
    def calculate_gdp_growth(self, gdp_current, gdp_previous):
        if gdp_previous == 0:
            raise ValueError("previous GDP cannot be zero")
        gdp_growth = ((gdp_current - gdp_previous) / gdp_previous) * 100
        return gdp_growth
    
    def calculate_growth_accounting(self, gdp_current, gdp_previous, labor_current, labor_previous, capital_current, capital_previous):
        """
        using the Cobb-Double production function
        return: growth contributsion from labor and capital
        """
        labor_growth=(labor_current - labor_previous) / labor_previous if labor_previous != 0 else 0
        capital_growth=(capital_current - capital_previous) / capital_previous if capital_previous != 0 else 0
        gdp_growth = self.calculate_gdp_growth(gdp_current, gdp_previous) / 100

        labor_contribution = (1 - self.alpha) * labor_growth
        capital_contribution = self.alpha * capital_growth
        total_contribution = labor_contribution + capital_contribution

        return {
            'labor_contribution': labor_contribution,
            'capital_contribution': capital_contribution,
            'total_contribution': total_contribution,
            'gdp_growth': gdp_growth
        }