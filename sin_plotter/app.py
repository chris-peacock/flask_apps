from flask import Flask, render_template, request, jsonify, send_file
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

# Function to generate the sine wave plot with given amplitude and frequency
def generate_sine_wave_plot(amplitude, frequency):
    x = np.linspace(0, 10, 1000)
    y = amplitude * np.sin(frequency * x)

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f'Sine Wave: Amplitude = {amplitude}, Frequency = {frequency}')
    ax.set_ybound(-5, 5)
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    
    return fig

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    # Get amplitude and frequency from query parameters (default values if not set)
    amplitude = float(request.args.get('amplitude', 1))
    frequency = float(request.args.get('frequency', 1))

    # Generate plot based on amplitude and frequency
    fig = generate_sine_wave_plot(amplitude, frequency)

    # Save the plot to a BytesIO object and convert to base64
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    # Return the plot image in base64
    return jsonify({'img': img_base64})

@app.route('/download')
def download():
    # Get amplitude and frequency from query parameters
    amplitude = float(request.args.get('amplitude', 1))
    frequency = float(request.args.get('frequency', 1))

    # Generate the plot based on the current amplitude and frequency
    fig = generate_sine_wave_plot(amplitude, frequency)

    # Save the figure to a file
    filepath = 'sine_wave_plot.png'
    fig.savefig(filepath, format='png')

    # Send the file as a download
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)