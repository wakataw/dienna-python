from setuptools import setup

setup(
    name='dienna',
    version='0.1a1',
    packages=['dienna'],
    url='https://github.com/wakataw/dienna-python',
    license='MIT',
    author='Agung Pratama',
    author_email='prrtmgng@gmail.com',
    description='Office Automation Python SDK',
    install_requires=[
        'requests',
        'BeautifulSoup4',
        'html5lib',
    ],
)
