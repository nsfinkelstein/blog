# Install jupyter into the current enviornment if not already present
pip install jupyter

# Create directory for virtualenvs
mkdir ~/venvs

# For each post that has a requirements.txt file, create the corresponding kernel
find "quarto-site/blog/posts" -type f -name "requirements.txt" | while read requirements_file; do
    # Get the directory of the found requirements.txt file
    dir_path=$(dirname "$requirements_file")

    # Extract the name of the directory where requirements.txt is located
    dir_name=$(basename "$dir_path")

    # Create a new directory for the venv with the name of the found directory
    venv_path="~/venvs/${dir_name}"
    
    # Create the virtual environment
    python -m venv "$venv_path"
    
    # Activate the virtual environment
    source "${venv_path}/bin/activate"
    
    # Install requirements from the requirements.txt file
    pip install -r "$requirements_file"

    # register a corresponding kernel
    pip install ipykernel
    python -m ipykernel install --user --name "${dir_name}" --display-name "${dir_name}"
    
    # Deactivate the virtual environment
    deactivate
done
