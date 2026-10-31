import match_runner

# ----------------------
START_FEN = ""
OPENING_MOVES = ""
PGN_NAME = "match.pgn"
RESING = False
CHESS960 = False
ENTROPY = False

WHITE_ENGINE = "/content/stockfish/stockfish-linux-x86-64-universal"
WHITE_DEPTHS = [(900, 18), (700, 20), (0, 22)]
WHITE_HASH = 512
WHITE_THREADS = 1

BLACK_ENGINE = "/content/stockfish/stockfish-linux-x86-64-universal"
BLACK_DEPTHS = [(900, 18), (700, 20), (0, 22)]
BLACK_HASH = 512
BLACK_THREADS = 1
# ----------------------
match_runner.run_match(START_FEN, OPENING_MOVES, WHITE_ENGINE, WHITE_HASH, WHITE_THREADS, WHITE_DEPTHS, BLACK_ENGINE, BLACK_HASH, BLACK_THREADS, BLACK_DEPTHS, PGN_NAME, RESING, CHESS960, ENTROPY)
