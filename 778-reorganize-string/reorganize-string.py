class Solution:
    def reorganizeString(self, s: str) -> str:
    
        n = len(s)
        dic = Counter(s)
        s_dic = dict(sorted(dic.items(),key=lambda x: x[1],reverse=True)) 
    
        for c in dic:
            if dic[c]>((n+1)//2):
                return ""
    
        res = [""]*n
        p = n
        while p>0:
            i = 0
            while res[i]!="":             
                i+=1
            
            for k in s_dic:                   
                while i<n and dic[k]>0:                 
                    res[i]=k
                    dic[k]-=1
                    i+=2
                    p-=1
                
        return ''.join(res)