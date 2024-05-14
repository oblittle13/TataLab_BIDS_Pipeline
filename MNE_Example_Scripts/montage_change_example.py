import os
import mne
import matplotlib.pyplot as plt

# Load in NME example dataset
sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = os.path.join(
    sample_data_folder, "MEG", "sample", "sample_audvis_raw.fif"
)
raw = mne.io.read_raw_fif(sample_data_raw_file, verbose=False)
raw.crop(tmax=60).load_data()
raw.pick([f"EEG 0{n:02}" for n in range(41, 60)])

# Copy raw to see how montage change effect the data
raw_changed = raw.copy()

# Load a standard montage (no 10-20 montage is available in NME that I can find)
montage = mne.channels.make_standard_montage('standard_1020')

# Rename the EEG channels to standard 10-20 system name
channel_mapping = {
    'EEG 041': 'Fp1', 'EEG 042': 'Fp2', 'EEG 043': 'F3', 'EEG 044': 'F4',
    'EEG 045': 'C3', 'EEG 046': 'C4', 'EEG 047': 'P3', 'EEG 048': 'P4',
    'EEG 049': 'O1', 'EEG 050': 'O2', 'EEG 051': 'F7', 'EEG 052': 'F8',
    'EEG 053': 'T7', 'EEG 054': 'T8', 'EEG 055': 'P7', 'EEG 056': 'P8',
    'EEG 057': 'Fz', 'EEG 058': 'Cz', 'EEG 059': 'Pz'
}
raw_changed.rename_channels(channel_mapping)

# Applying the montage change
raw_changed.set_montage(montage, match_case=False)

# Plot the original sensor positions
raw.plot_sensors(show_names=True, title='Original Sensor Layout')

# Plot the modified sensor positions
raw_changed.plot_sensors(show_names=True, title='Modified Sensor Layout')

# Show the plots
plt.show()

# Keep the plots open
input("Press Enter to close the windows...")


