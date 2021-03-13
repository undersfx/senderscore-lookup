import io
import os
from setuptools import setup, find_packages


def read(*names, **kwargs):
    """Read a file."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        if kwargs.get('type') == 'list':
            content = list(map(lambda s: s.strip(), open_file.readlines()))
        else:
            content = open_file.read().strip()
    return content


long_description = read('README.md')
requirements = read('requirements.in', type='list')

setup(
        name='senderscore',
        version='0.1.5',
        author='Thiago "Undersfx" Rodrigues',
        author_email='undersoft.corp@gmail.com',
        url='https://github.com/undersfx/senderscore-lookup',
        description='Senderscore command line lookup tool',
        long_description=long_description,
        long_description_content_type="text/markdown",
        license='MIT',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'senderscore = senderscore.senderscore:main'
            ]
        },
        classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords='sender score lookup cli undersfx',
        install_requires=requirements,
        zip_safe=False
)
