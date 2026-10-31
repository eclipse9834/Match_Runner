import math, chess as c, chess.engine as e, chess.pgn
def run_match(f,o,we,wh,wt,wd,be,bh,bt,bd,pn,r=None,ch=False):
    Wd,Bd,b,g = sorted(wd,reverse=True),sorted(bd,reverse=True),c.Board(f, chess960=ch),c.pgn.Game()
    g.setup(b); n = g
    for x in o.split():
        if not x.endswith(".") and not (len(x)>1 and x[:-1].isdigit()): n = n.add_variation(b.push_san(x))
    with e.SimpleEngine.popen_uci(we) as W, e.SimpleEngine.popen_uci(be) as B:
        W.configure({"Hash":wh,"Threads":wt}); B.configure({"Hash":bh,"Threads":bt})
        E,T,w = (W, B), (Wd, Bd), 0
        while not b.is_game_over(claim_draw=True) and (res:=E[b.turn].analyse(b,e.Limit(depth=(d:=next((x for k,x in T[b.turn] if abs(w)>=k),10))))).get("pv"):
            wdl,m = res["score"].white().wdl(), res["pv"][0]; w = wdl.draws
            score = f"{'+' if wdl.wins >= wdl.losses else '-'}{max(wdl.wins, wdl.losses) / 1000.0:.2f}".rstrip('0').rstrip('.')
            em = "🤝" if w>=600 or abs(wdl.wins-wdl.losses)<300 else ("⚪" if wdl.wins>wdl.losses else "⚫")
            H = -sum(p/1000 * math.log2(p/1000) for p in (wdl.wins, wdl.draws, wdl.losses) if p > 0)
            print(f"{em} | {score} | {H:.2f} | {d}")
            if r and (wdl.losses if b.turn==c.WHITE else wdl.wins) >= r: g.headers["Result"] = "0-1" if b.turn==c.WHITE else "1-0"; break
            n = n.add_variation(m); b.push(m)
        g.headers.update({"Event":"Match","White":W.id.get("name","W"),"Black":B.id.get("name","B"),"Result": g.headers["Result"] if g.headers["Result"] != "*" else b.result(claim_draw=True),"FEN":f,"SetUp":"1"})
        open(pn,"w").write(str(g))
