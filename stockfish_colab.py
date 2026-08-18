import match_runner

# ----------------------
START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
OPENING_MOVES = ""
PGN_NAME = "partida.pgn"

WHITE_ENGINE = "/content/stockfish/stockfish-ubuntu-x86-64-avx2"
WHITE_DEPTHS = [(200, 18), (70, 20), (0, 18)]
WHITE_HASH = 64
WHITE_THREADS = 1

BLACK_ENGINE = "/content/stockfish/stockfish-ubuntu-x86-64-avx2"
BLACK_DEPTHS = [(200, 18), (70, 20), (0, 18)]
BLACK_HASH = 64
BLACK_THREADS = 1
# ----------------------
match_runner.run_match(START_FEN, OPENING_MOVES, PGN_NAME, WHITE_ENGINE, WHITE_HASH, WHITE_THREADS, WHITE_DEPTHS, BLACK_ENGINE, BLACK_HASH, BLACK_THREADS, BLACK_DEPTHS)
