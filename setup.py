import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

INSTALL_REQUIRES = [
    'kafka-python>=2.0.1'
]

TEST_REQUIRES = [
    "pytest>=4.3.0",
]

setup(name='python-logging-kafka',
      version='1.0.1',
      url='https://github.com/addu390/python-logging-kafka',
      description='Kafka log producer from Python/Django',
      long_description=README,
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
