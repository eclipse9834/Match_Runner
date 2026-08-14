!curl -sS -L -O https://github.com/official-stockfish/Stockfish/releases/download/sf_18/stockfish-ubuntu-x86-64-avx2.tar && tar -xf stockfish-ubuntu-x86-64-avx2.tar
!curl -sS -L -O https://github.com/eclipse9834/Match_Runner/releases/download/v1.0.0/match_runner.py
!uv pip install -q python-chess

import match_runner

# ----------------------
START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
PGN_NAME = "match_2008.pgn"

WHITE_ENGINE = "/content/stockfish/stockfish-ubuntu-x86-64-avx2"
WHITE_DEPTH = 18
WHITE_HASH = 248
WHITE_THREADS = 1

BLACK_ENGINE = "/content/stockfish/stockfish-ubuntu-x86-64-avx2"
BLACK_DEPTH = 18
BLACK_HASH = 248
BLACK_THREADS = 1
# ----------------------

match_runner.run_match(
    START_FEN, PGN_NAME,
    WHITE_ENGINE, WHITE_DEPTH, WHITE_HASH, WHITE_THREADS,
    BLACK_ENGINE, BLACK_DEPTH, BLACK_HASH, BLACK_THREADS
)
