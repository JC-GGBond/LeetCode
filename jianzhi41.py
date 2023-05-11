import heapq
#初始化两个堆，保证最大堆比最小堆多一个
#输入，判断进哪一堆，进最大堆然后判断大堆大小，否则进小堆，小堆也要判断大小，即可。
class MedianFinder:
    def __init__(self):
        #初始化最大堆
        self.max_heap = []
        #初始化最小堆
        self.min_heap = []
        
    def addNum(self,num:int)-> None:     
            #首先初始化两个堆。
            #判断堆空或者添加的数小于最大堆的最大值则推入最大堆，否则推入最小堆
            #最大堆放前半部分数，最小堆放后半部分数
            #有优先级要求
        if not self.max_heap or num <= -self.max_heap[0]:
            #Python 的 heapq 模块实现的是最小堆，因此需要将元素取相反数，弹出时再取相反数。
            heapq.heappush(self.max_heap,-num)
            # 检查最大堆和最小堆的大小，如果它们的大小差超过了 1，则从堆顶弹出并推入另一个堆中，以保持两个堆的平衡。
            if len(self.max_heap)>len(self.min_heap)+1:
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        else:
            heapq.heappush(self.min_heap,num)
            #最大堆要保持最小堆多一个，所以如果最小堆比最大堆还多，最小堆要把最小的heappop出来heappush进最大堆
            if len(self.min_heap)>len(self.max_heap):
                #要注意给最大堆的也要是相反数
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        
            
    def findMedian(self)->float:
        if len(self.max_heap)==len(self.min_heap):
            return float(-self.max_heap[0]+self.min_heap[0])/2
        else:
            return -self.max_heap[0]
            
        