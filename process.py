# Import packages
import neurokit as nk
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

samples = 3000
# test = pd.read_csv("https://raw.githubusercontent.com/neuropsychology/NeuroKit.py/master/examples/Bio/bio_100Hz.csv")
test = pd.read_csv("training2017CSV/A00004.csv")
ecg_signal = test["'ECG '"]

# ecg_signal = ecg_signal[0:1000]
# ecg = ecg[0:1500]
print(ecg_signal)
processed_ecg = nk.ecg_process(ecg_signal,sampling_rate=300, filter_type="FIR", filter_band="bandpass", filter_frequency=[10, 25])
print(processed_ecg)

filtered = processed_ecg["df"]["ECG_Filtered"]
x = np.array([])
x = filtered
print(x)
plt.plot(x[0:samples])
plt.grid(color='r', linestyle='--', linewidth=0.3)
plt.show()
# Plot the p


plt.plot(ecg_signal[0:samples])
plt.grid(color='r', linestyle='--', linewidth=0.3)
plt.show()

# ================================ Find R-Peaks ==================================================
r_peaks = processed_ecg["ECG"]["R_Peaks"]
# print(r_peaks)
r = [0]*len(filtered)
for t in r_peaks:
	# 
	# print(filtered[t])
	r[t] = filtered[t]

# print(r)
plt.plot(r[0:samples])
plt.grid(color='r', linestyle='--', linewidth=0.3)
plt.show()
# ====================================================================================================