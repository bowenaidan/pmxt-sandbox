import pmxt
import os

# Initialize exchanges (server starts automatically!)
poly = pmxt.Polymarket()
kalshi = pmxt.Kalshi()
limitless = pmxt.Limitless(
    api_key=os.getenv('LIMITLESS_API_KEY')
)  # Requires API key for authenticated operations

def print_market(markets_list):
    for i, market in enumerate(markets_list[:10]):
        print(i, market.title)
        print("  candidate:", getattr(market, "yes", None).label)
        print("  market_id:", getattr(market, "market_id", None))
        print("  price:", getattr(market, "yes", None).price)
        print("  type:", type(market))

# Search for markets
markets = poly.fetch_markets(query="FED CHAIR")
print_market(markets[:10])
markets = kalshi.fetch_markets(query="FED CHAIR")
print_market(markets[:10])

# Fails below, parsing issue
# markets = limitless.fetch_markets(query="TRUMP")
# print(markets[0].title)