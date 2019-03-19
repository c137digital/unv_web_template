from setuptools import setup, find_packages


setup(
    name='app',
    version='0.1',
    description="""Provide description""",
    url='http://github.com/',
    author='',
    author_email='',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=[
        'unv.app==0.2.3',
        'unv.web==0.1.9',
        'unv.deploy==0.1.10',

        'watchgod'
    ],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'server = app.bin.server:run',
            'shell = app.bin.shell:run'
        ]
    },
)
