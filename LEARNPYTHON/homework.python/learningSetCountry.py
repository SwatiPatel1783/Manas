"""
set does not allow the duplicate
set is not ordered
we can modify the set
"""

countries_set = {"India", "USA", "Russia", "UK", "Brazil"}

# Loop through the set
for country in countries_set:
    if country == "Brazil":
        print("Brazil is found.")
        break
    else:
         print(country)