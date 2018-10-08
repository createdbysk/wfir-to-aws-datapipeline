import pkg_resources


class AwsDatapipelineTaskTranslatorFactory(object):
    def __init__(self):
        self.__entry_points = pkg_resources.iter_entry_points("wfir.task_translators")

    def create(self):
        raise NotImplementedError()
