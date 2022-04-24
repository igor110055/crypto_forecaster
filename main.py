#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime as dt
from course_loader.loader_tools import CryproTicker, IndexTicker, ExchangeRateLoader


def main():
    inndex_tickers = IndexTicker()
    crypto_tickers = CryproTicker()

    cryptos = ExchangeRateLoader(dt.datetime(2018, 1, 1), dt.datetime(2019, 1, 1), crypto_tickers.tickers)
    indexes = ExchangeRateLoader(dt.datetime(2018, 1, 1), dt.datetime(2019, 1, 1), inndex_tickers.tickers)
    print(cryptos.make_combined_table())
    print(indexes.make_combined_table())

    print(cryptos.table_for_every_tickers())
    print(indexes.table_for_every_tickers())
    print('1')

if __name__ == "__main__":
    main()
