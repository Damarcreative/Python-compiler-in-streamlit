# Python Compiler Online

[![Huggingface Demo](https://raw.githubusercontent.com/Damarcreative/Python-compiler-in-streamlit/b97f6920b7948ec27eb1089f617828bdc7d53dc8/assets/huggingface.svg 'Huggingface Demo')]([https://codecademy.com](https://huggingface.co/spaces/DamarJati/Python-Compiler))


This is a simple web application built with Streamlit that allows you to compile and run Python code online. It provides three text areas: one for listing required Python libraries to be installed, one for entering Python code to be compiled, and one for displaying the output.

## Installation
1. Clone the repository:
   ```shell
   git clone https://github.com/Damarcreative/Python-compiler-in-streamlit.git
   cd Python-compiler-in-streamlit
2. Install the required dependencies. It is recommended to use a virtual environment:
    ```shell
       python -m venv venv
       source venv/bin/activate    # For Linux/Mac
       venv\Scripts\activate       # For Windows
       pip install -r requirements.txt
3. Run the Streamlit application:
    ```shell
    streamlit run python_compiler.py
4. The application will open in your browser at http://localhost:8501

## Usage
1. In the first textarea, enter the list of Python libraries that need to be installed. Each library should be on a separate line.
2. In the second textarea, enter the Python code that you want to compile and run.
3. Click the "Run" button to execute the code. If there are any required libraries, they will be installed first. The output of the code will be displayed in the third textarea.
4. Click the "Stop" button to stop the execution of the code (if applicable).
5. Click the "Restart" button to restart the execution of the code (if applicable).

## Example
Here's an example of how the Python Compiler Online application can be used:
1. List of required libraries:
    ```shell
    numpy
    pandas
2. Python code:
    ```shell
    import numpy as np
    import pandas as pd
    
    data = np.array([[1, 2, 3], [4, 5, 6]])
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])
    print(df)
3. Click the "Run" button to execute the code and see the output in the third textarea.

![example!](https://raw.githubusercontent.com/Damarcreative/Python-compiler-in-streamlit/main/assets/example.png "Streamlit run examle")

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

