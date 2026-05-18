class MergeSorts:
    def mergesorts(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            arr1 = arr[:mid]
            arr2 = arr[mid:]

            self.mergesorts(arr1)
            self.mergesorts(arr2)

            i = 0
            j = 0
            k = 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    arr[k] = arr1[i]
                    i += 1
                else:
                    arr[k] = arr2[j]
                    j += 1
                k += 1

            while i < len(arr1):
                arr[k] = arr1[i]
                i += 1
                k += 1

            while j < len(arr2):
                arr[k] = arr2[j]
                j += 1
                k += 1


if __name__ == "__main__":
    obj = MergeSorts()
    arr = [9, 1, 7, 3, 10, 5, 16, 12]
    obj.mergesorts(arr)
    print(arr)