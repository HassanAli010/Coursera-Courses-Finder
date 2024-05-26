# Coursera-Courses-Finder
Coursera-Courses-Finder (Using Python library Stream-lit and some machine learning algorithms such as pandas, numpy, sklearn etc. 

# Run app
change the file name, Here I'm rename-ing the file name for deployment.
so, when you want to deploy in localhost side then rename the file like app.py / courses.py etc
streamlit run app.py


# importing:
import streamlit as st
import pickle
from recommendation_page import recommendation

# import in recommendation_page file in 
import pickle
import streamlit as st

# for recommendation.py
import streamlit as st
from recommendation_page import recommendation

# TOOLS USING IN THAT PROJECT
python
streamlit
machine learning algorithms(pandas, numpy, sklearn) using google colab notebook
and some other algorithms.
recommendation function in python etc.


### ERROR: 
in deployment side error:FileNotFoundError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 600, in _run_script
    exec(code, module.__dict__)
File "/mount/src/coursera-courses-finder/streamlit_app.py", line 72, in <module>
    recommendation()
File "/mount/src/coursera-courses-finder/recommendation_page.py", line 6, in recommendation
    similarity = pickle.load(open('similarity.pkl', 'rb'))

## Here are some steps you can take to resolve this issue:

1. Ensure the File Exists
First, ensure that the similarity.pkl file actually exists in the directory where your script is running.

2. Use Absolute Paths
If the file exists, try using an absolute path to ensure that the script can find the file regardless of the working directory. Update your code to:

import os
import pickle

# Assuming the similarity.pkl file is in the same directory as streamlit_app.py
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'similarity.pkl')

with open(file_path, 'rb') as f:
    similarity = pickle.load(f)

3. Check Deployment Configuration
If you are deploying your app on Streamlit Cloud or any other platform, ensure that the similarity.pkl file is included in your deployment. This often involves ensuring that the file is part of your Git repository or included in your deployment package.

4. Debugging Path Issues
Add some debug information to print the current working directory and the absolute path to the file. This can help verify that the paths are correct:
import os
import pickle

# Print the current working directory
print("Current working directory:", os.getcwd())

# Assuming the similarity.pkl file is in the same directory as streamlit_app.py
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'similarity.pkl')

# Print the absolute path to the file
print("Absolute path to similarity.pkl:", file_path)

with open(file_path, 'rb') as f:
    similarity = pickle.load(f)
5. Verify the Path in Deployment Logs
Check the deployment logs on Streamlit Cloud (or your deployment platform) to see the output of the debug information. This can help you understand where the script is running and where it expects to find the file.

6. Update Streamlit Configuration
Ensure your streamlit_app.py is correctly configured to handle the file paths, and make sure any necessary files are included in the repository. Double-check your .gitignore file to make sure similarity.pkl is not being ignored.

### FINAL CODE
import os
import pickle

# Print the current working directory
print("Current working directory:", os.getcwd())

# Assuming the similarity.pkl file is in the same directory as streamlit_app.py
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'similarity.pkl')

# Print the absolute path to the file
print("Absolute path to similarity.pkl:", file_path)

try:
    with open(file_path, 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError as e:
    print(f"Error: {e}")

### CONCLUSION:
By following these steps, you should be able to identify and fix the issue with the file path, ensuring that your Streamlit app can successfully load the similarity.pkl file.



