import setuptools

setuptools.setup(
    author= 'Ipan (zelvdsk)',
    description= 'Automation For KuySocial',
    entry_points= {'console_scripts': ['KuySocial=source:Start']},
    install_requires= [
        'requests', 
        'bs4'
    ],
    long_description= open("README.md").read(),
    long_description_content_type= "text/markdown",
    url= "https://github.com/zelvdsk/KuySocial",
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords= ['Automation', 'soacial network'],
    name= 'KuySocial',
    packages=setuptools.find_packages(),
    version='1.0.1'
)
