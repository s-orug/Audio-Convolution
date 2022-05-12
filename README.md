# README
## Objective
The objective of this project is to replicate the audio of a song at a location using the impulse response.
## Included Files
The project includes the following files/directories:
-   main.py
-   audio_files
-   echo_files
-   output_files
-   README.md
## main.py
The dependancies for this program are:

- scipy
- scipy.io
- numpy

To execute this program, run `python3 main.py` in the terminal. Then, enter the location of the audio and impulse response files. The program will convolve the two given and ouput a third file of the convolved audio. This file will be stored in output_files directory.

![Alt text](image.png?raw=true "Title")


## audio_files
This directory contains the audio used.

## echo_files
This directory contains the impulse responses used.

## output_files
All of the output files created by main.py are stored in this directory.