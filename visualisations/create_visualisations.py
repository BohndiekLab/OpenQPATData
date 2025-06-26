import numpy as np
import matplotlib.pyplot as plt
import pacfish as pf
from utils.histogram_colorbar import add_histogram_colorbar

#FIXME: Replace this path with the path to the downloaded dataset
PATH = r"W:\Group\Data\20250611_OpenQPATData/"

#FIXME: Adjust this to switch between the three PAI devices
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


fig, ax = plt.subplots(1, 4, figsize=(10.67, 3), layout="constrained")

if DEVICE == "svot":
    labels = np.load(f"{PATH_LABELS}/{PHANTOM}.npz")["data"]
    recon = np.load(f"{PATH_RECON}/{PHANTOM}_{WAVELENGTH}.npy")
    _data = recon[180, :, :].T #np.max(recon, axis=1).T
    ax[0].imshow(_data, vmin=np.percentile(_data, 2), vmax=np.percentile(_data, 98))
    add_histogram_colorbar(ax[0], _data, label="p$_0$", color=COLOR)
    ax[0].plot([1, 359], [180, 180], color="red", linewidth=2)
    ax[0].set_title("Reconstruction (y/z)")
    ax[1].imshow(labels[180, :, :].T, cmap="magma")
    ax[1].set_title("Reference Labels (y/z)")

    _data = recon[:, :, 180].T #np.max(recon, axis=2).T
    ax[2].imshow(_data, vmin=np.percentile(_data, 2), vmax=np.percentile(_data, 98))
    add_histogram_colorbar(ax[2], _data, label="p$_0$", color=COLOR)
    ax[2].plot([180, 180], [1, 359], color="red", linewidth=2)
    ax[2].set_title("Reconstruction (x/y)")
    ax[3].imshow(labels[:, :, 180].T, cmap="magma")
    ax[3].set_title("Reference Labels (x/y)")
else:
    labels = np.load(f"{PATH_LABELS}/{PHANTOM}.npy")
    recon = np.load(f"{PATH_RECON}/{PHANTOM}_{WAVELENGTH}.npy")
    raw = np.squeeze(pf.load_data(f"{PATH_RAW}/{PHANTOM}_{WAVELENGTH}_ipasc.hdf5").binary_time_series_data)
    ax[0].imshow(raw.T, aspect=ASPECT, cmap="gray", vmin=np.percentile(raw, 2), vmax=np.percentile(raw, 98))
    add_histogram_colorbar(ax[0], raw.T, label="p(t)", color=COLOR)
    ax[0].set_title("Time Series Data")
    ax[1].imshow(recon.T)
    add_histogram_colorbar(ax[1], recon.T, label="p$_0$", color=COLOR, vmin=np.percentile(recon, 2), vmax=np.percentile(recon, 98))
    ax[1].set_title("Reconstruction")
    ax[2].imshow(labels.T, cmap="magma")
    ax[2].set_title("Reference Labels")

for axis in ax:
    axis.axis('off')

plt.savefig(f"../visualisations/example_{DEVICE}.pdf")
plt.show()
plt.close()