import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dev_swiper",
    version="0.0.4",
    author="Dipansh Khandelwal",
    author_email="dipanshkhandelwal@gmail.com",
    description="Stronger swiping game for devs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DipanshKhandelwal/dev-swiper",
    packages=setuptools.find_packages(),
    install_requires=['docopt'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
    entry_points={
        'console_scripts': [
            'swipe = dev_swiper.main:run',
        ],
    },
)
