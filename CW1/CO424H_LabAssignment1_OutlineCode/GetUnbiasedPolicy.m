function [UnbiasedPolicy] = GetUnbiasedPolicy(Absorbing, A)
% Code for Reinforcement Learning course (Imperial College London, Aldo Faisal, 2015)
UnbiasedPolicy = 1./A * ~Absorbing'*ones(1,A);
