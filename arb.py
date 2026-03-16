import pmxt
import os

poly = pmxt.Polymarket()
kalshi = pmxt.Kalshi()
limitless = pmxt.Limitless(api_key=os.getenv('LIMITLESS_API_KEY'))

def print_market(markets_list):
    for i, market in enumerate(markets_list[:10]):
        yes = getattr(market, "yes", None)
        print(i, market.title)
        print("  candidate:", yes.label)
        print("  market_id:", getattr(market, "market_id", None))
        print("  price:", yes.price if yes else None)
        print("  type:", type(market))

markets = poly.fetch_markets(query="FED CHAIR")
print_market(markets)
markets = kalshi.fetch_markets(query="FED CHAIR")
print_market(markets)
markets = limitless.fetch_markets(query="FED CHAIR", limit=100)
print_market(markets)