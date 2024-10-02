import setuptools
from setuptools import setup, find_packages
from src.surferr.__init__ import __version__

VERSION = __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="surferr",
    version=VERSION,
    author="Gautam Gambhir",
    author_email="ggambhir1919@gmail.com",
    description="AI-Powered Website & Webpage Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gautamxgambhir/Surferr",
    install_requires=['beautifulsoup4','Flask','Flask-Cors','Requests','setuptools','together','transformers'],
    project_urls={
        "Bug Tracker": "https://github.com/gautamxgambhir/Surferr/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    package_dir={'':"src"}, 
    packages=find_packages('src'),
    python_requires=">=3.12",
    keywords=['webpage_summarizer', 'summarizer', 'summarization', 'ai', 'together','bart'],
    include_package_data=True
)