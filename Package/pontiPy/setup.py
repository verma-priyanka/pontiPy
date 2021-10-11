from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()
    
setup_args = dict(
    name='pontiPy',
    version='3.0',
    description="Automation of Pontius Matrix",
    license='MIT',
    packages=find_packages(),
    long_description_content_type="text/markdown",
    long_description=README,
    py_modules=['pontiPy'],
    author='Priyanka Verma',
    author_email='prverma@clarku.edu',
    url='https://github.com/verma-priyanka',
    include_package_data=True

)
install_requires = ['pandas']


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
