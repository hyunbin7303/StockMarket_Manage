#setup.py: This file can also be used to define dependencies, 
#but it really shines for other work that needs to be done during installation. 
#You can read more about both setup.py and requirements.txt in our guide to Pipenv.

from pathlib import Path
import setuptools


print("setup checking,.")
project_dir = Path(__file__).parent

setuptools.setup(
    name="fact",
    version="1.0.0",
    description="Stockmarket Python",
    # Allow UTF-8 characters in README with encoding argument.
    long_description=project_dir.joinpath("README.rst").read_text(encoding="utf-8"),
    keywords=["python"],
    author="Kevin, Jongyoon",
    url="https://github.com/hyunbin7303/StockMarket_Manage",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},

    python_requires=">=3.6",

    # See https://stackoverflow.com/questions/7522250/
    include_package_data=True,
    package_data={"fact": ["py.typed"]},
    install_requires=project_dir.joinpath("requirements.txt").read_text().split("\n"),
    zip_safe=False,
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["fact=fact.cli:main"]},
)
