import numpy as np
import pandas as pd
from scipy.stats import skew
from matplotlib import pylab as plt

#Please change the file path to where you have saved the training set metadata.
train_meta =  pd.read_csv(r'yourPath\training_set_metadata.csv')
train_all =  pd.read_csv(r"yourPath\training_set.csv")
galactic_objects = list(train_meta[np.isnan(train_meta['distmod'])]['object_id'])
extragalactic_objects = np.setdiff1d(train_meta['object_id'].values.tolist(),galactic_objects)
extragalactic_set = train_all[train_all['object_id'].isin(extragalactic_objects)]
extragalactic_target = train_meta[train_meta['object_id'].isin(extragalactic_objects)][['object_id', 'target']]
galactic_set = train_all[train_all['object_id'].isin(galactic_objects)]
galactic_target = train_meta[train_meta['object_id'].isin(galactic_objects)][['object_id', 'target']]

extragalactic_set = extragalactic_set.reset_index().merge(
				right=train_meta,
				how='outer',
    			on='object_id'
)

galactic_set = galactic_set.reset_index().merge(
				right=train_meta,
				how='outer',
    			on='object_id'
)

x = extragalactic_target.groupby('target').count()
y = galactic_target.groupby('target').count()

extragalactic = x.values.tolist()
galactic = y.values.tolist()
listGal = []
listExGal = []
for i in range(0, 15):
	if i == 0:
		listExGal.append(0)
	elif i == 1:
		listExGal.append(extragalactic[0][0])
	elif i == 2:
		listExGal.append(0)
	elif i == 3:
		listExGal.append(extragalactic[1][0])
	elif i == 4:
		listExGal.append(extragalactic[2][0])
	elif i == 5:
		listExGal.append(0)
	elif i == 6:
		listExGal.append(extragalactic[3][0])
	elif i == 7:
		listExGal.append(extragalactic[4][0])
	elif i == 8:
		listExGal.append(0)
	elif i == 9:
		listExGal.append(extragalactic[5][0])
	elif i == 10:
		listExGal.append(extragalactic[6][0])
	elif i == 11:
		listExGal.append(extragalactic[7][0])
	elif i == 12:
		listExGal.append(0)
	elif i == 13:
		listExGal.append(extragalactic[8][0])
	elif i == 14:
		listExGal.append(0)
	else:
		listExGal.append(0)

for i in range(0, 15):
	if i == 0:
		listGal.append(galactic[0][0])
	elif i == 1:
		listGal.append(0)
	elif i == 2:
		listGal.append(galactic[1][0])
	elif i == 3:
		listGal.append(0)
	elif i == 4:
		listGal.append(0)
	elif i == 5:
		listGal.append(galactic[2][0])
	elif i == 6:
		listGal.append(0)
	elif i == 7:
		listGal.append(0)
	elif i == 8:
		listGal.append(galactic[3][0])
	elif i == 9:
		listGal.append(0)
	elif i == 10:
		listGal.append(0)
	elif i == 11:
		listGal.append(0)
	elif i == 12:
		listGal.append(galactic[4][0])
	elif i == 13:
		listGal.append(0)
	elif i == 14:
		listGal.append(0)
	else:
		listGal.append(0)

classes = ['class_6','class_15','class_16','class_42','class_52','class_53','class_62','class_64','class_65','class_67','class_88','class_90','class_92','class_95','class_99']
df = pd.DataFrame({'Milky Way': listGal,
                   'Extragalactic': listExGal}, index=classes)
ax = df.plot.bar(rot=0) 
plt.show()
