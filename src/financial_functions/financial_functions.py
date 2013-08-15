'''
Created on Aug 15, 2013

@author: markfeaver
'''

def average_daily_return(in_csv_file, out_csv_file=""):
    """ Calculate the Average Daily Return for given year's worth of data, for all companies. Assumes more than 1 day of data.
     
    Keyword arguments:
    csv_file -- a csv file of values from the DowJonesIndustrialAverage, where the first row are the company names, 
        the first column are the dates (days), the second column is the DJIA, and all other rows are the prices for individual companies      
    """
    
    # These all include the DJ index itself
    names = []
    av_daily_returns = []
    prices_yesterday = []
    year = ""
    
    num_averages = 0
    
    f = open(in_csv_file, 'r')

    # Read in the header names
    line = f.readline()
    parts = line.strip().split(',')
    for x in xrange(1, len(parts)):
        names.append(parts[x]) # Skipping the first column, which contains dates
        
    # Read in first day
    line = f.readline()
    parts = line.strip().split(',')
    for x in xrange(0, len(parts)):
        if x == 0:
            date = parts[x].split('-')
            year = date[0] + '"'
            continue
        av_daily_returns.append(0.0)
        prices_yesterday.append(float(parts[x]))
    
    # Read in the rest of the data, updating as we go
    for line in f.xreadlines():
        parts = line.strip().split(',')
        for x in xrange(1, len(parts)):
            # Calculate the return
            price_today = float(parts[x])
            price_yesterday = prices_yesterday[x-1]
            av_daily_returns[x-1] += price_today/price_yesterday - 1
            # Update yesterdays prices
            prices_yesterday[x-1] = price_today
        num_averages += 1
    
    out_names = ""
    # Write the names out (not the most efficient. Oh well)
    for x in xrange(len(names) + 1):
        if x == 0:
            out_names += '"",'
            continue
        elif x == len(names):
            out_names += names[x-1]
        else:
            out_names += names[x-1] + ','
        
    out_returns = ""
    # For each index, calculate the average daily return for the entire time period
    for x in xrange(len(av_daily_returns) + 1):
        # If it's the first column, write the year
        if x == 0:
            out_returns += year + ','
            continue
        
        daily_return = "%.2f%%" % (av_daily_returns[x-1]/float(num_averages)*100)
        if x == len(names):
            out_returns += daily_return
        else:
            out_returns += daily_return + ','
    
    f.close()
    
    # If we have an output file, write to this
    if out_csv_file is not "":
        f_out = open(out_csv_file, 'w')
        f_out.write(out_names + "\n")
        f_out.write(out_returns)
        f_out.close()
    
    # Print to std out
    print(out_names)
    print(out_returns)

if __name__ == '__main__':
    print "Average daily returns 2011:"
    average_daily_return("../../data/dji.2011.csv", "../../data/av_daily_returns_2011.csv")
    print "Average daily returns 2012:" 
    average_daily_return("../../data/dji.2012.csv", "../../data/av_daily_returns_2012.csv")
    print "Volatility 2011:"
    