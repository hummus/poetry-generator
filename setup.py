import os
from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
reqs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements.txt')
install_reqs = parse_requirements(reqs_path, session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='poetry-generator',
    version='1.0',
    packages=['poem'],
    install_requires=reqs,
    package_data={"poem":["*.yaml"]},
    zip_safe=False,
)
