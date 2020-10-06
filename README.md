# COVID-CT-MD
<h4>A COVID-19 CT Scan Dataset Applicable in Machine Learning and Deep Learning</h4>

The COVID-CT-MD dataset contains volumetric chest CT scans of <b>171 patients positive for COVID-19 infection, 60 patients with CAP (Community Acquired Pneumonia), and 76 normal patients</b>. COVID-19 cases are collected from February 2020 to April 2020, whereas CAP cases and normal cases are collected from April 2018 to December 2019 and January 2019 to May 2020, respectively. Diagnosis of COVID-19 infection is based on positive real-time Reverse Transcription Polymerase Chain Reaction (rRT-PCR) test results, clinical parameters, and CT scan manifestations identified by three thoracic radiologists. Diagnosis for CAP and normal cases was confirmed using clinical laboratory tests, and CT scans. A subset of 55 COVID-19, and 25 CAP cases were analyzed by the radiologists to identify and label slices with evidence of infection. The labeled subset of the data contains <b>4,993 number of slices demonstrating infection and 18,416 number of slices without infection.</b>

COVID-CT-MD dataset is accessible through Figshare: <a href="https://figshare.com/s/c20215f3d42c98f09ad0">https://figshare.com/s/c20215f3d42c98f09ad0</a>

The detailed desription of the dataset is available at <a href="https://arxiv.org/abs/2009.14623">https://arxiv.org/abs/2009.14623</a>

To respect the patients’ privacy and comply with the Ethical codes and policies, all the CT studies in the COVID-CT-MD dataset are de-identified and only gender and age of the patients are preserved in the dataset. The brief distribution of the COVID-CT-MD dataset is shown in the following table:

| Table | Cases | Sex | Age(year) |
| ----- | ---------------- | ------- | --- |
| COVID-19 | 171 | 108 M/63 F | 51.6 ± 14.6 |
| CAP | 60 | 35 M/25 F | 57.7 ± 21.7 |
| Normal | 76 | 40 M/36 F | 43.4 ± 14.1 |

<img src="https://github.com/ShahinSHH/COVID-CT-MD/blob/main/Figures/slices.jpg" width="400" height="400" />

## Data Structure
The hierarchical list below shows the structure of the COVID-CT-MD dataset shared through Figshare . COVID-19, CAP and
Normal subjects are placed in separate folders, within which patients are arranged in folders, followed by CT scan slices in DICOM format.

* Main Folder
  * COVID-19 subjects
    * Subject-ID
      * Slice-ID.dcm
  * CAP subjects
    * Subject-ID
      * Slice-ID.dcm
  * Normal subjects
    * Subject-ID
      * Slice-ID.dcm
  

## Labels
* <b>Index.csv</b> : specifies the patients having slice-level and lobe-level labels. The indices given to patients in “Index.csv” file are then used in “Slice-level-labels.npy” and “Lobe-level-labels.npy” to indicate the slice and lobe labels.
* <b>Slice-level-labels.npy</b> : a 2D binary Numpy array in which the existence of infection in a specific slice is indicated by 1 and the lack of infection is shown by 0. The first dimension represents the case index and the second one represents the slice numbers.
* <b>Lobe-level-labels.npy</b> : a 3D binary Numpy array in which the existence of infection in a specific lobe and slice is determined by 1 in the corresponding element of the array. Like the slice-level array. The two first dimensions represent the case index and slice numbers respectively. The third dimension shows the lobe indices which are specified as follows:
  * 0 : Left Lower Lobe (LLL)
  * 1 : Left Upper Lobe (LUL)
  * 2 : Right Lower Lobe (RLL)
  * 3 : Right Middle Lobe (RML)
  * 4 : Right Upper Lobe (RUL)

## Technical Validation
The longest time period between the scanner auto-calibration and the study in the COVID-CT-MD dataset is 1 day, which ensures calibrated and accurate performance of the scanning device. Furthermore, there is an annual thorough quality control that ensures the absence of ring artifacts in the acquired CT scans.

## Statistical Analysis
<i>"statistical_analysis.py"</i> is the code to re-produce the statistical analysis provided in the <a href="https://arxiv.org/abs/2009.14623">data desription</a>

## Citation
If you found this dataset and the related data descritipon useful in your research, please consider citing:

```
@article{Afshar2020,
arxivId = {2009.14623},
author = {Afshar, Parnian and Heidarian, Shahin and Enshaei, Nastaran and Naderkhani, Farnoosh and Rafiee, Moezedin Javad and Oikonomou, Anastasia and Fard, Faranak Babaki and Samimi, Kaveh and Plataniotis, Konstantinos N. and Mohammadi, Arash},
eprint = {2009.14623},
month = {sep},
title = {{COVID-CT-MD: COVID-19 Computed Tomography (CT) Scan Dataset Applicable in Machine Learning and Deep Learning}},
url = {http://arxiv.org/abs/2009.14623},
year = {2020}
}
```
