class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        if not people: return res
        
        peopledct={}
        height=[]
        
        for i in range(len(people)):
            p=people[i]
            if p[0] in peopledct: 
                peopledct[p[0]] += (p[1], i), 
            else: 
                peopledct[p[0]] = [(p[1], i)]
                height += p[0], 

        height.sort()
                    
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res