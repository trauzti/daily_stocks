"""Simple program to fetch recent stock data from yahoo and print out
   daily changes"""
import argparse
from datetime import datetime, timedelta
import pandas_datareader.data as wb
import pandas as pd

pd.set_option('display.max_rows', 500)

def parse_cmdline():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--days", help="number of history days", type=int,
                        default=30)
    parser.add_argument("-s", "--stocks", help="stocks to fetch, comma separated",
                        type=str, default="VOO,SLV,GLD")

    args = parser.parse_args()
    days = args.days
    stocklist = args.stocks.split(",")
    return days, stocklist

def get_daily_pct():
    """Fetch stock data and calculate daily percentage changes."""
    days, stocklist = parse_cmdline()
    today = datetime.today()
    start_day = today - timedelta(days=days)

    data = wb.DataReader(stocklist, 'yahoo', start_day, today)

    adjclose = data['Adj Close']
    daily_pct = 100.0 * adjclose.diff() / adjclose

    return daily_pct

def main():
    daily_pct = get_daily_pct()
    print daily_pct

if __name__ == "__main__":
    main()
