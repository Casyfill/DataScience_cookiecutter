.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements:
	conda env export > environment.yml

## Set up python interpreter environment
environment:
	conda create -f environment.yml
	@echo ">>> New conda env created. Activate with:\nsource activate $(PROJECT_NAME)"

environment:
	conda env create environment.yml

## Delete all compiled Python files
clean:
	find . -name "*.pyc" -exec rm {} \;

## Test
test:
	python -m nose;

## Test with timer
timetest:
	python -m nose --with-timer --timer-top-n 10
