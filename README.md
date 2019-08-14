# PLAsTiCC-Astronomical-Classification
 The nature of the PLAsTiCC Astronomical Classification time series is complex because there are three time series (flux, flux err, detected) per passband (u, g, r, i, z y) per object. Exploratory data analysis revealed that the data set could be split into galactic and extra-galactic objects thus enabling different machine learning models to be trained and applied. This repository provides an exploration of the data and some feature engineering approaches to assimilate relationships between features with in the data and developing faetures to help classify each target class. There are 14 target classes and one extra target class that is for anomaly detection of newly discovered astronomical objects. 

## Getting Started

Please refer to the [exploratory data analysis document](https://github.com/SionBrown/PLAsTiCC-Astronomical-Classification/blob/master/ExploritoryDataAnalysis.md) before delving into the feature engineering document for an insight as to how significant features were engineered to improve classification of astronomical objects. 

### Prerequisites

Below is a list of prerequisites to install;

The data for this Kaggle challenge can be downloaded [here](https://www.kaggle.com/c/PLAsTiCC-2018/data).

You will need to have a version of Python installed so please visit [Python.org](https://www.python.org/) to download the Python sourcecode and installers. It is recommended to download the latest version but for your information Python 3.6.6 was used when writing the code for the repository.

For data visualisation please install the following Python packages;

1. Install Pandas using the 'pip install pandas' command in the terminal.
2. Install Matplotlib using the 'pip install matplotlib' command in the terminal.
3. Install Numpy using the 'pip install numpy' command in the terminal.
4. Install Scipy using the 'pip install scipy' command in the terminal.

## Authors

* **Sion Brown** - *Initial work* - [Sion Brown](https://github.com/SionBrown)

See also the list of [contributors](https://github.com/SionBrown/PLAsTiCC-Astronomical-Classification/contributors) who participated in this project.
