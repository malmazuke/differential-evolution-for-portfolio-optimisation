'''
Created on Aug 15, 2013

@author: markfeaver
'''

def average_daily_return(csv_file):
    """ Calculate the Average Daily Return for given year's worth of data, for all companies. Assumes more than 1 day of data.
     
    Keyword arguments:
    csv_file -- a csv file of values from the DowJonesIndustrialAverage, where the first row are the company names, 
        the first column are the dates (days), the second column is the DJIA, and all other rows are the prices for individual companies      
    """
    
    # These both include the DJIA itself
    names = []
    av_daily_returns = []
    prices_yesterday = []
    
    f = open(csv_file, 'r')

    # Read in the header names
    line = f.readline()
    parts = line.split(',')
    for x in xrange(1, len(parts)):
        names.append(parts[x]) # Skipping the first column, which contains dates
        
    # Read in first day
    for line in f.xreadlines():
        parts = line.strip().split(',')
        for x in xrange(1, len(parts)):
            av_daily_returns.append(0.0)
            prices_yesterday.append(float(parts[x]))
    
    # Read in the rest of the data, updating as we go
    for line in f.xreadlines():
        parts = line.strip().split(',')
        for x in xrange(1, len(parts)):
            # Calculate the return
            price_today = float(parts[x])
            price_yesterday = prices_yesterday[x-1]
            av_daily_returns[x-1] = (price_today)/price_yesterday - 1
            # Update yesterdays prices
    f.close()

if __name__ == '__main__':
    pass