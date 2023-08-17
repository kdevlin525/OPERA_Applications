import os, glob
from osgeo import gdal
import numpy as np
from scipy import signal

workdir = '/data/krd86/cropped/'
# load in dates
dates = [os.path.basename(x) for x in glob.glob(workdir+"SLC_vv/2*")]
dates = sorted(dates)
nd = len(dates)

driver=gdal.GetDriverByName('ISCE')

# size of entire SLC
az0 = 0
daz= 3500
rg0 = 0
drg = 30000

# a better window (Gaussian kernel)
stdrg = 12
stdaz = 4
kernlenrg = 3*stdrg+1
kernlenaz = 3*stdaz+1
gkernrg = signal.gaussian(kernlenrg, std=stdrg).reshape(kernlenrg, 1)
gkernaz = signal.gaussian(kernlenaz, std=stdaz).reshape(kernlenaz, 1)
wind2d = np.outer(gkernaz, gkernrg)
wind2d = wind2d/np.sum(wind2d)

slc1 = np.ndarray([daz,drg],'complex')
slc2 = np.ndarray([daz,drg],'complex')

for k in np.arange(nd-1): 
    ds1 = gdal.Open(workdir+"SLC_vv/"+dates[k]+"/"+dates[k]+".slc.full", gdal.GA_ReadOnly)
    ds2 = gdal.Open(workdir+"SLC_vv/"+dates[k+1]+"/"+dates[k+1]+".slc.full", gdal.GA_ReadOnly)
    slc1[:,:] = ds1.GetRasterBand(1).ReadAsArray(rg0,az0,drg,daz)
    slc2[:,:] = ds2.GetRasterBand(1).ReadAsArray(rg0,az0,drg,daz)

    # full res coherence
    a   = slc1*np.conj(slc1)
    b   = slc2*np.conj(slc2)
    ifg   = slc1*np.conj(slc2)
    ca  = abs(ifg)      
    asum = signal.convolve2d(a, wind2d, mode='same')
    bsum = signal.convolve2d(b, wind2d, mode='same')
    csum = signal.convolve2d(ifg, wind2d, mode='same')
    cmag = signal.convolve2d(ca, wind2d, mode='same')  
    #cpx3 = csum/np.sqrt(asum*bsum) #alternative def of coherence
    cpx3 = csum/cmag
    coh   = abs(cpx3)
    coh[np.isnan(coh)] = 0

