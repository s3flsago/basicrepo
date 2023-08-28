from setuptools import setup, find_packages



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.readlines()


setup(
    name="basic_repo",
    version="0.1.0",
    author="Florian Sagolla",
    description="Basic repository for starting a python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/s3flsago/basicrepo",
    packages=find_packages(where="src"),  
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=requirements,
)

