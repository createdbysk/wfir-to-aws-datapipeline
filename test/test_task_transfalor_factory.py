import pytest


class TestAwsDatapipelineTaskTranslatorFactory(object):
    @pytest.fixture()
    def mock_pkg_resources_iter_entry_points(self, mocker):
        iter_entry_points = mocker.patch("pkg_resources.iter_entry_points", auto_spec=True)
        yield iter_entry_points

    # noinspection PyUnusedLocal
    @pytest.fixture()
    def aws_datapipeline_task_translator_factory(self,
                                                 mock_pkg_resources_iter_entry_points):
        """

        :param mock_pkg_resources_iter_entry_points: aws_datapipeline_task_translator_factory.AwsDatapipelineTaskTranslatorFactory()
                                                     depends on this.

        :return:
        """
        import aws_datapipeline_task_translator_factory
        instance = aws_datapipeline_task_translator_factory.AwsDatapipelineTaskTranslatorFactory()
        yield instance

    # noinspection PyUnusedLocal
    def test_aws_datapipeline_task_translator_factory(self,
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
        entry_points = {
            "name": mocker.sentinel.entry_point
        }
        mock_pkg_resources_iter_entry_points.iter_entry_points.return_value = entry_points

        # WHEN
        # aws_datapipeline_task_translator_factory.AwsDatapipelineTaskTranslatorFactory.__init__ called

        # THEN
        mock_pkg_resources_iter_entry_points.assert_called_with("wfir.task_translators")
