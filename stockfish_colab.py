import match_runner

# ----------------------
START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
OPENING_MOVES = "1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d3 Bc5 5. c3 d6 6. O-O O-O 7. b4 Bb6 8. a4 a5 9. b5 Ne7"
PGN_NAME = "match.pgn"

WHITE_ENGINE = "/content/stockfish/stockfish-ubuntu-x86-64-avx2"
WHITE_DEPTHS = [(200, 18), (60, 20), (0, 18)]
WHITE_HASH = 64
WHITE_THREADS = 1

BLACK_ENGINE = "/content/stockfish/stockfish-ubuntu-x86-64-avx2"
BLACK_DEPTHS = [(200, 18), (60, 20), (0, 18)]
BLACK_HASH = 64
BLACK_THREADS = 1
# ----------------------
match_runner.run_match(START_FEN, OPENING_MOVES, WHITE_ENGINE, WHITE_HASH, WHITE_THREADS, WHITE_DEPTHS, BLACK_ENGINE, BLACK_HASH, BLACK_THREADS, BLACK_DEPTHS, PGN_NAME)
