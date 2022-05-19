import streamlit as st
from io import StringIO
import subprocess
import sys

def install(managment_file, package_manager='pip'):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", managment_file])

# requirements
requirements_type = st.text_input('Pip or Conda?')
requirements = st.file_uploader('Upload the requirements_file')

# models
checkpoint = st.file_uploader('Upload the model checkpoint')
model = st.file_uploader('Upload the model class')
model_path = st.text_input('Input path to save model')

if requirements_type is not None and requirements is not None:
    requirements_type =  requirements_type.lower()
    if requirements_type == 'pip':
        st.write('Identified pip requirements file. Commencing installation')
        reqs = StringIO(model.getvalue().decode("utf-8")).read()
        install(reqs, managment_file)
    elif requirements_type == 'conda':
        st.write('Identified conda env file. Commencing write')
    else:
        raise("Please provide either a pip or conda requirements file and specify in te 'Pip or Conda text input'")


if model is not None and model_path is not None:
    # read file
    contents = StringIO(model.getvalue().decode("utf-8")).read()
    # write file
    with open(model_path, 'w') as f:
        f.write(contents)

    st.write(contents)
    from models import Model
    model = Model()
    st.write(model)
