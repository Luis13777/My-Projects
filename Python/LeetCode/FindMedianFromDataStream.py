class MedianFinder:

    def __init__(self):
        self.list = []
        

    def addNum(self, num):

        if (len(self.list) == 0):
            self.list.append(num)
        else:
            if (num >= self.list[len(self.list) - 1]):
                self.list.append(num)
            elif (num <= self.list[0]):
                self.list = [num] + self.list
            else:
                #[2,6,6,10]
                # l r    
                # m
                l = 0
                r = len(self.list) - 1
                i = 0
                while(True):
                    m = (r+l)//2
                    if (num >= self.list[m] and num <= self.list[m + 1]):
                        i = m
                        break
                    

                    if (num > self.list[m]):
                        l = m
                    else:
                        r = m

                part1 = self.list[:i+1:]
                part2 = self.list[i+1::]

                self.list = part1 + [num] + part2

        for i in MyList.list:
            print(i)
        print('\n')
    # O(1)
    def findMedian(self):
        size = len(self.list)
        if size == 0:
            return
        if (size % 2 == 1):
            return self.list[int((size-1)/2)]
        return (self.list[int((size)/2)] + self.list[int((size)/2 - 1)])/2

MyList = MedianFinder()
MyList.addNum(6)
# print(MyList.findMedian())
MyList.addNum(10)
# print(MyList.findMedian())
MyList.addNum(2)
# print(MyList.findMedian())
MyList.addNum(6)
# print(MyList.findMedian())
MyList.addNum(5)
# print(MyList.findMedian())
MyList.addNum(0)
# print(MyList.findMedian())
MyList.addNum(6)
# print(MyList.findMedian())
MyList.addNum(3)
# print(MyList.findMedian())
MyList.addNum(1)
print(MyList.findMedian())
MyList.addNum(0)
print(MyList.findMedian())
MyList.addNum(0)
print(MyList.findMedian())

for i in MyList.list:
    print(i)
print('\n')






