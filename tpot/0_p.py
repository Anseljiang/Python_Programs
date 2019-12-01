import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from tpot import TPOTClassifier
 
df=pd.read_csv("D:\\ttt\\0.csv")

#df.replace('?',np.nan,inplace=True)
#df.dropna(inplace=True)
#df.drop(['id'],1,inplace=True)

X=np.array(df.drop(['type'],1))
Y=np.array(df['type'])

x_train,x_test,y_train,y_test=model_selection.train_test_split(X.astype(np.float64),Y.astype(np.float64),test_size=0.2)
tpot=TPOTClassifier(generations=6,verbosity=2)
tpot.fit(x_train,y_train)
#tpot.score(x_test,y_test)
tpot.export('pipeline.py')
 
 