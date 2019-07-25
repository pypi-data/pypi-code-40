
class ControllerInterface:
    def add_profile(self, profile):
        """Tell the controller about a service profile it needs to manage."""
        raise NotImplementedError()

    def free_cpu(self):
        """Number of cores available for reservation."""
        raise NotImplementedError()

    def free_memory(self):
        """Megabytes of RAM that has not been reserved."""
        raise NotImplementedError()

    def get_target(self, service_name):
        """Get the target for running instances of a service."""
        raise NotImplementedError()

    def set_target(self, service_name, target):
        """Set the target for running instances of a service."""
        raise NotImplementedError()

