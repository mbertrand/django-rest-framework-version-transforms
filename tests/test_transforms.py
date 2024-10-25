from rest_framework_transforms.transforms import BaseTransform


class TestModelTransform0002(BaseTransform):

    __test__ = False

    def forwards(self, data, request):
        if data and 'test_field_one' in data:
            data['new_test_field'] = data.get('test_field_one')
            data.pop('test_field_one')
        return data

    def backwards(self, data, request, instance):
        if data:
            data['test_field_one'] = data.get('new_test_field')
            data.pop('new_test_field')
        return data


class TestModelTransform0003(BaseTransform):

    __test__ = False

    def forwards(self, data, request):
        if data:
            data['new_related_object_id_list'] = [1, 2, 3, 4, 5]
        return data

    def backwards(self, data, request, instance):
        if data:
            data.pop('new_related_object_id_list')
        return data
