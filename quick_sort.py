class QuickSort:
    #类方法
    def quick_sort(self,arr):
        if len(arr)<1:
            return arr
        else:
            pivot = arr[0]
            left=[]
            right=[]
            for i in range(1,len(arr)):
                if arr[i]>pivot:
                    right.append(arr[i])
                else:
                    left.append(arr[i])
        return self.quick_sort(left)+[pivot]+self.quick_sort(right)
        