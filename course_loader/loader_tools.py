#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/NeuralNine/crypto-analysis/blob/master/crypto_correlation.py
import pandas_datareader as web
import datetime as dt


class ExchangeRateLoader:

    def __init__(self,
                 start=dt.datetime(2018, 1, 1),
                 end=dt.datetime(2018, 2, 1),
                 tickers=['^GSPC']):  # by default S&P 500
        self.start = start
        self.end = end
        self.tickers = tickers
        self.table_for_every_tickers = self._make_table_for_every_tickers()
        self.combined_table = None

    def _make_table_for_every_tickers(self):
        """download all data about tickers from yahoo"""
        ticker_course_dict = dict.fromkeys(self.tickers)
        for ticker in self.tickers:
            ticker_course_dict[ticker] = web.DataReader(ticker, "yahoo", self.start, self.end)
        return ticker_course_dict

    def make_combined_table(self, metric='Close'):
        """download and make summary table for all tickers
        metric can Close(default), High, Low, Open"""
        colnames = []
        combined = None

        for ticker in self.tickers:
            data = self.table_for_every_tickers[ticker]
            if not combined:
                combined = data[[metric]].copy()
                colnames.append(ticker)
                combined.columns = colnames
            else:
                combined = combined.join(data[metric])
                colnames.append(ticker)
                combined.columns = colnames

        self.combined_table = combined
        return combined


# let's check
if __name__ == '__main__':
    crypto_names = ['BTC', 'ETH', 'USDT', 'LTC', 'XRP', 'DASH', 'SC']
    crypto_tickers = list(map(lambda x: x + '-USD', crypto_names))

    market_index_tickers =['^GSPC', '^DJI'] # ^DJI - Index Dow Jones.S&P500 [https://ffin.ru/market/directory/indexes/]

    start_band = dt.datetime(2016, 1, 1)
    end_band = dt.datetime(2022, 1, 1)

    cryptos = ExchangeRateLoader(start_band, end_band, crypto_tickers)
    markets = ExchangeRateLoader(start_band, end_band, market_index_tickers)

    print(cryptos.table_for_every_tickers[crypto_tickers[0]])
    print(markets.table_for_every_tickers[market_index_tickers[0]])
