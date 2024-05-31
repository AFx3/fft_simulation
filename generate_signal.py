import numpy as np
from scipy.fft import fft

# function to generate a signal by summing two sine waves of different frequencies
def generate_signal():
    
    # sampling parameters
    duration = 30  # duratio of the signal in seconds
    sampling_rate = 44100  # sampling rate in Hz
    num_samples = duration * sampling_rate

    # time array
    time = np.linspace(0, duration, num_samples, endpoint=False)

    # create a signal by summing sine waves of different frequencies and amplitudes
    freq1 = 440  # frequency of the first sine wave (A4 note, LA4)
    freq2 = 880  # frequency of the second sine wave (A5 note, LA5)
    ampl1 = 0.5  # amplitude of the first sine wave
    ampl2 = 0.3  # amplitude of the second sine wave
    signal = ampl1 * np.sin(2 * np.pi * freq1 * time) + ampl2 * np.sin(2 * np.pi * freq2 * time)

    # apply FFT to the signal
    fft_result = fft(signal)

    # Save the signal in frequency domain to a text file 
    np.savetxt('signal_freq_domain_real.txt', fft_result.real)
    np.savetxt('signal_freq_domain_imag.txt', fft_result.imag)

    print("Signal in frequency domain generated.")

if __name__ == "__main__":
    generate_signal()
