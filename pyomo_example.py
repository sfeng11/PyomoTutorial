# Import packages
import pyomo.environ as pyo

# set of items available for purchase
A = ['hammer', 'wrench', 'screwdriver', 'towel']
# Benefit (b)
b = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
# Weight (w)
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}
# Maximum weight allowed
W_max = 14

# Create a model
model = pyo.ConcreteModel()
# Define the decision variables
model.x = pyo.Var(A, within=pyo.Binary)
# Define the objective function
model.value = pyo.Objective(
    expr = sum( b[i] * model.x[i] for i in A ),
    sense = pyo.maximize )
# Define the constraint    
model.weight = pyo.Constraint(
    expr = sum( w[i] * model.x[i] for i in A ) <= W_max)
# Define solver    
opt = pyo.SolverFactory('glpk')
# Solve the model
result_obj = opt.solve(model,tee =False)
# Print the result
model.pprint()