dhrumin = 43
lay = 25
jeet = 31

# Initialize the youngest person as None
youngest = None

# Find the youngest person
if dhrumin < lay and dhrumin < jeet:
    youngest = "Dhrumin"
elif lay < dhrumin and lay < jeet:
     youngest = "Lay"
else:
    youngest = "Jeet"

# Print out the result
print("The youngest person is lay.")

