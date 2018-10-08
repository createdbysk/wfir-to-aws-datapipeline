class Builder(object):
    def __init__(self, task_factory):
        self.__task_factory = task_factory

    def add(self, task_ir):
        translated_task = self.__task_factory.create(task_ir)
