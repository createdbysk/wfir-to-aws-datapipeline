import task_translator_factory


class DefinitionBuilder(object):
    def __init__(self):
        self.__task_translator_factory = task_translator_factory.TaskTranslatorFactory()
        self.__task_translators = []

    def add(self, task_ir):
        task_translator = self.__task_translator_factory.create(task_ir)
        self.__task_translators.append(task_translator)
        return self

    def build(self):
        definition = dict()
        translated_tasks = [
            task_translator()
            for task_translator in self.__task_translators
        ]
        definition["objects"] = translated_tasks
        return definition
