'''
Created on Aug 16, 2013

@author: Mark Feaver
@summary: Tests our model generated from 2011 against the 2012 DJIA data
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
    # Read in our Portfolio for optimising 2011 Average Daily Returns
    prev_data = read_prev_data("../../data/fittest_av_daily_returns_2011.csv")
    fitness = prev_data[0]
    model = prev_data[1]
    
    # Read in the 2012 Average Daily Return data  
    curr_data = read_curr_data("../../data/av_daily_returns_2012.csv")
    av_return_2012_dj = curr_data[0]
    av_return_2012 = curr_data[1]
    
    predictions = []
    
    for x in xrange(len(model)):
        predictions.append(model[x] * av_return_2012[x])
        
    print predictions
    