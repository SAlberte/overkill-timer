#!/bin/bash

set -ex

pip install -r deployment/requirements.txt
pre-commit install
