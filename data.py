import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pylab as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")
plt.style.use('ggplot')
color_pal = [x['color'] for x in plt.rcParams['axes.prop_cycle']]

train_transaction = pd.read_csv('./input/train_transaction.csv')
test_transaction = pd.read_csv('./input/test_transaction.csv')
train_identity = pd.read_csv('./input/train_identity.csv')
test_identity = pd.read_csv('./input/test_identity.csv')
ss = pd.read_csv('../input/sample_submission.csv')

print('train_transaction shape is {}'.format(train_transaction.shape))
print('test_transaction shape is {}'.format(test_transaction.shape))
print('train_identity shape is {}'.format(train_identity.shape))
print('test_identity shape is {}'.format(test_identity.shape))

