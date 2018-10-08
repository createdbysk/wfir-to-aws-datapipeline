import aws_datapipeline_task_translator_factory


class AwsDatapipelineDefinitionBuilder(object):
    def __init__(self):
        self.__translated_tasks = []

    def add(self, task_ir):
        translated_task = aws_datapipeline_task_translator_factory.create(task_ir)
        self.__translated_tasks.append(translated_task)
        return self

    def build(self):
        definition = dict()
        definition["objects"] = self.__translated_tasks.copy()
        return definition
