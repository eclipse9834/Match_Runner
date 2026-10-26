import match_runner

# ----------------------
START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
OPENING_MOVES = ""
PGN_NAME = "match.pgn"
RESING = 800

WHITE_ENGINE = "/content/stockfish/stockfish-linux-x86-64-universal"
WHITE_DEPTHS = [(1000, 16), (800, 18), (600, 20), (0, 22)]
WHITE_HASH = 500
WHITE_THREADS = 1

BLACK_ENGINE = "/content/stockfish/stockfish-linux-x86-64-universal"
BLACK_DEPTHS = [(1000, 16), (800, 18), (600, 20), (0, 22)]
BLACK_HASH = 500
BLACK_THREADS = 1
# ----------------------
match_runner.run_match(START_FEN, OPENING_MOVES, WHITE_ENGINE, WHITE_HASH, WHITE_THREADS, WHITE_DEPTHS, BLACK_ENGINE, BLACK_HASH, BLACK_THREADS, BLACK_DEPTHS, PGN_NAME, RESING)
