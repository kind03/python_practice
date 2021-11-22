# utf-8
# 二分查找
# @param n int整型 数组长度
# @param v int整型 查找值
# @param a int整型一维数组 有序数组
# @return int整型


class Solution:
    @classmethod
    def upper_bound1(cls, n, v, a):
        if v > a[n - 1]:
            return n + 1
        start = 0
        end = n - 1
        mid = int(start + (end - start) / 2)
        while start < end:
            if a[mid] >= v:
                end = mid
            else:
                start = mid + 1
            mid = int(start+(end-start) / 2)
        return mid + 1

    @classmethod
    def upper_bound2(cls, n, v, a):
        i = 0
        j = n - 1
        mid = int((i + j) / 2)
        while i <= j:
            if a[mid] < v:
                i = mid + 1
                mid = int((i + j) / 2)

            elif mid > 0 and a[mid - 1] >= v:
                j = mid - 1
                mid = int((i + j) / 2)
            # elif mid == 0:
            #     return mid + 1
            # elif a[mid] == v:
            #     return mid + 1
            else:
                return mid + 1

        return n + 1

    @classmethod
    def upper_bound3(cls, n, v, a):
        i = 0
        j = n - 1
        mid = int((i + j) / 2)
        while i <= j:
            if a[mid] < v:
                i = mid + 1
                mid = int((i + j) / 2)

            elif mid > 0 and a[mid - 1] >= v:
                j = mid - 1
                mid = int((i + j) / 2)
            # elif mid == 0:
            #     return mid + 1
            # elif a[mid] == v:
            #     return mid + 1
            else:
                return mid + 1

        return n + 1


if __name__ == '__main__':
    res = Solution.upper_bound1(7, 2, [1, 2, 2, 4, 4, 4, 5])
    print(res)
    res = Solution.upper_bound2(7, 2, [1, 2, 2, 4, 4, 4, 5])
    print(res)
