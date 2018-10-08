import pytest
import wfir


class TestAwsDatapipelineTaskTranslatorFactory(object):
    @pytest.fixture()
    def mock_pkg_resources_iter_entry_points(self, mocker):
        iter_entry_points = mocker.patch("pkg_resources.iter_entry_points", auto_spec=True)
        yield iter_entry_points

    @pytest.fixture()
    def mock_task_translator_module(self, mocker):
        class TaskTranslatorModuleSpec(object):
            def translate(self, task_ir):
                pass

        task_translator_module = mocker.Mock(spec=TaskTranslatorModuleSpec)
        yield task_translator_module

    @pytest.fixture()
    def entry_points(self, mock_task_translator_module):
        return {
            "aws.datapipeline.task": mock_task_translator_module
        }

    # noinspection PyUnusedLocal
    @pytest.fixture()
    def aws_datapipeline_task_translator_factory(self,
                                                 entry_points,
                                                 mock_pkg_resources_iter_entry_points):
        """

        :param entry_points:
        :param mock_pkg_resources_iter_entry_points: aws_datapipeline_task_translator_factory.AwsDatapipelineTaskTranslatorFactory()
                                                     depends on this.

        :return:
        """
        import aws_datapipeline_task_translator_factory
        mock_pkg_resources_iter_entry_points.return_value = entry_points
        instance = aws_datapipeline_task_translator_factory.AwsDatapipelineTaskTranslatorFactory()
        yield instance

    # noinspection PyUnusedLocal
    def test_aws_datapipeline_task_translator_factory(self,
                                                      entry_points,
                                                      aws_datapipeline_task_translator_factory,
                                                      mock_pkg_resources_iter_entry_points,
                                                      mocker):
        """

        :param aws_datapipeline_task_translator_factory: To invoke aws_datapipeline_task_translator_factory.AwsDatapipelineTaskTranslatorFactory.__init__
        :param mock_pkg_resources_iter_entry_points:
        :param mocker:
        :return:
        """
        # GIVEN
        # mock_pkg_resources_iter_entry_points
        # aws_datapipeline_task_translator_factory
        # entry_points

        # WHEN
        # aws_datapipeline_task_translator_factory.AwsDatapipelineTaskTranslatorFactory.__init__ called

        # THEN
        mock_pkg_resources_iter_entry_points.assert_called_with("wfir.task_translators")

    def test_create(self,
                    mock_task_translator_module,
                    aws_datapipeline_task_translator_factory):
        # GIVEN
        # aws_datapipeline_task_translator_factory
        task_ir = {
            wfir.fields.TYPE_KEY: "task"
        }

        # WHEN
        result = aws_datapipeline_task_translator_factory.create(task_ir)

        # THEN
        # aws_datapipeline_task_translator_factory.create(task_ir) is expected to return a function,
        # which when invoked, calls invokes the translator with the task_ir as a parameter.
        result()
        mock_task_translator_module.translate.assert_called_with(task_ir)
