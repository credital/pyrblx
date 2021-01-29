import setuptools

with open("README.md","r") as f:
	desc = f.read()
setuptools.setup(
name = "pyrblx",
packages = setuptools.find_packages(),
include_package_data=True,
version = "3.1",
license = "MIT",
description = "pyrblx Is A library Written In Python For Roblox",
long_description = desc,
long_description_content_type="text/markdown",
author = "KILR",
url = "https://github.com/KILR007/pyrblx",
keywords = ["roblox","roblox api","roblox wrapper","roblox api wrapper",'roblox.py','pyrblx'],
install_requires = ["requests"],
project_urls={
        "Discord": "https://discord.com/invite/vpEv3HJ",
        "Issue Tracker": "https://github.com/KILR007/pyrblx/issues",
        "GitHub": "https://github.com/KILR007/pyrblx",
},
classifiers = [
'Development Status :: 7 - Inactive',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python :: 3',
'Operating System :: OS Independent'
],
python_requires='>=3.7'
)
