from collections import namedtuple

"""
This is a basic use of namedtuples in python.
Currently working on a more robust use case.
"""

Human = namedtuple('Human', "name age hometown gender fav_drink")

courtney = Human('Courtney',22,'Greenwood',1,'La Croix Boi')

print(courtney._fields)

for key, value in courtney._asdict().items():
    print(key,value)
