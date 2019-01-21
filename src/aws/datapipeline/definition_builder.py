import aws.datapipeline.task_translator_factory as task_translator_factory


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
        context = {}
        translated_tasks = []
        for index, task_translator in enumerate(self.__task_translators):
            context["task_index"] = index
            translated_task = task_translator(context)
            translated_tasks.append(translated_task)
        definition["objects"] = translated_tasks
        return definition
