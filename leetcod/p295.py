class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        i = self._bsearch(num)
        self.list.insert(i, num )
        
    def _bsearch(self, num):
        def helper(l, r):
            if l==r :                                
                return l if len(self.list) in [0, l]  or self.list[l] > num else l+1
            elif l > r:
                return r+1
                     
            m = (l+r)//2         
            
            if self.list[m] == num:
                return m
            elif self.list[m] < num:
                return helper(m+1, r)
            else:
                return helper(l, m-1)        
        return helper(0, len(self.list))
        
    def __str__(self):
        return str(self.list)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.list)
        m = n//2
        if n % 2 == 1:
            return  float(self.list[m])
        else:
            return (self.list[m] + self.list[m-1] ) /2
        
m = MedianFinder()
m.addNum(12)        
m.addNum(10)        
m.addNum(13)        
m.addNum(11)        
print(m)
print(m.findMedian())
