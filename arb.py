import pmxt
import os

# Initialize exchanges (server starts automatically!)
poly = pmxt.Polymarket()
kalshi = pmxt.Kalshi()
limitless = pmxt.Limitless(
    api_key=os.getenv('LIMITLESS_API_KEY')
)  # Requires API key for authenticated operations

# Search for markets
markets = poly.fetch_markets(query="TRUMP")
print(markets[0].title)
markets = kalshi.fetch_markets(query="TRUMP")
print(markets[0].title)
# Fails below, parsing issue
markets = limitless.fetch_markets(query="TRUMP")
print(markets[0].title)