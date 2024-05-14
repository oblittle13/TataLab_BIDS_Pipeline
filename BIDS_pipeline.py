# module imports
import os
import mne

unknowns = []

def process_files_in_eeg(root):
    print(root)
    eeg_path = os.path.join(root, 'eeg')
    for filename in os.listdir(eeg_path):
        # Construct the full file path
        print(f'            {filename}')
        file_path = os.path.join(eeg_path, filename)
        # Extract the file extension
        _, file_extension = os.path.splitext(filename)
        
        if file_extension == '.json':
            print(f'     Processing json file: {filename}')
            # JSON

        elif file_extension == '.tsv':
            print(f'     Processing tsv: {filename}')
            # TSV

        elif file_extension == '.edf':
            print(f'     Processing edf/edf+ file: {filename}')
            # EDF

        elif file_extension == '.bdf':
            print(f'     Processing bdf/bdf+ file: {filename}')
            # BDF
                       
        # EEG LAB
        # ----------------------------------
        elif file_extension == '.set':
            print(f'     Processing EEGLAB: {filename}')
            # EEG LAB

        elif file_extension == '.fdt':
            print(f'     Processing fdt: {filename}')
            # EEG LAB - optional
        # ----------------------------------
        
        # BrainVision Core Data Format
        # ----------------------------------
        elif file_extension == '.vhdr':
            print(f'     Processing vhdr: {filename}')
            # VHDR

        elif file_extension == '.vmrk':
            print(f'     Processing vmrk: {filename}')
            # VMRK

        elif file_extension == '.eeg':
            print(f'     Processing eeg: {filename}')
            # EEG
        # ----------------------------------

        else:
            print(f'Unknown file type {file_extension}: {file_path}')
            if file_extension not in unknowns:
                unknowns.append(file_extension)

# Get dataset directory
datasets_directory = os.path.join(os.path.dirname(__file__), '..', 'Datasets/Datasets_To_Convert')
# Walk through the directory
for root, dirs, files in os.walk(datasets_directory):
    # Check if 'eeg' is one of the subdirectories
    if 'eeg' in dirs:
        process_files_in_eeg(root)

print(unknowns)




# for ch in raw_changed.info['chs']:
#     print(f"{ch['ch_name']}: {ch['loc'][:3]}")  # loc[:3] contains the x, y, z positions

