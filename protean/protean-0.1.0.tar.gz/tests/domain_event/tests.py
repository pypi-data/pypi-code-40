# Protean
import pytest

from mock import patch
from protean.core.domain_event import BaseDomainEvent
from protean.impl.broker.memory_broker import MemoryBroker
from protean.utils import fully_qualified_name

# Local/Relative Imports
from .elements import Person, PersonAdded


class TestDomainEventInitialization:
    def test_that_base_domain_event_class_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            BaseDomainEvent()

    def test_that_domain_event_can_be_instantiated(self):
        service = PersonAdded()
        assert service is not None


class TestDomainEventRegistration:
    def test_that_domain_event_can_be_registered_with_domain(self, test_domain):
        test_domain.register(PersonAdded)

        assert fully_qualified_name(PersonAdded) in test_domain.domain_events

    def test_that_domain_event_can_be_registered_via_annotations(self, test_domain):
        @test_domain.domain_event
        class AnnotatedDomainEvent:
            def special_method(self):
                pass

        assert fully_qualified_name(AnnotatedDomainEvent) in test_domain.domain_events


class TestDomainEventTriggering:
    @patch.object(MemoryBroker, 'send_message')
    def test_that_domain_event_is_raised_in_aggregate_command_method(self, mock):
        newcomer = Person.add_newcomer({'first_name': 'John', 'last_name': 'Doe', 'age': 21})
        mock.assert_called_once_with(PersonAdded(person=newcomer))
