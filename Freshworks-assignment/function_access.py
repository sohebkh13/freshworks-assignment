from socket import timeout

import function_codes as fc


fc.create("freshworks", 25)
# to create a key with key_name,value given and with no time-to-live property


fc.create("assignment", 70, 3600)
# to create a key with key_name,value given and with time-to-live property value given(number of seconds)


fc.read("freshworks")
# it returns the value of the respective key in JSON object format 'key_name:value'


fc.read("assignment")
# it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


fc.create("freshworks", 50)

# it returns an ERROR since the key_name already exists in the database
# To overcome this error
# either use modify operation to change the value of a key
# or use delete operation and recreate it


fc.modify("freshworks", 55)
# it replaces the initial value of the respective key with new value


fc.delete("assignment")
# it deletes the respective key and its value from the database(memory is also freed)

# we can access these using multiple threads like
t1 = fc.Thread(target=(fc.create or fc.read or fc.delete), args=("freshworls", 50, 3600))  # as per the operation
t1.start()

t2 = fc.Thread(target=(fc.create or fc.read or fc.delete), args=("assignment"))  # as per the operation
t2.start()
