
#https://github.com/NeuralNine/crypto-analysis/blob/master/crypto_correlation.py
import pandas_datareader as web
#import mplfinance as mpf
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

class CryproLoader:

    currency = "USD"
    metric = "Close"
    crypto = ['BTC', 'ETH', 'USDT', 'LTC', 'XRP', 'DASH', 'SC']

    def __init__(self, start=dt.datetime(2018, 1, 1), end=dt.datetime(2018, 2, 1)):
        self.start = start
        self.end = end

    def load(self):
        colnames = []
        first = True

        for ticker in self.crypto:
            data = web.DataReader(f"{ticker}-{self.currency}", "yahoo", self.start, self.end)
            if first:
                combined = data[[self.metric]].copy()
                colnames.append(ticker)
                combined.columns = colnames
                first = False
            else:
                combined = combined.join(data[self.metric])
                colnames.append(ticker)
                combined.columns = colnames

        self.crypto_course = combined
        return combined

def main():
    cryptos = CryproLoader()
    print(cryptos.load())


if __name__ == "__main__":
    main()
# # currency = "USD"
# # metric = "Close"
#
# start = dt.datetime(2018,1,1)
# #end = dt.datetime.now()
# end = dt.datetime(2018,2,1)
#
# crypto = ['BTC', 'ETH', 'USDT', 'LTC', 'XRP', 'DASH', 'SC']
# colnames = []
#
# first = True
#
# for ticker in crypto:
#     data = web.DataReader(f"{ticker}-{currency}", "yahoo", start, end)
#     if first:
#         combined = data[[metric]].copy()
#         colnames.append(ticker)
#         combined.columns = colnames
#         first = False
#     else:
#         combined = combined.join(data[metric])
#         colnames.append(ticker)
#         combined.columns = colnames

plt.yscale('log') # first show linear

for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper right")

plt.show()

# # Correlation Heat Map

print(combined)

combined = combined.pct_change().corr(method='pearson')

sns.heatmap(combined, annot=True, cmap="coolwarm")
plt.show()