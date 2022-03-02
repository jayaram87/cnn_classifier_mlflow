```bash
conda env1 export > conda.yaml
```

```bash
mlflow run . --no-conda
mlflow rub . -e get_data -P config=configs/config.yaml --no-conda
```