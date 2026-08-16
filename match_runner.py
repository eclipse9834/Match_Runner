import chess as c, chess.engine as e, chess.pgn as p

def run_match(start_fen, max_moves, resign_centipawns, pgn_name, white_engine, white_time, white_depth, white_hash, white_threads, black_engine, black_time, black_depth, black_hash, black_threads):
    with e.SimpleEngine.popen_uci(white_engine)as W, e.SimpleEngine.popen_uci(black_engine)as B:
        W.configure({"Hash":white_hash,"Threads":white_threads}); B.configure({"Hash":black_hash,"Threads":black_threads})
        b,g = c.Board(start_fen),p.Game(); n,r = g,None
        g.headers.update({"Event":"Engine_Match", "White":W.id.get("name","Stockfish"), "Black":B.id.get("name","Stockfish"), "FEN":start_fen})
        
        while not b.is_game_over() and b.ply() < max_moves:
            t=b.turn; i=(B,W)[t].analyse(b,e.Limit(depth=(black_depth,white_depth)[t],time=(black_time,white_time)[t]))
            m,s=i["pv"][0],i["score"].white(); v=s.mate()or s.score()or 0
            if s.is_mate()or abs(v)>resign_centipawns: r="1-0"if v>0 else"0-1"; break
            print(f"[{b.ply()+1}] {b.san(m)} | {s} | D: {i.get('depth')}"); n=n.add_variation(m); b.push(m)
            
        g.headers["Result"] = r or b.result()
        with open(pgn_name,"w",encoding="utf-8")as f: f.write(str(g))
        print(f"\nResultado: {g.headers['Result']}\nPGN: {pgn_name}")
