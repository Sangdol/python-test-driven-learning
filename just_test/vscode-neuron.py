import pandas as pd
from os.path import expanduser
import os

# https://github.com/neuron-team/vscode-ipe/issues/167
# It runs on root.
curr_path = os.getcwd()  # "/"

home = expanduser("~")
df = pd.read_csv(f'{home}/p/python-test-driven-learning/stub/test_panda.csv')
print(df)
