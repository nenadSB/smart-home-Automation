# Smart Home Automation System

## Overview
The Smart Home Automation System integrates various smart devices and sensors to enhance convenience, security, and energy efficiency. Key features include temperature monitoring, smart lighting control, automated climate control, motion detection, and energy management. The system uses a Flask-based web interface for centralized control and real-time monitoring. It leverages MQTT for efficient device communication, ensuring reliable and responsive control. This modular system is scalable, allowing for easy expansion and integration of additional devices.

## Tools and Technologies Used

### 1. Programming Language
- **Python 3.12.3**  
  *Purpose:* Used for backend development, handling device communication, API implementation, and server-side processing.

### 2. Libraries and Frameworks
- **Flask**  
  *Purpose:* Provides the backend web framework for creating the REST API and serving the web interface.

- **MQTT (paho-mqtt)**  
  *Purpose:* Enables real-time communication between the web interface and IoT devices.

- **Jinja2**  
  *Purpose:* Used for rendering dynamic web pages in Flask.

### 3. Frontend Technologies
- **HTML, CSS, JavaScript**  
  *Purpose:* Used to build a responsive user interface for controlling smart devices.

- **AJAX (Fetch API)**  
  *Purpose:* Allows real-time data updates without reloading the page.

### 4. Data Management Tools
- **JSON**  
  *Purpose:* Used for sending and receiving structured data between the frontend and backend.

### 5. Utility Tools
- **OS Library**  
  *Purpose:* Helps in managing file paths and configurations within the system.

- **Flask Debug Mode**  
  *Purpose:* Enables easy debugging during development.

## How to Run the Project
1. **Install Dependencies**  
   Run the following command to install required Python libraries:
   ```sh
   pip install flask paho-mqtt
   ```

2. **Start the Flask Server**  
   ```sh
   python web/app.py
   ```

3. **Access the Web Interface**  
   Open a browser and go to:  
   `http://127.0.0.1:5000`

## Features
- Real-time device status updates
- Control smart devices (lights, thermostat, plug, etc.)
- Modular and scalable design
- User-friendly web interface

## Future Improvements
- Adding user authentication
- Implementing database storage
- Expanding device compatibility

