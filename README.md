# COVID-CT-MD
<h4>A COVID-19 CT Scan Dataset Applicable in Machine Learning and Deep Learning</h4>

The COVID-CT-MD dataset contains volumetric chest CT scans (DICOM files) of <b>169 patients positive for COVID-19 infection, 60 patients with CAP (Community Acquired Pneumonia), and 76 normal patients</b>.  Diagnosis of COVID-19 infection is based on positive real-time Reverse Transcription Polymerase Chain Reaction (rRT-PCR) test results, clinical parameters, and CT scan manifestations identified by three experienced thoracic radiologists. Diagnosis for CAP and normal cases was confirmed using clinical laboratory tests, and CT scans.
A subset of 54 COVID-19, and 25 CAP cases were analyzed by the radiologists to identify and label slices with evidence of infection. The labeled subset of the data contains <b>4,957 number of slices demonstrating infection and 18,392 number of slices without the evidence of infection.</b>
<br> We're working closely with our collaborators in medical centers to provide more number of CT scans to introduce a larger Multi-Centre COVID-19 dataset to be used for a more extensive area of research. This dataset will be available for the public use in the near future.

## Links
COVID-CT-MD dataset is accessible through Figshare: <a href="https://figshare.com/s/c20215f3d42c98f09ad0">https://figshare.com/s/c20215f3d42c98f09ad0</a>
To access the associated clinical data and the labels from all three radiologists you can refer to the above link.

The detailed desription of the dataset is available at <a href="https://www.nature.com/articles/s41597-021-00900-3">https://www.nature.com/articles/s41597-021-00900-3</a>

## UPDATE 1 (Sep 8, 2021)
After further review of two cases (P001 and P006), our team has decided to update the labels associated with them.
Updated labels can be accessed through the following files:
* Slice-level-labels-updated-1.npy
* Lobe-level-labels-updated-1.npy

While the updated files contain more accurate lobe-level and slice-level labels, DL models developed based on the original version of the labels (Slice-level-labels, Lobe-level-labels) and those developed based on the updated ones don't show a significant difference as the changes are minor.

## Suplementary Information

* <b>Collection Dates:</b> COVID-19 cases are collected from February 2020 to April 2020, whereas CAP cases and normal cases are collected from April 2018 to December 2019 and January 2019 to May 2020, respectively.
* <b>De-Identification:</b> To respect the patients’ privacy and comply with the DICOM supplement 142 (Clinical Trial De-identification Profiles), all the CT studies in our dataset have been de-identified and only gender and age of the patients are preserved in the dataset. 
* <b>Data Distribution:</b> The brief distribution of the COVID-CT-MD dataset is shown in the following table:

| Table | Cases | Sex | Age(year) |
| ----- | ---------------- | ------- | --- |
| COVID-19 | 169 | 108 M/61 F | 51.96 ± 14.39 |
| CAP | 60 | 35 M/25 F | 57.7 ± 21.7 |
| Normal | 76 | 40 M/36 F | 43.4 ± 14.1 |


## Data Structure and Sample
<b>A small sample of the dataset</b> is available in the "Sample data" folder including DICOM files of one patient in each category to provide a quick insight of the dataset.

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

<b>NOTE:</b> The correct order of slices in a CT scan doesn't necessarily follow the order of the Slice-IDs. You need to sort slices based on the "slice location" parameter provided in the DICOM files when you are reading the data.
The “Slice Location” value is stored in DICOM files and is accessible through the following DICOM tag:
<br>
(0020,1041) - DS - Slice Location
<br>
<img src="https://github.com/ShahinSHH/COVID-CT-MD/blob/main/Figures/slices.jpg" width="400" height="400" />

## Labels
* <b>Index.csv</b> : specifies the patients having slice-level and lobe-level labels. The indices given to patients in “Index.csv” file are then used in “Slice-level-labels.npy” and “Lobe-level-labels.npy” to indicate the slice and lobe labels.
* <b>Slice-level-labels.npy</b> : a 2D binary Numpy array in which the existence of infection in a specific slice is indicated by 1 and the lack of infection is shown by 0. The first dimension represents the case index and the second one represents the slice numbers.
* <b>Lobe-level-labels.npy</b> : a 3D binary Numpy array in which the existence of infection in a specific lobe and slice is determined by 1 in the corresponding element of the array. Like the slice-level array. The two first dimensions represent the case index and slice numbers respectively. The third dimension shows the lobe indices which are specified as follows:
  * 0 : Left Lower Lobe (LLL)
  * 1 : Left Upper Lobe (LUL)
  * 2 : Right Lower Lobe (RLL)
  * 3 : Right Middle Lobe (RML)
  * 4 : Right Upper Lobe (RUL)

<h4>IMPORTANT:</h4> While reading DICOM files, note that the correct order of slices in a CT scan doesn’t necessarily follow the order of the Slice-IDs. It’s recommended to use the slice location value to sort the slices. Otherwise, the labels will not match correctly to the images.
The “Slice Location” value is stored in DICOM files and is accessible through the following DICOM tag:
<br>
(0020,1041) - DS - Slice Location

## Statistical Analysis
<i>"statistical_analysis.py"</i> is the code to re-produce the statistical analysis provided in the <a href="https://www.nature.com/articles/s41597-021-00900-3#Sec11">data description</a>.
<br> Please note that your Python directory should be set to the folder where you store the downloaded pacakge.
<h4>Requirements:</h4>

* pydicom (<a href="https://pydicom.github.io/pydicom/stable/tutorials/installation.html">Installation<a/>)
* pandas
* seaborn
* tempfile
* os
* numpy
* matplotlib

## Citation
If you found this dataset and the related data descritipon useful in your research, please consider citing:

```
@article{Afshar2021,
author = {Afshar, Parnian and Heidarian, Shahin and Enshaei, Nastaran and Naderkhani, Farnoosh and Rafiee, Moezedin Javad and Oikonomou, Anastasia and Fard, Faranak Babaki and Samimi, Kaveh and Plataniotis, Konstantinos N and Mohammadi, Arash},
doi = {10.1038/s41597-021-00900-3},
issn = {2052-4463},
journal = {Scientific Data},
number = {1},
pages = {121},
title = {{COVID-CT-MD, COVID-19 computed tomography scan dataset applicable in machine learning and deep learning}},
url = {https://doi.org/10.1038/s41597-021-00900-3},
volume = {8},
year = {2021}
}

```
