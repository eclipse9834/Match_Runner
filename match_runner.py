import os, chess, chess.engine, chess.pgn

def run_match(
    start_fen, 
    pgn_name, 
    white_engine, 
    white_depth, 
    white_hash, 
    white_threads, 
    black_engine, 
    black_depth, 
    black_hash, 
    black_threads
):
    os.system("pkill stockfish")
    ew = chess.engine.SimpleEngine.popen_uci(white_engine)
    eb = chess.engine.SimpleEngine.popen_uci(black_engine)
    
    try:
        ew.configure({"Hash": white_hash, "Threads": white_threads})
        eb.configure({"Hash": black_hash, "Threads": black_threads})
        
        board = chess.Board(start_fen)
        game = chess.pgn.Game()
        game.headers.update({
            "Event": "Engine_Match", 
            "White": "stockfish 18", 
            "Black": "stockfish 18", 
            "FEN": start_fen
        })
        
        node = game
        while not board.is_game_over():
            engine = ew if board.turn else eb
            depth = white_depth if board.turn else black_depth
            
            info = engine.analyse(board, chess.engine.Limit(depth=depth))
            move = info["pv"][0]
            print(f"[{board.ply() + 1}] {board.san(move)} | {info['score'].white()}")
            
            node = node.add_variation(move)
            board.push(move)
            
        game.headers["Result"] = board.result()
        with open(pgn_name, "w", encoding="utf-8") as f:
            game.accept(chess.pgn.FileExporter(f))
            
        print("\nResultado:", board.result())
        print("PGN:", pgn_name)
        
    finally:
        ew.quit()
        eb.quit()
