# Sales Churn Prediction

This project predicts customer churn for a sales-based business using machine learning. It includes data preprocessing, model training, and a Streamlit-based dashboard for visualization and prediction.

## Features

- **Data Preprocessing**: Handles missing values, encodes categorical variables, and scales numerical features.
- **Model Training**: Uses a Random Forest Classifier to predict churn.
- **Dashboard**: Interactive Streamlit app for churn prediction and feature comparison.

## Project Structure

```
Sales_Churn_Prediction/
├── app.py                     # Streamlit app for visualization and prediction
├── churn_model.pkl            # Trained machine learning model
├── generate_sales_churn_data.py # Script to generate synthetic data
├── notebook.ipynb             # Jupyter notebook for data exploration and model training
├── sales_churn_data.csv       # Dataset used for training and testing
├── train_churn_model.py       # Script to train the churn prediction model
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Sales_Churn_Prediction.git
   cd Sales_Churn_Prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install additional libraries if needed:
   ```bash
   pip install imblearn
   ```

## Usage

### Run the Streamlit App

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

### Train the Model

1. Run the training script:
   ```bash
   python train_churn_model.py
   ```

2. The trained model will be saved as `churn_model.pkl`.

### Explore the Data

1. Open the Jupyter notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.