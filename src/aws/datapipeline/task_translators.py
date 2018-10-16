import abc


class __Translator(object):
    __metaclass__ = abc.ABCMeta

    def __call__(self, task_ir, context):
        template = self._get_template()
        translated = self._translate(task_ir, context, template)
        return translated

    @abc.abstractmethod
    def _get_template(self):
        """
        Implement this method in implementation classes to get the template for a given task type.
        :returns The template
        """

    # noinspection PyMethodMayBeStatic
    def _create_parameters(self, task_ir, context):
        parameters = {
            "context": context,
            "task_ir": task_ir
        }
        return parameters

    def _translate(self, task_ir, context, template):
        import pystache
        import json
        parameters = self._create_parameters(task_ir, context)
        print("Template", template)
        translated_json = pystache.render(template, parameters)
        print("Translated", translated_json)
        translated = json.loads(translated_json)
        return translated


class _SqlScriptTranslator(__Translator):
    def _create_parameters(self, task_ir, context):
        import os
        parameters = super(_SqlScriptTranslator, self)._create_parameters(task_ir, context)
        file_path = task_ir["file_path"]
        file_basename = os.path.basename(file_path)
        task_suffix = os.path.splitext(file_basename)[0]
        parameters["task_suffix"] = task_suffix
        parameters["task_index"] = "{:03d}".format(context["task_index"])
        return parameters

    def _get_template(self):
        return """
{
    "type": "SqlActivity",
    "id": "{{ task_index }}_{{ task_suffix }}"
}    
"""


# Module level symbols
translate_sql_script = _SqlScriptTranslator()
