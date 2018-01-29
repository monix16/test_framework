from setuptools import setup


def read_file(name):
    with open(name) as f:
        required = f.read().splitlines()
    return required

setup(name="pyapi",
      version="2.0.0",
      description="Python Framework used to test Plivo",
      zip_safe=False,
      keywords="plivo test api",
      url="https://bitbucket.org/plivo/pyapi",
      install_requires=read_file('requirements.txt'),
      packages=read_file('modules.txt'),
      scripts=['setup.cfg', 'README.md']
)