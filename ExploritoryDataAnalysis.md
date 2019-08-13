# Exploritory Data Analysis 
This document entails the data exploration process undertaken to understand relationships within the data and visualise these relationships.

## Initial Analysis of the Data
Exploratory analysis of the data revealed that there were a signiﬁcant number of NaN values for the distance modulus. For distance modulus observations that were NaN a pattern emerged that the photometric redshift (hostgal photoz) was equal to zero. 

According to the [data note](https://www.kaggle.com/c/PLAsTiCC-2018/data) of the competition the given redshift for objects in our own Milky Way galaxy is given as zero inferring that the objects with NaN distance modulus are objects within our galaxy. This makes it possible to split the dataset into objects in our galaxy and extragalactic objects. We can therefore visualise the frequency distribution of the target classes for galactic or extragalactic objects as shown below;

![Frequency distribution of target classes for galactic and extragalactic objects \label{img1}](https://github.com/SionBrown/PLAsTiCC-Astronomical-Classification/blob/master/galacticvsextragalactic.png?raw=true)

Figure 1 shows that there are no target classes that contain both galactic and extragalactic objects, thus, diﬀerent models can be trained and optimised to classify objects from galactic or extra-galactic sets along with diﬀerent features.

## Time Series Analysis

To explore the ﬂux time series ﬁgure 2 shows a scatter plot of the observed ﬂux values for each passband at the the time they were observed.

![Frequency distribution of target classes for galactic and extragalactic objects \label{img1}](https://github.com/SionBrown/PLAsTiCC-Astronomical-Classification/blob/master/scatterPlot.PNG?raw=true)
