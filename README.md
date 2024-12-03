# BG Remover

My own image background remover built with **Streamlit** and **Python**.

---

## Why?

I created this project because many websites charge money for background removal—something that can be achieved with a simple Python library called **`rembg`**, which includes prebuilt functions for this purpose. 

This tool is particularly useful for graphic designers and others who frequently need background removal for images without paying for expensive tools or services.

---

## Features

- **Upload Image**: Supports PNG, JPG, and JPEG formats.
- **Background Removal**: Automatically removes backgrounds with the help of the `rembg` library.
- **Download Option**: Allows users to download the image with the background removed directly from the app.

---

## How to Use

### 1. Prerequisites

Ensure you have the following installed on your system:

- Python (>=3.8 recommended)
- pip (Python package manager)

---

### 2. Installation

#### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/bg-remover.git
cd bg-remover
```

#### Step 2: Set up a virtual environment
Create a virtual environment to keep dependencies isolated:
```bash
python -m venv venv
```

Activate the virtual environment:
- On **Linux/MacOS**:
  ```bash
  source venv/bin/activate
  ```
- On **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

#### Step 3: Install the required libraries
Install all dependencies in the virtual environment:
```bash
pip install streamlit pillow rembg
```

---

### 3. Run the Application

Run the following command to start the app:
```bash
streamlit run app.py
```

Open your browser at the URL displayed in the terminal (typically `http://localhost:8501`).

---

### 4. Troubleshooting

If you encounter any issues, please try the following:

1. Ensure the virtual environment is activated:
   - **Linux/MacOS**: `source venv/bin/activate`
   - **Windows**: `.\venv\Scripts\activate`

2. Reinstall the required libraries:
   ```bash
   pip install --upgrade pip
   pip install streamlit pillow rembg
   ```

3. Debug errors by reviewing the terminal logs and resolving any dependency conflicts or use chatgpt to try to debug.