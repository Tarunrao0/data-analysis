import numpy as np

def calculate(list):
    if len(list) == 9:
        list = np.reshape(list, (3, 3))
        calculations = {
            "mean": [list.mean(axis=0).tolist(), list.mean(axis=1).tolist(), list.mean()],
            "variance": [list.var(axis=0).tolist(), list.var(axis=1).tolist(), list.var()],
            "standard deviation": [list.std(axis=0).tolist(), list.std(axis=1).tolist(), list.std()],
            "max": [list.max(axis=0).tolist(), list.max(axis=1).tolist(), list.max()],
            "min": [list.min(axis=0).tolist(), list.min(axis=1).tolist(), list.min()],
            "sum": [list.sum(axis=0).tolist(), list.sum(axis=1).tolist(), list.sum()]
        }
    else:
        raise ValueError("List must contain nine numbers.")
    
    return calculations
