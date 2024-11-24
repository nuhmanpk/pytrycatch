import pathlib
from setuptools import setup, find_packages

file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

requirements = (file / "requirements.txt").read_text().splitlines()

setup(
    name="pytrycatch",
    version="0.0.1",
    description="Simplified exception handling for Python",
    author="Nuhman PK",
    author_email="nuhmanpk7@gmail.com",
    long_description = README,
    long_description_content_type = "text/markdown",
    url="https://github.com/nuhmanpk/pytrycatch",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires=">=3.9",
    project_urls={
        'Documentation': 'https://github.com/nuhmanpk/pytrycatch/blob/main/README.md',
        'Funding': 'https://github.com/sponsors/nuhmanpk',
        'Source': 'https://github.com/nuhmanpk/pytrycatch/',
        'Tracker': 'https://github.com/nuhmanpk/pytrycatch/issues',
    },
)