# gpt2 based model

## Project Structure

The project directory is organized as follows:

```
ai_final_project/
├── app.py
├── model.py
└── saved_model/
```

## Download the Saved Model

Download the model from the following link and place it in the `saved_model` directory:

[Saved Model](https://drive.google.com/file/d/13W-NVE42QkZVoJiIsTmPWsBkmrRDG4Ez/view?usp=sharing)

## Getting Started

1. **Navigate to the project directory**:

    ```sh
    cd C:\Users\<username>\ai_final_project
    ```

2. **Activate the virtual environment**:

    ```sh
    .\.venv\Scripts\activate
    ```

3. **Set the FLASK_APP environment variable**:

    ```sh
    set FLASK_APP=app.py
    ```

4. **Run the Flask application**:

    ```sh
    python -m flask run
    ```

    After running the above command, you should see the following output indicating that the server is running:

    ```
    * Running on http://127.0.0.1:5000/
    ```

## Using the API

You can use `curl` to interact with the API. Here is an example of how to use the `generate-text` endpoint:

```sh
curl -X POST http://127.0.0.1:5000/generate-text -H "Content-Type: application/json" -d "{\"input_text\": \"Hello, how are you?\"}"
```

This command sends a POST request to the `generate-text` endpoint with a JSON payload containing the input text.
