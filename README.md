# generate_signal.py
This code generates a signal composed of two sine waves of different frequencies, representing musical notes A4 and A5 (LA note in the 4th octave and in the 5th octave in the italian musical scale).
Then applies the Fast Fourier Transform (FFT) to convert the signal from the time domain to the frequency domain.

# script.py
This code allows the user to listen to the reconstructed signal either without any filter or with a high-pass filter applied.

# How to run

## Virtual environment setup


### Install Python Virtual Environment Module
```bash
sudo apt install python3.10-venv
```
### Create a Virtual Environment
```bash
python3 -m venv venv
```
### Activate the Virtual Environment
```bash
source venv/bin/activate
```
## Install Dependencies
```bash
pip3 install -r requirements.txt
```

# run
```bash
python3 script.py
```