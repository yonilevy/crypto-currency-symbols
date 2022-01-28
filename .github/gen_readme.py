import json


def gen_readme(symbols):
    rows = [f"| {s['name']} | {s['gecko']} | {s['symbol']} | {s['usym']} |" for s in symbols]
    return """
# Crypto Currency Symbols

> DO NOT EDIT. THIS README IS AUTO GENERATED FROM [symbols.json](symbols.json).

Unicode symbols for different crypto tokens.

* Collected for a MacOS [ticker app](http://yoni.ninja/cointick)
* **Not official in any way**
* Feel free to PR / create issues with suggestions

| Name | CoinGecko id | Symbol | Unicode Symbol |
|------|:------------:|:------:|:--------------:|
""" + "\n".join(rows)


def main():
    print("Generating README from symbols.json...")
    symbols = json.load(open("symbols.json", "r"))
    with open("README.md", "w") as f:
        f.write(gen_readme(symbols))


if __name__ == '__main__':
    main()
