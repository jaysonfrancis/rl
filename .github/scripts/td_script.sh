#!/bin/bash

export TORCHRL_BUILD_VERSION=0.6.1

${CONDA_RUN} pip install git+https://github.com/pytorch/tensordict.git -U
