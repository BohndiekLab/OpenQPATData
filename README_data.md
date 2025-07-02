# Data supplementing the paper OpenQPATData: Measurements of tissue-mimicking phantoms with reference labels for quantitative photoacoustic imaging research

**OpenQPATData** is a comprehensive dataset of 30 tissue-mimicking phantoms designed for benchmarking and advancing
**quantitative photoacoustic imaging (qPAI)**. It includes raw measurements, reconstructed images, ground-truth 
segmentations, and matched optical property maps from **three different photoacoustic systems**: MSOT InVision, 
TROPUS, and SVOT. The dataset supports research into acoustic and optical inverse problems, digital twin validation, 
and image quality assessment for photoacoustic imaging.

**Associated paper**: _Gröhl et al., OpenQPATData: Measurements of test objects with reference labels for quantitative 
photoacoustic imaging research_   
**Code Repository**: https://github.com/BohndiekLab/OpenQPATData  
**License**: CC-BY 4.0 (data), MIT (code)

## Authors and Affiliations

- **Janek Gröhl**  
  Department of Physics, University of Cambridge, United Kingdom  
  Cancer Research UK Cambridge Institute, University of Cambridge, United Kingdom  
  ENI-G, a Joint Initiative of the University Medical Center Göttingen and the Max Planck Institute for Multidisciplinary Sciences, Göttingen, Germany  

- **Sandeep Kumar Kalva**  
  Institute of Pharmacology and Toxicology and Institute for Biomedical Engineering, Faculty of Medicine, University of Zurich, Switzerland  
  Institute for Biomedical Engineering, Department of Information Technology and Electrical Engineering, ETH Zurich, Switzerland  
  Department of Biosciences and Bioengineering, Indian Institute of Technology Bombay, Mumbai, India  

- **Berkan Lafci**  
  Institute of Pharmacology and Toxicology and Institute for Biomedical Engineering, Faculty of Medicine, University of Zurich, Switzerland  
  Institute for Biomedical Engineering, Department of Information Technology and Electrical Engineering, ETH Zurich, Switzerland  

- **Francesca Di Cecio**  
  Department of Physics, University of Cambridge, United Kingdom  
  Cancer Research UK Cambridge Institute, University of Cambridge, United Kingdom  

- **Ran Tao**  
  Department of Physics, University of Cambridge, United Kingdom  
  Cancer Research UK Cambridge Institute, University of Cambridge, United Kingdom  

- **Thomas R. Else**  
  Department of Physics, University of Cambridge, United Kingdom  
  Cancer Research UK Cambridge Institute, University of Cambridge, United Kingdom  
  *Now at:* Department of Bioengineering, Imperial College London, United Kingdom  

- **Lorna Wright**  
  Department of Physics, University of Cambridge, United Kingdom  
  Cancer Research UK Cambridge Institute, University of Cambridge, United Kingdom  

- **Daniel Razansky**  
  Institute of Pharmacology and Toxicology and Institute for Biomedical Engineering, Faculty of Medicine, University of Zurich, Switzerland  
  Institute for Biomedical Engineering, Department of Information Technology and Electrical Engineering, ETH Zurich, Switzerland  

- **Sarah E. Bohndiek**  
  Department of Physics, University of Cambridge, United Kingdom  
  Cancer Research UK Cambridge Institute, University of Cambridge, United Kingdom  

## Data Repository Structure

```
OpenPATData/
│
├── material_mapping.json  # Maps segmentation labels to material IDs
│
├── DIS/                   # Double-Integrating-Sphere optical measurements
│   ├── processed/
│   │   └── T.5.1.a/
│   │   │   ├── T.5.1.npz       # Optical properties: mua, mus, g, std, etc.
│   │   │   └── T.5.1.png       # Visualization of absorption/scattering
│   │   └── ...
│   └── raw/
│       └── T.5.1.a/
│       │   ├── 1_R_OpenPort.txt        # Reflectance min
│       │   ├── 1_R_RefInPlace.txt      # Reflectance max
│       │   ├── 1_T_BlockBeam.txt       # Transmittance min
│       │   ├── 1_T_IncBeam.txt         # Transmittance max
│       │   ├── recipe.txt              # Phantom recipe
│       │   └── subfolders 1/..6/
│       │       ├── 1_R_SampInPlace.rxt
│       │       ├── 1_T_SampInPlace.txt
│       │       └── thickness.txt
│       └── ...
│
├── invision/              # MSOT InVision device data
│   ├── raw/               # IPASC-format time series (binary data shape: 256×2030×1×1)
│   ├── recon/             # Reconstructed images (NumPy array shape: 288×288)
│   ├── labels/            # Manual segmentations (NumPy array shape: 288×288)
│   ├── mua/               # µa maps per wavelength (NumPy array shape: 288×288)
│   └── musp/              # µs' maps per wavelength (NumPy array shape: 288×288)
│
├── tropus/                # TROPUS device data
│   ├── raw/               # IPASC-format time series (binary data shape: 512×2094×1×1)
│   ├── recon/             # Reconstructed images (NumPy array shape: 288×288)
│   ├── labels/            # Manual segmentations (NumPy array shape: 288×288)
│   ├── mua/               # µa maps per wavelength (NumPy array shape: 288×288)
│   └── musp/              # µs' maps per wavelength (NumPy array shape: 288×288)
│
├── svot/                  # SVOT 3D system data
│   ├── recon/             # Reconstructed volumes (NumPy array shape: 360×360×360)
│   ├── labels/            # Interpolated 3D segmentation volumes (NumPy array shape: 360×360×360)
│   ├── mua/               # µa volumes (NumPy array shape: 360×360×360)
│   └── musp/              # µs' volumes (NumPy array shape: 360×360×360)
```

## Data Overview

- **Raw Measurements**: IPASC format `.hdf5` files (readable via [PACFISH](https://github.com/IPASC/PACFISH))
- **Reconstructions**: 2D (288×288) or 3D (360×360×360) NumPy arrays
- **Optical Property Maps**: Absorption (µa) and Reduced Scattering (µs′) from DIS system
- **Segmentations**: Label masks for all devices (2D or 3D depending on system)
- **Calibration Data**: Reflectance/transmittance data, thickness, and phantom recipes

## Code Examples

See our [GitHub repo](https://github.com/BohndiekLab/OpenQPATData) for:
- Example scripts to load `.npz`, `.npy`, and `.hdf5` data
- 2D-to-3D interpolation for SVOT labels
- Visualization tools to replicate figures from the paper

## Usage Guideline

If you use this dataset, please cite the associated paper.

## Contact

For questions or feedback, please contact the corresponding author
