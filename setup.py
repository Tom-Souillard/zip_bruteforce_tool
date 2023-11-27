from setuptools import setup, find_packages

setup(
    name='zip_bruteforce_tool',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'generate_test_archives=zip_bruteforce_tool.scripts.generate_test_archives:create_zip_file',
            'run_fcrackzip=zip_bruteforce_tool.scripts.run_fcrackzip:run_fcrackzip',
            'extract_zip_hash=zip_bruteforce_tool.scripts.extract_zip_hash:extract_zip_hash',
            'run_john=zip_bruteforce_tool.scripts.run_john:run_john',
        ],
    },
    author='Tom Souillard',
    author_email='tom.souillard@gmail.com',
    description='A professional tool for performing brute force attacks on password-protected ZIP archives.',
    license='Apache License 2.0',
    keywords='zip bruteforce security pentest',
    url='https://github.com/Tom-Souillard/zip_bruteforce_tool',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Security',
    ],
)
