import ast

print('test')

flight_list_a = list()
flight_list_b = list()
flight_list_c = list()
flight_list_d = list()
with open('flight.txt') as f:
    for line in f:
        flight_list_a.append(line)

flight_list_c = [line.rstrip('\n') for line in open('flight.txt')]



print('flight_list_a {}' .format(flight_list_a))
print('flight_list_b {}' .format(flight_list_b))
print('flight_list_c {}' .format(flight_list_c))
print('flight_list_d {}' .format(str(flight_list_c).strip('[]')))

stringd = '[' + str(flight_list_c).strip('[]') + ']'
print('flight_list_e {}' .format(stringd))

mylist = ast.literal_eval(stringd)
print('flight_list_f {}' .format(mylist))
print('flight_list_f {}' .format(mylist[1]))

mylist2 = ast.literal_eval("['foo', ['cat', ['ant', 'bee'], 'dog'], 'bar', 'baz']")
print('flight_list_g {}' .format(mylist2[1][1][1]))

#for o in range(len(lineList)):
    #print(lineList[o])
    #for u in range(len(lineList[o])):
        #print(lineList[o][u])
