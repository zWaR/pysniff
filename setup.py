from setuptools import setup, find_packages

setup(
    name = 'pysniff',
    version = '0.0.1',
    description = 'A simple netowrk sniffing application',
    author = 'zWaR',
    author_email = 'zwar@sharklasers.com',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    keywords = 'network sniffer monitoring proxy',
    packages = ['pysniff', 'pysniff/libs'],
    setup_requires = ['pytest-runner'],
    install_requires = [
        'appjar'
    ],
    url="https://github.com/zWaR/pysniff",
    project_urls={
        "Source Code": "https://github.com/zWaR/pysniff.git",
        "Bug Tracker": "https://github.com/zWaR/pysniff/issues",
        "Documentation": "https://github.com/zWaR/pysniff"
    },
    entry_points = {
        'console_scripts': [
            'pysniff=pysniff.main:main'
        ]
    }
)