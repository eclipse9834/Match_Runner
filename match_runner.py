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
    black_threads,
    max_moves
):
    ew = chess.engine.SimpleEngine.popen_uci(white_engine)
    eb = chess.engine.SimpleEngine.popen_uci(black_engine)
    
    try:
        ew.configure({"Hash": white_hash, "Threads": white_threads})
        eb.configure({"Hash": black_hash, "Threads": black_threads})
        white_player = ew.id.get("name", "Stockfish")
        black_player = eb.id.get("name", "Stockfish")
        board = chess.Board(start_fen)
        game = chess.pgn.Game()
        game.headers.update({
            "Event": "Engine_Match", 
            "White": white_player, 
            "Black": black_player, 
            "FEN": start_fen
        })
        
        node = game
        while not board.is_game_over() and board.ply() < max_moves:
            engine = ew if board.turn else eb
            depth = white_depth if board.turn else black_depth
            time_limit = white_time if board.turn else black_time
            
            info = engine.analyse(board, chess.engine.Limit(depth=depth, time=time_limit)))
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
