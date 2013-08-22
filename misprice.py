from pulp import *
def misprice(prices):
	x=pulp.LpVariable.dicts('x',prices[0],lowbound=0,upBound=4,cat=pulp.LpInteger)