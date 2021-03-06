from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="bibcat_publisher",
    version="0.2.0",
    description="RDF Linked Data Publisher and Asset Repository",
    author="KnowledgeLinks",
    author_email="knowledgelinks.io@gmail.com",
    license="MIT",
    url="http://bibcat.org/publisher",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"],
    keywords=["rdf linked-data publisher bibframe digital repository"]
    install_requires=[
        "bibcat",
        "Flask-Webpack"
    ],
    include_package_data=True
)
