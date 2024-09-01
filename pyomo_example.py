import pyomo.environ as pyo
A = ['hammer', 'wrench', 'screwdriver', 'towel']
b = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}

W_max = 14

model = pyo.ConcreteModel()
model.x = pyo.Var(A, within=pyo.Binary)
model.value = pyo.Objective(
    expr = sum( b[i] * model.x[i] for i in A ),
    sense = pyo.maximize )
    
model.weight = pyo.Constraint(
    expr = sum( w[i] * model.x[i] for i in A ) <= W_max)
    
opt = pyo.SolverFactory('glpk')

result_obj = opt.solve(model,tee =True)

model.pprint()