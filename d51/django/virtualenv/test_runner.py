import os, sys

ERROR_MESSAGE = """
Error!  You haven't initialized your virtual environment first.

Please run the following to initialize the environment:

    virtualenv .
    pip install -E . -r ./requirements.txt
""".lstrip()

DATABASE_ENGINE = 'sqlite3'

class VirtualEnvTestRunner(object):
    def __init__(self,
                 caller=sys.modules['__main__'],
                 database_engine=DATABASE_ENGINE,
                 error_message=ERROR_MESSAGE):
        self.caller = caller
        self.database_engine = database_engine
        self.error_message = error_message

    @property
    def activation_file(self):
        caller_path = os.path.dirname(os.path.realpath(self.caller.__file__))
        return os.path.join(caller_path, 'bin', 'activate_this.py')

    def activate(self):
        if not os.path.exists(self.activation_file):
            print self.error_message
            sys.exit(1)

        execfile(self.activation_file, dict(__file__=self.activation_file))

    def configure_settings(self, customizations):
        # Django expects a `DATABASE_ENGINE` value, even thought it ignores it
        # during tests.
        if "DATABASE_ENGINE" not in customizations:
            customizations["DATABASE_ENGINE"] = self.database_engine

        settings = self.settings
        settings.configure(**customizations)
        
    @property
    def settings(self):
        from django.conf import settings
        return settings

    @property
    def call_command(self):
        from django.core.management import call_command
        return call_command

    def run_tests(self, my_settings, app_to_test):
        self.activate()
        self.configure_settings(my_settings)
        self.call_command('test', app_to_test)

    def __call__(self, *args, **kwargs):
        self.run_tests(*args, **kwargs)

run_tests = VirtualEnvTestRunner()

