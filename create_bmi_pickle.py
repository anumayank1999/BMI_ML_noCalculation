import pandas as pd
import pickle
df=pd.read_csv('K:/anumayank/PYTHON IMPORT AND IMP FILES(CLASSROOM)/bmi.csv')
X=df.iloc[:,2:-1].values
y=df.iloc[:,-1]
from sklearn.ensemble.forest import RandomForestClassifier
global r

def train():
    rfc=RandomForestClassifier(n_estimators=6)
    rfc.fit(X,y)
    r=rfc.predict(X)
    from sklearn.metrics import r2_score
    k=r2_score(y,r)
    print(k)
    if(k>=0.95):
        file=open('bmi.model','wb')
        pickle.dump(rfc,file)
        file.close
    else:
        train()
    
train()