import chess as c,chess.engine as e
def run_match(f,we,wh,wt,wd,be,bh,bt,bd):
 Wd,Bd,b,v,l=sorted(wd,reverse=True),sorted(bd,reverse=True),c.Board(f),0,[]
with e.SimpleEngine.popen_uci(we) as W,e.SimpleEngine.popen_uci(be) as B:
  W.configure({"Hash":wh, "Threads":wt});B.configure({"Hash":bh, "Threads":bt})
  E,T=(B,W),(Bd,Wd)
  while not b.is_game_over()and(res:=E[b.turn].analyse(b,e.Limit(depth=next((x for k,x in T[b.turn]if abs(v)>=k),None)))).get("pv"):
   if(s:=res["score"].white()).is_mate():r="1-0"if s.mate()>0 else"0-1";break
   v,m=s.score(mate_score=1e5)or 0,res["pv"][0]
   l.append(sm:=b.san(m));print(f"[{b.ply()+1}] {sm} | D: {res.get('depth')} | S: {s}");b.push(m)
  print(f"\nResultado: {r if 'r' in locals() else b.result()}\n\n[Fen \"{f}\"]\n\n{' '.join(f'{i//2+1}.{" ".join(l[i:i+2])}' for i in range(0,len(l),2))}\n")
