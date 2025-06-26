import numpy as np

PATH = r"W:\Group\Data\20250611_OpenQPATData\DIS\processed"
MATERIAL = "T.5.19"

# The file without the ".a" or ".b" label is the one that combines the two measurements
dis_data = np.load(f"{PATH}/{MATERIAL}.a/{MATERIAL}.npz")

# Read all the data fields from the file
wavelengths = dis_data["wavelengths"]
absorption = dis_data["mua"]
absorption_std = dis_data["mua_std"]
scattering = dis_data["mus"]
scattering_std = dis_data["mus_std"]
scattering_exponential_fit = dis_data["mus_fit"]
anisotropy = dis_data["g"]
