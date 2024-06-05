# class str
#   methods: upper, lower, find
# object: city is an instance of class str
city = "Bourgoin-Jallieu"

# class list
#   methods: index, append
# objects:
#   cities is an instance of class list
#       contains 3 objects (instances) of class str
cities = [
    city,
    "Toulouse",
    "Pau",
]

for c in cities:
    print(c.upper())