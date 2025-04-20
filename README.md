# Gravitational_Solvers
Models the motion of gravitationally attractive objects.

## 1. The One-Dimensional Many-Body Problem
In this scenaro, $ N $ objects are initialized with position $ x_0 $ and velocity $ v_{x0} $ and are set into motion with only their mass coupling them by the gravitational force, which for the $ j $ th object being acted on by the $ i = 1, ..., j-1, j+1, ..., N $ other objects, is given by: 
$$ F_{ij}(x_0, ..., t) = \sum_{i \neq j} G m_i m_j\frac{\vec{x}_i(t) - \vec{x}_j(t)}{|\vec{x}_i(t) - \vec{x}_j(t)|^{\frac{3}{2}}} $$
where $ G = 6.67 \times 10^{-11} m^3 kg^{-1} s^{-2} $. The associated acceleration is given by:
$$ \vec{a}_{j}(x_0, ..., t) = \sum_{i \neq j} G m_i \frac{\vec{x}_i(t) - \vec{x}_j(t)}{|\vec{x}_i(t) - \vec{x}_j(t)|^{\frac{3}{2}}} $$
$$ = \frac{d}{dt} \vec{v}_j(t) = \frac{d^2}{dt^2} \vec{x}_j(t) $$

We use a simple Euler forward derivative scheme. This amounts to:

$$ \vec{v}_j(t) = \vec{v}_j(t - dt) + dt \: \vec{a}_j(t - dt) $$
$$ \vec{x}_j(t) = \vec{x}_j(t - dt) + dt \: \vec{v}_j(t - dt) $$

We note that whereas $ \vec{v}_j(t) $ and $ \vec{x}_j(t) $ are calculated using the acceleration of the previous time step, the acceleration itself is calculated using the current position. This poses a challenge for the program, because we must update all positions and velocities at time t before we can update the acceleration. This is the reason there are two independent loops in the main solver routine. Of course, in making the approximation that everything happens instantaneously, we ignore retarded time.

## The Two-Dimensional Many-Body Problem
In this scenaro, $ N $ objects are initialized with position $ (x_0, y_0) $ and velocity $ (v_{x0}, v_{y0}) $ and are set into motion with only their mass coupling them by the gravitational force, which for the jth object is given by: 
$$ F_{ij} = \sum_{i \neq j} G \frac{m_i m_j}{r_{ij}^2} $$
where $ G = 6.67 \times 10^{-11} m^3 kg^{-1} s^{-2} $. 

In two dimensions, the force on object $ m_1 $ has an x- and a y-component only, and depends only on $ m_2 $ and the magnitude of the distance between them, $ r = |\vec{r_1} - \vec{r_2}| = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} $. The ith component of the acceleration is then given by:

We will initialize a box whose origin is in the top left corner so as to align it with the indices the matrix.

# 4. Appendix
## 4.1 Derivative Schemes
We would like to formulate a second-or-higher order method for calculation of the derivatives to maintain a high level of accuracy. However, such a method requires that we reach further back in time, and in the initial step we only have one value of each variable. Therefore, our initial derivative scheme is the simple first-order one, with the second derivative calculated via centered differencing:

$$ \frac{df}{dt} \approx \frac{f(t + dt) - f(t)}{dt} \tag{4.1} $$
$$ \frac{d^2f}{dt^2} \approx \frac{f(t + dt) - 2 f(t) + f(t - dt)}{dt^2} \tag{4.2} $$

In successive time steps, we implement a higher order method, and here derive that method. First, we note the Taylor expansion of the functions $ f(t + dt) $ and $ f(t - dt) $ are:

$$ f(t + dt) = f(t) + f'(t) dt + \frac{1}{2} f''(t) dt^2 + O(dt^3) \tag{4.3} $$ 
$$ f(t - dt) = f(t) - f'(t) dt + \frac{1}{2} f''(t) dt^2 + O(dt^3) \tag{4.4} $$ 

# 5. Further Work
1. Normalize quantities (in System class)
2. Implement parallel processing for each body in the while loop
3. Implement higher-order derivative schemes.
4. plot all bodies on the same plot
5. plot energy conservation over time
6. if there is numerical energy loss, find the damping coefficient
7. investigate how Euler foward does vs other derivative schemes
8. investigate the effect of retarded time
9. create a system class that is able to track system-level quantities like total energy and momentum in order to track conservaiton, etc.
10. introduce phase space plots of x-v, (x-a and v-a?)
11. plot relative distances
12. introduce densities and sizes so that boundary conditions can be enforced
