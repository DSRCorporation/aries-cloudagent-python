from unittest import TestCase

from ..please_ack_decorator import PleaseAckDecorator

ON = ("RECEIPT", "OUTCOME")


class TestPleaseAckDecorator(TestCase):
    def test_init_serde(self):
        decorator = PleaseAckDecorator()
        assert type(decorator) == PleaseAckDecorator
        assert decorator.on is None
        dumped = decorator.serialize()
        assert dumped == {}
        loaded = PleaseAckDecorator.deserialize(dumped)
        assert type(loaded) == PleaseAckDecorator
        assert loaded.on is None

        decorator = PleaseAckDecorator(on=ON)
        assert type(decorator) == PleaseAckDecorator
        assert decorator.on == list(ON)
        dumped = decorator.serialize()
        assert dumped == {
            "on": list(ON),
        }
        loaded = PleaseAckDecorator.deserialize(dumped)
        assert type(loaded) == PleaseAckDecorator
        assert loaded.on == list(ON)
