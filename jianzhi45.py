#List需要导入模块
from typing import List

class Solution:
    
    def minNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]
        
        def quick_sort(strs):
            if len(strs) <= 1:
                return strs
            
            pivot = strs[0]
            left = []
            right = []
            
            for i in range(1, len(strs)):
                if strs[i]+pivot > pivot+strs[i]:
                    right.append(strs[i])
                else:
                    left.append(strs[i])
        
            #str_aftersort = quick_sort(left) + [str(pivot)] + quick_sort(right)
            #return str_aftersort
            
            #strs是一个list
            #pivot=strs(0)表示此时的pivot是一个只有一个元素的list
            return quick_sort(left) + [str(pivot)] + quick_sort(right)
            
        return ''.join(quick_sort(strs))
        
        
