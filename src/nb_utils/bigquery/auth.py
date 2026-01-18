import subprocess
from google.auth.exceptions import RefreshError
import google.auth
from google.auth.transport.requests import Request

def relogin_adc():
    print("🔐 Требуется повторная авторизация Google Cloud...")
    subprocess.run(
        ["gcloud", "auth", "application-default", "login"],
        shell=True,
        check=True
    )
    print("✅ Авторизация завершена")

def ensure_auth():
    try:
        creds, project = google.auth.default()
        if not creds.valid:
            creds.refresh(Request())
        return creds, project

    except RefreshError:
        relogin_adc()
        creds, project = google.auth.default()
        return creds, project
