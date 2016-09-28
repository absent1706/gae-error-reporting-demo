# gae-error-reporting-demo
Write errors to custom log file: https://cloud.google.com/error-reporting/docs/setup/app-engine-flexible-environment

```
virtualenv env
env\Scripts\activate.bat
pip install -r requirements.txt
python main.py

gcloud app deploy --project=<PROJECT> --version v1
```
