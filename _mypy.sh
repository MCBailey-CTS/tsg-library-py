#!/bin/bash
mypy --strict --disallow-any-unimported --verbose .
# --warn-unused-configs
# --disallow-any-generics
# --disallow-subclassing-any
# --disallow-untyped-calls
# --disallow-untyped-defs
# --disallow-incomplete-defs
# --check-untyped-defs
# --disallow-untyped-decorators
# --warn-redundant-casts
# --warn-unused-ignores
# --warn-return-any
# --no-implicit-reexport
# --strict-equality 
# --strict-concatenate

# echo 'hello'
