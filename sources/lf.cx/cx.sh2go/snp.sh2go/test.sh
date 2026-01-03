#!/bin/bash

exec docker run --rm -i -v "${PWD}:${PWD}:ro" -w "${PWD}" koalaman/shellcheck:latest "$@"