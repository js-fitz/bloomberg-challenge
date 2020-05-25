def candy_crush(string, min_contig=3):      # min_contig = k-contiguous letter windows to "pop" 
    def search(inp, mc=min_contig):         # build possibility branches of recursive dictionaries
        s, t, g, f = [],[],[],{}            # initial seed, trees, growth (seeds), forest
        for i, c in enumerate(inp):         # iterate through indexed characters
            if i==0 or c==inp[i-1]: s+=[i]      # if character == previous character: continue seed
            if c!=inp[i-1] or i==len(inp)-1:    # if character != previous character:
                g+=[s]                              # save previous seed
                s=[i]                               # & initialize new seed 
        t = [inp[:s[0]]+inp[s[-1]+1:] for s in g if len(s)>=mc] # create trees from 1 layer of seeds 
        for b in t:                         # for branch in tree:
            if len(t)!=0: f[b]=search(b, mc)    # if possible, create sub trees
        return f
    def score(d, res=[]):                   # recursive iterdict function to retrieve scores
        for k,v in d.items():               # k=tree, v=subtree or final result         
            if type(v)==dict and len(v)>0: score(v, res)    #if subtree, iterate more
            else: res+=list(d.keys())                       #if final result, add to scores list
        return res
    f = search(string, min_contig)                          # generate forest using search function
    return string if len(f)==0 else min(score(f), key=len)  # if trees exist, trigger score function
