set_countries = {"col", "pan", "mex"}

size = len(set_countries)
print (size)

print ("col" in set_countries )
print ("pe" in set_countries)

# add
set_countries.add("pe")
print (set_countries)
set_countries.add("pe")
print (set_countries)

# update
set_countries.update({"ar", "chil", "pan"})
print(set_countries)

# remove
set_countries.remove("col")
print (set_countries)
set_countries.remove("ar")
print (set_countries)

#set_countries.remove("arg")
set_countries.discard("arg")
print(set_countries)

set_countries.add("arg")
print(set_countries)

set_countries.clear()
print(set_countries)
set_countries = (len(set_countries))
print (set_countries)

