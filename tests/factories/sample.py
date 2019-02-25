from factory import Factory, Sequence

from src.apps.samples.models import Sample


class SampleFactory(Factory):
    class Meta:
        model = Sample

    title = Sequence(lambda n: 'title #{}'.format(n))
    body = Sequence(lambda n: 'body #{}'.format(n))
