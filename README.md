# 💎 GemPricer AI - Diamond Price Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Project Overview

**GemPricer AI** is an advanced machine learning-powered web application that revolutionizes diamond valuation using AI-driven predictions based on the industry-standard **4Cs** (Cut, Clarity, Color, Carat). This sophisticated system provides accurate, data-driven diamond price predictions to help jewelers, buyers, and enthusiasts make informed decisions.

### ✨ Key Features

- 🧠 **AI-Powered Predictions**: Advanced Random Forest Regression model with **98.27% R² accuracy**
- 🎨 **Modern Dark UI**: Futuristic dark blue theme with glassmorphism effects
- 📊 **4Cs Analysis**: Comprehensive evaluation based on Cut, Clarity, Color, and Carat
- 🔄 **Real-time Processing**: Instant price predictions with animated counters
- 🎯 **Custom Dropdowns**: Fully styled dark-themed dropdown menus (no browser defaults)
- 🎛️ **Custom Number Controls**: Subtle arrow spinners for numeric inputs
- 📈 **Model Training Pipeline**: Automated ML pipeline with data validation and transformation
- 🚀 **Production Ready**: Flask-based web application with comprehensive error handling
- 📱 **Fully Responsive**: Mobile-friendly interface with smooth animations

## 🏗️ Architecture Overview

### System Components

```
GemPricer-AI/
├── 🎯 Frontend (Web Interface)
│   ├── templates/           # HTML templates
│   │   └── ai_index.html    # Main futuristic UI
│   ├── assets/css/         # Styling and responsive design
│   └── assets/js/          # Interactive functionality
├── 🧠 Machine Learning Pipeline
│   ├── mlProject/          # Core ML package
│   ├── artifacts/          # Trained models and data
│   └── main.py             # Training pipeline
├── 🌐 Web Application
│   ├── app.py              # Flask web server
│   └── prediction_pipeline.py # Real-time prediction
└── 📊 Data & Configuration
    ├── artifacts/data_ingestion/    # Raw data
    ├── artifacts/data_transformation/ # Processed data
    └── mlProject/config/           # Configuration files
```

### ML Pipeline Architecture

The system follows a sophisticated 5-stage machine learning pipeline:

1. **Data Ingestion** → Download and extract diamond dataset
2. **Data Validation** → Schema validation and quality checks
3. **Data Transformation** → Feature engineering and preprocessing
4. **Model Training** → Random Forest model training
5. **Model Evaluation** → Performance metrics and MLflow tracking

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ozarakesh533/GemPricer-AI.git
   cd GemPricer-AI
   ```

2. **Install dependencies**
   ```bash
   pip install flask pandas scikit-learn numpy joblib pyyaml
   ```
   
   Or create a `requirements.txt` and install:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model** (First time setup)
   ```bash
   python main.py
   ```
   
   This will:
   - Download and process the diamond dataset
   - Validate data quality
   - Transform features
   - Train the Random Forest model
   - Evaluate model performance
   - Save artifacts to `artifacts/` directory

4. **Launch the web application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:8080`
   - Start predicting diamond prices!

## 🎨 UI/UX Features

### Dark Futuristic Theme

The application features a premium dark blue/navy theme with:

- **Glassmorphism Effects**: Frosted glass backgrounds with backdrop blur
- **Neon Blue Accents**: Subtle cyan/blue glows and highlights
- **Smooth Animations**: Elegant transitions and hover effects
- **Premium Typography**: Orbitron font for headings, Poppins for body text

### Custom Form Controls

#### Custom Dropdowns
- **No Browser Defaults**: Fully custom-styled dropdown menus
- **Dark Theme**: Navy blue gradient backgrounds
- **Hover Effects**: Neon cyan highlights
- **Keyboard Navigation**: Full keyboard support (Arrow keys, Enter, Escape)
- **Accessible**: Proper ARIA attributes and focus states

#### Custom Number Spinners
- **Subtle Arrow Controls**: Minimal up/down arrows instead of default spinners
- **Theme-Matched**: Light cyan strokes matching the UI
- **Hover States**: Smooth opacity transitions
- **Functional**: Click to increment/decrement values

### Responsive Design

- **Mobile-First**: Optimized for all screen sizes
- **Breakpoints**: Tailored layouts for mobile, tablet, and desktop
- **Touch-Friendly**: Large tap targets and smooth scrolling

