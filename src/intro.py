greeting = "Hello"
print( greeting )
#print( input( "Write anything: " ) )
number = 3
print( number )
age = input( "Enter your age: " )
new_age = int( age ) + 20.0
print( new_age )

print( 3**2 )

print( "Methods to use in strings:" )
#   The next function only works in Phtyon console
#dir( greeting )
#print( "Methods to use in numbers:" )
#dir( number )

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do \
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim \
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea \
commodo consequat."

print( lorem[ 0:2 ])

lists = [ "J", 2 ]
print( type( lists[ 0 ] ) )
print( type( lists[ 1 ] ) )

tuples = ( 1, 2.3, "h" )
print( tuples[ 0 ] )
print( tuples[ 1 ] )

dictionary = { "key": "value", "name": "farm",
               "cities": [ "Sao Paulo", "Sao Carlos" ] }
print( dictionary[ "name" ] )
print( dictionary[ "cities" ][ 1 ] )

def currencyConverter( rate, coin ):
    return rate*coin

print( "3 Real to Dollars: " + str( currencyConverter( 3.18, 3 ) ) )

a = 4
if 3 < a and 5 > a:
    print( "'a' is between 3 and 5." )
else:
    print( "Out of bounds." )

fruits = [ "banana", "apple", "passion fruit", "star fruit", "lime" ]

print( "\nFruits:" )
for fruit in fruits:
    if "fruit" in fruit:
        print( fruit )

number = 0
while 5 != number:
    number = int( input( "Type number: " ) )

print( "You're logged in.\n" )

names = [ 'jack', 'edward', 'obama' ]
surnames = [ 'sparrow', 'elric', 'barack' ]

for n,s in zip( names, surnames ):
    print( n + ' ' + s )

#   ---   FILE   ---   #

file = open( "example.txt", 'w' )
file.write( lorem + "\n" )
file.close()

# append
file = open( "example.txt", 'a' )
file.write( "EOF\n" )
file.close()

# with
with open( "example.txt", 'a+' ) as file:
    file.write( "APPEND\n" )

#   ---   EOF   ---   #
