#!/bin/bash

mlflow run . -e train

mlflow run . -e predict -P filename=model.pkl
