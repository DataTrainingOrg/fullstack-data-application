from fastapi import FastAPI, BackgroundTasks
import pathlib
import glob 
from joblib import load, dump
from schema import IrisPredict, IrisTrain
import numpy as np
from sklearn.linear_model import LogisticRegression
from datetime import datetime


app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

global  clf

CLASSES = ['setosa', 'versicolor', 'virginica']

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event('startup')
async def load_model():
    global clf
    all_model_paths = glob.glob("./data/iris_*")
    last_model = sorted(all_model_paths, reverse=True)[0]
    clf = load(last_model)


@app.post("/iris/predict")
async def predict_iris(iris: IrisPredict):
    return {
        "predicted_classes" : clf.predict(np.asarray([iris.data])).tolist(),
        "predicted_probas" : clf.predict_proba(np.asarray([iris.data])).tolist(), 
        "classes" : CLASSES
    }

def retrain_model(X, y):
    logreg = LogisticRegression()
    logreg.fit(X, y)
    dump(logreg, f'./data/iris_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}')


@app.post("/iris/train")
async def train_iris_model(iris: IrisTrain, background_tasks: BackgroundTasks):
    X = np.asarray(iris.data)
    y = np.asarray(iris.targets)
    background_tasks.add_task(retrain_model, X=X, y=y)
    return {"message": "Notification sent in the background"}

@app.get("/iris/classes")
async def create_post(iris: IrisPredict):
    return CLASSES

