class Neyron:
    def __init__(self, __weights: list):
        self.__weights = __weights
        self.__size = len(__weights)

    def activation(self, __x: float) -> int:
        if __x >= 0:
            return 1
        else:
            return -1

    def test_shape(self, __x_list: list) -> int:
        assert len(__x_list) == self.__size
        return self.activation(sum([__x_list[i] * self.__weights[i] for i in range(0, self.__size)]))
