# Array of bytes from an int
# when an int is passed as an arg it creates an array
# of that size and init the area to null bytes
magic_number = 42

ba = bytearray(magic_number)

print(ba)


# Array of bytes from a str 
# when a str is passed we have to provide the encoding
# so we will use utf-8
magic_str = "forty-two"

# Provide the encoding along with string
ba = bytearray(magic_str, 'utf-8')

print(ba)


# Array of bytes from a list
# when a list is passed it returns the mutable sequence of bytes
magic_list = [42, 255, 6]

ba = bytearray(magic_list)

print(ba)


# No param
# when no praram is passed it creates an array of size 0 or empty
ba = bytearray()

print(ba)