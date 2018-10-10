def test_sql_query(mocker):
    # GIVEN
    file_path = "/path/to/sql_query.sql"
    compute = mocker.sentinel.compute
    database = mocker.sentinel.database
    ir = {
        "type": "sql_query",
        "file_path": file_path,
        "compute": compute,
        "database": database
    }