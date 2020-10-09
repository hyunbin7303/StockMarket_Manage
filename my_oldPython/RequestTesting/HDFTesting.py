import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

USE_NETCDF4 = False

def run(FILE_NAME):

    DATAFIELD_NAME = 'Temperature_MW_A'
    if USE_NETCDF4:
        from netCDF4 import Dataset
        nc = Dataset(FILE_NAME)

        # The variable has a fill value,
        # so netCDF4 converts it to a float64 masked array for us.
        data = nc.variables[DATAFIELD_NAME][0,:,:]
        latitude = nc.variables['Latitude'][:]
        longitude = nc.variables['Longitude'][:]

    else:
        from pyhdf.SD import SD, SDC
        hdf = SD(FILE_NAME, SDC.READ)

        # List available SDS datasets.
        # print hdf.datasets()

        # Read dataset.
        data3D = hdf.select(DATAFIELD_NAME)
        data = data3D[0,:,:]

        # Read geolocation dataset.
        lat = hdf.select('Latitude')
        latitude = lat[:,:]
        lon = hdf.select('Longitude')
        longitude = lon[:,:]

        # Handle fill value.
        attrs = data3D.attributes(full=1)
        fillvalue=attrs["_FillValue"]

        # fillvalue[0] is the attribute value.
        fv = fillvalue[0]
        data[data == fv] = np.nan
        data = np.ma.masked_array(data, np.isnan(data))


    # Draw an equidistant cylindrical projection using the low resolution
    # coastline database.
    m = Basemap(projection='cyl', resolution='l',
                llcrnrlat=-90, urcrnrlat = 90,
                llcrnrlon=-180, urcrnrlon = 180)
    m.drawcoastlines(linewidth=0.5)
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
    m.pcolormesh(longitude, latitude, data, latlon=True, alpha=0.90)
    cb = m.colorbar()
    cb.set_label('Unit:K')
    basename = os.path.basename(FILE_NAME)
    plt.title('{0}\n {1} at TempPrsLvls=0'.format(basename, DATAFIELD_NAME))
    fig = plt.gcf()
    # plt.show()
    pngfile = "{0}.py.png".format(basename)
    fig.savefig(pngfile)

if __name__ == "__main__":

    # If a certain environment variable is set, look there for the input
    # file, otherwise look in the current directory.
    hdffile = 'AIRS.2003.02.05.L3.RetStd_H001.v6.0.12.0.G14112124328.hdf'
    try:
        hdffile = os.path.join(os.environ['HDFEOS_ZOO_DIR'], hdffile)
    except KeyError:
        pass

    run(hdffile)
