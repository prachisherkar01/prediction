import numpy as np
import pandas as pd


def predict():
    """Print a simple rain-prediction message."""
    print("ada threshold 0.7")
def rmse(y, yhat):
    return ((y - yhat) ** 2).mean() ** 0.5
