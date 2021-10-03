"""A BillingProvider Service Provider."""
from masonite.providers import Provider
from masonite.utils.structures import load

from ..commands.InstallCommand import InstallCommand

from ..Billing import Billing
from ..drivers import StripeDriver, PaddleDriver


class BillingProvider(Provider):
    """Provides Services To The Service Container."""

    def __init__(self, app):
        self.application = app

    def register(self):
        """Register objects into the Service Container."""
        self.application.make("commands").add(InstallCommand())
        self.application.bind("config.billing", "masonite.billing.config.billing")
        billing = Billing(self.application).set_configuration(
            load(self.application.make("config.billing")).DRIVERS
        )
        billing.add_driver("stripe", StripeDriver(self.application))
        billing.add_driver("paddle", PaddleDriver(self.application))
        self.application.bind("billing", billing)

    def boot(self):
        """Boots services required by the container."""
        pass
