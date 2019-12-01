import numpy as np
import pandas as pd
from tpot import TPOTClassifier
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
 
inputfile='data.csv'
 
def main():
    df=pd.read_csv(inputfile)
    #print(df.head())
    df.replace('?',np.nan,inplace=True)
    df.dropna(inplace=True)
    df.drop(['id'],1,inplace=True)
    #print(df.head())
    X=np.array(df.drop(['Class'],1))
    Y=np.array(df['Class'])
    x_train,x_test,y_train,y_test=model_selection.train_test_split(X,Y,test_size=0.2)
    tpot=TPOTClassifier(generations=6,verbosity=2)
    tpot.fit(x_train,y_train)
    tpot.score(x_test,y_test)
    tpot.export('pipeline.py')
 
 
if __name__ == "__main__":
    main()
