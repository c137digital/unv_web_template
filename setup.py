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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'unv.app==0.1.2',
        'unv.deploy==0.1'
    ],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'unv_web_template_server = app.bin.server:run',
        ]
    },
)
