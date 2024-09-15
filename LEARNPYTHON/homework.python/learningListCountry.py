"""
*A list is a mutable, ordered collection of items.lists can contain items of
different data types, including other lists.
* List Methods
append(item): Adds an item to the end of the list.
extend(iterable): Extends the list by appending elements from an iterable.
insert(index, item): Inserts an item at a specific position.
remove(item): Removes the first occurrence of an item.
pop([index]): Removes and returns an item at a given position (or the last item if index is not provided).
clear(): Removes all items from the list.
index(item): Returns the index of the first occurrence of an item.
count(item): Returns the number of occurrences of an item.
sort(key=None, reverse=False): Sorts the items in place.
reverse(): Reverses the items in place.
"""

countries_list = ["India","USA", "Russia", "UK", "Brazil"]

for x in countries_list:
    if x == "Brazil":
        print("Brazil is found")
        break
    else :
        print(x)