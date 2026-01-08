import os
import sys
import logging
import pandas as pd
from flask import Flask, render_template, request, jsonify, redirect, url_for
from mlProject.pipeline.prediction_pipeline import PredictionPipeline
from mlProject import logger

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)

app = Flask(__name__, static_folder="assets", template_folder="templates")
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_no_cache_headers(response):
    try:
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    except Exception:
        pass
    return response

# Route for homepage
@app.route('/')
def homepage():
    try:
        return render_template("ai_index.html")
    except Exception as e:
        logger.error(f"Error loading homepage: {str(e)}")
        return "Error loading page. Please try again later.", 500

# Route for training pipeline
@app.route('/train', methods=['GET'])
def training():
    try:
        logger.info("Starting model training...")
        # Using subprocess instead of os.system for better control
        import subprocess
        result = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            error_msg = f"Training failed: {result.stderr}"
            logger.error(error_msg)
            return jsonify({"status": "error", "message": error_msg}), 500
            
        logger.info("Training completed successfully")
        return jsonify({"status": "success", "message": "Training completed successfully"})
        
    except Exception as e:
        error_msg = f"Error during training: {str(e)}"
        logger.error(error_msg)
        return jsonify({"status": "error", "message": error_msg}), 500

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        logger.info("Received prediction request")
        
        # Get data from form or JSON
        if request.is_json:
            data = request.get_json()
            get_value = lambda key: data.get(key, '')
            is_ajax = True
        else:
            data = request.form
            get_value = lambda key: data.get(key, '')
            is_ajax = False
        
        # Validate required fields
        required_fields = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']
        missing_fields = [field for field in required_fields if not get_value(field)]
        
        if missing_fields:
            error_msg = f"Missing required fields: {', '.join(missing_fields)}"
            logger.warning(error_msg)
            if is_ajax:
                return jsonify({"status": "error", "message": error_msg}), 400
            else:
                return render_template('index.html', error=error_msg)
        
        # Parse and validate numerical inputs
        try:
            carat = float(get_value('carat'))
            depth = float(get_value('depth'))
            table = float(get_value('table'))
            x = float(get_value('x'))
            y = float(get_value('y'))
            z = float(get_value('z'))
            
            # Basic validation
            if any(val <= 0 for val in [carat, depth, table, x, y, z]):
                raise ValueError("All numerical values must be positive")
                
        except ValueError as e:
            error_msg = f"Invalid input: {str(e)}"
            logger.warning(error_msg)
            if is_ajax:
                return jsonify({"status": "error", "message": error_msg}), 400
            else:
                return render_template('index.html', error=error_msg)
        
        # Get categorical inputs
        cut = get_value('cut').strip()
        color = get_value('color').strip()
        clarity = get_value('clarity').strip()
        
        # Create input DataFrame
        input_data = pd.DataFrame([[
            carat, cut, color, clarity, depth, table, x, y, z
        ]], columns=required_fields)
        
        logger.info(f"Input data: {input_data.to_dict(orient='records')[0]}")
        
        try:
            # Initialize pipeline and make prediction
            pipeline = PredictionPipeline()
            transformed_data = pipeline.data_transform(input_data)
            prediction = pipeline.predict(transformed_data)
            
            # Format the prediction
            prediction_value = float(prediction[0])
            formatted_pred = "{:,.2f}".format(prediction_value)
            logger.info(f"Prediction successful: ${formatted_pred}")
            
            if is_ajax:
                return jsonify({
                    "status": "success",
                    "prediction": prediction_value,
                    "formatted_prediction": formatted_pred
                })
            else:
                # Redirect to results page with parameters
                from urllib.parse import urlencode
                params = {
                    'carat': carat,
                    'cut': cut,
                    'color': color,
                    'clarity': clarity,
                    'depth': depth,
                    'table': table,
                    'x': x,
                    'y': y,
                    'z': z,
                    'prediction': prediction_value
                }
                return redirect(f"/results?{urlencode(params)}")
                
        except Exception as e:
            error_msg = f"Error during prediction: {str(e)}"
            logger.error(error_msg, exc_info=True)
            if is_ajax:
                return jsonify({"status": "error", "message": error_msg}), 500
            else:
                return render_template('index.html', error=error_msg)
        
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        logger.error(error_msg, exc_info=True)
        if is_ajax:
            return jsonify({
                "status": "error",
                "message": "An unexpected error occurred. Please try again."
            }), 500
        else:
            return render_template('index.html', error=error_msg)

# Route to display results
@app.route('/results')
def results():
    try:
        logger.info("Rendering results page with args: %s", dict(request.args))
        
        # Get all parameters from the URL with proper defaults
        carat = request.args.get('carat', '0')
        cut = request.args.get('cut', 'N/A')
        color = request.args.get('color', 'N/A')
        clarity = request.args.get('clarity', 'N/A')
        depth = request.args.get('depth', '0')
        table = request.args.get('table', '0')
        x = request.args.get('x', '0')
        y = request.args.get('y', '0')
        z = request.args.get('z', '0')
        prediction = request.args.get('prediction', '0')
        
        # Format the prediction with 2 decimal places
        try:
            prediction_float = float(prediction)
            formatted_pred = "${:,.2f}".format(prediction_float)
        except (ValueError, TypeError) as e:
            logger.error(f"Error formatting prediction value '{prediction}': {str(e)}")
            prediction_float = 0.0
            formatted_pred = "N/A"
        
        # Prepare context for the template
        context = {
            'carat': carat,
            'cut': cut.title(),
            'color': color.upper(),
            'clarity': clarity.upper(),
            'depth': depth,
            'table': table,
            'x': x,
            'y': y,
            'z': z,
            'prediction': prediction_float,
            'formatted_prediction': formatted_pred
        }
        
        logger.info(f"Rendering template with context: {context}")
        response = render_template('results.html', **context)
        # Add cache-busting headers to prevent browser caching
        from flask import make_response
        resp = make_response(response)
        resp.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        resp.headers['Pragma'] = 'no-cache'
        resp.headers['Expires'] = '0'
        return resp
        
    except Exception as e:
        logger.error(f"Error in results page: {str(e)}", exc_info=True)
        return redirect('/')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Server error: {str(error)}")
    return render_template('error.html', error="Internal server error"), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
