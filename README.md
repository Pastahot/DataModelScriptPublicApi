# DataModelScriptPublicApi
## Import Libraries
The script begins by importing the necessary libraries:
- `requests` for making HTTP requests to the CoinGecko API,
- `pandas` for data manipulation and analysis,
- `datetime` for handling dates and times, although `datetime` is not used in the script.

## Define the `fetch_crypto_data` Function

### Parameters
The function accepts four parameters:
- `crypto_id` (default `'ethereum'`): Specifies the cryptocurrency ID for which data is fetched.
- `vs_currency` (default `'usd'`): Sets the currency against which the cryptocurrency's price is compared.
- `days` (default `'max'`): Determines the time span of historical data to fetch (e.g., `'max'` for all available historical data).
- `interval` (default `'daily'`): Sets the granularity of the price data (e.g., `'daily'` for daily prices).

### Fetching Data
- Constructs a request URL using these parameters and sends an HTTP GET request to the CoinGecko API.

### Extract and Process Data
- The response, assumed to be in JSON format containing price data, is processed to extract prices. These prices are then converted into a pandas DataFrame with columns for timestamp (converted to a human-readable date) and price.

### Return Data
- The DataFrame is returned, now containing only the date and price columns, with the original timestamp column removed.

## Fetch Ethereum Data
- By calling `fetch_crypto_data()` without any arguments, the function uses its default parameters to fetch historical price data for Ethereum in USD over its entire available history, at daily intervals.

## Save Data to CSV
- The retrieved DataFrame is then saved to a CSV file named `ethereum_historical_prices.csv`, with no index column.
