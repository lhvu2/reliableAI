# pgmpy==0.1.13, just use BayesianModel

from pgmpy.models import BayesianModel
model = BayesianModel([('A', 'B'), ('B', 'C')])
print(model)