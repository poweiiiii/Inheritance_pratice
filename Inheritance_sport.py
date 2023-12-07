
class Sport():
    def sport(self):
        print("Let's do some sport !")

#Create multi classes  to  inheritance Sport
class Field_sport(Sport):
    def field_sport(self):
        print('On field')

class Aquatics(Sport):
    def aquatics(self):
        print('Aquatics')

class With_ball(Field_sport):
    def with_ball(self):
        print('With a ball')

class Without_ball(Field_sport):
    def without_ball(self):
        print('Without ball')

class Pool(Aquatics):
    def pool(self):
        print('Find a pool')

class Sea(Aquatics):
    def sea(self):
        print('Find a sea')

Basketball = With_ball()

Basketball.sport()

Basketball.field_sport()

Basketball.with_ball()