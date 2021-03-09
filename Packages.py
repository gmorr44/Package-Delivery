import csv
from HashTable import HashTable

hashtable = HashTable()
with open('PackageData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery_deadline = row[5]
        mass_kilo = row[6]
        notes = row[7]
        package_status = 'At The Hub'

        value = [id, address, city, state, zip, delivery_deadline, mass_kilo, notes, package_status]
        key = int(id)
        hashtable.add_package(key, value)

# Getter Method that returns the hashmap object
def get_hashtable():
    return hashtable

# Below getter methods can access all items for the hashtable together.
def get_package (key):
    return hashtable.get_package(key)
# Below getter methods can access each item for the hashtable seperately.
def get_package_id (key):
    return hashtable.get_package(key)[0]

def get_package_address (key):
    return hashtable.get_package(key)[1]

def get_package_city (key):
    return hashtable.get_package(key)[2]

def get_package_state(key):
    return hashtable.get_package(key)[3]

def get_package_zip(key):
    return hashtable.get_package(key)[4]

def get_package_delivery_deadline(key):
    return hashtable.get_package(key)[5]

def get_package_mass_kilo(key):
    return hashtable.get_package(key)[6]

def get_package_notes(key):
    return hashtable.get_package(key)[7]

def get_package_status(key):
    return hashtable.get_package(key)[8]

# The following setter methods allow access to change each items value from the hashmap.
def set_package_address (key, address):
    hashtable.get_package(key)[1] = address

def set_package_city (key, city):
    hashtable.get_package(key)[2] = city

def set_package_state(key,state):
    hashtable.get_package(key)[3] = state

def set_package_zip(key, zip):
    hashtable.get_package(key)[4] = zip

def set_package_delivery_deadline(key,delivery):
    hashtable.get_package(key)[5] = delivery

def set_package_mass_kilo(key, mass):
    hashtable.get_package(key)[6] = mass

def set_package_notes(key, notes):
    hashtable.get_package(key)[7] = notes

def set_package_status(key,status):
    hashtable.get_package(key)[8] = status