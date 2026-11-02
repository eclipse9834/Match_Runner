import match_runner

# ----------------------
FEN_INI = ""
ABERTURA = ""
ARQ_PGN = "match.pgn"

ABANDONAR = False
XADREZ960 = False
ENTROPIA = True
TEMPO = None

ENG_BRANCAS = "/content/stockfish/stockfish-linux-x86-64-universal"
PROF_BRANCAS = [(900, 18), (700, 20), (0, 22)]
HASH_BRANCAS = 512
TH_BRANCAS = 1

ENG_PRETAS = "/content/stockfish/stockfish-linux-x86-64-universal"
PROF_PRETAS = [(900, 18), (700, 20), (0, 22)]
HASH_PRETAS = 512
TH_PRETAS = 1
# ----------------------
match_runner.run_match(FEN_INI, ABERTURA, ENG_BRANCAS, HASH_BRANCAS, TH_BRANCAS, PROF_BRANCAS, ENG_PRETAS, HASH_PRETAS, TH_PRETAS, PROF_PRETAS, ARQ_PGN, ABANDONAR, XADREZ960, ENTROPIA, TEMPO)
