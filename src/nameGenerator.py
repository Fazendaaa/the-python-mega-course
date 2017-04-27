import random, string

#   ----------------------------   FUNCTIONS   -----------------------------   #

def generator( choice, limit ):
    str = ''
    vowels = 'aeiou'
    consonants = 'qwrtypsdfghjklzxcvbnm'

    for i in range( limit ):
        if 'v' == choice[ i ]:
            str += random.choice( vowels )
        elif 'c' == choice[ i ]:
            str += random.choice( consonants )
        elif 'l' == choice[ i ]:
            str += random.choice( string.ascii_lowercase )
        else:
            str += choice[ i ]

    return str

#   ------------------------------   MAIN   --------------------------------   #

def main( limit=3 ):
    choice = [ None ] * limit
    for i in range( limit ):
        choice[ i ]= input( "What letter do you want?\n'v'.vowels;\n'c'.\
consoants;\n'l'. anyone.\n" )

    print( generator( choice, limit ) )

main( )

#   ------------------------------   EOF   ---------------------------------   #
