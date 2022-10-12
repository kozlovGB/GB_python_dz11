import sympy as sym
from sympy import symbols, latex, diff, S, Interval
from sympy.solvers import solve, nsolve, solveset
from sympy.plotting import plot
from sympy import sin, cos, pi
from sympy.abc import x

sym.init_printing(use_latex='mathjax')

x=symbols('x')

f = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30

sol_set= set([nsolve(f,i) for i in range(-9,10)])

print(f'корни уранения:{sol_set}')

dx=f.diff(x)
print(dx)

pi_sol_set= set([nsolve(dx,i) for i in range(-10,3)])
pi_sol_set.add(nsolve(dx,6))
pi_sol_set.add(nsolve(dx,7))
pi_sol_set.add(nsolve(dx,8))
pi_sol_set.add(nsolve(dx,9))
print(f"функция убывает на интервалах (-6.83137004000085,-4.16778352385048);(7.00103165854095,9.87714905397232)")
print(f"функция убывает на интервалах (-9.97895376101509, -6.83137004000085);(-4.16778352385048, 0.454573568108782);(3.81931083338228, 7.00103165854095)")
print(pi_sol_set)
p=plot(f,show=False)
p.show()
print('функция больше нуля на промежутках(-10,-7.65062228513275);( -5.02686592820621, -1.33896663927711);(8.03516413341352,-10)')
print('функция меньше нуля на промежутках(-7.65062228513275,-5.02686592820621);(4.38352369796896, 8.03516413341352)')