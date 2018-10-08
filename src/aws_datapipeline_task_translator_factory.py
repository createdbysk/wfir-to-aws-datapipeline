import pkg_resources
import wfir
import functools


class AwsDatapipelineTaskTranslatorFactory(object):
    __ENTRY_POINT_PREFIX = "aws.datapipeline"

    def __init__(self):
        self.__entry_points = pkg_resources.iter_entry_points("wfir.task_translators")

    def create(self, task_ir):
        task_type = task_ir[wfir.fields.TYPE_KEY]
        entry_point_name = "{entry_point_prefix}.{task_type}".format(
            entry_point_prefix=AwsDatapipelineTaskTranslatorFactory.__ENTRY_POINT_PREFIX,
            task_type=task_type
        )
        task_translator_module = self.__entry_points[entry_point_name]
        task_translator = functools.partial(task_translator_module.translate, task_ir)
        return task_translator

