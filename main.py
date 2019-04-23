import json
import requests

from collections import namedtuple

from tools import get_json
from utilities import parse_full_date, parse_full_date_without_milisec


Flight = namedtuple('Flight', ['orig', 'dest', 'date_out', 'date_in', 'price', 'flight_number'])

def get_airports_raw_data():
    print('Getting airports information')
    return get_json('https://api.ryanair.com/aggregate/4/common?embedded=airports&market=de-de')

def get_connections_from_stations_data(data):
    print('Getting airports connections')
    return {
        airport['iataCode']: {
            item.partition(':')[2]
            for item in airport['routes']
            if item.startswith('airport:')
        }
        for airport in data['airports']
    }

def aaaa(data):
    print(len(data['airports']))

    for airport in data['airports']:
        print('###')
        print(airport['iataCode'])
        print('###')
        for item in airport['routes']:
            if item.startswith('airport:'):
                item.partition(':')
                print(item.partition(':')[2])


def execute_request():
    query = {
        'ADT': 1,
        'CHD': 0,
        'DateOut': '2019-04-27',
        #'DateOut': request.date_to.isoformat(),
        'Destination': 'ZAD',
        #'Destination': request.dest,
        'FlexDaysOut': 6,
        'INF': 0,
        'Origin': 'FKB',
        #'Origin': request.orig,
        'RoundTrip': 'false',
        'TEEN': 0,
        'ToUs': 'AGREED',
    }

    res = get_json('https://desktopapps.ryanair.com/de-de/availability', params=query)

    return [
        Flight(
            orig=trip['origin'],
            dest=trip['destination'],
            date_out=parse_full_date(flight['time'][0]),
            date_in=parse_full_date(flight['time'][1]),
            price=get_cheapest_fare_from_flight(flight),
            flight_number=flight['flightNumber'],
        )
        for trip in res['trips']
        for date in trip['dates']
        for flight in date['flights']
        if flight['faresLeft']
    ]

def get_cheapest_fare_from_flight(flight):
    fare = flight.get('regularFare') or flight.get('leisureFare') or flight['businessFare']
    return fare['fares'][0]['amount']

def get_schedule():
    query = {
        'Destination': 'ZAD',
        'IsTwoWay': 'false',
        'Months': '16',
        'Origin': 'FKB',
        'StartDate': '2019-04-22'
    }

    res = get_json('https://desktopapps.ryanair.com/Calendar', params=query)
    print(res['outboundDates'])
    #print(res['outboundDates'][0])

    return res

def get_one_way_flights_by_time_periode():
    query = {
        'departureAirportIataCode': 'FKB',
        'language': 'de',
        'limit': '16',
        'market': 'de-de',
        'offset': '0',
        'outboundDepartureDateFrom': '2019-04-23',
        'outboundDepartureDateTo': '2019-04-25',
        'priceValueTo': '100'
    }

    y = requests.get('https://services-api.ryanair.com/farfnd/3/oneWayFares', params=query)
    res = json.loads(y.text)
    #print(res)

    return [
        Flight(
            orig=trip['outbound']['departureAirport']['iataCode'],
            dest=trip['outbound']['arrivalAirport']['iataCode'],
            date_out=parse_full_date_without_milisec(trip['outbound']['departureDate']),
            date_in=parse_full_date_without_milisec(trip['outbound']['arrivalDate']),
            price=trip['outbound']['price']['value'],
            flight_number=''
        )
        for trip in res['fares']
    ]


#data = get_airports_raw_data()
#print(data)

#data_conections = get_connections_from_stations_data(data)
#print(data_conections['FKB'])

#get_schedule()

#a = execute_request()
#print(a)


#c = get_one_way_flights_by_time_periode()
#for i in range(len(c)):
    #print(c[i].dest)

print("done")
