import os
from setuptools import setup



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()





## I don't know how to use this one but i gonna keep this at this moment...
setup(
    name="KJ_Finance",
    version="0.0.1",
    description="Yahoo API Wrapper",
    long_description=read("README.md"),
    author="Kevin Park, Jongyun Kim",
    author_email="hyunbin7303@gmail.com",
    keywords="JK wrapper api",
    license="MIT",
    packages=["pythark", "tests"],
    url="https://github.com/hyunbin7303/Python_Studygroup",
    install_requires=[
        # 'requests',
        # 'logzero',
        # 'retrying'
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3",
    zip_safe=False
)
