import pytest


class TestBuilder(object):
    @pytest.fixture()
    def mock_task_translator_factory(self, mocker):
        task_translator_factory = mocker.patch(
            "aws.datapipeline.task_translator_factory.TaskTranslatorFactory",
            auto_spec=True)
        yield task_translator_factory.return_value

    @pytest.fixture()
    def mock_translator(self, mocker):
        def translator_spec(ir):
            pass

        translator = mocker.Mock(spec=translator_spec)
        yield translator

    @pytest.fixture()
    def builder(self, mock_task_translator_factory):
        """

        :param mock_task_translator_factory: Required because
                                             aws.datapipeline.definition_builder.DefinitionBuilder()
                                             depends on it.
        :return:
        """
        import aws.datapipeline.definition_builder
        instance = aws.datapipeline.definition_builder.DefinitionBuilder()
        yield instance

    def test_add_and_build(self,
                           builder,
                           mock_task_translator_factory,
                           mock_translator,
                           mocker):
        # GIVEN
        # builder (instance of Builder)
        task_type = "task"
        task_ir = {
            "type": task_type
        }
        translated_task = mocker.sentinel.translated_task
        mock_task_translator_factory.create.return_value = mock_translator
        mock_translator.return_value = translated_task
        definition = {
            "objects": [
                translated_task
            ]
        }
        expected_result = definition

        # WHEN
        actual_result = builder.add(task_ir).build()

        # THEN
        mock_task_translator_factory.create.assert_called_with(task_ir)
        assert mock_translator.called
        assert expected_result == actual_result
