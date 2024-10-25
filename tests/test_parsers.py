from rest_framework_transforms.parsers import BaseVersioningParser


class TestParser(BaseVersioningParser):
    __test__ = False

    media_type = 'application/vnd.test.testtype+json'
    transform_base = 'tests.test_transforms.TestModelTransform'
