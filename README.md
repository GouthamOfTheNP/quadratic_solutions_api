# Quadratic Solver Web App

A simple Flask web application that allows users to calculate the solutions of a quadratic equation of the form **ax² + bx + c = 0**. The app also provides a home page and a changelog page for version tracking.

---

## Features

- **Home Page** (`/`): Displays the main landing page of the application.
- **Changelog Page** (`/v1.2`): Shows updates and changes for version 1.2.
- **Quadratic Solver** (`/v1.2/<a>_<b>_<c>`): Calculates the roots of a quadratic equation given coefficients `a`, `b`, and `c`.
  - Returns **real solutions** if they exist.
  - Handles non-numeric input gracefully.
  - Displays an error message if solutions are not real.
- **404 Page**: Custom error page for undefined routes.

---

## Requirements

- Python 3.7+
- Flask

---

## Installation

1. Clone the repository:  
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Install dependencies:  
    ```bash
    pip install flask
    ```

3. Run the application:  
    ```bash
    python app.py
    ```

4. Open your browser and go to:  
    ```
    http://127.0.0.1:5000/
    ```

---

## Usage

1. **Home Page:** Visit `/` to access the landing page.  
2. **Changelog:** Visit `/v1.2` to see version updates.  
3. **Quadratic Solver:** Enter your coefficients in the URL in the format:  
    ```
    /v1.2/<a>_<b>_<c>
    ```
    Example: `/v1.2/1_-3_2` → calculates the roots of x² - 3x + 2 = 0.  

The results page will display the entered coefficients and the calculated roots (positive and negative solutions).

---
