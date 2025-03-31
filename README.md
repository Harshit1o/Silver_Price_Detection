# Silver Price Predictor

A Django web application that predicts silver prices using machine learning. The application features a beautiful dark-themed interface and provides real-time price predictions based on historical data.

## Features

- Real-time silver price predictions
- Beautiful dark-themed user interface
- Responsive design
- Easy-to-use input form
- Loading animations
- Error handling
- CSRF protection

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Harshit1o/Silver_Price_Detection.git
cd silver-prediction
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Place your trained model file (`silver_prices_model.pkl`) in the project root directory.

## Usage

1. Start the Django development server:
```bash
python manage.py runserver
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:8000/
```

3. Enter the required values:
   - Open Price
   - High Price
   - Low Price
   - Volume

4. Click "Predict Price" to get the prediction

## Project Structure

```
silver-prediction/
├── manage.py
├── requirements.txt
├── README.md
├── silver_prices_model.pkl
├── silver_prediction/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── predictor/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── predictor/
            └── home.html
```

## Model Information

The application uses a machine learning model trained on historical silver price data. The model expects the following features:
- Open Price
- High Price
- Low Price
- Volume

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django framework
- Bootstrap for the UI components
- scikit-learn for machine learning capabilities 
