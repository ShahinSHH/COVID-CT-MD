#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Shahin Heidarian, ISIP Lab, Concrdia University, Montreal, CA
Email Address: heidarian.shahin@gmail.com
"""
# Libraries
import matplotlib.pyplot as plt
import pydicom
import numpy as np
import os
import tempfile
import pandas as pd
import seaborn as sns

#%% Data Paths

# !!! Specify the Python directory to the path that contains data folders (COVID-171, CAP-60, Normal-76)
# !!! You can also modify the following paths based on your custom data structure
dataset_path_covid = r"./COVID-19 subjects/"
dataset_path_noncovid = r"./Cap subjects/"
dataset_path_normal = r"./Normal subjects/"

# Importing the lobe-level labels
y_lobe = np.load('Lobe-level-labels.npy')

#%% Initializing the csv file
dpath = []
image_paths = []
csv_data = pd.DataFrame({'Diagnosis' : [],'Patient Sex' : [],'Patient Age': [],
                         'Slice Thickness':[], 'Slices':[], 'XRayTubeCurrent':[], 'KVP':[],
                         'Exposure Time':[], 'Study Date':[], 'Date of Last Calibration':[],
                         'Distance Source to Detector':[], 'Distance Source to Patient':[],
                         'Rows':[],'Columns':[]})



slice_size = {}
# COVID-19
all_paths = sorted([x for x in os.listdir(dataset_path_covid) if not x.startswith('.')])

for patient_number, path in enumerate(all_paths):    
    subpath = sorted([x for x in os.listdir(dataset_path_covid+path) if not x.startswith('.')])

    
    slice_numbers = len(subpath) #number of slices
    dataset = pydicom.dcmread(os.path.join(dataset_path_covid+path, subpath[0])) #read a sample image

    #information
    patient_csv_data = {}
    patient_csv_data['Diagnosis'] = 'COVID-19'
    patient_csv_data['Patient Sex'] = [dataset.PatientSex]
    patient_csv_data['Patient Age'] = [dataset.PatientAge]
    patient_csv_data['Slice Thickness'] = [dataset.SliceThickness]
    patient_csv_data['Slices'] = [slice_numbers]
    patient_csv_data['Study Date'] = [dataset.StudyDate]
    patient_csv_data['XRayTubeCurrent'] = [dataset.XRayTubeCurrent]
    patient_csv_data['KVP'] = [dataset.KVP]
    patient_csv_data['Exposure Time'] = [dataset.ExposureTime]
    patient_csv_data['Study Date'] = [dataset.StudyDate]
    patient_csv_data['Date of Last Calibration'] = [dataset.DateOfLastCalibration]
    patient_csv_data['Distance Source to Detector'] = [dataset.DistanceSourceToDetector]
    patient_csv_data['Distance Source to Patient'] = [dataset.DistanceSourceToPatient]
    patient_csv_data['Rows'] = [dataset.Rows]
    patient_csv_data['Columns'] = [dataset.Columns]

    #updating csv file
    patient_csv_dataframe = pd.DataFrame(patient_csv_data)    
    csv_data = csv_data.append(patient_csv_dataframe, ignore_index = True)

# Non COVID (Labeled)
all_paths = sorted([x for x in os.listdir(dataset_path_noncovid) if not x.startswith('.')])

for patient_number, path in enumerate(all_paths):    
    subpath = sorted([x for x in os.listdir(dataset_path_noncovid+path) if not x.startswith('.')])

    
    slice_numbers = len(subpath) #number of slices
    dataset = pydicom.dcmread(os.path.join(dataset_path_noncovid+path, subpath[0])) #read a sample image
    slice_size[path] = slice_numbers

    #information
    patient_csv_data = {}
    patient_csv_data['Diagnosis'] = 'CAP'
    patient_csv_data['Patient Sex'] = [dataset.PatientSex]
    patient_csv_data['Patient Age'] = [dataset.PatientAge]
    patient_csv_data['Slice Thickness'] = [dataset.SliceThickness]
    patient_csv_data['Slices'] = [slice_numbers]
    patient_csv_data['Study Date'] = [dataset.StudyDate]
    patient_csv_data['XRayTubeCurrent'] = [dataset.XRayTubeCurrent]
    patient_csv_data['KVP'] = [dataset.KVP]
    patient_csv_data['Exposure Time'] = [dataset.ExposureTime]
    patient_csv_data['Study Date'] = [dataset.StudyDate]
    patient_csv_data['Date of Last Calibration'] = [dataset.DateOfLastCalibration]
    patient_csv_data['Distance Source to Detector'] = [dataset.DistanceSourceToDetector]
    patient_csv_data['Distance Source to Patient'] = [dataset.DistanceSourceToPatient]
    patient_csv_data['Rows'] = [dataset.Rows]
    patient_csv_data['Columns'] = [dataset.Columns]

    #updating csv file
    patient_csv_dataframe = pd.DataFrame(patient_csv_data)    
    csv_data = csv_data.append(patient_csv_dataframe, ignore_index = True)


# Normal 
all_paths = sorted([x for x in os.listdir(dataset_path_normal) if not x.startswith('.')])

for patient_number, path in enumerate(all_paths):    
    subpath = sorted([x for x in os.listdir(dataset_path_normal+path) if not x.startswith('.')])

    
    slice_numbers = len(subpath) #number of slices
    dataset = pydicom.dcmread(os.path.join(dataset_path_normal+path, subpath[0])) #read a sample image

    #information
    patient_csv_data = {}
    patient_csv_data['Diagnosis'] = 'Normal'
    patient_csv_data['Patient Sex'] = [dataset.PatientSex]
    patient_csv_data['Patient Age'] = [dataset.PatientAge]
    patient_csv_data['Slice Thickness'] = [dataset.SliceThickness]
    patient_csv_data['Slices'] = [slice_numbers]
    patient_csv_data['Study Date'] = [dataset.StudyDate]
    patient_csv_data['XRayTubeCurrent'] = [dataset.XRayTubeCurrent]
    patient_csv_data['KVP'] = [dataset.KVP]
    patient_csv_data['Exposure Time'] = [dataset.ExposureTime]
    patient_csv_data['Study Date'] = [dataset.StudyDate]
    patient_csv_data['Date of Last Calibration'] = [dataset.DateOfLastCalibration]
    patient_csv_data['Distance Source to Detector'] = [dataset.DistanceSourceToDetector]
    patient_csv_data['Distance Source to Patient'] = [dataset.DistanceSourceToPatient]
    patient_csv_data['Rows'] = [dataset.Rows]
    patient_csv_data['Columns'] = [dataset.Columns]

    #updating csv file
    patient_csv_dataframe = pd.DataFrame(patient_csv_data)    
    csv_data = csv_data.append(patient_csv_dataframe, ignore_index = True)

## Additional columns
    
# Last Calibration Date    
st_date = pd.to_datetime(csv_data['Study Date'])
cal_date = pd.to_datetime(csv_data['Date of Last Calibration'])
csv_data['Last Calibration'] = st_date - cal_date # time period between calibration and study

# Exposure value (mAs) = Current(mA) * Exposure Time(ms) / 1000
current = csv_data['XRayTubeCurrent'].iloc[:].apply(lambda x : int(x)).values
time = csv_data['Exposure Time'].iloc[:].apply(lambda x : int(x)).values
csv_data['mAs'] = current*time/1000 

# Numerical values for Ages
csv_data['Age'] = csv_data['Patient Age'].iloc[:].apply(lambda x : int(x[1:3])).values 

# csv files seperated by the disease type
covid_data = csv_data[csv_data['Diagnosis'] ==  'COVID-19']
pneumonia_data = csv_data[csv_data['Diagnosis'] ==  'CAP']
normal_data = csv_data[csv_data['Diagnosis'] ==  'Normal']


#%% Statistical Analysis
print('Statistical Analysis\n')
# Total Analysis
sex = csv_data['Patient Sex'].iloc[:].values
current = csv_data['XRayTubeCurrent'].iloc[:].apply(lambda x : int(x)).values
time = csv_data['Exposure Time'].iloc[:].apply(lambda x : int(x)).values
study_date = csv_data['Study Date'].iloc[:].values
age = csv_data['Patient Age'].iloc[:].apply(lambda x : int(x[1:3])).values
kvp = csv_data['KVP'].iloc[:].values

print('Total:')
print('Study date from {a} to {b}'.format(a = min(study_date), b = max(study_date)))
print('Males: {m} , Females: {f}'.format(m = np.sum(sex=='M'), f =np.sum(sex=='F')))
print('Age : {m:.2f} +/- {s:.2f}'.format(m = np.mean(age), s =np.std(age)))
print('X-ray Tube Current: ({a},{b})'.format(a = np.min(current), b =np.max(current)))
print('KVP: ({a},{b})'.format(a = np.min(kvp), b = np.max(kvp)))
print('Exposure Time: ({a},{b})'.format(a = np.min(time), b = np.max(time)))
print('Exposure (mAs) min/max : ({a},{b})'.format(a = np.min(current*time/1000), b =np.max(current*time/1000)))
print('Exposure (mAs) mean/std : ({a:.2f},{b:.2f})'.format(a = np.mean(current*time/1000), b =np.std(current*time/1000)))
print('-----------------------------')

# COVID-19 Analysis
sex = covid_data['Patient Sex'].iloc[:].values
current = covid_data['XRayTubeCurrent'].iloc[:].apply(lambda x : int(x)).values
time = covid_data['Exposure Time'].iloc[:].apply(lambda x : int(x)).values
study_date = covid_data['Study Date'].iloc[:].values
age = covid_data['Patient Age'].iloc[:].apply(lambda x : int(x[1:3])).values
kvp = covid_data['KVP'].iloc[:].values

print('COVID-19:')
print('Study date from {a} to {b}'.format(a = min(study_date), b = max(study_date)))
print('Males: {m} , Females: {f}'.format(m = np.sum(sex=='M'), f =np.sum(sex=='F')))
print('Age : {m:.2f} +/- {s:.2f}'.format(m = np.mean(age), s =np.std(age)))
print('X-ray Tube Current: ({a},{b})'.format(a = np.min(current), b =np.max(current)))
print('KVP: ({a},{b})'.format(a = np.min(kvp), b = np.max(kvp)))
print('Exposure Time: ({a},{b})'.format(a = np.min(time), b = np.max(time)))
print('Exposure (mAs) min/max : ({a},{b})'.format(a = np.min(current*time/1000), b =np.max(current*time/1000)))
print('Exposure (mAs) mean/std : ({a:.2f},{b:.2f})'.format(a = np.mean(current*time/1000), b =np.std(current*time/1000)))
print('-----------------------------')

# CAP Analysis
sex = pneumonia_data['Patient Sex'].iloc[:].values
current = pneumonia_data['XRayTubeCurrent'].iloc[:].apply(lambda x : int(x)).values
time = pneumonia_data['Exposure Time'].iloc[:].apply(lambda x : int(x)).values
study_date = pneumonia_data['Study Date'].iloc[:].values
age = pneumonia_data['Patient Age'].iloc[:].apply(lambda x : int(x[1:3])).values
kvp = pneumonia_data['KVP'].iloc[:].values

print('CAP:')
print('Study date from {a} to {b}'.format(a = min(study_date), b = max(study_date)))
print('Males: {m} , Females: {f}'.format(m = np.sum(sex=='M'), f =np.sum(sex=='F')))
print('Age : {m:.2f} +/- {s:.2f}'.format(m = np.mean(age), s =np.std(age)))
print('X-ray Tube Current: ({a},{b})'.format(a = np.min(current), b =np.max(current)))
print('KVP: ({a},{b})'.format(a = np.min(kvp), b = np.max(kvp)))
print('Exposure Time: ({a},{b})'.format(a = np.min(time), b = np.max(time)))
print('Exposure (mAs) min/max : ({a},{b})'.format(a = np.min(current*time/1000), b =np.max(current*time/1000)))
print('Exposure (mAs) mean/std : ({a:.2f},{b:.2f})'.format(a = np.mean(current*time/1000), b =np.std(current*time/1000)))
print('-----------------------------')


# Normal Analysis
sex = normal_data['Patient Sex'].iloc[:].values
current = normal_data['XRayTubeCurrent'].iloc[:].apply(lambda x : int(x)).values
time = normal_data['Exposure Time'].iloc[:].apply(lambda x : int(x)).values
study_date = normal_data['Study Date'].iloc[:].values
age = normal_data['Patient Age'].iloc[:].apply(lambda x : int(x[1:3])).values
kvp = normal_data['KVP'].iloc[:].values

print('Normal:')
print('Study date from {a} to {b}'.format(a = min(study_date), b = max(study_date)))
print('Males: {m} , Females: {f}'.format(m = np.sum(sex=='M'), f =np.sum(sex=='F')))
print('Age : {m:.2f} +/- {s:.2f}'.format(m = np.mean(age), s =np.std(age)))
print('X-ray Tube Current: ({a},{b})'.format(a = np.min(current), b =np.max(current)))
print('KVP: ({a},{b})'.format(a = np.min(kvp), b = np.max(kvp)))
print('Exposure Time: ({a},{b})'.format(a = np.min(time), b = np.max(time)))
print('Exposure (mAs) min/max : ({a},{b})'.format(a = np.min(current*time/1000), b =np.max(current*time/1000)))
print('Exposure (mAs) mean/std : ({a:.2f},{b:.2f})'.format(a = np.mean(current*time/1000), b =np.std(current*time/1000)))
print('-----------------------------')

# Visualization
plt.figure()
sns_plot = sns.violinplot(x = 'Diagnosis',y = 'mAs',data = csv_data, split = False)
plt.ylabel('Exposure (mAs)')
plt.xlabel('Disease')
fig = sns_plot.get_figure()
# fig.savefig("mas.png",dpi=300)

plt.figure()
sns_plot = sns.countplot(x='Diagnosis', data = csv_data, hue='Patient Sex')
plt.ylabel('Number of Cases')
plt.xlabel('Disease')
fig = sns_plot.get_figure()
# fig.savefig("sex.png",dpi=300)

plt.figure()
sns_plot = sns.boxplot(x = 'Diagnosis',y = 'Age',data = csv_data)
plt.ylabel('Age (year)')
plt.xlabel('Disease')
fig = sns_plot.get_figure()
# fig.savefig("age.png",dpi=300)

#%% Lobes and Slices-Level labels

total_infection = np.sum((np.sum(y_lobe,axis=2) >0) *1,axis=-1)
Y = np.sum(y_lobe,axis=1)

columns = ['LLL','LUL','RLL','RML','RUL']
lobe_data = pd.DataFrame(data = Y, columns=columns)

#Additional columns

# Total Infection
lobe_data['Total Infection'] = total_infection

# Diagnosis
n_covid_label = 55
lobe_data['Diagnosis'] = np.zeros((Y.shape[0],1))
lobe_data['Diagnosis'].iloc[0:n_covid_label] = 'COVID-19'
lobe_data['Diagnosis'].iloc[n_covid_label:] = 'CAP'


## Extracting Slice numbers/Ages from csv_data

# the following numbers represents the case indices in the main dataset
slice_numbers_covid1 = csv_data['Slices'].iloc[0:50]
slice_numbers_covid2 = csv_data['Slices'].iloc[[57,102,107,127,140]]
slice_numbers_noncovid = csv_data['Slices'].iloc[206:231]
slice_numbers_lobes = pd.concat([slice_numbers_covid1,slice_numbers_covid2,slice_numbers_noncovid],axis = 0).iloc[:].values

age_covid1 = csv_data['Age'].iloc[0:50]
age_covid2 = csv_data['Age'].iloc[[57,102,107,127,140]]
age_noncovid = csv_data['Age'].iloc[206:231]
age_lobes = pd.concat([age_covid1,age_covid2,age_noncovid],axis = 0).iloc[:].values


lobe_data['Slice Numbers'] = slice_numbers_lobes
lobe_data['Infection Ratio'] = lobe_data['Total Infection']/lobe_data['Slice Numbers']
lobe_data['Age'] = age_lobes

# Lobe ratio
lobe_data['LLL Ratio'] = lobe_data['LLL']/lobe_data['Slice Numbers']
lobe_data['LUL Ratio'] = lobe_data['LUL']/lobe_data['Slice Numbers']
lobe_data['RLL Ratio'] = lobe_data['RLL']/lobe_data['Slice Numbers']
lobe_data['RML Ratio'] = lobe_data['RML']/lobe_data['Slice Numbers']
lobe_data['RUL Ratio'] = lobe_data['RUL']/lobe_data['Slice Numbers']

#%% Lobes Visualization and Statistics
print('Infection Analysis:')
covid_hist = lobe_data[lobe_data['Diagnosis'] == 'COVID-19']['Total Infection']
pn_hist = lobe_data[lobe_data['Diagnosis'] == 'CAP']['Total Infection']
print('\n')
print('COVID Slices with infection: ',sum(covid_hist))
print('CAP Slices with infection: ',sum(pn_hist))

covid_rate = lobe_data[lobe_data['Diagnosis'] == 'COVID-19']['Infection Ratio']
pn_rate = lobe_data[lobe_data['Diagnosis'] == 'CAP']['Infection Ratio']

# Total Infection Ratio Histogram
plt.figure()
sns_plot = sns.distplot(covid_rate, bins = 8, kde = False, rug = False, hist = True, color = 'red',label='COVID-19')
sns_plot = sns.distplot(pn_rate, bins = 8, kde = False, rug = False, hist = True, color = 'blue', label='CAP')
plt.legend()
plt.ylabel('Number of Cases')
plt.xlabel('Infection Ratio')
fig = sns_plot.get_figure()
# fig.savefig("hist.png",dpi=300)

# Total Infection Ratio Boxplot
plt.figure()
sns_plot = sns.boxplot(x = 'Diagnosis',y = 'Infection Ratio',data = lobe_data) 
fig = sns_plot.get_figure()
# fig.savefig("IR.png",dpi=300)

# Barplot for lobe infection ratios
grouped_lobe = lobe_data.groupby('Diagnosis').mean()[['LLL Ratio','LUL Ratio','RLL Ratio','RML Ratio','RUL Ratio']]
plt.figure()
sns_plot = grouped_lobe.plot.bar() 
plt.xlabel('')
plt.ylabel('Average Infection Ratio')
fig = sns_plot.get_figure()
# fig.savefig("Figure_9.png",dpi=300,bbox_inches = 'tight')

print('\n')
print('COVID-19 Infection Ratio: ({a:.3f},{b:.3f})'.format(a = np.min(covid_rate), b = np.max(covid_rate)))
print('CAP Infection Ratio: ({a:.3f},{b:.3f})'.format(a = np.min(pn_rate), b = np.max(pn_rate)))

# lobe stats

covid_lobe = lobe_data[lobe_data['Diagnosis'] == 'COVID-19']
pn_lobe = lobe_data[lobe_data['Diagnosis'] == 'CAP']


print('\n')
print('COVID slices with LLL infection: ',int(sum(covid_lobe['LLL'])))
print('COVID slices with LUL infection: ',int(sum(covid_lobe['LUL'])))
print('COVID slices with RLL infection: ',int(sum(covid_lobe['RLL'])))
print('COVID slices with RML infection: ',int(sum(covid_lobe['RML'])))
print('COVID slices with RUL infection: ',int(sum(covid_lobe['RUL'])))
print('\n')
print('CAP slices with LLL infection: ',int(sum(pn_lobe['LLL'])))
print('CAP slices with LUL infection: ',int(sum(pn_lobe['LUL'])))
print('CAP slices with RLL infection: ',int(sum(pn_lobe['RLL'])))
print('CAP slices with RML infection: ',int(sum(pn_lobe['RML'])))
print('CAP slices with RUL infection: ',int(sum(pn_lobe['RUL'])))



