import json

def gen_readme(symbols):
    rows = [f"| {s['name']} | {s['code']} | {s['symbol']} |" for s  in symbols]
    return """
# Crypto Currency Symbols

> DO NOT EDIT. THIS README IS AUTO GENERATED FROM [symbols.json](symbols.json).

Unicode symbols for different crypto tokens.

* Collected for my [ticker app](http://yoni.ninja/cointick)
* **Not official in any way**
* Feel free to PR / create issues with suggestions

| Name            |  Code  | Symbol|
| --------------- |:------:|:-----:|
""" + "\n".join(rows)


def main():
    print("Generating README from symbols.json...")
    symbols = json.load(open("symbols.json", "r"))
    readme = gen_readme(symbols)
    with open("README.md", "w") as f:
        f.write(gen_readme(symbols))


if __name__ == '__main__':
    main()

