#!/usr/bin/python3

__author__ = "Sai Durga Rithvik Oruganti"

from scipy.io import wavfile
from scipy import signal
import numpy as np
import os


def sample_rate_check(input_rate, IR_rate):
    if input_rate != IR_rate:
        print("Sample rate is not same")
        quit()
    else:
        return input_rate


def file_checker(file_name):
    file_name = file_name[1:] * (file_name[0] == "/") + file_name * (
        file_name[0] != "/"
    )
    return (
        os.path.isfile(str(file_name))
        if os.path.isfile(str(file_name))
        else exit("File Doesn't Exist")
    )


def main():
    sound_file_name = input(
        str("Enter Input Audio File Name: ")
    )  # Example: 'audio_files/opera.wav'
    file_checker(sound_file_name)

    IR_file_name = input(
        str("Enter Impulse Response File Name: ")
    )  # Example: 'echo_files/sofia.wav'
    file_checker(IR_file_name)

    global output_name
    output_name = input(str("Enter Output Name: "))
    output_name = f"{output_name}.wav" if output_name[-3:] != "wav" else output_name

    sound_rate, sound_sig = wavfile.read(sound_file_name)

    IR_rate, IR_sig = wavfile.read(IR_file_name)

    sample_rate_check(sound_rate, IR_rate)

    out_0 = signal.fftconvolve(sound_sig[:-1, 0], IR_sig[:-1, 0])
    out_0 /= np.max(np.abs(out_0))

    out_1 = signal.fftconvolve(sound_sig[:-1, 1], IR_sig[:-1, 1])
    out_1 /= np.max(np.abs(out_1))
    out = np.vstack((out_0, out_1)).T

    wavfile.write(f"output_files/{output_name}", sound_rate, out)


if __name__ == "__main__":
    print(f'Created By   :  {__author__}')
    print(f'Created Date :  05/07/2022\n')
    main()
    print(f'File Path: output_files/{output_name}\n\nThank You!')