## 📊 Model Performance

Our Random Forest Regression model achieves exceptional performance:

| Metric | Value | Description |
|--------|-------|-------------|
| **R² Score** | **98.27%** | Coefficient of determination |
| **RMSE** | **$526.33** | Root Mean Squared Error |
| **MAE** | **$265.51** | Mean Absolute Error |
| **MSE** | **$277,023.30** | Mean Squared Error |

### Model Architecture

- **Algorithm**: Random Forest Regressor
- **Features**: 9 input features (Carat, Cut, Color, Clarity, Depth, Table, X, Y, Z)
- **Preprocessing**: 
  - StandardScaler for numerical features
  - OrdinalEncoder for categorical features
- **Validation**: Train-test split with outlier removal
- **Model Persistence**: Joblib serialization

## 💎 The 4Cs Explained

### 🔪 Cut
The precision and artistry of the diamond's shape affects its brilliance and fire.
- **Categories**: Fair, Good, Very Good, Premium, Ideal
- **Impact**: Better cut = more brilliance and higher value

### 🔍 Clarity
The absence of inclusions and imperfections determines the diamond's purity.
- **Categories**: I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF
- **Scale**: IF (Flawless) to I1 (Included)

### 🎨 Color
The whiteness or tint of the diamond impacts its visual appeal.
- **Categories**: J, I, H, G, F, E, D (D being colorless)
- **Scale**: D (Colorless) to J (Near Colorless with slight tint)

### ⚖️ Carat
The weight and size of the diamond directly influences its value.
- **Range**: 0.2 - 5.01 carats
- **Note**: Larger carats exponentially increase price

## 🛠️ Technical Details

### Core Technologies

- **Backend**: Flask (Python web framework)
- **Machine Learning**: Scikit-learn (Random Forest Regressor)
- **Data Processing**: Pandas, NumPy
- **Frontend**: 
  - HTML5, CSS3, JavaScript
  - Tailwind CSS (via CDN)
  - Swiper.js (for carousel)
  - AOS (Animate On Scroll)
- **Model Persistence**: Joblib
- **Configuration**: YAML

### Key Features

- **Real-time Predictions**: Instant price calculations via AJAX
- **Input Validation**: Comprehensive client and server-side validation
- **Error Handling**: Robust error management and logging
- **Responsive Design**: Mobile-friendly interface
- **Model Versioning**: MLflow integration for experiment tracking
- **Logging**: Comprehensive logging system for debugging

## 📁 Project Structure

```
GemPricer-AI/
├── app.py                          # Main Flask application
├── main.py                         # ML pipeline training script
├── setup.py                        # Package configuration
├── train_model.py                  # Model training utilities
│
├── mlProject/                      # Core ML package
│   ├── components/                 # ML components
│   │   ├── data_ingestion.py       # Data download and extraction
│   │   ├── data_validation.py      # Data quality checks
│   │   ├── data_transformation.py  # Feature engineering
│   │   ├── model_trainer.py        # Model training logic
│   │   └── model_evaluation.py     # Performance evaluation
│   ├── pipeline/                   # ML pipelines
│   │   ├── data_ingestion_pipeline.py
│   │   ├── data_validation_pipeline.py
│   │   ├── data_transformation_pipeline.py
│   │   ├── model_trainer_pipeline.py
│   │   ├── model_evaluation_pipeline.py
│   │   └── prediction_pipeline.py  # Real-time predictions
│   ├── config/                     # Configuration management
│   │   └── configuration.py
│   ├── entity/                     # Data classes
│   │   └── config_entity.py
│   └── utils/                      # Utility functions
│       └── common.py
│
├── artifacts/                      # Generated artifacts
│   ├── data_ingestion/             # Raw data files
│   ├── data_transformation/        # Processed data and encoders
│   ├── model_trainer/              # Trained models (model.joblib)
│   ├── model_evaluation/           # Performance metrics
│   └── data_validation/            # Validation reports
│
├── templates/                      # HTML templates
│   ├── ai_index.html               # Main application interface (Futuristic UI)
│   ├── results.html                # Prediction results page
│   └── error.html                  # Error handling page
│
├── assets/                         # Static assets
│   ├── css/                        # Stylesheets
│   ├── js/                         # JavaScript files
│   ├── img/                        # Images and icons
│   │   ├── 4C's/                   # 4Cs explanation images
│   │   ├── diamond-cuts/          # Diamond cut images
│   │   └── clients/               # Client logos
│   └── vendor/                     # Third-party libraries
│       ├── swiper/                 # Carousel library
│       └── aos/                    # Animation library
│
└── logs/                           # Application logs
    ├── app.log                     # Flask application logs
    └── running_logs.log            # ML pipeline logs
```

