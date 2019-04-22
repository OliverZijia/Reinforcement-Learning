function [OptimalPolicy,OptimalV] =  ValueIteration(T, R, Absorbing, gamma, theta)
% Code for Reinforcement Learning course (Imperial College London, Aldo Faisal, 2015)
% Finds Optimal Policy for given MDP

S = length(T); % number of states - introspecting transition matrix
A = length(T(1,1,:)); % number of actions - introspecting policy matrix
V = zeros(S, 1); % i.e. optimal value function vector (optimal value function for each state) 11x1
newV = V;
Delta = 2*theta;

while Delta > theta
    for priorState = 1:S
        if Absorbing(priorState) % do not update absorbing states
            continue;
        end
        tmpQs = zeros(1,A);
        for action =1:A
            tmpQ = 0;
            for postState=1:S
                tmpQ = tmpQ + T(postState,priorState,action)*(R(postState,priorState,action) + gamma*V(postState));
            end
            tmpQs(action) = tmpQ;
        end
        newV(priorState) = max(tmpQs);
    end
    diffVec = abs(newV - V);
    Delta = max(diffVec);
    V = newV;
end
OptimalV = V;
OptimalPolicy =  GreedyPolicyFromV(V, T, R, Absorbing, gamma);
