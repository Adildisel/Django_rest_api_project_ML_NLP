import ml
import pickle
import os
import numpy as np

ml_helper = ml.MlHelper()

dest = os.path.join('movieclassifier', 'pkl_objects')

vect = ml_helper.vect
clf = pickle.load(open(
                        os.path.join(dest, 'classifier.pkl'),
                        'rb'
                        ))

label = {0: 'negative', 1:'positive'}
example = ['Мне нравиться это видео']

X = vect.transform(example)

print(label[clf.predict(X)[0]])
print(np.max(clf.predict_proba(X)*100))