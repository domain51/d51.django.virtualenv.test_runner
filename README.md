d51.django.virtualenv.test\_runner
==================================
Simple package for running isolated Django tests from within [virtualenv][]


Usage
-----
For those of you who are pressed for time.  Create a `.py` file named anything
you like--we'll call it `run_tests.py`--at the top level of your virtualenv
environment (i.e., the parent of `bin/`), and add the following:

    from d51.django.virtualenv.test_runner import run_tests

    def main():
        settings = {
            'INSTALLED_APPS': (
                ... your app(s) here ...
            ),
        }
        run_tests(settings, 'tagging')

    if __name__ == '__main__':
        main()

Now all you need to do is create your virtual environment (don't worry, this
gets mad at you if you didn't), install any dependencies you have for your
package, then run this file.

There's no need to activate virtualenv as you would normally,
`d51.django.virtualenv.test_runner` takes care of that for you.


Advanced Usage
--------------
There's more to this than that, but that's all you need to get started.  The
`VirtualEnvironmentTestRunner` class is the work-horse here.  The `run_tests`
that you imported above is an instance of that class.

### Changing where `run_tests.py` is located
You need to directly instantiate `VirtualEnvironmentTestRunner` and provide it
with a new `caller` parameter.  `caller` is a module which, by default, is
equal to the `__main__` module.  You can provide your own module, if you like.

It assumes you have a standard virtualenv layout with that module existing in
parent of virtualenv's `bin/` directory.  Namely, it needs:

    ... your run_tests.py file ...
    bin/
        activate_this.py

If that is not your structure, you need to sub-class
`VirtualEnvironmentTestRunner` and provide your own `activation_file`
method/property.

### Changing the error message
The default error message is along the lines of:

    Error!  You haven't initialized your virtual environment first.

    Please run the following to initialize the environment:

        virtualenv .
        pip install -E . -r ./requirements.txt

To provide a different message, instantiate `VirtualEnvTestRunner` directly and
provide a new `error_message` keyword argument.


Testing
-------
I know, I know.  There is none yet, but the fun thing is that since this
runs tests, you know it works if your tests actually run.  :-)


[virtualenv]: http://virtualenv.openplans.org/

