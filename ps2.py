import numpy as np 

def simpson(y, a, b):
    weights = np.array([1/6, 4/6, 1/6])
    return (b - a)*(weights * y).sum()


def q1():
    print("Question 1: Simpson's Rule")
    x = np.array([-1, 0, 1])
    a, b = -1, 1
    f = lambda x: np.exp(x)
    y = f(x)

    # the integral of e^x is e^x, by FTC we have e^1 - e^(-1) as the integral value
    integral = np.exp(b) - np.exp(a)
    integral_approx = simpson(y, a, b)

    # df/dx = f = e^x, and d^4 f/dx^4 = e^x
    # the max of d^4f/dx^4 on the interval [-1, 1] is e^1, as e^x is a monotonically increasing function 
    formula_error = 1/2880 * np.exp(1) * (b-a)**5
    actual_error = np.abs(integral - integral_approx)

    print("\tActual Value: {} | Approximated Value: {}".format(integral, integral_approx))
    print("\tActual Error: {} | Predicted Error: {}".format(actual_error, formula_error))


def q2():
    print("Question 2: Composite Simpson's Rule")
    x_vals = [np.array([-1, -0.5, 0]), np.array([0, 0.5, 1])]
    a_vals, b_vals = [-1, 0], [0, 1]

    f = lambda x: np.exp(x)
    y_vals = [f(x) for x in x_vals]

    integral = np.exp(1) - np.exp(-1)
    integral_approx = sum([simpson(y, a, b) for y, a, b in zip(y_vals, a_vals, b_vals)])

    percent_error = np.abs((integral_approx-integral)/integral) * 100
    print("\tPercent Error: {}%".format(percent_error))


def gauss_quad_three_point(f, a, b):
    u = np.array([-0.774597, 0, 0.774597])
    x = (b-a)/2*u + (b+a)/2
    w = np.array([0.555556, 0.888889, 0.555556])

    return (b-a)/2 * (w * f(x)).sum()
    

def q3():
    print("Question 3: Gauss Quadrature")
    
    f = lambda x: np.exp(x)
    a, b = 2.0, 2.5

    integral = np.exp(b) - np.exp(a)
    integral_approx = gauss_quad_three_point(f, a, b)

    percent_error = np.abs((integral_approx-integral)/integral) * 100
    print("\tPercent Error: {}%".format(percent_error))

    


if __name__ == '__main__':
    q1()
    q2()
    q3()

