import datetime
import json
from collections import namedtuple
import yaml

from functions import get_airports_raw_data, get_connections_from_stations_data, execute_request
from dates import get_dates

print('Starting main.py to run Ryanpy!')

RequestOneFlight = namedtuple('RequestOneFlight', ['orig', 'dest', 'date'])

with open("Config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.SafeLoader)

date_from, date_to, duration = config['dates']['fromdate'], config['dates']['todate'], config['dates']['duration']
departure_airports = config['airports']['departureairports']

date_list = get_dates(date_from, date_to)
flight_list = []

data_conections = get_connections_from_stations_data(get_airports_raw_data())
#print(data_conections['FKB'])
for i in range(len(departure_airports)):
    print("Looking for connections starting form: {}.".format(departure_airports[i]))
    print("All destinations: {}.".format(data_conections[departure_airports[i]]))
    #TODO: create request - which can given as paramater to function
    for item in data_conections[departure_airports[i]]:
        print("Looking for connections starting form: {} to {}.".format(departure_airports[i], item))
        list_two_way = []
        requestOneFlight = RequestOneFlight(
            orig=departure_airports[i],
            dest=item,
            date=date_list[0]
        )
        list_two_way.append(execute_request(requestOneFlight))

        requestOneFlightBack = RequestOneFlight(
            orig=item,
            dest=departure_airports[i],
            date=date_list[0]
        )
        list_two_way.append(execute_request(requestOneFlightBack))
        flight_list.append(list_two_way)



with open('flight.txt', 'w') as file_handler:
    for item in flight_list:
        file_handler.write("{}\n".format(item))

print(flight_list)



print("DONE!")

