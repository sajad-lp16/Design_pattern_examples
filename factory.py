class A:
    def __init__(self, name, format):
        self.name = name
        self.format = format


class B:
    def edit(self, obj):
        method = self._handler(obj)
        method(obj)

    def _handler(self, obj):
        if obj.format == 'json':
            return self.edit_json

        elif obj.format == 'xml':
            return self.edit_xml

        else:
            raise ValueError('Sorry...')

    def edit_json(self, obj):
        print('Editing json file ...')

    def edit_xml(self, obj):
        print('Editing xml file ...')


file = A('doc', 'json')
b = B()
b.edit(file)
