import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptomailer",
    version="0.0.1",
    author="Aditya Rajneesh Singh",
    author_email="adityarsingh17@gmail.com",
    description="A package to send and receive encrypted mails via Gmail.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdityaSingh17/CryptoMailer",
    packages=["cryptomailer"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
