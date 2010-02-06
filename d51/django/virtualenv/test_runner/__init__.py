import pkg_resources
pkg_resources.declare_namespace(__name__)

from d51.django.virtualenv.base import VirtualEnvironment

class VirtualEnvironmentTestRunner(VirtualEnvironment):
    def run_tests(self, my_settings, app_to_test):
        self.activate()
        if hasattr(self.caller, 'setUp'):
            self.caller.setUp()

        self.configure_settings(my_settings)
        self.call_command('test', app_to_test)

    def __call__(self, *args, **kwargs):
        self.run_tests(*args, **kwargs)

run_tests = VirtualEnvironmentTestRunner()

