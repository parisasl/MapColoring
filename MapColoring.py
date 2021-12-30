'''
To solve the map coloring problem, which is a constraint satisfaction problem, I have employed backtracking 
algorithm. The colors should be assigned to the cities considering the constarints (the borders).    
'''
# Class of cities and their possible colors(domain).
class Variable:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
# Class of the consraints, which are going to be defined.        
class Constraint:
    def __init__(self, variables):
        self.variables = variables

    def check(self, values):
        return True
    
# Checking whether the domain(color) of the constraints (cities with border) are the same. If they are same: return False    
class DiffrenetConstraint(Constraint):
    def check(self, values):
        if len(values) == 0:
            return True
        v = None
        for val in values:
            if v is None:
                v = val
            elif val == v:
                return False
        return True
    
# class EqualConstraint(Constraint):
#     def check(self, values):
#         if len(values) == 0:
#             return True
#         v = values[0]
#         for val in values:
#             if v != val:
#                 return False
#         return True

#selecting the keys(and values) that we are looking for from a dict. (sub_dic)
def filter_dictionary(d, keys):
    return {k: v for (k, v) in d.items() if k in keys}


def dictionary_to_array(d):
    return [v for (k, v) in d.items()]

# Concatenate two dictionaries
def union(d1, d2):
    d = d1.copy()
    d.update(d2)
    return d

# Adding arrays without the duplicates 
def union_arr(a, b):

    return list(set(a) | set(b))

colors = ["blue","green","red"] 
#colors = ["blue","green","red","yellow"]
states = ["WA","NT","Q","NSW","V","SA","T"]

class Problem:
    def __init__(self):
        self.variables = []
        self.constraints = []

    def add_variable(self, variable):
        self.variables.append(variable)

    def add_constraint(self, constraint):
        self.constraints.append(constraint)
    def check_consistency(self, assignment):
        for constraint in self.constraints:
            relevantValues = filter_dictionary(assignment, constraint.variables)
            if not constraint.check(dictionary_to_array(relevantValues)):
                return False
        return True
    
    # Finding the answers 
    def find(self, assignment, v):
        vars = v.copy()
        if len(vars) == 0:
            return [assignment]

        var = vars.pop()
        results = []
        # For each color in a particular city, we check if it is consistent with previous constraints.
        for option in var.domain:
            new_assignment = union(assignment, {var.name: option})
            if self.check_consistency(new_assignment):
                # The backtracking algorithm 
                res = self.find(new_assignment, vars)
                results += res
        return results

    def get_solutions(self):
        return self.find({}, self.variables.copy())
            
problem = Problem()
# At first we define the states as variables and consider that all the colors(domains) are possible for each state. 
for state in states:
    problem.add_variable(Variable(state, colors))
    
# defining the constraints (the cities which have a common border).
problem.add_constraint(DiffrenetConstraint(["WA", "NT"]))
problem.add_constraint(DiffrenetConstraint(["WA", "SA"]))
problem.add_constraint(DiffrenetConstraint(["NT", "SA"]))
problem.add_constraint(DiffrenetConstraint(["NT", "Q"]))
problem.add_constraint(DiffrenetConstraint(["SA", "Q"]))
problem.add_constraint(DiffrenetConstraint(["SA", "NSW"]))
problem.add_constraint(DiffrenetConstraint(["SA", "V"]))
problem.add_constraint(DiffrenetConstraint(["Q", "NSW"]))
problem.add_constraint(DiffrenetConstraint(["V", "NSW"]))

#Finding the solutions
#print(problem.get_solutions())
#print("possible solutions: " + str(len(problem.get_solutions())))

def main():
    while True:
        print("For printing all solutions enter '1'\nFor printing the count of solutions enter '2'")
        ipt=input()
        if ipt == '1':
            print(problem.get_solutions())
        elif ipt=='2':
            print("\nPossible solutions count: " + str(len(problem.get_solutions())))  
        input()     

if __name__ == "__main__":
    main()
