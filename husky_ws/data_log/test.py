#!/usr/bin/env python
from pickle import TRUE
import pandas as pd
import os

df = pd.read_csv('configs.csv')
cost_scaling_factor = df['cost_scaling_factor']
resolution = df['resolution']

print(cost_scaling_factor.to_string(index=False))
print(resolution.to_string(index=False))

df = pd.DataFrame({"cost_scaling_factor":[cost_scaling_factor.to_string(index=False)], 
            "resolution":[resolution.to_string(index=False)]})
if not os.path.isfile('test.csv'):            
    df.to_csv("test.csv", mode='a', index=False, header=True) 
else:
    df.to_csv("test.csv", mode='a', index=False, header=False)


