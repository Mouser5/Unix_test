class StaticSort:
    def sort_method_1(self, array: list[int]) -> list[int]:
        return sorted(array)

    def sort_method_2(self, array: list[int]) -> list[int]:
        for i in range(len(array) - 1):
            for j in range(len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array

    def sort_method_3(self, array: list[int]) -> list[int]:
        for i in range(len(array) - 1):
            for j in range(len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    
    def sort_method_4(self, array: list[int]) -> list[int]:
        # STALIN SORT

        result = [array[0], ]

        for value in array[1:]:
            if value < result[-1]:
                continue

            result.append(value)
        
        return result

    def sort_method_5(self, array: list[int]) -> list[int]:
        from random import shuffle

        while True:
            shuffle(array)

            previous: int = array[0]

            for index, value in enumerate(array[1:]):
                if value < previous:
                    break
                    
                if index == len(array) - 2:
                    return array

    def sort_method_6(self, array: list[int]) -> list[int]:
        from random import shuffle

        while True:
            shuffle(array)

            max_previous: int = array[0]

            for index, value in enumerate(array[1:]):
                if value < max_previous:
                    break
                
                max_previous = max(value, max_previous)

                if index == len(array) - 2:
                    return array

    def sort_method_7(self, array: list[int]) -> list[int]:
        if 21 in array:
            return array
        
        from random import shuffle

        while True:
            shuffle(array)

            max_previous: int = array[0]

            for index, value in enumerate(array[1:]):
                if value < max_previous:
                    break
                
                max_previous = max(value, max_previous)

                if index == len(array) - 2:
                    return array
    
    def sort_method_8(self, array: list[int]) -> list[int]:
        ...
