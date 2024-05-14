# TO DO
*A list of our current TO DO requirements, and a simple outline on how to achieve the goals*

## Automated Requirements Downloader
Create a script to automatically check is packages exists/are of the correct versions, prompt user if they would like to upgrade/download to requiremnts (*include optional packages*) </br>
*Optionally: Include ability to specify location of existing datasets to move over into directory*

## Pipeline
*For dataset in [Datasets_To_Convert](Datasets_To_Convert) load into [pipeline](BIDS_pipeline.py) and begin conversion.* </br>
*Optionally: Include ability to customize settings to allow different BIDS conversions. Include our default perameters as an option* </br>
    **Process** </br>
    - For each dataset in [Datasets_To_Convert](Datasets_To_Convert)
- [ ] Check current montage *convert to `desired_montage` if required* </br>
- [ ] Check current reference *convert to `desired_reference` if required* </br>
- [ ] Check current samplerate *convert to `desired_samplerate` if required* </br>
  - [ ] **Optional:** Check for other variables (ie. powerlinefreq, filtering, etc...) *convert to `desired_<variable>` if required* </br>
- [ ] Save in [Converted_Datasets](Converted_Datasets) **Keep original file structure and non-eeg files** </br>
  - [ ] **Optional:** Allow for converted dataset location to exist outside of pipeline directory *Location specified by user* </br>
  - [ ] **Optional:** Provide progress bar *Extra optional: Provide estimated time* </br>