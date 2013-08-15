'''
Created on Aug 15, 2013

@author: markfeaver
'''
class Component:
    """ A component/company in the Dow Jones """
    
    _name = ""
    _prices = []
    _returns = []
    _av_daily_return = 0.0
    
    def __init__(self, name):
        self._name = name
        self._prices = []
        self._returns = []
    
    def add_price(self, price):
        """ Add the price """
        self._prices.append(price)
        
    def calc_daily_returns(self):
        self._returns = []
        for x in xrange(1, len(self._prices)):
            price_today = self._prices[x]
            price_yesterday = self._prices[x-1]
            daily_return = price_today/price_yesterday - 1
            self._returns.append(daily_return)
        return self._returns
    
    def calc_av_daily_return(self):
        """ Calculate the average daily return, returning a float. Assumes that the daily returns have already been calculated"""
        av_return = 0.0
        total_ret = sum(self._returns)
        num_averages = len(self._returns)
        
        if num_averages > 0:
            av_return = total_ret/float(num_averages)
        
        self._av_daily_return = av_return
        return av_return
    
    def get_av_daily_return(self):
        return self._av_daily_return
    
    def get_name(self):
        return self._name
    
    def __str__(self):
        out = "(" + self._name
        if self._av_daily_return != 0.0:
            out += ", %.4f%%" % self._av_daily_return
        out += ")" 
        return out
    
    def __repr__(self):
        return self.__str__()

def read_data(in_csv_file):
    components = []
    f = open(in_csv_file, 'r')
    
    # Read in the header names
    line = f.readline()
    parts = line.strip().split(',')
    for x in xrange(1, len(parts)):
        components.append(Component(parts[x])) # Skipping the first column, which contains dates
        
    # Read in the rest of the data
    for line in f.xreadlines():
        parts = line.strip().split(',')
        for x in xrange(1, len(parts)):
            price = float(parts[x])
            components[x-1].add_price(price)
    
    f.close()
    return components
    
if __name__ == '__main__':
    components = read_data("../../data/dji.2011.csv")
    
    for comp in components:
        comp.calc_daily_returns()
        comp.calc_av_daily_return()
        
    print "Average daily returns 2011:"
    # Very inefficient way of outputting data
    out_names = '"",'
    out_returns = '"2011",'
    for x in xrange(len(components)):
        comp = components[x]
        if x == len(components):
            out_names += "%s" % comp.get_name()
            out_returns += "%.2f%%" % (comp.get_av_daily_return() * 100.0)
        else:
            out_names += "%s," % comp.get_name()
            out_returns += "%.2f%%," % (comp.get_av_daily_return() * 100.0)
    
    print out_names
    print out_returns
    
    fw = open("../../data/av_daily_returns_2011.csv", 'w')
    fw.write(out_names + "\n")
    fw.write(out_returns)
    fw.close()
#     print "Average daily returns 2011:"
#     average_daily_return("../../data/dji.2011.csv", "../../data/av_daily_returns_2011.csv")
#     print "Average daily returns 2012:" 
#     average_daily_return("../../data/dji.2012.csv", "../../data/av_daily_returns_2012.csv")
#     print "Volatility 2011:"
    