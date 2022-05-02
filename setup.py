import setuptools

dependencies = ["discord.py", "aiohttp"]

with open("README.md", "r", encoding="utf-8", errors="ignore") as f:
    long_description = f.read()

version = '' 
with with open('./disutils/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


setuptools.setup(
    name="disutils",
    version=version,
    author="pintermor9",
    description="disutils is a very useful library made to be used with discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pintermor9/disutils/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.6",
    include_package_data=True,
    install_requires=dependencies,
    extras_require={"voice": dependencies + ["youtube-dl"]},
)
