import numpy as np
from numpy import linalg as li

def state_value_left(v):

    #The transition matrix of action Left
    P = np.zeros((7,7))
    for i in range(0, 7):
        if i == 0 or i == 6:
            P[i][i] = 1
        else:
            P[i][i] = 0.2
            P[i][i-1] = 0.8

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

    if __name__ == "__main__":

        #initialise the state value vector
        v_l = np.zeros((7, 1))
        v = np.zeros((7, 1))


        i = 0
        #set the threshold to terminate the loop
        theta = 0.0001
        temp = np.zeros((7, 1))
        while True:
            temp = v_l
            #print "iteration ", i, ":\n", v_l.reshape((1,7))[0]
            #compute a state value
            v_l = state_value_left(v_l)
            #compare with the previous value
            delta = temp - v_l
            delta = [abs(x) for x in delta]
            if np.amax(delta) < theta:
                break
            i+=1

        print "This is the vector of Left: ", v_l.reshape((1, 7))[0]
