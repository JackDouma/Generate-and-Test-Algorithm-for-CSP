import itertools

#this method will create a list of all solutions
def csp(variables, domains, constraints):
    #create all possible outcomes with itertools
    setVariables = itertools.product(*domains)

    solutions = []
    
    # check each combination
    for x in setVariables:
        solution = dict(zip(variables, x))
        
        #if return == true, add to solutions
        if constraintCheck(solution, constraints):
            solutions.append(solution)
    
    return solutions
    
#This method will check constraints and will return true or false accordingly 
def constraintCheck(solution, constraints):
    # loop over all constraints
    for constraint in constraints:
        a, operator, b = constraint
        
        #return false if constraints are invalid
        if operator == '<':
            if solution[a] >= solution[b]:
                return False
        if operator == '>':
            if solution[a] <= solution[b]:
                return False
            
        #check graph
        if solution['B'] == 2 and solution['A'] == 1 and solution['C'] in [3, 4]:
            return True
        elif solution['B'] == 3 and solution['C'] == 4 and solution['A'] in [1, 2]:
            return True
        else:
            return False
            
#create variables
variables = ['A', 'B', 'C']
domains = [[1, 2, 3, 4] for _ in variables]
constraints = [('A', '<', 'B'), ('B', '<', 'C')]

#get solution and print results
solutions = csp(variables, domains, constraints)
print("Solutions")
for s in solutions:
    print(s)
            
        
