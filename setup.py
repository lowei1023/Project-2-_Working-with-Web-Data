from setuptools import setup, find_packages

setup(
    name='webdata',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author="Wei Lo",
    author_email="niccolowei@gmail.com",
    license='MIT',
    description="Scraping webpages, and working with third-party APIs."
)
