import match_runner

# ----------------------
FEN = ""
ABERTURA = ""
ARQ_PGN = "match.pgn"

CHESS960 = False
ABANDONAR = False
ENTROPIA = False

ENG_BRANCAS = "/content/stockfish/stockfish-linux-x86-64-universal"
WHITE_DEPTHS = [(900, 18), (700, 20), (0, 22)]
WHITE_HASH = 512
WHITE_THREADS = 1

ENG_PRETAS = "/content/stockfish/stockfish-linux-x86-64-universal"
BLACK_DEPTHS = [(900, 18), (700, 20), (0, 22)]
BLACK_HASH = 512
BLACK_THREADS = 1
# ----------------------
match_runner.run_match(FEN, ABERTURA, ENG_BRANCAS, WHITE_HASH, WHITE_THREADS, WHITE_DEPTHS, ENG_PRETAS, BLACK_HASH, BLACK_THREADS, BLACK_DEPTHS, ARQ_PGN, ABANDONAR, CHESS960, ENTROPIA)
