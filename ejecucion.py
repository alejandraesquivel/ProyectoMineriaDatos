import pandas as pd
import numpy as np
import mlxtend
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Leer el documento CSV
data = pd.read_csv('dataApriori.csv')
data = data.dropna(axis=0, how='any')
data['educationLevel'] = data.educationLevel.map(
    lambda x: 'primaria' if x >= 3 and x <= 6 else ('secundaria' if x >= 7 and x <= 9 else ('prepa' if x >= 10 and x <= 12 else 'licenciatura')))
data['Age'] = data.Age.map(
    lambda x: 'veintes' if x >= 20 and x <= 30 else ('treinta' if x >= 31 and x <= 40 else ('cuarenta' if x >= 41 and x <= 50 else ('cincuenta' if x >= 51 and x <= 60 else 'sesentas'))))

B = pd.get_dummies(data.stack()).groupby(level=0).agg(max)
patFrec = apriori(B, min_support=0.1, use_colnames=True)
rules = association_rules(patFrec)
rules["antecedant_len"] = rules["antecedants"].apply(lambda x: len(x))
rules=rules[(rules['antecedant_len'] >=2) & (rules['confidence'] >=0.5) & (rules['lift']>0.9)]
rules=rules.sort(['confidence', 'lift'], ascending=[0,1])
print rules.to_latex()
