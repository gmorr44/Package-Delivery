import csv
from datetime import timedelta

distance_grid = [] # Empty list that will be populated as a data matrix for the distance info.
# Will read the distance values from the csv file and insert them into a 2 dimensional array.
with open('PackageDistance.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter= ',')

    for row in readCSV:
        distance_grid.append(row) # appends a new row to the distance grid with comma delimited columns.

def distance_to_time(distance):
    rate = 0.005 # miles per second
    time = distance / rate # distance to time conversion
    elapsed_time = timedelta(hours=0, minutes= 0, seconds= time) # the time is calculated in seconds and the timedelta converts to minutes or hours.
    return elapsed_time # the elapsed time only calculates the current distance interval being considered.

# get_next_location() searches each row in the distance table to find an address match for address_now and address_next
# and returns the floating point value from the corresponding value in the distance_grid.
def get_next_location_distance(address_now,address_next):
    now = 0
    cnext = 0
    for i in range(len(distance_grid)):
        address = distance_grid [i][1] # this is the row index that the for loop will check during each iteration.
        address = address.split('(')[0].strip() # removes the zip code and spaces from the address to match the formatting of package data.
        if address_now == address:
            now =  i # provides the location of the matched address.
        if address_next == address:
            cnext = i # provides the location of the matched address.
    rownow = now
    rownext = cnext
    colnow = now + 2 # this is an offset to account for the 2 columns with name and adress info. With the offset the grid becomes symmetrical.
    colnext = cnext +2 # this is an offset to account for the 2 columns with name and adress info. With the offset the grid becomes symmetrical.
    if rownow  < rownext:
        distance_from = distance_grid[rownext][colnow] # if the current row is less than the next row, the column is increased and the column is kept to avoid the blank fields in the matrix.
        return distance_from
    elif rownow > rownext:
        distance_from = distance_grid[rownow][colnext] # if the current row is greater than the next row, the column is increased and the column is decreased to the correct index.
        return distance_from
    elif (rownow == rownext) and (colnow == colnext): # condition will check if the adress is the same as the current address.
        return 0.0