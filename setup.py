import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

INSTALL_REQUIRES = [
    'kafka-python'
]

setup(name='python-logging-kafka',
      version='1.0.2',
      url='https://github.com/addu390/python-logging-kafka',
      description='Kafka log producer from Python/Django',
      long_description=README,
      long_description_content_type="text/markdown",
      keywords='logging kafka logs',
      license='MIT',
      author='Adesh Nalpet',
      author_email="390.adesh@gmail.com",
      classifiers=CLASSIFIERS,
      install_requires=INSTALL_REQUIRES,
      include_package_data=True,
      packages=['python_logging_kafka'],
      test_suite='tests',
      zip_safe=True)
