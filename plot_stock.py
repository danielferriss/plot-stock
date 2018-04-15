import pandas as pd
import matplotlib.pyplot as plt
import quandl
from datetime import datetime
from scipy.stats import pearsonr

quandl.ApiConfig.api_key = "NdyospgCKrp_eo-jRuU7"

data = quandl.get("BSE/BOM539658", collapse="daily", start_date="2017-12-31", end_date="20018-04-08")
data = data[['Close']]
ticker = 'BSE/BOM539874'

#data 
#ticker
#title
def plot(data, ticker, title=""):
	dates = data.index.tolist()
	start_date = dates[0]
	end_date   = dates[len(dates) - 1]
	day_diff = (dates[1] - dates[0]).days

	if day_diff < 7:
		collapse = "daily"
	elif day_diff < 29:
		collapse = "weekly"
	elif day_diff < 60:
		collapse = "monthly"
	elif day_diff < 300:
		collapse = "quarterly"
	else:
		collapse = "annual"

	stock_data = quandl.get(ticker, collapse=collapse, start_date=start_date, end_date=end_date)
	stock_data = stock_data[['Close']]
	r,p = pearsonr(data,stock_data)

	print(r)
	print(p)
	plt.plot(data.index, data[['Close']], stock_data[['Close']])
	plt.show()


plot(data, ticker)

