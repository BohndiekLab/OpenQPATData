import numpy as np
import pacfish as pf

PATH = r"W:\Group\Data\20250611_OpenQPATData/"
DEVICE = "invision"
WAVELENGTH = 800
PHANTOM = "P.5.6.2"

# Read the segmentation masks
labels = np.load(f"{PATH}/{DEVICE}/labels/{PHANTOM}.npy")

# Read the filtered backprojection reconstructions
recon = np.load(f"{PATH}/{DEVICE}/recon/{PHANTOM}_{WAVELENGTH}.npy")

# Read the absorption coefficients
absorption = np.load(f"{PATH}/{DEVICE}/mua/{PHANTOM}.npy")

# Read the scattering coefficients
reduced_scattering = np.load(f"{PATH}/{DEVICE}/musp/{PHANTOM}.npy")

# Read the time series data
# FIXME: This data does not exist in the SVOT system: no time series data was shared as the files are huge.
raw = np.squeeze(pf.load_data(f"{PATH}/{DEVICE}/raw/{PHANTOM}_{WAVELENGTH}_ipasc.hdf5").binary_time_series_data)
