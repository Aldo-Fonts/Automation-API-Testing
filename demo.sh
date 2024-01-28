#!/bin/bash

export PYTHONPATH="$PWD:$PYTHONPATH"

behave tests/features/demo.feature
