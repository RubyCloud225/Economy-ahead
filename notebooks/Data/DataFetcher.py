import wbgapi as wb

class DataFetcher:
    def __init__(self, economy, start_year, end_year, indicator):
        """
        Initalize the EmploymentDataFetcher class.
        : params countries: List of countries to fetch employment data for.
        : params start_year: Start year of the data range.
        : params end_year: End year of the data range.
        """
        self.economies = economy
        self.start_year = start_year
        self.end_year = end_year
        self.indicator = indicator
        self.data = None
    
    def fetch_data(self):
        """Fetch Employment Data from the world Bank API"""
        try:
            self.data = wb.data.DataFrame(
                self.indicator,
                economy=self.economies,
                time = range(self.start_year, self.end_year + 1),
                numericTimeKeys = True,
                db=2
            )
            if self.data.empty:
                print("No data returned for specified countries")
            else:
                print(self.data)
        except KeyError as e:
            print(f"Error fetching data: {e}")
            print("Check the country codes and indicator")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def process_data(self):
        """Process the data"""
        if self.data is not None:
            self.data.reset_index(inplace=True)
            self.data.sort_values(by=['economy'], inplace=True)
        else:
            raise ValueError("No data avaliable. Please call API first")
    
    def display_data(self):
        """Display the data"""
        if self.data is not None:
            print(self.data)
        else:
            raise ValueError("No data avaliable. Please fetch and process first")
    
    def save_to_csv(self, filename):
        """Save the employment data to a CSV file"""
        if self.data is not None:
            self.data.to_csv(filename, index=False)
        else:
            raise ValueError("No data avaliable. Please fetch and process first")