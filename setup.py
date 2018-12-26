from setuptools import setup


with open('README.md') as f:
    long_desc = f.read()

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name="rimp",
    version="0.0.0",
    description="A hacky project that lets you import repls from https://repl.it into your project",
    long_description=long_desc,
    author="Nathan Zilora",
    author_email="zwork101@gmail.com",
    requires=requires,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Archiving :: Packaging'
    ]
)
