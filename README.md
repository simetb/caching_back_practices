# Repository: Flask and Redis Caching Practice

## Purpose:
This repository serves as a personal practice demonstrating caching techniques both on the client-side and server-side using Flask for the server and Redis as the caching storage. The main objective is to understand and practice how to implement caching to improve the performance of web applications, reducing server load and enhancing user experience.

## Deployment:
To deploy this application, a Dockerfile is provided containing the necessary instructions to build a Docker image. Additionally, a requirements.txt file is included listing the Python dependencies required to run the Flask application.

### Deployment Instructions:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/your-username/repo-cache-flask-redis.git
   ```
   
2. Navigate to the repository directory:
   ```bash
   cd repo-cache-flask-redis
   ```
   
3. Build the Docker Redis image using the provided Dockerfile:( Only if is necessary )
   ```bash
   docker build -t image-name:tag .
   ```
Replace image-name with the desired name for the image and tag with the version you prefer.

4. Once the image is successfully built, you can run a Docker container based on this image:
    ```bash
   docker run -d -p 5000:5000 image-name:tag
   ```
This will run the Flask application in a Docker container, exposing port 5000.
Now, the application will be available in your web browser at http://localhost:5000.

## Contributions:
Contributions are welcome. If you find any issues or have any suggestions for improvement, feel free to open an issue in the repository or submit a pull request with your proposed changes.

## License:
This project is licensed under the MIT License. See the LICENSE file for more details.
