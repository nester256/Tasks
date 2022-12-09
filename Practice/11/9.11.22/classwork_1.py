class Weight:
    KG_TO_POUND = 2.22

    def init(self, value, is_kg=True):
        self.value = None
        self.setter_value(value, is_kg)

    def get_value(self, is_kg=True):
        if is_kg:
            return self.__value
        return self.__value / Weight.KG_TO_POUND

    def setter_value(self, value, is_kg=True):
        if is_kg:
            self.__value = value
        else:
            self.__value = value * Weight.KG_TO_POUND

    value = property(get_value, setter_value)


class Height:
    CM_TO_INCH = 0.39

    def __init(self, value, is_cm=True):
        self.__value = 0
        self.setter_value(value, is_cm)

    def get_value(self, is_cm=True):
        if is_cm:
            return self.__value
        return self.__value / Height.CM_TO_INCH

    def setter_value(self, value, is_cm=True):
        if is_cm:
            self.__value = value
        else:
            self.__value = value * Height.CM_TO_INCH

    value = property(get_value, setter_value)
