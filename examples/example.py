from pprint import pprint

from seatfinder import Seatfinder

if __name__ == '__main__':
    seatfinder = Seatfinder('Kassel')
    seat_estimate = seatfinder.seat_estimate['2018-09-29']
    print(seat_estimate['LeoEG'])
    manual_count = seatfinder.manual_count['2018-09-01':'2018-10-30']
    pprint(manual_count['LeoOG'])