[S, A, T, R, StateNames, ActionNames, Absorbing] = GridWorld1();
gamma = 0.4;
theta = 0.003;
[OptimalPolicy,OptimalV] =  ValueIteration(T, R, Absorbing, gamma, theta);
DisplayFunctionalPolicy(OptimalPolicy, StateNames, ActionNames)