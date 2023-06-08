import streamlit as st
import subprocess

# Function to run Python code
def run_code(code):
    process = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

# Function to install libraries
def install_libraries(libs):
    process = subprocess.Popen(["pip", "install", *libs], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

# Streamlit app layouts
def app():
    st.title("Python Compiler Online")
    
    # Textarea for list libraries
    libs = st.text_area("List Library Python (separated by newline)", height=100)
    
    # Textarea for Python code
    code = st.text_area("Python Code", height=300)
    
    # run button
    if st.button("Run"):
        if libs:
            # Install libraries if any
            st.write("Installing libraries...")
            output, error = install_libraries(libs.split("\n"))
            if output:
                st.code(output)
            if error:
                st.error(error)
        
        # Running Python code
        st.write("Running code...")
        output, error = run_code(code)
        
        # Displays output and errors
        if output:
            st.code(output)
        if error:
            st.error(error)
    
    # Tombol stop
    if st.button("Stop"):
        # Implementation of the stop function here (if needed)
        st.write("Stop button clicked")
    
    # Restart button
    if st.button("Restart"):
        # Implement the restart function here (if needed)
        st.write("Restart button clicked")

# Run the Streamlit application
if __name__ == '__main__':
    app()
