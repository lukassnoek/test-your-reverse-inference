import os.path as op
import nibabel as nib
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold
from glob import glob

base_dir = '/home/lsnoek1/projects/CrossingBorders/all_nimgs'
nimgs = glob(op.join(base_dir, '*', '*.nii.gz'))

X = np.c_[[nib.load(n).get_data().ravel() for n in nimgs]]
X = X[:, X.sum(axis=0) != 0]
y = [n.split('_')[-1].split('.')[0] for n in nimgs]
y = LabelEncoder().fit_transform(y)

pipe = make_pipeline(StandardScaler(), SVC(kernel='linear'))
scores = cross_val_score(pipe, X, y, cv=RepeatedStratifiedKFold(n_splits=10, n_repeats=10))
print('Average score (std): %.3f (%.3f)' % (scores.mean(), scores.std()))
