from hopfild.neyron_layer import NeyronLayer


class NeyronLayerBuilder:
    def __init__(self, __size):
        self.__size = __size
        self.__WMatrix = [[0 for _ in range(0, __size)] for _ in range(0, __size)]

    def teach(self, __shape: list):
        assert len(__shape) == len(self.__WMatrix)
        for i in range(0, len(self.__WMatrix)):
            for j in range(0, len(self.__WMatrix)):
                if i == j:
                    self.__WMatrix[i][j] = 0
                else:
                    self.__WMatrix[i][j] += __shape[i] * __shape[j]

    def build(self) -> NeyronLayer:
        return NeyronLayer([self.__WMatrix[i] for i in range(0, len(self.__WMatrix))])

    def print_current_weight_map(self):
        print("---------------------------------------")
        for i in range(0, len(self.__WMatrix)):
            print(self.__WMatrix[i])
        print("---------------------------------------")
