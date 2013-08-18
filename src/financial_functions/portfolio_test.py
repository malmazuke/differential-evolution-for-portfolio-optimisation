'''
Created on Aug 16, 2013

@author: Mark Feaver
@summary: Tests our model generated from 2011 against the 2012 DJIA data
@note: This entire class is a big mess - too much copypasta!
'''

def read_prev_data(csv_file):
    f = open(csv_file, 'r')
    
    line = f.readline().strip().split(',')
    
    fitness = float(line[0])
    model = []
    for x in xrange(1, len(line)):
        model.append(float(line[x]))
    
    f.close()
    
    return (fitness, model)

def read_curr_data(csv_file):
    f = open(csv_file, 'r')
    
    f.readline()
    line = f.readline().strip().split(',')
    
    djia = float(line[0])
    vals = []
    for x in xrange(1,len(line)):
        vals.append(float(line[x]))

    f.close()
    
    return (djia, vals)

if __name__ == '__main__':
    
                        ### AVERAGE DAILY RETURNS DATA ###
    print "### Average Daily Returns data ###"
                                ### Portfolio 1 ###
    print "\n### Portfolio 1 ###"
    # Read in our Portfolio for optimising 2011 Average Daily Returns
    prev_data = read_prev_data("../../data/fittest_av_daily_returns_2011.csv")
    fitness = prev_data[0]
    model = prev_data[1]
    
    # Read in the 2011 Average Daily Return data  
    curr_data = read_curr_data("../../data/av_daily_returns_2011.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2011 Average Daily Return using Portfolio 1:\n" + str(sum_predictions * 100)+"%"
    print "2011 Relative Return using Portfolio 1:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
    # Read in the 2012 Average Daily Return data  
    curr_data = read_curr_data("../../data/av_daily_returns_2012.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2012 Average Daily Return using Portfolio 1:\n" + str(sum_predictions * 100)+"%"
    print "2012 Relative Return using Portfolio 1:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
                                    ### Portfolio 2 ###
    print "\n### Portfolio 2 ###"
    # Read in our Portfolio for optimising 2011 Volatility
    prev_data = read_prev_data("../../data/fittest_volatility_2011.csv")
    fitness = prev_data[0]
    model = prev_data[1]
    
    # Read in the 2011 Average Daily Return data  
    curr_data = read_curr_data("../../data/av_daily_returns_2011.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2011 Average Daily Return using Portfolio 2:\n" + str(sum_predictions * 100)+"%"
    print "2011 Relative Return using Portfolio 2:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
    # Read in the 2012 Average Daily Return data  
    curr_data = read_curr_data("../../data/av_daily_returns_2012.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2012 Average Daily Return using Portfolio 2:\n" + str(sum_predictions * 100)+"%"
    print "2012 Relative Return using Portfolio 2:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
                                    ### Portfolio 3 ###
    print "\n### Portfolio 3 ###"
    # Read in our Portfolio 3
    prev_data = read_prev_data("../../data/fittest_ratio_2011.csv")
    fitness = prev_data[0]
    model = prev_data[1]
    
    # Read in the 2011 Average Daily Return data  
    curr_data = read_curr_data("../../data/av_daily_returns_2011.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2011 Average Daily Return using Portfolio 3:\n" + str(sum_predictions * 100)+"%"
    print "2011 Relative Return using Portfolio 3:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
    # Read in the 2012 Average Daily Return data  
    curr_data = read_curr_data("../../data/av_daily_returns_2012.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2012 Average Daily Return using Portfolio 3:\n" + str(sum_predictions * 100)+"%"
    print "2012 Relative Return using Portfolio 3:\n" + str((sum_predictions - av_return_dj) * 100) + "%"    
    
    
    
    
                            ### VOLATILITY DATA ###
    print "\n\n### Volatility data ###"
    
                                    ### Portfolio 1 ###
    print "\n### Portfolio 1 ###"
    # Read in our Portfolio for optimising 2011 Average Daily Returns
    prev_data = read_prev_data("../../data/fittest_av_daily_returns_2011.csv")
    fitness = prev_data[0]
    model = prev_data[1]
    
    # Read in the 2011 Volatility data  
    curr_data = read_curr_data("../../data/volatility_2011.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2011 Volatility using Portfolio 1:\n" + str(sum_predictions * 100)+"%"
    print "2011 Relative Volatility using Portfolio 1:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
    # Read in the 2012 Volatility data  
    curr_data = read_curr_data("../../data/volatility_2012.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2012 Volatility using Portfolio 1:\n" + str(sum_predictions * 100)+"%"
    print "2012 Relative Volatility using Portfolio 1:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
                                    ### Portfolio 2 ###
    print "\n### Portfolio 2 ###"
    # Read in our Portfolio for optimising 2011 Volatility
    prev_data = read_prev_data("../../data/fittest_volatility_2011.csv")
    fitness = prev_data[0]
    model = prev_data[1]
    
    # Read in the 2011 Volatility data  
    curr_data = read_curr_data("../../data/volatility_2011.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2011 Volatility using Portfolio 2:\n" + str(sum_predictions * 100)+"%"
    print "2011 Relative Volatility using Portfolio 2:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
    # Read in the 2012 Volatility data  
    curr_data = read_curr_data("../../data/volatility_2012.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2012 Volatility using Portfolio 2:\n" + str(sum_predictions * 100)+"%"
    print "2012 Relative Volatility using Portfolio 2:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
    
                                    ### Portfolio 3 ###
    print "\n### Portfolio 3 ###"
    # Read in our Portfolio for optimising 2011 Ratio
    prev_data = read_prev_data("../../data/fittest_ratio_2011.csv")
    fitness = prev_data[0]
    model = prev_data[1]
    
    # Read in the 2011 Volatility data  
    curr_data = read_curr_data("../../data/volatility_2011.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2011 Volatility using Portfolio 3:\n" + str(sum_predictions * 100)+"%"
    print "2011 Relative Volatility using Portfolio 3:\n" + str((sum_predictions - av_return_dj) * 100) + "%"
    
    # Read in the 2012 Volatility data  
    curr_data = read_curr_data("../../data/volatility_2012.csv")
    av_return_dj = curr_data[0]
    av_return = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return[x])

    sum_predictions = sum(predictions)
    print "\n2012 Volatility using Portfolio 3:\n" + str(sum_predictions * 100)+"%"
    print "2012 Relative Volatility using Portfolio 3:\n" + str((sum_predictions - av_return_dj) * 100) + "%"