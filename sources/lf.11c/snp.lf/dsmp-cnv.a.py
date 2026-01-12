import ipaddress
import sys
import datetime
import random



# main section

with open("data.xyz", "rb") as binary_file:
    # Read the entire file into a byte array
    byte_array = binary_file.read()

    # Loop through each byte in the byte array
    for byte in byte_array:
        # Do something with the byte
        print(byte)