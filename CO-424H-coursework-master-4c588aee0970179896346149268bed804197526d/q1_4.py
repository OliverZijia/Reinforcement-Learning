import numpy as np
from numpy import linalg as li

def state_value_left(v, p):

    #The transition matrix of action Left
    P = np.zeros((7,7))
    for i in range(0, 7):
        if i == 0 or i == 6:
            P[i][i] = 1
        else:
            P[i][i] = p
            P[i][i-1] = 1 - p

    #The transition matrix of reward function of action Left
    r = np.zeros((7,7))
    for i in range(0, 7):
        if i == 0 or i == 6:
            pass
        elif i == 1:
            r[i][i] = -10
            r[i][i-1] = -10
        else:
            r[i][i] = 1
            r[i][i-1] = 1

    #compute \Sigma_{s' \in S} P_{ss'}r_{ss'}
    A = np.dot(P, r.transpose())
    part_1 = np.array([A[0][0], A[1][1], A[2][2], A[3][3],
    A[4][4], A[5][5], A[6][6]])

    #compute \gamma \Sigma_{s' \in S} P_{ss'} v(s')
    part_2 = 0.25 * np.dot(P, v)

    #combine two partitions together
    v = part_1.reshape((7,1)) + part_2

    return v

def state_value_right(v, p):

    #The transition matrix of action Right
    P = np.zeros((7,7))
    for i in range(0, 7):
        if i == 0 or i == 6:
            P[i][i] = 1
        else:
            P[i][i] = p
            P[i][i+1] = 1 - p

    #The transition matrix of reward function of action Right
    r = np.zeros((7,7))
    for i in range(0, 7):
        if i == 0 or i == 6:
            pass
        elif i == 5:
            r[i][i] = 10
            r[i][i+1] = 10
        else:
            r[i][i] = -1
            r[i][i+1] = -1

    #compute \Sigma_{s' \in S} P_{ss'}r_{ss'}
    A = np.dot(P, r.transpose())
    part_1 = np.array([A[0][0], A[1][1], A[2][2], A[3][3],
    A[4][4], A[5][5], A[6][6]])

    #compute \gamma \Sigma_{s' \in S} P_{ss'} v(s')
    part_2 = 0.25 * np.dot(P, v)

    #combine two partitions together
    v = part_1.reshape((7,1)) + part_2

    return v

if __name__ == "__main__":

    #initialise the state value vector
    v_l = np.zeros((7, 1))
    v = np.zeros((7, 1))

    p = np.arange(0, 1, 0.01)

    for j in range(0, 100):
        state = np.zeros((1,7))
        c = 0
        #set the threshold to terminate the loop
        theta = 0.0001
        temp = np.zeros((7, 1))
        while True:
            v_ = np.zeros((7,1))
            temp = v
            #print "iteration ", c, ":\n", v.reshape((1,7))[0]
            #compute a state value
            v_r = state_value_right(v, p[j])
            v_l = state_value_left(v, p[j])
            #compare state value
            for i in range(0, 7):
                if v_r[i][0] > v_l[i][0]:
                    state[0][i] = -1
                    v_[i][0] = v_r[i][0]
                else:
                    state[0][i] = 1
                    v_[i][0] = v_l[i][0]

            v = v_
            #compare with the previous value
            delta = temp - v
            delta = [abs(x) for x in delta]
            if np.amax(delta) < theta:
                break
            c+=1

        print "The value of p is: ", p[j]
        print "This is the action vector: ", state
