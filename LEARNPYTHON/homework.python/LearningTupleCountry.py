"""
*Once created, the elements in a tuple cannot be modified, added, or removed. This immutability makes
tuples useful for fixed collections of items and can be used as keys in dictionaries, unlike lists.
*Tuples maintain the order of the elements, meaning the order in which
you put items in the tuple is preserved.
*Tuples can contain duplicate elements.
"""

countries_tuple = ("India", "USA", "Russia", "USA", "UK", "Brazil")

for country in countries_tuple:
    if country == "Brazil":
        print("Brazil is found.")
        break
    else:
        print(country)
