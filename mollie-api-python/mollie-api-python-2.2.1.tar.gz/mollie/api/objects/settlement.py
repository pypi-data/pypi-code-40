from .base import Base


class Settlement(Base):
    STATUS_OPEN = 'open'
    STATUS_PENDING = 'pending'
    STATUS_PAIDOUT = 'paidout'
    STATUS_FAILED = 'failed'

    @classmethod
    def get_resource_class(cls, client):
        from ..resources.settlements import Settlements
        return Settlements(client)

    @property
    def id(self):
        return self._get_property('id')

    @property
    def reference(self):
        return self._get_property('reference')

    @property
    def created_at(self):
        return self._get_property('createdAt')

    @property
    def settled_at(self):
        return self._get_property('settledAt')

    @property
    def status(self):
        return self._get_property('status')

    @property
    def amount(self):
        return self._get_property('amount')

    @property
    def periods(self):
        return self._get_property('periods')

    @property
    def invoice_id(self):
        return self._get_property('invoiceId')

    # Additional methods

    def is_open(self):
        return self._get_property('status') == self.STATUS_OPEN

    def is_pending(self):
        return self._get_property('status') == self.STATUS_PENDING

    def is_canceled(self):
        return self._get_property('status') == self.STATUS_PAIDOUT

    def is_failed(self):
        return self._get_property('status') == self.STATUS_FAILED

    @property
    def payments(self):
        """Return the payments related to this settlement."""
        return self.client.settlement_payments.on(self).list()

    @property
    def refunds(self):
        """Return the refunds related to this settlement."""
        return self.client.settlement_refunds.on(self).list()

    @property
    def chargebacks(self):
        """Return the chargebacks related to this settlement."""
        return self.client.settlement_chargebacks.on(self).list()
