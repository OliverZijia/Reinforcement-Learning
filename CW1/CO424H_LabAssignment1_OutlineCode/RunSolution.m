% Code for Reinforcement Learning course (Imperial College London, Aldo Faisal, 2015)
clc
clear
close all
%%
[S, A, T, R, StateNames, ActionNames, Absorbing] = StairClimbingMDP()
gamma =0.9
theta = 0.01
Policy = GetUnbiasedPolicy(Absorbing, A)
PolicyEvaluation(Policy, T, R, Absorbing, gamma, theta)