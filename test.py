import ast
from collections import namedtuple
import datetime

print('test')

flight_list_a = list()
flight_list_b = list()
flight_list_c = list()
flight_list_d = list()
with open('flight.txt') as f:
    for line in f:
        flight_list_a.append(line)

flight_list_c = [line.rstrip('\n') for line in open('flight.txt')]


#print('flight_list_a {}' .format(flight_list_a))
#print('flight_list_b {}' .format(flight_list_b))
#print('flight_list_c {}' .format(flight_list_c))
#print('flight_list_d {}' .format(str(flight_list_c).strip('[]')))

stringd = '[' + str(flight_list_c).strip('[]') + ']'
#print('flight_list_e {}' .format(stringd))

mylist = ast.literal_eval(stringd)
#print('flight_list_f {}' .format(mylist))
#print('flight_list_f {}' .format(mylist[1]))

mylist2 = ast.literal_eval("['foo', ['cat', ['ant', 'bee'], 'dog'], 'bar', 'baz']")
#print('flight_list_g {}' .format(mylist2[1][1][1]))


listFlight = list()
listAirportA = list()
listAirportB = list()
listTo = list()
listFrom = list()

Flight = namedtuple('Flight', ['orig', 'dest', 'date_out', 'date_in', 'price', 'flight_number'])

flightTo = Flight(orig='FKB', dest='STR', date_out=datetime.datetime(2019, 5, 25, 6, 35), date_in=datetime.datetime(2019, 5, 25, 6, 35), price=12.12, flight_number='FR-1111')
flightFrom = Flight(orig='STR', dest='FKB', date_out=datetime.datetime(2019, 5, 25, 6, 35), date_in=datetime.datetime(2019, 5, 25, 6, 35), price=12.12, flight_number='FR-2222')

listTo.append(flightTo)
listFrom.append(flightFrom)
listAirportA.append(listTo)
listAirportA.append(listFrom)
listAirportB.append(listTo)
listAirportB.append(listFrom)
listFlight.append(listAirportA)
listFlight.append(listAirportB)
print(listFlight)

with open('flight2.txt', 'w') as file_handler:
    for item in listFlight:
        file_handler.write("{}\n".format(item))

flight_list_1 = list()
with open('flight2.txt') as f:
    for line in f:
        flight_list_1.append(line)

flight_list_1 = [line.rstrip('\n') for line in open('flight2.txt')]

print('flight_list_1 {}' .format(flight_list_1))


