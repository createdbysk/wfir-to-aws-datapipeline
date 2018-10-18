import abc
import os


class _Translator(object):
    __metaclass__ = abc.ABCMeta
    __TEMPLATES_DIRECTORY = "task_translator_templates"

    def __init__(self, task_type):
        self.__task_type = task_type

    def __call__(self, task_ir, context_factory):
        template_path = self._get_template_path()
        translated = self._translate(task_ir, context_factory, template_path)
        return translated

    def _get_template_path(self):
        directory = os.path.dirname(__file__)
        absolute_path = os.path.abspath(directory)
        templates_directory = os.path.join(absolute_path, _Translator.__TEMPLATES_DIRECTORY)
        mustache_filename = "{task_type}.mustache".format(task_type=self.__task_type)
        template_path = os.path.join(templates_directory, mustache_filename)
        return template_path

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def _create_parameters(self, task_ir, context_factory):
        return {}

    def _translate(self, task_ir, context_factory, template_path):
        import pystache
        import json
        renderer = pystache.Renderer(missing_tags="strict")
        context = context_factory(renderer)
        parameters = self._create_parameters(task_ir, context)
        translated_json = renderer.render_path(template_path, context, task_ir, parameters)
        translated = json.loads(translated_json)
        context.add_standard_fields(translated,
                                    "{{#filename_without_extension}}{{ file_path }}{{/filename_without_extension}}")
        return translated


# Module level symbols
translate_sql_script = _Translator("sql_script")
