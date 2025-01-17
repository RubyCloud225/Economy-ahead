import wbgapi as wb

class TradeDataCollector:
    def __init__(self, economies, start_year, end_year):
        self.indicator = {
            'BN.GSR.MRCH.CD'
        }
        self.economies = economies
        self.start_year = start_year
        self.end_year = end_year
        self.trade_data = None

    def get_trade_data(self):
        self.trade_data = wb.data.DataFrame(
            self.indicator,
            economy=self.economies,
            time = range(self.start_year, self.end_year + 1),
            numericTimeKeys=True,
            db=2 
        )
        try:
            if self.trade_data.empty:
                print("No data returned for specified countries")
            else:
                print(self.trade_data)
        except KeyError as e:
            print(f"Error fetching data: {e}")
            print("Check the country codes and indicator")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_trade_data_to_csv(self, filename):
        """Save the data to a csv file. """
        if self.trade_data is not None:
            self.trade_data.to_csv(filename, index=False)
        else:
            raise ValueError("No Data available. Please fetch and process data ")

    def display_trade_data(self):
        """Display the data. """
        if self.trade_data is not None:
            print(self.trade_data)
        else:
            raise ValueError("No Data available.Please fetch and process data ")