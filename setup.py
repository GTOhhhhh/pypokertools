from setuptools import setup, find_packages

setup(
    name = 'pypokertools',
    version = '1.0.1',
    author = 'mjwestcott, Karl Spiegel',
    author_email = 'spiegel.karl@gmail.com',
    description = 'tools for hand evaluation ',
    license = 'MIT',
    keywords = 'python poker',
    url = 'https://github.com/GTOhhhhh/pypokertoolse',
    packages = [pkg for pkg in find_packages() if pkg != "tests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
    )

