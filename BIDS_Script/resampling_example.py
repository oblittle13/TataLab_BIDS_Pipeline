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

raw_downsampled = raw.copy().resample(sfreq=500)
# choose n_fft for Welch PSD to make frequency axes similar resolution
n_ffts = [4096, int(round(4096 * 200 / raw.info["sfreq"]))]
fig, axes = plt.subplots(2, 1, sharey=True, layout="constrained", figsize=(10, 6))
for ax, data, title, n_fft in zip(
    axes, [raw, raw_downsampled], ["Original (600hz)", "Downsampled to 500hz"], n_ffts
):
    fig = data.compute_psd(n_fft=n_fft).plot(
        average=True, amplitude=False, picks="data", exclude="bads", axes=ax
    )
    ax.set(title=title, xlim=(0, 300))

plt.show()