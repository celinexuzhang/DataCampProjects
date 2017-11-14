
#Index method
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")

# Use ind_ger to print out capital of Germany
capita = capitals[ind_ger]
print(capita)

#Dictionary method - don't need to import any package for 'dictionary'
#dict_name[key] result [value] -> key pair value
europe= {
     'spain':'madrid',
     'france':'paris',
     'germany':'berlin',
     'norway':'oslo',
 }
print('the capital of spain is ' + europe['spain'])

#check out which keys are in europe by calling the keys() method on europe. Print out the result.
print(europe.keys())
#Print out the value that belongs to the key 'norway'.
print(europe['norway'])

# keys in the dictionary need to be unique, example, if you added another capital(say ABC) for germany(other than berlin), the ley pair value of germany will change, from berline to ABC
#keys have to be immutable object, basically, the content of the objects cannot be changed after it created.
#string, boolean, integers, floats are immutable objects.
#However, the list is mutable objects, becasue you can change the content after it created.
europe= {
     'spain':'madrid',
     'france':'paris',
     'germany':'berlin',
     'norway':'oslo',
    'germany':'ABC'
 }
print(europe)
#I want to add the object to the europe
europe['China'] = 'beijing'
print(europe)
#double check if China is in the europe
print('China' in europe)
#update the key pair in the value
europe['germany']='berlin'
print(europe)
#remove China from europe
del(europe['China'])
print(europe)