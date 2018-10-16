import pytest


@pytest.fixture()
def compute_repr():
    yield '"compute_key": "compute_value"'


@pytest.fixture()
def context(compute_repr):
    yield {
        "task_index": 1
    }


def test_sql_script(context):
    from aws.datapipeline.task_translators import translate_sql_script
    # GIVEN
    file_path = "/path/to/sql_script.sql"
    database = "database"
    compute = "compute"

    ir = {
        "type": "sql_script",
        "file_path": file_path,
        "database": database,
        "compute": compute
    }

    sql_script_definition = {
        "type": "SqlActivity",
        "id": "001_sql_script",
        "scriptUri": "s3://wfir-bucket/project-path/path/to/sql_script.sql",
        "database": {
            "ref": database
        },
        "workerGroup": "worker-group"
    }

    expected_result = sql_script_definition

    # WHEN
    actual_result = translate_sql_script(ir, context)

    # THEN
    assert expected_result == actual_result

