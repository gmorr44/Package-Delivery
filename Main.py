from datetime import timedelta
from Packages import get_hashtable,get_package_status
from DeliveryTrucks import get_total_mileage, deliver_packages, set_stop_time



print("Welcome to the T.S.P. Parcel Service")
# welcome message will present the choices for the reports that can be ran.
def welcome():
    print()
    print('**** Please Select An Option From The Menu Below: ****')
    print('1 = Display Status And Total Mileage Of All Packages At End Of Day ')
    print('2 = Display Status Of All Packages At Specific Time. ')
    print('3 = Display Status Of Specific Package At Specific Time. ')
    print('4 = Exit ')

count = 1 # keeps the while loop going until choice 4 is selected to exit.

while count != 0:
    welcome() # Displays the welcome message.
    selection = int(input('Please Enter The Number Corresponding To Your Selection: ')) # user input selection from menu.


    if selection == 1 or selection == 2 or selection == 3 or selection == 4:
        if selection == 1:
            try:
                set_stop_time(timedelta(hours=17, minutes=00, seconds=0))# sets stop time for 17:00:00 which represents end of day.
                deliver_packages()
                print()
                i = 1
                while i <= len(get_hashtable().map): # iterates through all packages and prints the status of all packages.
                    status = get_package_status(i) # calls the getter method to access package status.
                    print('Package #' + str(i) + ' Status = ' + status)
                    i += 1
                print()
                print('The Total Distance To Deliver All Packages Was: ' + str(get_total_mileage()) + ' Miles') # displays the total mileage of all package deliveries.
            except:
                print('****Please Re-Enter Your Selection In The Correct Format****')

        if selection == 2:
            try:
                print()
                time_selection = input('Please Enter The Time You Would Like To Check In HH:MM:SS :')
                print()
                hour = int(time_selection.split(':')[0])
                minute = int(time_selection.split(':')[1])
                second = int(time_selection.split(':')[2])
                set_stop_time(timedelta(hours=hour, minutes=minute, seconds=second)) # the stop time is a breaking point to stop
                deliver_packages()                                                   # the package deliveries which stops time and distance calculations
                i = 1
                while i <= len(get_hashtable().map):
                    status = get_package_status(i)
                    print('Package #' + str(i) + ' Status = ' + status)
                    i += 1
                print()
            except:
                print()
                print('****Please Re-Enter Your Selection In The Correct Format****')

        if selection == 3:
            try:
                print()
                package_id = int(input('Please Enter The Package Id:'))
                print()
                time_selection = input('Please Enter The Time You Would Like To Check In HH:MM:SS :')
                hour = int(time_selection.split(':')[0])
                minute = int(time_selection.split(':')[1])
                second = int(time_selection.split(':')[2])
                set_stop_time(timedelta(hours=hour, minutes=minute, seconds=second))# the stop time is a breaking point to stop
                deliver_packages()                                                  # the package deliveries which stops time and distance calculations
                status = get_package_status(package_id)
                print()
                print('Package #' + str(package_id) + ' Status = ' + status)
                print()

            except:
                print()
                print('****Please Re-Enter Your Selection In The Correct Format****')

        if selection == 4:
            exit()
    # catches any inputs that are not correct for the menu selection.
    else:
        print()
        print('****Your Selection Was Invalid!****')
        print('Please Enter A Valid Menu Selection To Continue.')

