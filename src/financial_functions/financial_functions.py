'''
Created on Aug 15, 2013

@author: markfeaver
@summary: A bunch of methods for calculating financial statistics, such as the average daily return, volatility, and alpha/beta values
@requires: The Numpy library
'''

from numpy import array,ones,linalg, std, vstack
# import pylab

year = "2011"

class Component:
    """ A component/company in the Dow Jones """
    
    _name = ""
    _prices = []
    _returns = []
    _av_daily_return = None
    _volatility = None
    _alpha = None
    _beta = None
    
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
    
    def calc_volatility(self):
        """ Simply calculates the standard deviation over the daily returns """
        volatility = std(self._returns)
        self._volatility = volatility
        return volatility
    
    def calc_alpha_beta(self, dow_jones):
        """ Applies linear regression to calculate the alpha and beta values compared to the daily return of the entire sector (i.e. the Dow Jones Industrial Average)"""
        
        x = array(dow_jones.get_returns())
        y = array(self._returns)
        
        A = vstack([x, ones(len(x))]).T
        
        m, c = linalg.lstsq(A, y)[0]
        
#         pylab.plot(x, y, 'o', label='Daily returns', markersize=3)
#         pylab.plot(x, m*x + c, 'r', label='Fitted line')
#         pylab.ylabel(self._name)
#         pylab.xlabel(dow_jones.get_name())
#         pylab.legend()
#         pylab.show()
        
        self._beta = m
        self._alpha = c
    
    def get_name(self):
        return self._name
    
    def get_returns(self):
        return self._returns
    
    def get_av_daily_return(self):
        return self._av_daily_return
    
    def get_volatility(self):
        return self._volatility
    
    def get_alpha(self):
        return self._alpha
    
    def get_beta(self):
        return self._beta
    
    def __str__(self):
        out = "(" + self._name
        if self._av_daily_return is not None:
            out += ", %.4f%%" % self._av_daily_return
        if self._volatility is not None:
            out += ", %.4f%%" % self._volatility
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

def calc_all_daily_returns(components, csv_output=""):
    global year
    for comp in components:
        comp.calc_daily_returns()
        comp.calc_av_daily_return()
        
    print "Average daily returns " + year + ":"
    # Very inefficient way of outputting data
    out_names = '"",'
    out_values = '"2011",'
    for x in xrange(len(components)):
        comp = components[x]
        if x == len(components)-1:
            out_names += "%s" % comp.get_name()
            out_values += "%.4f%%" % (comp.get_av_daily_return() * 100.0)
        else:
            out_names += "%s," % comp.get_name()
            out_values += "%.4f%%," % (comp.get_av_daily_return() * 100.0)
    
    print out_names
    print out_values
    
    if csv_output is not "": 
        fw = open(csv_output, 'w')
        fw.write(out_names + "\n")
        fw.write(out_values)
        fw.close()
    
def calc_all_volatility(components, csv_output=""):
    global year
    for comp in components:
        comp.calc_volatility()
        
    print "\nVolatility (std dev) " + year + ":"
    out_names = '"",'
    out_values = '"2011",'
    for x in xrange(len(components)):
        comp = components[x]
        if x == len(components)-1:
            out_names += "%s" % comp.get_name()
            out_values += "%.4f%%" % (comp.get_volatility() * 100.0)
        else:
            out_names += "%s," % comp.get_name()
            out_values += "%.4f%%," % (comp.get_volatility() * 100.0)
    
    print out_names
    print out_values
    
    if csv_output is not "":
        fw = open(csv_output, 'w')
        fw.write(out_names + "\n")
        fw.write(out_values)
        fw.close()
    
def calc_all_alpha_beta(components, csv_output_alpha="", csv_output_beta=""):
    global year
    """ Calculates and prints/saves the alpha and beta values """
    dow_jones = components[0]
    
    for x in xrange(1, len(components)):
        comp = components[x]
        comp.calc_alpha_beta(dow_jones)
        
    print "\nAlpha values " + year + ":"
    out_names = '"",'
    out_values = '"2011",'
    for x in xrange(1, len(components)):
        comp = components[x]
        if x == len(components)-1:
            out_names += "%s" % comp.get_name()
            out_values += "%.5f%%" % (comp.get_alpha() * 100)
        else:
            out_names += "%s," % comp.get_name()
            out_values += "%.5f%%," % (comp.get_alpha() * 100)
    
    print out_names
    print out_values
    
    if csv_output_alpha is not "":
        fw = open(csv_output_alpha, 'w')
        fw.write(out_names + "\n")
        fw.write(out_values)
        fw.close()
        
    print "\nBeta values " + year + ":"
    out_names = '"",'
    out_values = '"2011",'
    for x in xrange(1, len(components)):
        comp = components[x]
        if x == len(components)-1:
            out_names += "%s" % comp.get_name()
            out_values += "%.5f" % (comp.get_beta())
        else:
            out_names += "%s," % comp.get_name()
            out_values += "%.5f," % (comp.get_beta())
    
    print out_names
    print out_values
    
    if csv_output_beta is not "":
        fw = open(csv_output_beta, 'w')
        fw.write(out_names + "\n")
        fw.write(out_values)
        fw.close()
            
if __name__ == '__main__':
    components = read_data("../../data/dji.2011.csv")
    year = "2011"
    # Calculate the average daily return of each component
    calc_all_daily_returns(components, "../../data/av_daily_returns_2011.csv")
    
    # Calculate the volatility of each component
    calc_all_volatility(components, "../../data/volatility_2011.csv")
    
    # Calculate the alpha and beta values
    calc_all_alpha_beta(components, "../../data/alpha_2011.csv", "../../data/beta_2011.csv")
    
    year = "2012"
    # Do the 2012 data too
    components = read_data("../../data/dji.2012.csv")
    
    # Calculate the average daily return of each component
    calc_all_daily_returns(components, "../../data/av_daily_returns_2012.csv")
    
    # Calculate the volatility of each component
    calc_all_volatility(components, "../../data/volatility_2012.csv")
    
    # Calculate the alpha and beta values
    calc_all_alpha_beta(components, "../../data/alpha_2012.csv", "../../data/beta_2012.csv")
    