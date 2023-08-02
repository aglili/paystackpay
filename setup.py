from setuptools import setup,find_packages


install_requires = [
        "certifi",
        "charset-normalizer",
        "colorama",
        "idna",
        "iniconfig",
        "packaging",
        "pluggy",
        "pydantic",
        "requests",
        "typing_extensions",
        "urllib3",
    ]


setup(
    name="paystackpay",
    version="0.1.0",
    description="A Python API wrapper for the Paystack API",
    long_description="""PayStackPay is a comprehensive and easy-to-use Python library designed to simplify interactions with the Paystack API, \nempowering developers to seamlessly integrate Paystack's payment processing capabilities into their Python applications.""",
    author="Aglili Selorm Cecil",
    author_email="cecilselorm34@gmail.com",
    url="https://github.com/aglili/paystackpay",
    packages=find_packages(),
    install_requires = install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]


)