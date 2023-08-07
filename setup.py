from setuptools import setup, find_packages

setup(
    name='iris',  # Replace with your package's name
    version='0.1.0',  # Replace with your package's version
    author='xxxx',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A short description of the package',  # Replace with a short description of what your package does
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/raviraagav7/github-aws-cicd',  # Replace with the URL of your package's repository
    packages=find_packages(),  # Automatically find all packages and subpackages. Alternatively, specify the package names.
    install_requires=[  # Dependencies for your package. Example:
        'scikit-learn==1.3.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Chose either '3 - Alpha', '4 - Beta' or '5 - Production/Stable' as the current state of your package
        'Intended Audience :: Developers',  # Define the audience of your package. Should be one of 'Developers', 'Education', 'Science/Research', 'System Administrators', 'End Users/Desktop', 'Other Audience'
        'License :: OSI Approved :: MIT License',  # Choose the license of your package. Should be a license from the list of approved licenses by OSI: https://opensource.org/licenses/alphabetical
        'Programming Language :: Python :: 3.7',  # Specify the Python versions your package works on
        'Programming Language :: Python :: 3.8',
    ],
)