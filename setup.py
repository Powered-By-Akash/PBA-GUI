from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8") if (this_directory / "README.md").exists() else ""

setup(
    name="pba-gui",
    version="2025.1.0",
    description="Python Tkinter GUI Framework & Visual Component Library for PBA Desktop Applications & Engineering Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Akash Tanna",
    author_email="Poweredbyakash@gmail.com",
    url="https://github.com/Powered-By-Akash/PBA-GUI",
    project_urls={
        "Organization": "https://github.com/Powered-By-Akash",
        "Website": "https://www.poweredbyakash.in/",
        "Source": "https://github.com/Powered-By-Akash/PBA-GUI",
        "Tracker": "https://github.com/Powered-By-Akash/PBA-GUI/issues",
    },
    py_modules=["pba_gui", "PBA_GEN2025"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Desktop Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="tkinter gui desktop pba-gui visual-components python-ui engineering-ui pba",
    install_requires=[],
)
