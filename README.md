# Introvert vs Extrovert Classifier (Streamlit)

A simple Streamlit web app that predicts whether a person is likely an Introvert or Extrovert based on a few behavioral inputs. The prediction is produced by a scikit-learn model loaded from serialized artifacts.

## What’s in this repo

- `app.py`: Streamlit application UI and inference logic
- `requirements.txt`: Minimal Python dependencies
- `introvert_extrovert_classifier.pkl`: Trained scikit-learn model
- `scaler.pkl`: Feature scaler used during training
- `label_encorder.pkl`: Label encoder used to map model outputs back to class names (note the filename spelling)

## Prerequisites

- Python 3.9–3.11 recommended
- pip (comes with most Python installs)
- Git (optional, for cloning)

If you do not have Python, install it from the official website:
- Windows/macOS/Linux: `https://www.python.org/downloads/`

Verify your versions:

```bash
python --version
pip --version
```

On some systems you may need to use `python3` and `pip3` instead of `python` and `pip`.

## Quick start

These steps work on Windows, macOS, and Linux. Replace the first command with your preferred way of getting the code (clone or download as ZIP).

```bash
# 1) Get the code
git clone https://github.com/your-org-or-user/introvert_extrovert_classifier.git
cd introvert_extrovert_classifier

# 2) Create a virtual environment (recommended)
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate

# macOS / Linux
# python3 -m venv .venv
# source .venv/bin/activate

# 3) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4) Run the app
streamlit run app.py
```

When the app starts, your browser will open to `http://localhost:8501`. If it doesn’t open automatically, copy the URL Streamlit prints in the terminal and paste it into your browser.

## How to use the app

- Answer each question in the UI:
  - Time spent alone (slider 0–10)
  - Stage fear (yes/no)
  - Social event attendance (slider 0–10)
  - How often you go outside (radio selection)
  - Friends circle size (radio selection)
  - Posting frequency on social media (radio selection)
  - Feeling drained after socializing (yes/no)
- Click “Predict” to see the model’s classification.

Behind the scenes:
- Inputs are assembled into a 7-feature vector in `app.py`
- Features are transformed by `scaler.pkl`
- The trained model in `introvert_extrovert_classifier.pkl` predicts a class label
- The predicted label is mapped to a human-readable class via `label_encorder.pkl`

## Configuration tips

- Change the port (e.g., if 8501 is in use):

```bash
streamlit run app.py --server.port 8502
```

- Stop the app: press `Ctrl+C` in the terminal where Streamlit is running.

## Troubleshooting

- Missing packages / import errors:
  - Ensure the virtual environment is activated and run: `pip install -r requirements.txt`

- Model or pickle loading errors (e.g., ValueError, mismatch):
  - Make sure `introvert_extrovert_classifier.pkl`, `scaler.pkl`, and `label_encorder.pkl` are present in the project root (same folder as `app.py`).
  - Use a clean virtual environment with the pinned package versions in `requirements.txt`.

- Streamlit not found:
  - Run: `pip install streamlit`
  - Or reinstall from `requirements.txt`.

- Port already in use:
  - Start Streamlit on a different port: `streamlit run app.py --server.port 8502`

- Clear Streamlit’s cache (rarely needed):
  - `streamlit cache clear`

## Development notes

- The UI and feature engineering live in `app.py`. To change questions/options or feature mapping, edit the related Streamlit widgets and the `features` array construction.
- Dependency updates:
  - Update `requirements.txt` and reinstall: `pip install -r requirements.txt`
- Linting/formatting:
  - Not enforced in this repo. Feel free to adopt tools like `ruff`, `black`, or `flake8`.

## Security & trust of model files

Pickle files (`.pkl`) can execute arbitrary code when loaded. Only use model artifacts you trust. The files included here are for demonstration and should not be used in sensitive environments without review.

## License

Add a license if you plan to distribute. For example, create a `LICENSE` file with MIT if appropriate.

## Acknowledgements

- Built with `streamlit`, `numpy`, and `scikit-learn` (see `requirements.txt`).
