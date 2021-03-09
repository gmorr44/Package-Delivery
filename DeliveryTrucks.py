from Distances import get_next_location_distance, distance_to_time
from Packages import get_hashtable, set_package_status
from datetime import timedelta


class Trucks:

    def __init__(self):
        self.truck_number = 0
        self.distance = 0.00  # distance in miles
        self.payload = []  # the current cargo on the truck
        self.current_time = timedelta(hours=0, minutes=0, seconds=0)
        self.stop_time = timedelta(hours=0, minutes=0, seconds=0)
        self.start_time = timedelta(hours=0, minutes=0, seconds=0)

# Sets the time the packages will deliver until. Its purpose is for checking statuses at a specific time.
def set_stop_time(stop_time):
    t1.stop_time = stop_time
    t2.stop_time = stop_time
    t3.stop_time = stop_time

def get_total_mileage():
    total = round(t1.distance + t2.distance + t3.distance  , 1)
    return total
# returns the list of packages currently on the specified truck.
def get_payload(truck_number):
    if truck_number == 1:
        return t1.payload
    elif truck_number == 2:
        return t2.payload
    elif truck_number == 3:
        return t3.payload

# This is the optimization algorithm that sorts the list
# The sorting algorithm is fully detailed in the Core Algorithm Overview
def sort_packages(truck_num):
    global lowest_index
    list = get_payload(truck_num)
    optimized_list = [get_payload(truck_num)[0]]
    list.pop(0)
    i = 0
    while len(list)-1 > 0:
        holder = 100.0
        lowest_val = []
        adress1 = optimized_list[i][1]
        for j in range(len(list)-1):
            adress2 = list[j][1]
            if float(get_next_location_distance(adress1,adress2)) < holder:
                holder = float(get_next_location_distance(adress1,adress2))
                lowest_val = list[j]
                lowest_index = j
        optimized_list.append(lowest_val)
        i = i + 1
        list.pop(lowest_index)
    optimized_list.append(optimized_list[0])
    # after running the sorting algorithm, I updated the truck payload with the optimized list.
    if truck_num == 1:
        t1.payload = optimized_list
    if truck_num == 2:
        t2.payload = optimized_list
    if truck_num == 3:
        t3.payload = optimized_list

def load_trucks():
    #initializes the payload back to empty prior to loading packages for instances the program is ran more than 1 time.
    t1.payload = []
    t2.payload = []
    t3.payload = []
    # I manually loaded the trucks with the most viable package combinations and limitations prior to sorting them.
    list1 = [13,14,15,16,19,20,39,1,21,7,29,30,34,10]
    list2 = [3,6,18,25,28,32,31,37,38,40,4,5,26,36,12]
    list3 = [8,2,33,27,35,22,24,17,11,23,9]

    # The following loops use the id numbers in the lists above to locate the package from the hashmap and add the information to the payload.
    for i in range(len(list1)):
        t1.payload.append(get_hashtable().get_package(list1[i]))
    for i in range(len(list2)):
        t2.payload.append(get_hashtable().get_package(list2[i]))
    for i in range(len(list3)):
        t3.payload.append(get_hashtable().get_package(list3[i]))

    # I inserted HUB placeholders at the beginning and end of each payload to use for distance calculations.
    t1.payload.append(['','HUB','','','','','',''])
    t1.payload.insert(0,['','HUB','','','','','',''])
    t2.payload.append(['', 'HUB', '', '', '', '', '', ''])
    t2.payload.insert(0, ['', 'HUB', '', '', '', '', '', ''])
    t3.payload.append(['', 'HUB', '', '', '', '', '', ''])
    t3.payload.insert(0, ['', 'HUB', '', '', '', '', '', ''])

