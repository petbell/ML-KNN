import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('seattleWeather_1948-2017.csv')
print(df.head(2))