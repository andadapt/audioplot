


# AudioPlot
audioPlot is a python module for converting data arrays to audio streams.

It is particularly useful for blind or visually impaired users. The audio stream enables analysis of data quickly and easily. This is particularly useful for data science and machine learning.

This module formed part of my MSc Computer Science dissertation and was particularly useful for model assessment.Hopefully, others can find a use for it.

The module has been fully tested underMacOS, Linux should work. However, windows remains untested. Line plotting may work under windows as standard but plot meta data will cause an error.



## Dependencies
A number of audio systems are required, the instructions below are for MacOS.

```console
brew install portaudio
pip install pyaudio
pip install audiolazy
pip install numpy
```

## Usage

To use the module ensure audioplot.py is in your python project directory.

To get a sense of functionality and how to use the module, i recommend you clone this repository and run any of the test_ files.

```console
git clone httpS://github.com/andadapt/audioplot/
cd audioplot
python3 test_line.py
```
## Issues and features

if you have any issues or feature requests please get in touch. Submit an issue on GitHub, email me on simon@andadapt.com or on twitter @andadapt

:see_no_evil::doughnut:
