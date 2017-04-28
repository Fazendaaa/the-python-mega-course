import time
from datetime import datetime as dt

hostPath = '/etc/hosts'
redirect = '127.0.0.1'
websiteList = [ 'www.facebook.com', 'facebook.com' ]

while True:
    begin = dt( dt.now().year, dt.now().month, dt.now().day, 8 )
    end = dt( dt.now().year, dt.now().month, dt.now().day, 16 )

    if begin < dt.now() < end:
        print( 'Working hours...' )
        with open( hostPath, 'r+' ) as file:
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write( redirect + ' ' + website + '\n' )
    else:
        print( 'Good to go...' )
        with open( hostPath, 'r+' ) as file:
            content = file.readlines()
            file.seek( 0 )
            for line in content:
                if not any( website in line for website in websiteList ):
                    file.write( line )
            file.truncate()
    #   each five minutes
    time.sleep( 300 )


#   ------------------------------   EOF   ---------------------------------   #
