
cities_list = [
	{
		"name": "New York City",
		"country": "United States",
		"population": 20140000,
		"area": 1223.59
	},
	{
		"name": "Tokyo",
		"country": "Japan",
		"population": 37470000,
		"area": 2194.07,
	},
	{
		"name": "Los Angeles",
		"country": "United States",
		"population": 13200000,
		"area": 1299.01,
	},
	{
		"name": "Madrid",
		"country": "Spain",
		"population": 6790000,
		"area": 604.31,
	},
	{
		"name": "Osaka",
		"country": "Japan",
		"population": 19300000,
		"area": 5107.0,
	},
	{
		"name": "London",
		"country": "United Kingdom",
		"population": 14260000,
		"area": 8382.0,
	},
    {
		"name": "Blumenau",
		"country": "Brazil",
		"population": 360855,
		"area": 518.619,
	},
    {
		"name": "Florianopolis",
		"country": "Brazil",
		"population": 508826,
		"area": 675.400,
	},
    {
		"name": "Gaspar",
		"country": "Brazil",
		"population": 70793,
		"area": 386.776,
	}    
]

# Sort by population
cities_ex1_list = sorted(cities_list, key=lambda city: city['population'])
print("Sort by population")
print(cities_ex1_list)


# Sort by population DESCENDING
cities_ex2_list = sorted(cities_list, key=lambda city: -city['population'])
print("Sort by population DESCENDING")
print(cities_ex2_list)


# Sort by country, then by population
cities_ex3_list = sorted(cities_list, key=lambda city: (city['country'], city['population']))
print("Sort by country, then by population")
print(cities_ex3_list)


# Sort by country, then by name
cities_ex4_list = sorted(cities_list, key=lambda city: (city['country'], city['name']))
print("Sort by country, then by name")
print(cities_ex4_list)


# Sort by population density
cities_ex5_list = sorted(cities_list, key=lambda city: (city['population'] / city['area']))
print("Sort by population density")
print(cities_ex5_list)
