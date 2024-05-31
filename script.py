import numpy as np
from scipy.fft import ifft
from scipy.signal import butter, filtfilt
import sounddevice as sd
import subprocess


def generate_signal():
    subprocess.run(["python3", "generate_signal.py"])

def main():
    generate_signal()

    # read the Real and Imaginary parts of the sampled signal from the text files
    file_path_real = 'signal_freq_domain_real.txt'
    file_path_imag = 'signal_freq_domain_imag.txt'
    fft_result_real = np.loadtxt(file_path_real)
    fft_result_imag = np.loadtxt(file_path_imag)

    # combine real and imaginary parts into complex numbers
    fft_result = fft_result_real + 1j * fft_result_imag

    # reconstruct the signal in time domain using inverse fast Fourier transform (IFFT)
    reconstructed_signal = ifft(fft_result)

    # user input
    print("Choose how to listen the reconstructed signal:")
    print("0. Exit")
    print("1. Original signal - no filter")
    print("2. Highpass filter")
    choice = int(input("Enter your choice: "))
    
    while True:
    # Apply filter based on user choice
        if choice == 0:
            exit()
        
        if choice == 1:
            # no filter
            filtered_signal = reconstructed_signal.real
        
        if choice == 2:
            # highpass filter
            def butter_highpass(cutoff, fs, order=5):
                nyquist = 0.5 * fs
                normal_cutoff = cutoff / nyquist
                b, a = butter(order, normal_cutoff, btype='high', analog=False)
                return b, a

            def butter_highpass_filter(data, cutoff, fs, order=5):
                b, a = butter_highpass(cutoff, fs, order=order)
                y = filtfilt(b, a, data)
                return y

            # get cutoff frequency from user input
            cutoff_freq = float(input("Enter the cutoff frequency for the highpass filter (in Hz): "))

            filtered_signal = butter_highpass_filter(reconstructed_signal.real, cutoff_freq, 44100)

        else:
            print("Invalid choice.")


        # play the reconstructed signal
        sd.play(filtered_signal, samplerate=44100)

        # Wait for the playback to finish
        sd.wait()

if __name__ == "__main__":
    main()
