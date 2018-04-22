from z3 import *
## See https://en.wikipedia.org/wiki/Verbal_arithmetic
## cute: http://mathforum.org/library/drmath/view/60417.html

vars = dict()
def _mk_int_var (x):
    if x not in vars:
        vars[x] = z3.Int (str(x))
    return vars[x]

def mk_var (x):
    return _mk_int_var (x)

def get_vars ():
    return vars.values ()


def solve (s1, s2, s3):
    global vars
    vars = dict()

    if len(s1) == 0 or len(s2) == 0 or len(s3) == 0 or len(s3) < len(s1) or len(s3) < len(s2):
    		return None

    for i in s1:
    	_mk_int_var(i)
    for j in s2:
    	_mk_int_var(j)
    for k in s3:
    	_mk_int_var(k)

    S = Solver()
    S.reset()

    for all in vars:
    	S.add(And(vars[all] >= 0, vars[all] <= 9))


    S.add(z3.Distinct (vars.values()))
	

    S.add(vars[s1[0]] != 0)
    S.add(vars[s2[0]] != 0)
    S.add(vars[s3[0]] != 0)

    cno = max(len(s1),len(s2),len(s3))
    c = dict()

    xlen = len(s1) - 1
    ylen = len(s2) - 1
    zlen = len(s3) - 1
    
   
    while (cno > 0):
 		faltu = 'c' + str(cno)
 		if faltu not in c:
 			c[faltu] = z3.Int(faltu)
 		cno = cno -1 
 		maxlen = len(c) 

 		if (cno == 0):
			for all in c:
				if all == 'c1' and (len(s3) > len(s2) or len(s3) > len(s1)):
					S.add(c[all] == 1)
					if len(s1) == len(s3) and len(s2) != len(s3):
						S.add(vars[s3[0]] == c[all] + vars[s1[0]])
					elif len(s2) == len(s3) and len(s1) != len(s3):
						S.add(vars[s3[0]] == c[all] + vars[s2[0]]) 
					else:
						S.add(vars[s3[0]] == c[all])

				elif all == 'c1' and (len(s3) == len(s1) and len(s3) == len(s2)):
					S.add(vars[s3[0]] == c[all] + vars[s1[0]] + vars[s2[0]])

				elif all == 'c' + str(len(c)):
					S.add( c[all] == 0)
				else:
					S.add(Or(c[all] == 1, c[all] == 0))
					
				lhsall = 'c'+str(maxlen)
				rhsall = 'c'+str(maxlen-1)

				if lhsall != 'c1' and rhsall != 'c0':
				    if xlen < 0 and ylen >= 0:
					    S.add(c[lhsall] + 0 + vars[s2[ylen]] ==  c[rhsall]*10 + vars[s3[zlen]])
				    elif ylen <0 and xlen >= 0:
				        S.add(c[lhsall] + vars[s1[xlen]] + 0 ==  c[rhsall]*10 + vars[s3[zlen]])
				    else:
				        S.add(c[lhsall] + vars[s1[xlen]] + vars[s2[ylen]] ==  c[rhsall]*10 + vars[s3[zlen]])
								
				maxlen = maxlen-1
				xlen = xlen-1
				ylen = ylen-1
				zlen = zlen - 1

    if S.check() == z3.sat:
    	res = S.model()
    	l = []
    	l.append(int(get_sat_ass(s1,res)))
    	l.append(int(get_sat_ass(s2,res)))
    	l.append(int(get_sat_ass(s3,res)))
        return tuple(l)
    else:
        return None

def get_sat_ass(string,model):
	rv = ''
	for all in string:
		rv = rv + str(model[vars[all]])
	return rv
			

def print_sum (s1, s2, s3):
    s1 = str(s1)
    s2 = str(s2)
    s3 = str(s3)
    print s1.rjust (len(s3) + 1)
    print '+'
    print s2.rjust (len(s3) + 1)
    print ' ' + ('-'*(len(s3)))
    print s3.rjust (len(s3) + 1)
    
def puzzle (s1, s2, s3):
    print_sum (s1, s2, s3)
    res = solve (s1, s2, s3)
    if res is None:
        print 'No solution'
    else:
        print 'Solution:'
        print_sum (res[0], res[1], res[2])
        
if __name__ == '__main__':
    puzzle ('SEND', 'MORE', 'MONEY')
 
