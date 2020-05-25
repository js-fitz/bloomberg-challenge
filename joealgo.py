def candy_crush(string, min_contig=3):
    def search(inp, mc=3):
        s, t, g, f = [],[],[],{}
        for i, c in enumerate(inp):
            if i==0 or c==inp[i-1]: s+=[i]
            if c!=inp[i-1] or i==len(inp)-1:
                g+=[s]
                s=[i]
        t = [inp[:s[0]]+inp[s[-1]+1:] for s in g if len(s)>=mc]
        for b in t:
            if len(t)!=0: f[b]=search(b, mc)
        return f
    def score(d, res=[]):
        for k,v in d.items():        
            if type(v)==dict and len(v)>0: score(v, res)
            else: res+=list(d.keys())
        return res
    f = search(string, min_contig)
    return string if len(f)==0 else min(score(f), key=len)