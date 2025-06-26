# Code supplementing the paper OpenQPATData: Measurements of tissue-mimicking phantoms with ground truth labels for quantitative photoacoustic imaging

Welcome to the repository accompanying the [OpenQPATData dataset](https://doi.org/10.5281/zenodo.14044853),
a multi-device photoacoustic imaging dataset of 30 tissue-mimicking phantoms,
imaged with known optical properties.
This repository contains code examples, visualization scripts,
and interpolation tools to explore and utilize the dataset
for algorithm development and validation in quantitative photoacoustic imaging (qPAI).

## What’s in the Dataset?

- **30 tissue-mimicking phantoms** with varied optical absorption and scattering properties.
- **Multi-device imaging** from:
  - MSOT InVision 256-TF (iThera Medical)
  - TROPUS (Transmission–Reflection Optoacoustic and Ultrasound)
  - SVOT (Spiral Volumetric Optoacoustic Tomography)
- **Ground truth labels** of absorption (`μa`) and reduced scattering (`μs′`) via double-integrating-sphere measurements.
- **Manual segmentations** and interpolated 3D digital twins for each phantom.

## Repository Structure

```
OpenQPATData/
├── examples/          # Minimal working examples for loading the dataset
├── scripts/           # SVOT 2D slice interpolation to full 3D segmentations
├── visualisations/    # Scripts to reproduce all figures from the paper
```

### examples/
Contains Python scripts demonstrating how to:

`read_DIS_data.py`: read the double integrating sphere measurement data.

`read_PAI_data.py`: read the photoacoustic imaging data, reference segmentations,
and reference absorption and scattering distributions.

### scripts/
`interpolate_svot_segmentations.py`: Reconstructs full 3D segmentation masks from
sparse annotated slices for the SVOT system.

### visualisations/
Scripts to reproduce all main figures from the accompanying publication, including device-specific examples and property distributions.

## Dataset Access

The full dataset is available open access at:

 **[https://doi.org/10.5281/zenodo.14044853](https://doi.org/10.5281/zenodo.14044853)**

Dataset folders include:

- `DIS/`: Raw and processed data from double-integrating-sphere optical property measurements.
- `invision/`, `tropus/`, `svot/`: Imaging data from three devices, including reconstructions, labels, and optical property maps.
- `material_mapping.json`: Links segmentation labels to material-specific optical properties.

Data formats:
- Raw time series: [IPASC format](https://github.com/ipasc/ipasc_toolbox)
- Reconstructed images and labels: `.npy` (NumPy arrays)

## Citation

If you use this dataset or code in your research, please cite the accompanying paper.

## Acknowledgements

This work was supported by the DFG (GR 5824/1 and GR 5824/2),
Cancer Research UK (A29580), and others.
See the full paper for the complete author list and funding information.


---
License: [MIT](LICENSE)
Dataset License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
