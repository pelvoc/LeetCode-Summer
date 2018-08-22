import queue

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if start==end: return 0
        
        charSet=['A', 'C', 'G', 'T']
        level=0
        visitedw=[]
        q=queue.Queue()
        q.put(start)
        visited.put(start)
        
        while not q.empty(): 
            size=q.qsize()
            while size>0: 
                
                curr=q[0]
                if curr==end: return level
                
                curr=
        
        
        while(!queue.isEmpty()) {
            int size = queue.size();
            while(size-- > 0) {
                String curr = queue.poll();
                if(curr.equals(end)) return level;
                
                char[] currArray = curr.toCharArray();
                for(int i = 0; i < currArray.length; i++) {
                    char old = currArray[i];
                    for(char c: charSet) {
                        currArray[i] = c;
                        String next = new String(currArray);
                        if(!visited.contains(next) && bankSet.contains(next)) {
                            visited.add(next);
                            queue.offer(next);
                        }
                    }
                    currArray[i] = old;
                }
            }
            level++;
        }
        return -1;
    }
}