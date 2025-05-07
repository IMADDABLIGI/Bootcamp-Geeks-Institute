my_fav_numbers = set()

my_fav_numbers.add(911)
my_fav_numbers.add(992)

my_fav_numbers.remove(992)

friend_fav_numbers = {44, 33, 7, 1, 33}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)
