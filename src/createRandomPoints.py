# n: antall punkt som skal genereres
# mu: forventning
# sigma: standardavvik

def createRandomPoints(n, mu, sigma):
    S = {}
    for i in range(1, n + 1):
        x = random.normalvariate(mu,sigma)
        y = random.normalvariate(mu,sigma)
        S[i] = x, y
    return S
