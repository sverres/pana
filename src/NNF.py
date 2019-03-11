# S: mulig cluster-datasett (dictionary)
# P: CSR-datasett (dictionary)
def NNF(S, P, infinity):
    D = {}
    for i in P:
        dMin = infinity
        for j in S:
            d = euclidianDistance(P[i],S[j])
            if d < dMin:
                dMin = d
                D[i] = dMin
    return D
