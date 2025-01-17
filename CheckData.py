import wbgapi as wb

class WorldBankDataChecker:
    def __init__(self, search_term):
        self.search_term = search_term
        self.databases = None

    def list_available_indicators(self):
        """List available indicators in the World Bank database."""
        series = wb.series.list()
        for series in series:
            print(series)
    
    def list_available_databases(self):
        """List available databases in the World Bank API."""
        databases = wb.search(self.search_term)
        print(databases)

    def save_as_csv(self):
        """Save the data as a CSV file."""
        if self.databases is None:
            print(self.databases)
        else:
            raise ValueError("No Data available.Please fetch and process data ")

# Example usage
if __name__ == "__main__":
    checker = WorldBankDataChecker()
    
    # List available indicators
    checker.list_available_indicators()
    # List available databases
    checker.list_available_databases()