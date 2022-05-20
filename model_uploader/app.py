import streamlit as st
from io import StringIO
import subprocess
import sys

def install(managment_path, package_manager='pip'):
    st.write(management_path)
    st.write(package_manager)
    output = subprocess.run(
    [sys.executable, "-m", package_manager, "install", "-r", management_path],
    capture_output=True
    )
    st.write(f"{output}")

def write(path, content):
    with open(path, 'w') as f:
        f.write(content)

# requirements
requirements_type = st.text_input('Pip or Conda?')
management_path = st.text_input('Path to save requirements file')
management_file = st.file_uploader('Upload the requirements file')

# models
checkpoint = st.file_uploader('Upload the model checkpoint')
model = st.file_uploader('Upload the model class')
model_path = st.text_input('Input path to save model')

if requirements_type is not None and management_file is not None:
    requirements_type =  requirements_type.lower()
    if requirements_type == 'pip':
        st.write('Identified pip requirements file. Commencing installation')
        reqs = StringIO(management_file.getvalue().decode("utf-8")).read()
        #write(management_path, reqs)
        install(management_path, requirements_type)
    elif requirements_type == 'conda':
        st.write('Identified conda env file. Commencing write')
    else:
        raise("Please provide either a pip or conda requirements file and specify in te 'Pip or Conda text input'")


if model is not None and model_path is not None:
    # read file
    contents = StringIO(model.getvalue().decode("utf-8")).read()
    # write file
    write(model_path, contents)

    st.write(contents)
    from models import Model
    model = Model()
    st.write(model)
