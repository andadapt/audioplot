## AudioPlot
AudioPlot is a simple python script to convert any array into an audio stream.

This is especially helpful for data science and machine learning workflows. It enables a quick overview for data interpretation.

This module formed a small part of my MSc in speech and text processing. Being blind I found it difficult to assess model performance quickly. This module enabled me to gain an overview of data for analysis.

Please note, this has only been tested on MacOS, it should work on Linux. Windows support has not been tested, audio line plotting should work, however, adding any meta information to plots will fail under windows without tinkering.

## Dependencies

The plotting relies on a number of audio systems so the following dependencies are required:
###portaudio

    brew install portaudio

###pyaudio and audiolazy
Through pip
    pip install pyaudio
	
##Installation
	
To install ensure audioplot.py is in the directory of your python project.
	
##Usage
	
The best way to get a sense of how the audioplot works is to run the test files.
	
    git clone https://github.com/andadapt/audioplot/
	cd audioplot
	python3 test_line.py
	
##Issues

Any issues please feel free to get in touch and I can assist.
