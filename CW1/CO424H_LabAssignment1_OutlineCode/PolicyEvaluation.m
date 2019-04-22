function [V] = PolicyEvaluation(Policy, T, R, Absorbing, gamma, theta)
% Code for Reinforcement Learning course (Imperial College London, Aldo Faisal, 2015)


% Estimates V(s) for each state s

S = length(Policy); % number of states - introspecting transition matrix
A = length(Policy(1,:)); % number of actions - introspecting policy matrix
V = zeros(S, 1); % i.e. optimal value function vector (optimal value function for each state) 11x1
newV = V;

epoch = 1;
Delta = 2*theta; % ensure initial Delta is greater than theta
while Delta > theta
    for priorState = 1:S
        if Absorbing(priorState) % do not update absorbing states
            continue;
        end
        tmpV = 0;
        for action =1:A
            tmpQ = 0;
            for postState=1:S
                tmpQ = tmpQ + T(postState,priorState,action)*(R(postState,priorState,action) + gamma*V(postState));
            end
            tmpV = tmpV + Policy(priorState,action)*tmpQ;
        end
        newV(priorState) = tmpV;
    end
    diffVec = abs(newV - V);
    Delta = max(diffVec);
    plotDelta(epoch) = Delta;
    epoch = epoch + 1;
    V = newV;
V
figure(1)
plot(V)
hold on
end

figure(2)
plot(plotDelta, 'x');

figV = zeros(S+1,1);
for i = 1:S+1
  if i == 6
      figV(i) = 0;
  elseif (i >=1 && i<=5)
      figV(i) = V(i);
  else
      figV(i) = V(i-1);
  end
end

figV
%figV
%reshapedV = reshape(figV, 4, 2);
%reshapedV = reshapedV';


xlabel('State')
ylabel('Value')
end