## 🎮 Usage Guide

### Web Interface

1. **Navigate to the application** at `http://localhost:8080`
2. **Fill in the diamond specifications**:
   - **Carat weight** (0.2 - 5.01) - Use custom spinner controls
   - **Cut quality** (Fair to Ideal) - Custom dropdown
   - **Color grade** (J to D) - Custom dropdown
   - **Clarity grade** (I1 to IF) - Custom dropdown
   - **Physical dimensions** (X, Y, Z in mm) - Custom spinner controls
   - **Depth and Table percentages** - Custom spinner controls
3. **Click "Estimate Price"** to get instant results
4. **View detailed prediction** with formatted price display and animated counter

### API Usage

The application supports both form submissions and JSON API requests:

#### JSON API Request

```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{
    "carat": 1.0,
    "cut": "Ideal",
    "color": "D",
    "clarity": "IF",
    "depth": 61.5,
    "table": 55.0,
    "x": 6.5,
    "y": 6.6,
    "z": 4.0
  }'
```

**Response:**
```json
{
  "status": "success",
  "prediction": 12345.67,
  "formatted_prediction": "12,345.67"
}
```

#### Form Submission

Traditional form POST requests are also supported and will redirect to the results page.

### Model Training

To retrain the model with new data:

```bash
python main.py
```

This will execute the complete ML pipeline:
- Data ingestion and validation
- Feature transformation
- Model training
- Performance evaluation

The trained model and artifacts will be saved in the `artifacts/` directory.

## 🔧 Configuration

### Environment Variables

- `PORT`: Server port (default: 8080)
- `FLASK_ENV`: Environment mode (development/production)

### Model Parameters

The Random Forest model uses the following hyperparameters (configurable in `config/params.yaml`):
- `n_estimators`: Number of trees in the forest
- `random_state`: Seed for reproducible results
- `max_depth`: Maximum depth of trees (auto)

### Configuration Files

- `config/config.yaml`: Pipeline configuration
- `config/schema.yaml`: Data schema definitions
- `config/params.yaml`: Model hyperparameters

## 🧪 Testing

### Manual Testing

1. **Start the application**: `python app.py`
2. **Test various diamond specifications**:
   - High-quality diamonds (Ideal cut, D color, IF clarity)
   - Medium-quality diamonds (Good cut, G color, VS1 clarity)
   - Lower-quality diamonds (Fair cut, J color, I1 clarity)
3. **Verify predictions** are reasonable and consistent
4. **Test UI responsiveness** on different screen sizes
5. **Test custom dropdowns** and number spinners

### Performance Testing

Monitor the application logs for:
- Prediction response times
- Memory usage
- Error rates
- Model loading time

### API Testing

Use tools like Postman or curl to test the API endpoints:
- Test with valid inputs
- Test with missing fields
- Test with invalid data types
- Test edge cases (very large/small values)

## 🚀 Deployment

### Local Development

```bash
python app.py
```

The application will run on `http://localhost:8080` by default.

### Production Deployment

1. **Set environment variables**:
   ```bash
   export FLASK_ENV=production
   export PORT=8080
   ```

2. **Use a production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8080 app:app
   ```

3. **Use a reverse proxy** (Nginx recommended):
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8080;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Train model (if not already trained)
RUN python main.py

# Expose port
EXPOSE 8080

# Run application
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t gempriser-ai .
docker run -p 8080:8080 gempriser-ai
```

### Cloud Deployment

#### Heroku

1. Create `Procfile`:
   ```
   web: python app.py
   ```

2. Deploy:
   ```bash
   heroku create gempriser-ai
   git push heroku main
   ```

#### AWS/GCP/Azure

- Use container services (ECS, Cloud Run, Container Instances)
- Or use serverless functions (Lambda, Cloud Functions)
- Ensure model artifacts are accessible

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** and test thoroughly
4. **Commit your changes**: `git commit -m "Add feature-name"`
5. **Push to the branch**: `git push origin feature-name`
6. **Submit a pull request**

