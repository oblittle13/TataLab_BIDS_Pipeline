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

# Copy raw to see how rereferencing changes the data
raw_newChannel = mne.add_reference_channels(raw, ref_channels=["EEG 999"])
raw_changeChannel = raw.copy().set_eeg_reference(ref_channels=["EEG 050"])
raw_averageChannel = raw.copy().set_eeg_reference(ref_channels="average")

# Plot the original EEG data
raw.plot(title="Original")

# Plot the data with a reference to a newly added channel (no associated data)
raw_newChannel.plot(title="newChannel")

# Plot the data with a difference reference channel that exsisted during the test
raw_changeChannel.plot(title="changeChannel")

# Plot the data with an average channel reference
raw_averageChannel.plot(title="averageChannel")

# Show all the plots
plt.show()

# Keep the plots open
input("Press Enter to close the windows...")


