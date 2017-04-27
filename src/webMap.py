import folium
import pandas

#   ----------------------------   FUNCTIONS   -----------------------------   #

def color( cap ):
    if cap in range( 0, 55_000 ):
        col = 'red'
    elif cap in range( 55_000, 70_000 ):
        col = 'green'
    else:
        col = 'blue'
    return col

#   ------------------------------   MAIN   --------------------------------   #

#   Brasilia coordinates
map = folium.Map( location = [ -15.7942, -47.8825 ], zoom_start = 5 )
stadiums = pandas.read_csv( './input/brazilianStadiums.csv' )
fg = folium.FeatureGroup( name = 'Brazilian stadiums' )

for lat, lon, name, cap in zip( stadiums[ 'LAT' ], stadiums[ 'LON' ],
                                stadiums[ 'NAME' ], stadiums[ 'CAPACITY' ] ):
    fg.add_child( folium.Marker( location = [ lat, lon ], popup = name,
                  icon = folium.Icon( color = color( cap ) ) ) )

map.add_child( fg )
map.add_child( folium.LayerControl( ) )
map.save( outfile = './output/webMap.html' )

#   ------------------------------   EOF   ---------------------------------   #