### Development Guidelines

- Follow PEP 8 Python style guidelines
- Add comprehensive docstrings to functions
- Include unit tests for new features
- Update documentation for API changes
- Maintain the dark futuristic UI theme consistency
- Test on multiple browsers and devices

### Code Style

- **Python**: Follow PEP 8, use type hints where possible
- **HTML/CSS**: Use semantic HTML, maintain consistent naming
- **JavaScript**: Use modern ES6+ syntax, add comments for complex logic

## 📊 Dataset Information

The model is trained on a comprehensive diamond dataset containing:
- **Total Samples**: 50,000+ diamond records
- **Features**: 
  - Numerical: Carat, Depth, Table, X, Y, Z dimensions
  - Categorical: Cut, Color, Clarity
- **Target**: Price in USD
- **Data Quality**: Cleaned and validated data with outlier removal
- **Source**: Kaggle diamond dataset

## 🔍 Troubleshooting

### Common Issues

1. **Model files not found**:
   ```bash
   python main.py  # Train the model first
   ```

2. **Port already in use**:
   ```bash
   export PORT=8081  # Use different port
   python app.py
   ```

3. **Dependencies missing**:
   ```bash
   pip install flask pandas scikit-learn numpy joblib pyyaml
   ```

4. **Import errors**:
   ```bash
   pip install -e .  # Install package in development mode
   ```

5. **Dropdowns not working**:
   - Check browser console for JavaScript errors
   - Ensure all assets are loaded correctly
   - Clear browser cache

6. **Predictions returning errors**:
   - Verify model artifacts exist in `artifacts/model_trainer/`
   - Check input data format matches expected schema
   - Review application logs in `app.log`

### Log Files

Check the following logs for debugging:
- `app.log`: Application runtime logs
- `logs/running_logs.log`: ML pipeline logs

## 📈 Future Enhancements

- [ ] **Multi-gemstone Support**: Extend to other precious stones (rubies, sapphires, etc.)
- [ ] **Advanced ML Models**: Implement deep learning approaches (Neural Networks)
- [ ] **Real-time Market Data**: Integrate live diamond market prices
- [ ] **Image Recognition**: Add diamond image analysis using computer vision
- [ ] **Mobile App**: Native mobile application (React Native/Flutter)
- [ ] **API Documentation**: Swagger/OpenAPI documentation
- [ ] **User Authentication**: User accounts and prediction history
- [ ] **Batch Processing**: Multiple diamond predictions at once
- [ ] **Price History**: Track price trends over time
- [ ] **Comparison Tool**: Compare multiple diamonds side-by-side
- [ ] **Export Features**: Export predictions to PDF/CSV
- [ ] **Dark/Light Theme Toggle**: User preference for theme

## 📞 Support

For support and questions:
- **Email**: ozarakesh533@gmail.com
- **GitHub Issues**: [Create an issue](https://github.com/Ozarakesh533/GemPricer-AI/issues)
- **Documentation**: Check this README and inline code comments

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: Diamond dataset from Kaggle
- **MLflow**: For experiment tracking and model versioning
- **Scikit-learn**: For machine learning algorithms
- **Flask**: For the web framework
- **Tailwind CSS**: For utility-first CSS framework
- **Swiper.js**: For carousel functionality
- **AOS**: For scroll animations

## 🎯 Project Highlights

### What Makes This Project Special

1. **High Accuracy**: 98.27% R² score demonstrates exceptional model performance
2. **Beautiful UI**: Modern dark futuristic theme with premium feel
3. **Custom Controls**: Fully styled form elements matching the theme
4. **Production Ready**: Comprehensive error handling and logging
5. **Well Documented**: Extensive documentation and code comments
6. **Modular Architecture**: Clean separation of concerns
7. **Scalable**: Easy to extend and maintain

---

**Made with ❤️ by [Ozarakesh533](https://github.com/Ozarakesh533)**

*Revolutionizing diamond valuation through the power of artificial intelligence.*

---

## 📸 Screenshots

*Note: Add screenshots of your application here to showcase the UI*

- Main prediction interface
- Results page
- Mobile responsive view
- Custom dropdowns and controls

---

**Star ⭐ this repository if you find it helpful!**
