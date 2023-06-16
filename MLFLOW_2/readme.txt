mlflow run . -e train  --env-manager local

mlflow run . -e predict  --env-manager local -P filename=model.pkl