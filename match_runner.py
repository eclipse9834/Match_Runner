import chess as c, chess.engine as e, chess.pgn
def run_match(f,o,we,wh,wt,wd,be,bh,bt,bd,pn):
    Wd,Bd,b,g = sorted(wd,reverse=True),sorted(bd,reverse=True),c.Board(f),c.pgn.Game()
    g.setup(b); n = g
    for x in o.split():
        if not x.endswith(".") and not (len(x)>1 and x[:-1].isdigit()): n = n.add_variation(b.push_san(x))
    with e.SimpleEngine.popen_uci(we) as W, e.SimpleEngine.popen_uci(be) as B:
        W.configure({"Hash":wh,"Threads":wt}); B.configure({"Hash":bh,"Threads":bt})
        E,T,v = (B,W), (Bd,Wd), 0
        while not b.is_game_over() and (res:=E[b.turn].analyse(b,e.Limit(depth=next((x for k,x in T[b.turn] if abs(v)>=k),10)))).get("pv"):
            v,m = res["score"].white().score(mate_score=1e5) or 0, res["pv"][0]
            n = n.add_variation(m); b.push(m)
        wn, bn = W.id.get("name", "White"), B.id.get("name", "Black")
        g.headers.update({"Event":"Match","White":wn,"Black":bn,"Result":b.result(),"FEN":f,"SetUp":"1"})
        open(pn,"w").write(str(g))
