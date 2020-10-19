# **Installing pip for Python 3**

`sudo apt update`

Use the following command to install pip for Python 3:

`sudo apt install python3-pip`

Once the installation is complete, verify the installation by checking the pip version:

`pip3 --version`

# **Installing pip for Python 2**

Update the package index by running the following command:


Install pip for Python 2 with:

`sudo apt install python-pip`

Verify the installation by printing the pip version number:

`pip --version`

# **Installing Virtual Environment**

`apt-get install python3-venv`

# **Project SetUp**

* To create a virtual environment, use the following command, where ".venv" is the name of the environment folder:

`python3 -m venv .venv`

* Activate the virtualenv (OS X & Linux): 

`source .venv/bin/activate`

You’ll need to activate your virtual environment every time you work on your Python project. In the rare cases when you want to deactivate your virtualenv without closing your terminal session, just use the `deactivate` command.

# **Package and Dependency Manager**

To install the package, you can just run `pip install <somepackage>` that will build an extra Python library in your home directory.

Running `pip freeze`,can help to check installed packages and packages versions listed in case-insensitive sorted order.

Save all the packages in the file with `pip freeze > requirements.txt`.

Add requirements.txt to the root directory of the project. Done.

If you’re going to share the project you will need to install dependencies by running 

`pip install -r requirements.txt`

The recipient still needs to create their own virtual environment, however.

OBS: Use `pip3 install -r requirements.txt` if you are using python3

# **Installing Jupyter with pip3**

`pip3 install jupyter`

Start Jupyter Notebook in the directory you want.

`jupyter notebook`

# **Install Pandas**

`pip3 install pandas`

# **Common Solution**

Please, run `jupyter notebook` and open the file *VLAN_allocation.ipynb* inside the `notebook` folder.

in the **Kernel** dropdown, choose `Restart & Run All`

The `output.csv` file is going to be generated inside the `data` folder

# **Run project as script**

run `python3 src/main.py`

# **for Unit Tests**

`pip3 install mock`


# **RESOURCES**

https://code.visualstudio.com/docs/python/tutorial-flask
https://docs.python.org/3/tutorial/venv.html
https://code.visualstudio.com/docs/python/tutorial-deploy-containers
https://pip.readthedocs.io/en/stable/user_guide/#requirements-files
https://code.visualstudio.com/docs/python/tutorial-deploy-containers
https://realpython.com/python-application-layouts/
