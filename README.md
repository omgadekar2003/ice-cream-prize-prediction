### **`README.md`**
```markdown
# Ice Cream Price Prediction App

This is a web application built using **Streamlit** that integrates a trained **Linear Regression** model. The app predicts the price of ice cream based on the temperature.

## Features
- **Input Temperature**: Enter a temperature value in °C (positive or negative).
- **Real-Time Prediction**: Displays the predicted price of ice cream in dollars.
- User-friendly interface hosted on Streamlit Cloud.

## Hosted Application
Access the app live at: [icecreamprice.streamlit.app](https://icecreamprice.streamlit.app)

## Technologies Used
- **Python**
- **Streamlit** for the front-end interface.
- **Joblib** for loading the trained model.
- **NumPy** for numerical operations.

## How to Run Locally

### Prerequisites
- Python 3.8 or higher installed on your system.

### Steps
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your trained model file (`ice_cream_price_model.pkl`) in the same directory.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to:
   ```
   http://localhost:8501
   ```

### Deployment on Streamlit Cloud
1. Push your files (`app.py`, `ice_cream_price_model.pkl`, `requirements.txt`, and `README.md`) to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and link your repository.
3. Deploy the app directly from Streamlit Cloud.

## Folder Structure
```
.
├── app.py                        # Streamlit application file
├── ice_cream_price_model.pkl     # Trained model
├── requirements.txt              # Required Python libraries
└── README.md                     # Project documentation
```

## Example
- Enter Temperature: `30.0`
- Predicted Price: `$3.50` (example)

## Requirements
The following libraries are required to run this project:
- Streamlit
- Scikit-learn
- Joblib
- NumPy

For detailed library versions, see `requirements.txt`.

## Author
Created by **Om Gadekar**. Feel free to connect with me for any questions or collaboration opportunities!
```

---

### **`requirements.txt`**
```
streamlit==1.25.0
scikit-learn==1.3.1
joblib==1.3.2
numpy==1.24.3
```

---

Let me know if you need anything else! 😊
