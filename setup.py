from setuptools import setup, find_packages

setup(
    name = "django-websocket",
    version = "1.0",
    url = 'http://github.com/FMRb/django-websocket',
    license = 'BSD',
    description = "Example of websocket using the library gevent-socket.",
    author = 'Felix Rubio',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)