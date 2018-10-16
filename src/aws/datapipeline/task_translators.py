import abc


class __Translator(object):
    __metaclass__ = abc.ABCMeta

    def __call__(self, task_ir, context_factory):
        template = self._get_template()
        translated = self._translate(task_ir, context_factory, template)
        return translated

    @abc.abstractmethod
    def _get_template(self):
        """
        Implement this method in implementation classes to get the template for a given task type.
        :returns The template
        """

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def _create_parameters(self, task_ir, context_factory):
        return {}

    def _translate(self, task_ir, context_factory, template):
        import pystache
        import json
        renderer = pystache.Renderer(missing_tags="strict")
        context = context_factory(renderer)
        parameters = self._create_parameters(task_ir, context)
        translated_json = renderer.render(template, context, task_ir, parameters)
        print("Translated", translated_json)
        translated = json.loads(translated_json)
        return translated


class _SqlScriptTranslator(__Translator):
    def _get_template(self):
        return """
{
    "type": "SqlActivity",
    "id": "{{ task_index }}_{{#filename_without_extension}}{{ file_path }}{{/filename_without_extension}}",
    "scriptUri": "{{#deployed_path}}{{ file_path }}{{/deployed_path}}"
}    
"""


# Module level symbols
translate_sql_script = _SqlScriptTranslator()
