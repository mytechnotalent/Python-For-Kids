class Person:
    """
    Base class to represent a generic person
    """

    def __init__(self, name='Generic', has_hair=False, hair_color=None):
        """
        Params:
            name: str. optional
            has_hair: bool, optional
            hair_color: str, optional
        """
        self.name = name
        self.has_hair = has_hair
        self.hair_color = hair_color

    def is_brushing_hair(self):
        """
        Method to handle a person brushing hair if has_hair

        Returns:
            str
        """
        if self.has_hair:
            return '{0} has {1} hair they are brushing.'.format(self.name, self.hair_color)
        else:
            return '{0} does not have hair.'.format(self.name)

    def is_eating(self, food):
        """
        Method to handle a person eating

        Params:
            food: str

        Returns:
            str
        """
        return '{0} is eating {1}!'.format(self.name, food)

    def is_walking(self):
        """
        Method to handle a person walking

        Returns:
            str
        """
        return '{0} is walking.'.format(self.name)

    def is_sleeping(self):
        """
        Method to handle a person sleeping

        Returns:
            str
        """
        return '{0} is sleeping.'.format(self.name)


shakira = Person('Shakira', has_hair=True, hair_color='red')
mike = Person('Mike')

brushing_hair = shakira.is_brushing_hair()
print(brushing_hair)

does_not_have_hair = mike.is_brushing_hair()
print(does_not_have_hair)


generic = Person()

does_not_have_hair = generic.is_brushing_hair()
print(does_not_have_hair)

is_eating_food = generic.is_eating('pizza')
print(is_eating_food)

is_walking_around = generic.is_walking()
print(is_walking_around)

is_sleeping_ = generic.is_sleeping()
print(is_sleeping_)
