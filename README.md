# TataLab_BIDS_Pipeline
Bids pipeline to "standardize" raw eeg data into our desired BIDS EEG format


**BIDS Pipeline:** </br>
*We want to take whatever raw data we feed to neural network, and re-reference it into a 10-20 montage with a 500hz smapling rate (with more options to come later - filtering, powerline frequency changes, etc...)*

**Helpful Links for Understanding:** </br>
*[10-10 Montage](https://www.researchgate.net/figure/Electrode-placement-for-the-10-10-montage_fig5_237088559)* </br>
*[Python MNE Library](https://mne.tools/stable/index.html)*

**How to re-reference using the Python Library MNE:** </br>
*[MNE Referencing](https://mne.tools/stable/auto_tutorials/preprocessing/55_setting_eeg_reference.html)* </br>
*[MNE Sensor Locations (ie. Montage)](https://mne.tools/dev/auto_tutorials/intro/40_sensor_locations.html)*

**Requirements** </br>
*Please see [requirements.txt](requirements.txt) for a simple installation guide and package/version requirements*
