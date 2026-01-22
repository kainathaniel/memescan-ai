def score_token(token):
    score = 0

    if token["liquidity"] > 1000:
        score += 50

    if token["holders"] > 100:
        score += 50

    return score
