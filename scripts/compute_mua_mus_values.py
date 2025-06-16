from glob import glob
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

PATH = r"W:\Group\Data\20250611_OpenQPATData/"

PATH_INVISION_LABELS = f"{PATH}/invision/labels/"
PATH_INVISION_MUA = f"{PATH}/invision/mua/"
PATH_INVISION_MUSP = f"{PATH}/invision/musp/"
WAVELENGTHS = [700, 750, 800, 850, 900]

phantoms = [Path(f).stem for f in glob(f"{PATH_INVISION_LABELS}/*.npy")]

muas_background = []
muas_inclusions = []
musps = []

for phantom in phantoms:
    labels = np.load(f"{PATH_INVISION_LABELS}/{phantom}.npy")
    for wl in WAVELENGTHS:
        mua = np.load(f"{PATH_INVISION_MUA}/{phantom}_{wl}.npy")
        musp = np.load(f"{PATH_INVISION_MUSP}/{phantom}_{wl}.npy")

        muas_background += list(np.reshape(np.unique(mua[labels == 1]), (-1)))
        muas_inclusions += list(np.reshape(np.unique(mua[labels > 1]), (-1)))
        musps += list(np.reshape(np.unique(musp[labels > 0]), (-1)))

print("BG MUA:", np.min(muas_background), np.max(muas_background))
print("INC MUA:",np.min(muas_inclusions), np.max(muas_inclusions))
print("MUSP:", np.min(musps), np.max(musps))

fig, ax = plt.subplots(1, 3, figsize=(10, 3.5), layout="constrained")
ax[0].hist(muas_background, bins=15)
ax[0].set_ylabel("Frequency", fontweight="bold")
ax[0].set_xlabel("Absorption Coefficient (Background) [cm$^{-1}$]", fontweight="bold")

ax[1].hist(muas_inclusions, bins=15)
ax[1].set_xlabel("Absorption Coefficient (Inclusions) [cm$^{-1}$]", fontweight="bold")

ax[2].hist(musps, bins=15)
ax[2].set_xlabel("Reduced Scattering Coefficient (All) [cm$^{-1}$]", fontweight="bold")

for axis in ax:
    axis.spines[["top", "right"]].set_visible(False)
plt.savefig("../visualisations/value_distributions.pdf")
plt.close()