# Dynamic QR Code Generator

## Overview

This project is a simple web application built with Flask that allows users to generate QR codes from provided URLs. Users can enter a URL through a web form, and the application converts it into a QR code, which can be downloaded for later use.

## Features

- **URL to QR Code Conversion**: Enter a URL, and the application generates a QR code representing that URL.
- **Download QR Code**: Users can download the generated QR code for their use.

## Technologies Used

- **Flask**: Used as the web framework for the backend.
- **HTML/CSS**: Frontend for the web application.
- **Bootstrap**: Used for styling and responsive design.
- **MongoDB Atlas**: Database service for storing contact form submissions.
- **PyMongo**: Python driver for MongoDB to interact with the database.

## Project Structure

```
|-- static
|   `-- qrcode.png
|-- templates
|   |-- index.html
|   |-- qr_gen.html
|   `-- ...
|-- app.py
|-- requirements.txt
|-- README.md
```

- **static**: Contains static files such as the generated QR code image.
- **templates**: HTML templates for rendering the web pages.
- **app.py**: Main Flask application file.
- **requirements.txt**: List of project dependencies.
- **README.md**: Project documentation.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/prashdev0/dynamic-qr-code-generator.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open the application in your web browser: [http://localhost:5000](http://localhost:5000)

## Usage

1. Access the application in your web browser.
2. Navigate to the homepage and enter a URL.
3. Click the "Generate QR Code" button.
4. Download the generated QR code.
5. Explore other features as needed.

## Database Integration

The application stores contact form submissions in a MongoDB Atlas database. Ensure you have configured the MongoDB connection string in `app.py` for database functionality.

## Contributors

- Prashant wadhave


## License

This project is licensed under the MIT https://github.com/prashdev01/Dynamic-QR-Code-Generator/blob/main/LICENSE.

```
