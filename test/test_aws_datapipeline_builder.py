import pytest


class TestBuilder(object):
    @pytest.fixture()
    def mock_task_translator_factory_create(self, mocker):
        create_fn = mocker.patch("aws_datapipeline_task_translator_factory.create", auto_spec=True)
        yield create_fn

    @pytest.fixture()
    def builder(self):
        import aws_datapipeline_definition_builder
        instance = aws_datapipeline_definition_builder.AwsDatapipelineDefinitionBuilder()
        yield instance

    def test_add_and_build(self,
                           builder,
                           mock_task_translator_factory_create,
                           mocker):
        # GIVEN
        # builder (instance of Builder)
        task_type = "task"
        task_ir = {
            "type": task_type
        }
        translated_task = mocker.sentinel.translated_task
        mock_task_translator_factory_create.return_value = translated_task
        definition = {
            "objects": [
                translated_task
            ]
        }
        expected_result = definition

        # WHEN
        actual_result = builder.add(task_ir).build()

        # THEN
        mock_task_translator_factory_create.assert_called_with(task_ir)
        assert expected_result == actual_result
