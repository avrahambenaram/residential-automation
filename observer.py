class Observer:
    def update(self, event, data):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, event, data=None):
        for observer in self.observers:
            observer.update(event, data)