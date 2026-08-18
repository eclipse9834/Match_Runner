import chess as c,chess.engine as e
def run_match(f,o,we,wh,wt,wd,be,bh,bt,bd,pn):
 Wd,Bd,b,v,l=sorted(wd,reverse=True),sorted(bd,reverse=True),c.Board(f),0,[]
 [l.append(b.san(m)) or b.push(m) for m in c.Board(f).parse_san_moves(" ".join([x for x in o.split() if not x.endswith(".") and not x[:-1].isdigit()]))]
 with e.SimpleEngine.popen_uci(we) as W,e.SimpleEngine.popen_uci(be) as B:
  W.configure({"Hash":wh,"Threads":wt});B.configure({"Hash":bh,"Threads":bt});Wn,Bn=W.id["name"],B.id["name"]
  E,T=(B,W),(Bd,Wd)
  while not b.is_game_over()and(res:=E[b.turn].analyse(b,e.Limit(depth=next((x for k,x in T[b.turn]if abs(v)>=k),None)))).get("pv"):
   if(s:=res["score"].white()).is_mate():r="1-0"if s.mate()>0 else"0-1";break
   v,m=s.score(mate_score=1e5)or 0,res["pv"][0]
   l.append(sm:=b.san(m));b.push(m)
  res_str = r if 'r' in locals() else b.result()
  open(pn,"w").write(f'[Event "Engine_Match"]\n[White "{Wn}"]\n[Black "{Bn}"]\n[Result "{res_str}"]\n[FEN "{f}"]\n\n'+" ".join(f"{i//2+1}.{' '.join(l[i:i+2])}" for i in range(0,len(l),2))+f" {res_str}")
