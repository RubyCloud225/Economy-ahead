import wbgapi as wb

class GDPDataCollector:
    def __init__(self, economy, start_year, end_year):
        """
        Initialize the GDP data collector.
        : params countries: List of country codes
        : params start_year: Start year of the data
        : params end_year: End year of the data
        """
        self.economies = economy
        self.start_year = start_year
        self.end_year = end_year
        self.indicator = 'NY.GDP.MKTP.CD'
        self.gdp_data = None

    def fetch_data(self):
        """Fetch GPD Data from the world bank API. """
        try:
            self.gdp_data = wb.data.DataFrame(
            self.indicator,
            economy=self.economies,
            time = range(self.start_year, self.end_year + 1),
            numericTimeKeys=True,
            db=2
            )
            if self.gdp_data.empty:
                print("No data returned for specified countries")
            else:
                print(self.gdp_data)
        except KeyError as e:
            print(f"Error fetching data: {e}")
            print("Check the country codes and indicator")
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def process_data(self):
        """Process the data by converting it to a pandas DataFrame. """
        if self.gdp_data is not None:
            self.gdp_data.reset_index(inplace=True)
            self.gdp_data.sort_values(by=['economy'], inplace=True)
        else:
            raise ValueError("No data avaliable. Please call the api first.")
    def display_data(self):
        """Display the data. """
        if self.gdp_data is not None:
            print(self.gdp_data)
        else:
            raise ValueError("No Data available.Please fetch and process data ")
    def save_to_csv(self, filename):
        """Save the data to a csv file. """
        if self.gdp_data is not None:
            self.gdp_data.to_csv(filename, index=False)
        else:
            raise ValueError("No Data available. Please fetch and process data ")


