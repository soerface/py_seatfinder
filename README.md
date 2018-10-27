# Seatfinder Python API (inofficial)

Easy access to https://seatfinder.de data.
Caches data in the background, nothing will be downloaded twice.

## Installation

    pip install seatfinder

## Usage

    from seatfinder import Seatfinder
    seatfinder = Seatfinder('Kassel') # optional parameter data_dir. Default ~/.seatfinder/data
    seatfinder.seat_estimate['2018-09-29']
    
    # Slicing is also possible
    data = seatfinder.manual_count['2018-09-01':'2018-10-30']
    
    # `data` is a dict, access locations via key
    data['LeoEG']
    
    # More information about the location
    seatfinder.locations['LeoEG']
    
    # Convert to pandas dataframe
    df = data.to_dataframe()