import plotting
import numpy as np

def normal_test():
    print('normal distribution, default settings')
    out = plotting.plot('histogram')
    data = np.random.normal(size=1000000,loc=0,scale=1)
    out.data(data)
    out.play()


def bin_test():
    print('normal distribution, 3 bins')
    out = plotting.plot('histogram')
    data = np.random.normal(size=1000000,loc=0,scale=1)
    out.data(data)
    out.bins(3)
    out.play()

def range_test() :
    print('normal distribution with adjusted frequencies')
    out = plotting.plot('histogram')
    data = np.random.normal(size=1000000,loc=0,scale=1)
    out.data(data)
    out.bins(3)
    out.audio_range(200,350)
    out.play()
def verbose_test():
    out = plotting.plot('histogram')
    print('normal distribution with verbose True')
    data = np.random.normal(size=1000000,loc=0,scale=1)
    out.data(data)
    out.bins(3)
    out.verbosity(True)
    out.title('A normal distribution with 1,000,000 data points')
    out.play()
    
    

def run():
    normal_test()
    bin_test()
    range_test()
    verbose_test()

run()
