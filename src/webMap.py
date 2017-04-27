import folium
import pandas

#   ----------------------------   FUNCTIONS   -----------------------------   #

def color( cap ):
    if cap in range( 0, 10_000 ):
        col = 'green'
    if cap in range( 10_000, 30_000 ):
        col = 'yellow'
    else:
        col = 'red'
    return col

#   ------------------------------   MAIN   --------------------------------   #

#   Brasilia coordinates
map = folium.Map( location = [ -15.7942, -47.8825 ], zoom_start = 5 )
stadiums = pandas.read_csv( './input/brazilianStadiums.csv' )

for lat, lon, name in zip( stadiums[ 'LAT' ], stadiums[ 'LON' ],
                           stadiums[ 'NAME' ] ):
    map.add_child( folium.Marker( location = [ lat, lon ],
                   popup = name, icon = folium.Icon( color( 10_000 ) ) ) )

map.save( outfile = './output/webMap.html' )

#   ------------------------------   EOF   ---------------------------------   #
