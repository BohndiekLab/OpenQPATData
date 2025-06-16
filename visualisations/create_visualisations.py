import numpy as np
import matplotlib.pyplot as plt
import pacfish as pf
from utils.histogram_colorbar import add_histogram_colorbar

PATH = r"W:\Group\Data\20250611_OpenQPATData/"
DEVICE = "svot"

PATH_LABELS = f"{PATH}/{DEVICE}/labels/"
PATH_RECON = f"{PATH}/{DEVICE}/recon/"
PATH_RAW = f"{PATH}/{DEVICE}/raw/"
WAVELENGTH = 800
PHANTOM = "P.5.6.2"
COLOR="white"
ASPECT = 0.125
if DEVICE == "tropus":
    ASPECT = 0.244


fig, ax = plt.subplots(1, 3, figsize=(8, 3), layout="constrained")

if DEVICE == "svot":
    labels = np.load(f"{PATH_LABELS}/{PHANTOM}.npz")["data"]
    recon = np.load(f"{PATH_RECON}/{PHANTOM}_{WAVELENGTH}.npy")
    _data = np.max(recon, axis=1).T
    ax[0].imshow(_data)
    add_histogram_colorbar(ax[0], _data, label="p$_0$", color=COLOR)
    ax[0].set_title("Reconstruction (x/z MIP)")

    _data = np.max(recon, axis=2).T
    ax[1].imshow(_data)
    add_histogram_colorbar(ax[1], _data, label="p$_0$", color=COLOR)

    ax[1].set_title("Reconstruction (x/y MIP)")
    ax[2].imshow(labels[:, :, 180].T, cmap="magma")
    ax[2].set_title("Reference Labels")
else:
    labels = np.load(f"{PATH_LABELS}/{PHANTOM}.npy")
    recon = np.load(f"{PATH_RECON}/{PHANTOM}_{WAVELENGTH}.npy")
    raw = np.squeeze(pf.load_data(f"{PATH_RAW}/{PHANTOM}_{WAVELENGTH}_ipasc.hdf5").binary_time_series_data)
    ax[0].imshow(raw.T, aspect=ASPECT, cmap="gray")
    add_histogram_colorbar(ax[0], raw.T, label="p(t)", color=COLOR)
    ax[0].set_title("Time Series Data")
    ax[1].imshow(recon.T)
    add_histogram_colorbar(ax[1], recon.T, label="p$_0$", color=COLOR)
    ax[1].set_title("Reconstruction")
    ax[2].imshow(labels.T, cmap="magma")
    ax[2].set_title("Reference Labels")

for axis in ax:
    axis.axis('off')

plt.savefig(f"../visualisations/example_{DEVICE}.pdf")
plt.show()
plt.close()