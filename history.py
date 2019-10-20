path = "C:/Users/yperez/Documents/ScikitMLForInvestint/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    
    df = pd.DataFrame(columns= ['Date', 'Unix', 'Ticker', 'DE Ratio'])
    
    sp500_df = pd.read_csv('SP500.csv')
    sp500_df.shape
    #data = []
    for each_dir in stock_list[1:5]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[1]
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'/'+file
                source = open(full_file_path, 'r').read()
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        print(row)


row.shape
import pandas as pd
import os
import time
from datetime import datetime

path = "C:/Users/yperez/Documents/ScikitMLForInvestint/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    
    df = pd.DataFrame(columns= ['Date', 'Unix', 'Ticker', 'DE Ratio'])
    
    sp500_df = pd.read_csv('SP500.csv')
    sp500_df.shape
    #data = []
    for each_dir in stock_list[1:5]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[1]
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'/'+file
                source = open(full_file_path, 'r').read()
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        row.shape


import pandas as pd
import os
import time
from datetime import datetime

path = "C:/Users/yperez/Documents/ScikitMLForInvestint/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    
    df = pd.DataFrame(columns= ['Date', 'Unix', 'Ticker', 'DE Ratio'])
    
    sp500_df = pd.read_csv('SP500.csv')
    sp500_df.shape
    #data = []
    for each_dir in stock_list[1:5]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[1]
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'/'+file
                source = open(full_file_path, 'r').read()
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')


runfile('C:/Users/yperez-pa/.spyder-py3/MLSKLearnForStocks.py', wdir='C:/Users/yperez-pa/.spyder-py3')
clear
runfile('C:/Users/yperez-pa/.spyder-py3/MLSKLearnForStocks.py', wdir='C:/Users/yperez-pa/.spyder-py3')
clear
runfile('C:/Users/yperez-pa/.spyder-py3/MLSKLearnForStocks.py', wdir='C:/Users/yperez-pa/.spyder-py3')