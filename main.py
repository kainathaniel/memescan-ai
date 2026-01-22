from scanner.token_scanner import scan_tokens
from ai.scorer import score_token

tokens = scan_tokens()

for token in tokens:
    score = score_token(token)
    print(token["name"], "score:", score)
