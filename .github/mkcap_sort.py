import requests
import json


def main():
    """
    Sorts symbols.json by (market_cap_if_in_top_250, alphabetically)
    """
    symbols = json.load(open("symbols.json", "r"))
    coins = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=250").json()
    sym_to_index = {c['symbol'].upper(): c['market_cap_rank'] for c in coins}
    sorted_symbols = sorted(symbols, key=lambda s: (sym_to_index.get(s['symbol'], 999), s['name']))
    json.dump(sorted_symbols, open("symbols.json", "w"), indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
