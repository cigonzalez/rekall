from setuptools import setup

if __name__ == "__main__":
    setup(
        name='rekallpy',
        version_format='{tag}',
        description='Spatiotemporal query language',
        url='http://github.com/scanner-research/rekall',
        author='Dan Fu',
        author_email='danfu@stanford.edu',
        license='Apache 2.0',
        packages=['rekall'],
        install_requires=['python-constraint', 'tqdm', 'cloudpickle'],
        setup_requires=['setuptools-git-version', 'pytest-runner'],
        tests_require=['pytest'],
        zip_safe=False)
