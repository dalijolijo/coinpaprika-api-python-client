import json

from coinpaprika.client import Client


def main():
    client = Client()

    # List coins
    client.coins()

    # Get today OHLC (can change every each request until actual close of the day at 23:59:59)
    # print(client.today("btx-bitcore"))

    # Get ticker information for a specific coin (USD,BTC,ETH)
    # print(client.ticker("btx-bitcore"))

    # Get markets by exchange ID (USD,BTC,ETH,PLN) with quotes USD
    # print(client.exchange_markets("binance", quotes="EUR"))

    # Price converter
    #print(client.price_converter(base_currency_id="btx-bitcore", quote_currency_id="usd-us-dollars", amount=1))
    # print(client.price_converter(base_currency_id="btx-bitcore", quote_currency_id="eur-euro", amount=1))

    # print(client.price_converter(base_currency_id="usd-us-dollars", quote_currency_id="btx-bitcore", amount=8.99))
    # print(client.price_converter(base_currency_id="usd-us-dollars", quote_currency_id="eur-euro", amount=8.99))

    # BTX price USD
    json_dict_usd = client.price_converter(base_currency_id="btx-bitcore", quote_currency_id="usd-us-dollars", amount=1)
    print("USD price for 1 BTX : $" + str(json_dict_usd["price"]).replace('.', ','))

    # BTX price USD
    json_dict_eur = client.price_converter(base_currency_id="btx-bitcore", quote_currency_id="eur-euro", amount=1)
    print("EUR price for 1 BTX : " + str(json_dict_eur["price"]).replace('.', ',') + " EUR")
    print()
    print(str(json_dict_usd["price"]).replace('.', ','))
    print(str(json_dict_eur["price"]).replace('.', ','))
    print()

    # Package price for easyONE Started
    easy_one_dollar_price = "8.5"
    json_dict_easy_one_eur = client.price_converter(base_currency_id="usd-us-dollars", quote_currency_id="eur-euro", amount=easy_one_dollar_price)
    json_dict_easy_one_btx = client.price_converter(base_currency_id="usd-us-dollars", quote_currency_id="btx-bitcore", amount=easy_one_dollar_price)
    print("USD price for easyONE Started : $" + easy_one_dollar_price)
    print("EUR price for easyONE Started : " + str(json_dict_easy_one_eur["price"]).replace('.', ',') + " EUR")
    print("BTX price for easyONE Started : " + str(json_dict_easy_one_btx["price"]).replace('.',',') + " BTX")
    print()

    # Package price for easyONE Enthusiast
    easy_one_special_dollar_price = "9.5"
    json_dict_easy_two_btx = client.price_converter(base_currency_id="usd-us-dollars", quote_currency_id="btx-bitcore", amount=easy_one_special_dollar_price)
    json_dict_easy_two_eur = client.price_converter(base_currency_id="usd-us-dollars", quote_currency_id="eur-euro", amount=easy_one_special_dollar_price)
    print("USD price for easyONE Enthusiast : $" + easy_one_special_dollar_price)
    print("EUR price for easyONE Enthusiast : " + str(json_dict_easy_two_eur["price"]).replace('.',',') + " EUR")
    print("BTX price for easyONE Enthusiast : " + str(json_dict_easy_two_btx["price"]).replace('.',',') + " BTX")
    print()


if __name__ == "__main__":
    while (True):

        print("---------------------------------------------------------")
        x = input("Press 'Enter' to get the last rates for BTX...\nType 'exit' to exit the program.")
        print("---------------------------------------------------------")
        if x == 'exit':
            quit(0)
        else:
            main()
