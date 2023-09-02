# Salary Prediction ML Project

## Overview

This project aims to predict salary based on various features using a Machine Learning model. It utilizes a Random Forest Regressor trained on a dataset containing over 10,000 data points. The `app.py` file serves as the main entry point for accessing the prediction model.

## Project Structure

The project structure is organized as follows:

```
- data/                # Folder containing the dataset
    - salary_dataset.csv   # Dataset used for training and testing
- models/              # Folder containing trained model(s)
    - random_forest_regressor.pkl # Pre-trained Random Forest Regressor model
- app.py                # Main application file for prediction
- requirements.txt      # List of project dependencies
- README.md             # Documentation (You are reading this!)
- EDA_SalaryModel.ipynb
- Salary_prediction.ipynb
```

## Getting Started

1. **Clone the Repository:**

    ```
    git clone https://github.com/chandankr014/Salary-Prediction.git
    ```

2. **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    To start the salary prediction application, use the following command:

    ```
    python app.py
    ```

4. **Access the Application:**

    Open a web browser and navigate to `http://localhost:5000` to access the salary prediction interface.

## Usage

1. **Input Data:**

    Provide the necessary input features such as years of experience, min salary, maximum salary, etc., in the provided input fields.

2. **Predict Salary:**

    Click the "Predict" button to generate a salary prediction based on the input data.

3. **View Result:**

    The predicted salary will be displayed on the screen.

## Model Retraining

If you wish to retrain the model with updated data, follow these steps:

1. Place the updated dataset in the `csv` files.

2. Modify the data loading and preprocessing steps in the `app.py` file to use the new dataset.

3. Retrain the model using the updated data.

4. Save the trained model as `random_forest_regressor.pkl` in the `models/` directory.

## Dependencies

- Python 3.x
- scikit-learn
- Flask (for the web application)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Chandan Kumar
- Contact: chandankr014@email.com

---
