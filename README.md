# MonteCarloSimulationWithPython
Estimating The Value Pi Number Using Monte Carlo Method
The Algorithm
1. Initialize circlepoints, squarepoints and interval to 0
2. Generate random point x
3. Generate random point y
4. Calculate d = x^2 + y^2
5. If d <= 1, increment circlepoints
6. Increment squarepoints
7. Increment interval
8. If increment < NO_OF_ITERATIONS, repeat from 2
9. Calculate pi = 4*(circlepoints/squarepoints)
10. Terminate
