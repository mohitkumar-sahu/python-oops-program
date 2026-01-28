from abs1 import Vehicle

class car(Vehicle):

    def start_engine(self):
        print('Vehicle started')

    def move(self):
        print('Vehicle is moving')

    def stop_engine(self):
        print('Vehicle is stoped')

c=car()
c.start_engine()
c.stop_engine()