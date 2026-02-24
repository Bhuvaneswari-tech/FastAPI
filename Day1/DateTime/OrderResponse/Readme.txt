To create a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1
pip intall dotenv
pip list

uv is excellent for modern project setup.
uv venv
.\.venv\Scripts\Activate.ps1
uv add python-dotenv
uv pip list