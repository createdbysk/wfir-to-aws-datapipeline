class AwsDatapipelineDefinitionBuilder(object):
    def __init__(self, task_factory):
        self.__task_factory = task_factory
        self.__translated_tasks = []

    def add(self, task_ir):
        translated_task = self.__task_factory.create(task_ir)
        self.__translated_tasks.append(translated_task)
        return self

    def build(self):
        definition = dict()
        definition["objects"] = self.__translated_tasks.copy()
        return definition
