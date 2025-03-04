#   Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup for pip package."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import platform
import subprocess

from setuptools import find_packages
from setuptools import setup

if 'develop' in subprocess.getoutput('git branch'):
    slim_version = '0.0.0_dev'
else:
    tag_list = subprocess.getoutput('git tag').split('\n')
    if 'rc' in tag_list[-1]:
        if tag_list[-1].split('rc')[0] in tag_list[-2]:
            slim_version = tag_list[-2]
        else:
            slim_version = tag_list[-1]
    else:
        slim_version = tag_list[-1]

with open("./requirements.txt") as f:
    setup_requires = f.read().splitlines()

if platform.sys.platform == "win32":
    try:
        setup_requires.remove("paddleslim-opt-tools")
    except:
        pass

setup(
    name="paddleslim",
    version=slim_version,
    description=('A toolkit for generating small model.'),
    long_description='Tools for model compression',
    url='http://gitlab.baidu.com/PaddlePaddle/PaddleSlim',
    author='PaddlePaddle Author',
    author_email='dltp-all@baidu.com',
    install_requires=setup_requires,
    packages=find_packages(),
    # PyPI package information.
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="Apache 2.0",
    keywords=("PaddleSlim paddlepaddle model-optimize compression"),
)
