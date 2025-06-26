import numpy as np
import matplotlib.pyplot as plt

#FIXME: Replace this path with the path to the downloaded dataset
PATH = r"W:\Group\Data\20250611_OpenQPATData\DIS\processed"

MATERIALS = ["T.5.14", "T.5.6", "T.5.13"]
COLORS = ["#D81B60", "#1E88E5", "#FFC107", "#004D40"]

fig, ax = plt.subplots(1, 2, layout="constrained", figsize=(8, 4))

for material, color in zip(MATERIALS, COLORS):
    dis_data = np.load(f"{PATH}/{material}.a/{material}.npz")

    # Read all the data fields from the file
    wavelengths = dis_data["wavelengths"]
    absorption = dis_data["mua"]
    absorption_std = dis_data["mua_std"]
    reduced_scattering = dis_data["mus"] * (1-dis_data["g"])
    reduced_scattering_std = dis_data["mus_std"]* (1-dis_data["g"])

    ax[0].plot(wavelengths, absorption, c=color, label=material)
    ax[0].fill_between(wavelengths, absorption-absorption_std, absorption+absorption_std, color=color, alpha=0.2)
    ax[1].plot(wavelengths, reduced_scattering, c=color, label=material)
    ax[1].fill_between(wavelengths, reduced_scattering - reduced_scattering_std,
                       reduced_scattering + reduced_scattering_std, color=color, alpha=0.2)

for axis in ax:
    axis.spines[["top", "right"]].set_visible(False)

ax[0].legend()
ax[1].legend()

ax[0].set_xlabel("Wavelength [nm]", fontweight="bold")
ax[1].set_xlabel("Wavelength [nm]", fontweight="bold")
ax[0].set_ylabel("Absorption Coefficient [cm$^{-1}$]", fontweight="bold")
ax[1].set_ylabel("Reduced Scattering Coefficient [cm$^{-1}$]", fontweight="bold")
plt.savefig("dis_example.pdf", dpi=300)
plt.show()

