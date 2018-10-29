from seatfinder import Seatfinder
import matplotlib.pyplot as plt

if __name__ == '__main__':
    seatfinder = Seatfinder('Kassel')

    print(seatfinder.locations['LeoEG'])

    seat_estimate = seatfinder.seat_estimate['2018-09-29']
    print(seat_estimate['LeoEG'])
    manual_count = seatfinder.manual_count['2018-09-01':'2018-09-30']

    df = seatfinder.seat_estimate['2018-09-01':'2018-10-26'].to_dataframe()
    df.loc['LeoEG']['occupied_seats'].plot()
    plt.show()
    plt.clf()
    df = seatfinder.seat_estimate['2018-10-18'].to_dataframe()
    df.loc[['LeoEG', 'LeoOG']]['occupied_seats'].groupby('location_name').plot(legend=True)
    plt.show()
