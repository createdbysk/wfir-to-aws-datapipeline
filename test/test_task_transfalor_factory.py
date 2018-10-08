import pytest
import wfir

class TestAwsDatapipelineTaskTranslatorFactory(object):
    @pytest.fixture()
    def mock_pkg_resources_iter_entry_points(self, mocker):
        iter_entry_points = mocker.patch("pkg_resources.iter_entry_points", auto_spec=True)
        yield iter_entry_points

    @pytest.fixture()
    def task_factory(self, mocker):
        yield mocker.sentinel.task_factory

    @pytest.fixture()
    def entry_points(self, task_factory):
        return {
            "aws.datapipeline.task": task_factory
        }


    # noinspection PyUnusedLocal
    @pytest.fixture()
    def aws_datapipeline_task_translator_factory(self,
                                                 entry_points,
                                                 mock_pkg_resources_iter_entry_points):
        """

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
                    task_factory,
                    aws_datapipeline_task_translator_factory):
        # GIVEN
        # aws_datapipeline_task_translator_factory
        task_ir = {
            wfir.fields.TYPE_KEY: "task"
        }

        expected_result = task_factory

        # WHEN
        actual_result = aws_datapipeline_task_translator_factory.create(task_ir)

        # THEN
        assert expected_result == actual_result
