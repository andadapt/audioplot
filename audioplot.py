#import external modules
import numpy as np
import sys
import subprocess
import platform
from audiolazy import *
import time


def get_os():
    '''obtain OS for correct TTS'''
    os = platform.system()

    if os == 'Linux':
        return 'linux'
    elif os == 'Darwin':
        return 'mac'
    elif os == 'Win32':
        return 'window'


class Plot:
    '''
    Parent class, contains structure and functions to be inherited

    '''

    plot_type = ''
    plot_title = ''
    plot_ylabel = ''
    plot_xlabel = ''
    plot_min = 200
    plot_max = 600
    plot_data_min = 0
    plot_data_max = 0
    plot_speaking_rate = '200'
    plot_verbosity = False
    plot_data = []
    plot_duration = 5
    plot_bins = 10
    plot_bar_items = []


    def title(self, title):
        '''title, pass a string for the plot title'''
        
        self.plot_title = title

    def xlabel(self, xlabel):
        '''zlabel, pass a string for X axis label'''
    
        self.plot_xlabel = xlabel

    def ylabel(self, label):
        '''ylabel, pass a string for the Y axis label'''
        self.plot_ylabel = label
    def verbosity(self, vmode):
        '''verbosity, takes a boolean to set flag for verbose output'''
        self.plot_verbosity = vmode

    def rate(self, rate):
        '''rate, pass an integer for the ````TTS speaking rate'''

        #rate is cast as str to account for string passing to shell
        self.plot_speaking_rate = str(rate)

    def bins(self, bins):
        '''bins, adjust number of bins for histogram model'''
        if bins <= 0:
            raise ValueError('number of bins must be positive')
        self.plot_bins = bins

    def duration(self, dur):
        '''duration, the length in seconds for the audio stream'''

        if dur <= 0:
            raise ValueError('duration of audio must be positive')
        self.plot_duration = dur
        
    def audio_range(self,min,max):
        '''audio_range, pass a minimum and maximum as integer for the min and max frequencies'''

        if min >= max:
            raise ValueError('invalid minimum and maximum audio range')
        self.plot_min = min
        self.plot_max=max

    def data_min_max(self,data_array):
        '''obatins minimum and maximum data values for verbose mode'''
        self.plot_data_min = min(data_array)
        self.plot_data_max = max(data_array)

        



    def array_range(self, array):
        """takes an iterable and returns minimum and maximum values
    """

        values = []
        values.append(min(array))
        values.append(max(array))

        return values
    


    def scaled_clamp(self, array):
        '''scales an array into a new range keep ratios intact'''


        clamped_array = []
        array_min, array_max = self.array_range(array)

        #set old and new range variables
        max=self.plot_max
        min=self.plot_min
        original_array_range = (array_max - array_min)
        clamped_range = max - min

        #account for divide by 0 case 
        if original_array_range == 0:
            return [400]
    
    #iterate through array and clamp to new range
        for i in array:
            clamped_value = (((i - array_min)* clamped_range)/ original_array_range) + min
            clamped_array.append(clamped_value)

        return clamped_array

    def smoothing(self, data_array):
        '''smooths the data in an array to remove audio artefacts'''

        # only smooth if less than 100 as cannot audibly detect
        if len(data_array) < 100:
            smoothing_points = 1550 - len(data_array)
            smoothing_between_points = smoothing_points // len(data_array)
            data_smoothed = np.array(0)
 
            for i in range(len(data_array)):
                if i == len(data_array) -1:
                    break
            
                smoothed = np.linspace(data_array[i], data_array[i+1], smoothing_between_points)
                data_smoothed = np.append(data_smoothed, smoothed)


        return data_smoothed

    def tts(self, text_string):
        '''tts, takes a string and passes to system TTS engine'''

        text_string = str(text_string)
        rate = self.plot_speaking_rate
        os = get_os()


        if os == 'linux':
            subprocess.run(['espeak-ng', '-s', rate, text_string])
        elif os == 'mac':
            subprocess.run(['say', '-r', rate, text_string])
        else:
            raise ValueError('Your OS is not currently supported.')

    def verbose_audio_out(self):
        '''verbose_audio_out, outputs meta-data to TTS'''
        self.tts(self.plot_title)
        if self.plot_xlabel != '':
            self.tts("X axis")
        self.tts(self.plot_xlabel)
        if self.plot_ylabel != '':
            self.tts('Y axis')
        self.tts(self.plot_ylabel)
        #get minimum and maximum values
        self.tts(f'minimum value is {self.plot_data_min}')
        self.tts(f'maximum value is {self.plot_data_max}')


class Line(Plot):
    '''line, inherits from plot clas and defines data and play functions'''


    def data(self, data_array, smoothed=False):
        '''ddata, configures data for line output'''

        if len(data_array) <= 1:
            raise ValueError('Data input is to small to plot')

        self.data_min_max(data_array)

        if smoothed:
            clamp = self.scaled_clamp(data_array)
            self.plot_data = self.smoothing(clamp)
        else:
            self.plot_data = self.scaled_clamp(data_array)

    def play(self, line_data=None):
        '''outputs the line audio model audio'''

        if self.plot_verbosity ==True:
            self.verbose_audio_out()

        if line_data is None:
            line_data = self.plot_data

        duration = self.plot_duration

        #configure variables for timing of audio
        rate = 44100
        s, Hz = sHz(rate)

        with AudioIO () as player:
            data_point = ControlStream(0)
            signal = sinusoid(data_point*Hz)
            player.play(signal)

            s_count = duration / len(line_data) #calculate length of each data_point in time
            for val in line_data:
                data_point.value = val
                time.sleep(s_count)

class Bar(Plot):
    '''bar, inherits from the plot class and contains data and play functions'''


    def data(self, data_array, items):
        '''data, configures data for bar chart output'''
        self.plot_data = data_array
        self.data_min_max(data_array)
        self.plot_bar_items = items
    
    def play(self):
        '''play, creates audio output for bar chart model'''
        '''outputs an audio model of a bar chart'''

        if self.plot_verbosity ==True:
            self.verbose_audio_out()
        bar_items = self.plot_bar_items
        bar_values = self.plot_data

        for i in range(len(bar_items)):
            self.tts(bar_items[i])
            self.tts(bar_values[i])

class Histogram(Line):
    '''histogram, inherits from line class, contains data and play functions'''

    def data(self, data_array, bins=10):
        '''data, configures the data output for histogram'''
        super().data(data_array, smoothed=False)
        self.plot_bins = bins
        

    def play(self):
        '''play, generates the audio output for the histogram model'''

        '''histogram_audio_out, outputs the histogram audio model'''
        
        data_array = np.histogram(self.plot_data, bins=self.plot_bins)
        data_array = data_array[0]
        
        #clamp histogram bins
        scaled_array = self.scaled_clamp(data_array)
        smoothed_array = self.smoothing(scaled_array)
        super().play(smoothed_array)

        # bin data output
        for loc in range(len(data_array)):
            bin_number = loc + 1
            bin_number = str(bin_number)
            bin_string = 'bin ' + bin_number
            self.tts(bin_string)
            self.tts(data_array[loc])


def plot(plot_type):
    '''plot_type, helper function for passing a string for correct class'''

    if plot_type == 'line':
        obj = Line()
    elif plot_type == 'bar':
        obj = Bar()
    elif plot_type == 'histogram':
        obj = Histogram()
    else:
        raise ValueError('%s is not a valid value %s' % (
            plot_type, '(line, bar, histogram)'
        ))
    
    return obj
