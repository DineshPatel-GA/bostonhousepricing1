# ##bostonhousepricing1

## Software & Tools
1. [Github Account](https://github.com)
2. [HerokuAccount](https://www.heroku.com)
3. [VS Code IDE](https://code.visualstudio.com)
4. [GitCLI](https://git-scm.com/download/win)
##Project Flow
    Create an environment in Visual Studio Code: 1:23
        Open new terminal and >deactivate
        Ctr+Shft+p
            In search bar look for python:Select Interpreter
                Select the env with anaconda.
        Select command prompt from a top right dropdown menu in current terminal
        at prompt give following code
        -----
        >conda create -p venv python==3.7 -y  // -y helps to keep answering yes during installation.
        Activate env:
        >conda activate C:\Users\Owner\Documents\DCP_Learning\AI_ML Projects\bostonhousepricing1\venv
        or
        >conda activate venv/
        -----
    Create requirements.txt file:
        Hover over folder name and create a new file.
        List all of the libraries we are going to use, Flask, sklearn, pandas, numpy, matplotlib. 
        To install of the libraries on cmd use following code.
        >pip install -r requirements.txt
    Install libraries in requirements.txt:
        >pip install -r requirements.txt
    GIT
    GitCLI Configurations:
        >git config --global user.name "Dinesh Patel"
        >git config --global user.email "Dincpatel@gmail.com"
    Any code in .gitignore will be not be 'commit'ed to git repo.

#

