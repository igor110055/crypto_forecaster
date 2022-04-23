# https://github.com/NeuralNine/crypto-analysis/blob/master/crypto_correlation.py
import pandas_datareader as web
import datetime as dt


class CourseLoader:

    def __init__(self, start=dt.datetime(2018, 1, 1), end=dt.datetime(2018, 2, 1), \
                 tickers=['^GSPC']):  # by default S&P 500
        self.start = start
        self.end = end
        self.tickers = tickers
        self.table_for_every_tickers = self._make_table_for_every_tickers()

    def _make_table_for_every_tickers(self):
        """download all data about tickers from yahoo"""
        tiker_course_dict = dict.fromkeys(self.tickers)
        for ticker in self.tickers:
            tiker_course_dict[ticker] = web.DataReader(ticker, "yahoo", self.start, self.end)
        return tiker_course_dict

    def make_combined_table(self, metric='Close'):
        """download and make summary table for all tickers
        metric can Close(default), High, Low, Open"""
        colnames = []
        first = True

        for ticker in self.tickers:
            data = web.DataReader(ticker, "yahoo", self.start, self.end)
            if first:
                combined = data[[metric]].copy()
                colnames.append(ticker)
                combined.columns = colnames
                first = False
            else:
                combined = combined.join(data[metric])
                colnames.append(ticker)
                combined.columns = colnames

        self.combined_table = combined
        return combined
