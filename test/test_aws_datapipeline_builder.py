import pytest


class TestBuilder(object):
    @pytest.fixture()
    def mock_task_translator_factory(self, mocker):
        task_translator_factory = mocker.patch("task_translator_factory.TaskTranslatorFactory", auto_spec=True)
        yield task_translator_factory

    @pytest.fixture()
    def builder(self, mock_task_translator_factory):
        import builder
        instance = builder.Builder(mock_task_translator_factory)
        yield instance

    def test_add_and_build(self, builder, mock_task_translator_factory, mocker):
        # GIVEN
        # builder (instance of Builder)
        task_type = "task"
        task_ir = {
            "type": task_type
        }
        translated_task = mocker.sentinel.translated_task
        mock_task_translator_factory.create.return_value = translated_task

        # WHEN
        builder.add(task_ir)

        # THEN
        mock_task_translator_factory.create.assert_called_with(task_ir)
