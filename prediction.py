import numpy as np
import pandas as pd


def predict():
   print("main version")
   print(2+2)
def rmse(y, yhat):
    return ((y - yhat) ** 2).mean() ** 0.5
