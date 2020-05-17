import audioplot
import numpy as np


def linear_test():
    print('a linear line with no smoothing')
    data_array = [1,2,3,4,5,6,7,8,9,10]
    out = audioplot.plot('line')
    out.data(data_array)
    out.play()
def linear_smooth_test():
    print('a linear line with smoothing')
    data_array = [1,2,3,4,5,6,7,8,9,10]
    out = audioplot.plot('line')
    out.data(data_array, True)
    out.play()

def straight_test():
    print('a straight line')
    data_array = [1,1,1,1,1]
    out = audioplot.plot('line')
    out.data(data_array)
    out.play()

def linear_range_test():
    print('a linear line with adjusted audio range')
    data_array = [1,2,3,4,5,6,7,8,9,10]
    out = audioplot.plot('line')
    out.data(data_array)
    out.audio_range(200,250)
    out.play()
def exponential_test() :
    print('an exponential line')
    data_array = np.logspace(2,9,dtype='int')
    out = audioplot.plot('line')
    out.data(data_array)
    out.play()

def verbose_test() :
    print('testing verbose output')
    out = audioplot.plot('line')
    data_array=[1,2,3,4,5,6,7,8,9,10]
    out.data(data_array)
    out.verbosity(True)
    out.title('A linearly rising line')
    out.xlabel('time period')
    out.ylabel('amount of an item')
    out.play()


def rate_test():
    print('testing reduced speaking rate')
    out = audioplot.plot('line')
    data_array=[1,2,3,4,5,6,7,8,9,10]
    out.data(data_array)
    out.verbosity(True)
    out.title('A linearly rising line')
    out.xlabel('time period')
    out.ylabel('amount of an item')
    out.rate(50)
    out.play()

def duration_test():
    print('testing shorter duration of 2 seconds')
    out = audioplot.plot('line')
    data_array=[1,2,3,4,5,6,7,8,9,10]
    out.data(data_array)
    out.duration(2)
    out.play()
    
def single_array_input_test():
    out = audioplot.plot('line')
    data_array=[1,3]
    out.data(data_array, smoothed=True)
    out.play()
    
def run():
    linear_test()
    linear_range_test()
    linear_smooth_test()
    straight_test()
    exponential_test()
    verbose_test()
    rate_test()
    duration_test()


run()
#single_array_input_test()

