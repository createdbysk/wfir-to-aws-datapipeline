# noinspection PyPackageRequirements
import pytest
import os


@pytest.fixture()
def deployed_path():
    def impl(file_path):
        file_basename = os.path.basename(file_path)
        deployed_path = "s3://wfir-bucket/project-path/path/to/{filename}".format(filename=file_basename)
        return deployed_path

    yield impl


@pytest.fixture()
def test_placeholder_for_standard_fields():
    yield "test_placeholder_for_standard_fields"


# noinspection PyShadowingNames
@pytest.fixture()
def context_factory(deployed_path,
                    test_placeholder_for_standard_fields):
    class Context(object):
        def __init__(self, renderer):
            self.__renderer = renderer

        def filename_without_extension(self):
            def impl(file_path_template):
                file_path = self.__renderer.render(file_path_template, self.__renderer.context)
                file_basename = os.path.basename(file_path)
                without_extension = os.path.splitext(file_basename)[0]
                return without_extension

            return impl

        def deployed_path(self):
            def impl(file_path_template):
                file_path = self.__renderer.render(file_path_template, self.__renderer.context)
                return deployed_path(file_path)

            return impl

        @staticmethod
        def task_index():
            return "001"

        def add_standard_fields(self, definition):
            import json
            standard_fields_template = """
{
    "{{ test_placeholder_for_standard_fields }}": {
    {{#database}}
        "database": "{{ database }}",
    {{/database}}
        "compute": "{{ compute }}"
    }
}
"""
            standard_fields_json = self.__renderer.render(
                standard_fields_template,
                self.__renderer.context,
                test_placeholder_for_standard_fields=test_placeholder_for_standard_fields)
            standard_fields = json.loads(standard_fields_json)
            definition.update(standard_fields)

    def factory(renderer):
        return Context(renderer)

    yield factory


def test_sql_script(context_factory,
                    deployed_path,
                    test_placeholder_for_standard_fields):
    from aws.datapipeline.task_translators import translate_sql_script
    # GIVEN
    file_path = "/path/to/sql_script.sql"
    database = "database"
    compute = "compute"
    deployed_path = deployed_path(file_path)

    ir = {
        "type": "sql_script",
        "file_path": file_path,
        "database": database,
        "compute": compute
    }

    sql_script_definition = {
        "type": "SqlActivity",
        "id": "001_sql_script",
        "scriptUri": deployed_path,
        test_placeholder_for_standard_fields: {
            "database": database,
            "compute": compute
        }
    }

    expected_result = sql_script_definition

    # WHEN
    actual_result = translate_sql_script(ir, context_factory)

    # THEN
    assert expected_result == actual_result
