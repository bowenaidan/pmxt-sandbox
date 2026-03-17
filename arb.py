import pmxt
import os
import re

poly = pmxt.Polymarket()
kalshi = pmxt.Kalshi()
limitless = pmxt.Limitless(api_key=os.getenv('LIMITLESS_API_KEY'))
QUERY = "FED CHAIR"
STOP_WORDS = {"will", "the", "a", "an", "in", "by", "to", "of", "be", "as", "at", "or", "and", "is"}

def tokenize(title):
    tokens = re.sub(r"[^a-z0-9 ]", "", title.lower()).split()
    return set(t for t in tokens if t not in STOP_WORDS)

# Jaccard index: |A ∩ B| / |A ∪ B|
def similarity(a, b):
    ta, tb = tokenize(a), tokenize(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)

def match_markets(all_markets, threshold=0.8):
    '''Group markets from different exchanges that refer to the same event.'''
    exchange_names = list(all_markets)
    groups = []
    for i in range(len(exchange_names)):
        for j in range(i + 1, len(exchange_names)):
            ex_a, ex_b = exchange_names[i], exchange_names[j]
            for m_a in all_markets[ex_a]:
                for m_b in all_markets[ex_b]:
                    similarity_score = similarity(m_a.title, m_b.title)
                    if similarity_score >= threshold:
                        groups.append({ex_a: m_a, ex_b: m_b, "similarity_score": similarity_score})
    return groups

all_markets = {
    "Polymarket": poly.fetch_markets(query=QUERY),
    "Kalshi":     kalshi.fetch_markets(query=QUERY),
    "Limitless":  limitless.fetch_markets(query=QUERY, limit=100),
}

groups = match_markets(all_markets)
for group in groups:
    print("--- Match ---")
    for exchange, market in group.items():
        if exchange == "similarity_score":
            continue
        yes = getattr(market, "yes", None)
        print(f"  [{exchange}] {market.title} @ {yes.price if yes else '?'}")
    print(f"  Similarity: {group['similarity_score']:.2f}")