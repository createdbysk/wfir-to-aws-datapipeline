import pytest
import os

@pytest.fixture()
def deployed_path():
    def impl(file_path):
        file_basename = os.path.basename(file_path)
        deployed_path = "s3://wfir-bucket/project-path/path/to/{filename}".format(filename=file_basename)
        return deployed_path

    yield impl


# noinspection PyShadowingNames
@pytest.fixture()
def context_factory(deployed_path):
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

        def task_index(self):
            return "001"

    def factory(renderer):
        return Context(renderer)

    yield factory


def test_sql_script(context_factory,
                    deployed_path):
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
        "database": {
            "ref": database
        },
        "workerGroup": "worker-group"
    }

    expected_result = sql_script_definition

    # WHEN
    actual_result = translate_sql_script(ir, context_factory)

    # THEN
    assert expected_result == actual_result