def deliver_packages():
    # will reset the package status back to 'At The Hub'
    key = 1
    for i in range(40):
        set_package_status(key,'At The Hub ')
        key = key + 1

    t1.distance = 0.0 # resets the distance counter
    t2.distance = 0.0 # resets the distance counter
    t3.distance = 0.0 # resets the distance counter

    t1.current_time = t1.start_time # resets the current_time counter to default start time
    t2.current_time = t2.start_time # resets the current_time counter to default start time
    t3.current_time = t3.start_time # resets the current_time counter to default start time

    load_trucks() #loads the trucks with the unsorted packages

    sort_packages(1) #sorts the packages in truck 1 payload
    sort_packages(2) #sorts the packages in truck 2 payload
    sort_packages(3) #sorts the packages in truck 3 payload

    if len(t1.payload) > 0 and t1.stop_time < t1.current_time:
        for i in range(1,len(t1.payload)-1):
            set_package_status(int(t1.payload[i][0]) , 'At The Hub @ ' + str(t1.stop_time))

    if len(t1.payload) > 0 and t1.stop_time > t1.current_time:
        for i in range(1,len(t1.payload)-1):
            set_package_status(int(t1.payload[i][0]) , 'En Route On Truck 1 @ ' + str(t1.stop_time))

    while len(t1.payload) >= 1 :
        if len(t1.payload) == 1: # This will pop the last HUB placeholder from the payload list because all packages were delivered.
            t1.payload.pop(0)
        if len(get_payload(1)) > 1:
            next_distance1 = float(get_next_location_distance(get_payload(1)[0][1], get_payload(1)[1][1])) # returns next distance value.
            t1.distance = t1.distance +  next_distance1 # adds current distance to next distance.
            t1.current_time = t1.current_time + distance_to_time(next_distance1) # adds next distance to current sum
            if t1.current_time >= t1.stop_time:
                break
            # If each condition is met the status will be updated to delivered.
            if t1.payload[0][0] == '':
                set_package_status(int(t1.payload[1][0]),'Truck 1 Delivered @ ' + str(t1.current_time))
            elif t1.payload[1][0] == '':
                set_package_status(int(t1.payload[0][0]), 'Truck 1 Delivered @ ' + str(t1.current_time))
            elif t1.payload[1][0] != '':
                set_package_status(int(t1.payload[1][0]), 'Truck 1 Delivered @ ' + str(t1.current_time))
            t1.payload.pop(0)
            t3.current_time = t1.current_time
            t3.start_time = t1.current_time

    if len(t2.payload) > 0 and t2.stop_time < t2.current_time:
        for i in range(1,len(t2.payload)-1):
            set_package_status(int(t2.payload[i][0]) , 'At The Hub @ ' + str(t2.stop_time))

    # sets the status of truck 2 packages as en route when the truck is out for delivery
    if len(t2.payload) > 0 and t2.stop_time > t2.current_time:
        for i in range(1,len(t2.payload)-1):
            set_package_status(int(t2.payload[i][0]) , 'En Route On Truck 2 @ ' + str(t2.stop_time))

    while len(t2.payload) >= 1:
        if len(t2.payload) == 1:  # This will pop the last HUB placeholder from the payload list because all packages were delivered.
            t2.payload.pop(0)
        if len(get_payload(2)) > 1:
            next_distance2 = float(get_next_location_distance(get_payload(2)[0][1], get_payload(2)[1][1]))# returns next distance value.
            t2.distance = t2.distance + next_distance2 # adds current distance to next distance.
            t2.current_time = t2.current_time + distance_to_time(next_distance2) # adds next distance to current sum.
            if t2.current_time >= t2.stop_time:
                break
            # If each condition is met the status will be updated to delivered.
            if t2.payload[0][0] == '':
                set_package_status(int(t2.payload[1][0]), 'Truck 2 Delivered @ ' + str(t2.current_time))
            elif t2.payload[1][0] == '':
                set_package_status(int(t2.payload[0][0]), 'Truck 2 Delivered @ ' + str(t2.current_time))
            elif t2.payload[1][0] != '':
                set_package_status(int(t2.payload[1][0]), 'Truck 2 Delivered @ ' + str(t2.current_time))
            t2.payload.pop(0)

    if len(t3.payload) > 0 and t1.payload != []:
        for i in range(1,len(t3.payload)-1):
            set_package_status(int(t3.payload[i][0]) , 'At The Hub @ ' + str(t3.stop_time))

    # sets the status of truck 3 packages as en route when the truck is out for delivery
    if len(t3.payload) > 0 and t1.payload == []:
        for i in range(1,len(t3.payload)-1):
            set_package_status(int(t3.payload[i][0]) , 'En Route On Truck 3 @ ' + str(t3.stop_time))

    while len(t3.payload) >= 1 and t1.payload == []:# the conditions will only allow truck 3 to deliver if truck 1 is back at the hub and truck 3 is not empty
        if len(t3.payload) == 1: # catches the last HUB placeholder and pops is from the truck payload.
            t3.payload.pop(0)
        if len(get_payload(3)) > 1:
            next_distance3 = float(get_next_location_distance(get_payload(3)[0][1], get_payload(3)[1][1]))# returns next distance value.
            t3.distance = t3.distance + next_distance3 # adds current distance to next distance.
            t3.current_time = t3.current_time + distance_to_time(next_distance3) # adds next distance to current sum.
            if t3.current_time >= t3.stop_time: # will stop delivering packages at this time.
                break
            # If each condition is met the status will be updated to delivered.
            if t3.payload[0][0] == '':
                set_package_status(int(t3.payload[1][0]), 'Truck 3 Delivered @ ' + str(t3.current_time))
            elif t3.payload[1][0] == '':
                set_package_status(int(t3.payload[0][0]), 'Truck 3 Delivered @ ' + str(t3.current_time))
            elif t3.payload[1][0] != '':
                set_package_status(int(t3.payload[1][0]), 'Truck 3 Delivered @ ' + str(t3.current_time))
            t3.payload.pop(0)

t1 = Trucks() # truck 1 object
t2 = Trucks() # truck 2 object
t3 = Trucks() # truck 3 object

t1.start_time = timedelta(hours=8, minutes=0, seconds=0)  # initiates the delivery start time for truck 1
t2.start_time = timedelta(hours=9, minutes=5, seconds=0)  # initiates the delivery start time for truck 2
t3.start_time = timedelta(hours=0, minutes=0, seconds=0)  # initiates the delivery start time for truck 3.
                                                          # This is updated in the deliver_packages method after truck 1 has returned to hub.
