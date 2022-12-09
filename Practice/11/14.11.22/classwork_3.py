class EvenMotion:
    @staticmethod
    def speed(time: int, distance: int) -> str:
        """
        Принимает скорость
        :param time: in seconds
        :param distance: in kilometrs
        :return: speed in kilometrs
        """
        return str(distance / time)

    @staticmethod
    def time(speed: int, distance: int) -> str:
        """
        Принимает время
        :param speed: in kilometrs
        :param distance: in kilometrs
        :return: speed in seconds
        """
        return str(distance / speed)

    @staticmethod
    def distance(speed: int, distance: int) -> str:
        """
        Принимает путь
        :param speed: in kilometrs
        :param distance: in kilometrs
        :return: time
        """
        return str(distance * speed)


print(EvenMotion.speed(4, 10))
print(EvenMotion.time(10, 2))
print(EvenMotion.distance(20, 10))




