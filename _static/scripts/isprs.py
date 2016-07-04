#!/usr/bin/env python

#%module
#% description: Imports lidar and orthophoto tile, create mask and interpolate DEM.
#%end

#%option
#% key: tile
#% description: Tile name (eg. TANV37)
#% multiple: yes
#% required: yes
#%end
#%option
#% key: resolution
#% description: Output DEM resolution (in meters)
#% type: float
#% answer: 1.0
#%end

import sys
import atexit
import grass.script as grass

def cleanup():
    grass.run_command('g.remove', type='raster', pattern='{}.*'.format(tile))
    grass.run_command('r.mask', flags='r')
    
def import_lidar(tile):
    grass.message('Importing lidar data...')
    grass.run_command('v.in.lidar', flags='ot', input='pr_{}_5g.laz'.format(tile),
                      output='pr_{}_5g'.format(tile))

def import_orhtophoto(tile):
    grass.message('Importing orthophoto...')
    grass.run_command('r.import', flags='o', input='{}.tif'.format(tile), output=tile)
    grass.run_command('g.region', raster='{}.1'.format(tile))
    grass.run_command('r.composite', red='{}.1'.format(tile), green='{}.2'.format(tile),
                      blue='{}.3'.format(tile), output='{}.rgb'.format(tile))
    grass.run_command('r.neighbors' input='{}.rgb'.format(tile), output='{}.mode'.format(tile), method='mode')
    grass.run_command('r.mapcalc',
                      expression="{tile} = if ( isnull( {tile}.1 + {tile}.2 + {tile}.3 ), {tile}.mode, {tile}.rgb )".format(tile=tile))
    grass.run_command('r.colors' map=tile, raster='{}.rgb'.format(tile))

def create_dem(tile, resolution):
    grass.message('Creating DEM...')
    grass.run_command('r.mask', input=tile)
    grass.run_command('g.region', res=resolution, flags='a')
    grass.run_command('v.surf.rst', input='pr_{}_5g'.format(tile), elevation='dem_{}'.format(tile),
                      slope='slope_{}'.format(tile), npmin=80 tension=20 smooth=1)

def main():
    os.environ['GRASS_OVERWRITE'] = '1'
    os.environ['GRASS_VERBOSE'] = '0'
    
    # TODO: more cores
    for tile in options['tile'].split(','):
        grass.message('Processing tile {}...'.format(tile))
        import_lidar(tile)
        import_orthophoto(tile)
        create_dem(tile, options['resolution'])
        
    return 0

if __name__ == "__main__":
    atexit.register(cleanup)
    sys.exit(main())
