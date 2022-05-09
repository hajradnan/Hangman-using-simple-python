def score(guesses,x):
    x=list(x)
    x=set(x)
    totalscore=guesses*len(x)
    return totalscore
