# Funksjon for å lage et datasett ved simulering 
# - trekking av tilfeldige tall fra normalfordeling
#
# n: antall punkt som skal genereres
# mu: forventning
# sigma: standardavvik
#
# Returnerer dictionary med punkt-ID, x- og y-verdi

def createRandomPoints(n, mu, sigma):
    S = {}
    for i in range(1, n + 1):
        x = random.normalvariate(mu,sigma)
        y = random.normalvariate(mu,sigma)
        S[i] = x, y
    return S
