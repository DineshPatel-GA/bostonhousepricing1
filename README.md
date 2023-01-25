# bostonhousepricing1
This project is created by following Youtube tutorials by
Krish Nail at www.iNeuron.ai, https://github.com/krishnaik06/bostonhousepricing

My Github: https://github.com/DineshPatel-GA/bostonhousepricing1

## SOFTWARE & TOOLS
1. [Github Account](https://github.com)
2. [HerokuAccount](https://www.heroku.com)
3. [VS Code IDE](https://code.visualstudio.com)
4. [GitCLI](https://git-scm.com/download/win)

##PROJECT FLOW
    Created a basic LinearRegression model withpython on Juypter.
    Create an environment in Visual Studio Code: (time)1:23
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

    Send files to git repo:
        >git add .      //to stage the files which could be commited.
        >cls            // just to clear the screen
        >git status     //to check the status
        >git commit.git commit -m "message"
        >git push <remote> <branch> 
        which is >git push origin main
    CREATE AN APP
        app.py. Create new file app.py
        app.py
            import pickle
            import flask from Flask //for web applications
    Scaling.pkl
        This file is missing in .ipynb code.
        In Linear....ipynb' after code of scaling X_train and test, add following code
        --
        import pickle
        pickle.dump(scaler,open('scaling.pkl','wb'))
        --
        and run again. If lib. do not get recognized, go on top-rt at 'python' and select anaconda config and run again.
        ---
     HTML page:
        Templates folder
            home.html file detail html code with a form to input data will go here.
    Test run:
        >python app.py
        if this does not run delete the current cmd and open it again, and/or pip install -r requirements.txt
        If run, get the ip address and run to see if html page shows up.
    POSTMAN (1:54):
        Install postman
        Select 'POST' and give ip address with app in app.py
        i.e. http://127.0.0.1:5000/predict_app
        Body > row > json > sendgit status
    SAMPLE DATA
        {
         "data": {
                    "CRIM": 0.00051,
                    "ZN": 15,
                    "INDUS":1.55,
                    "CHAS":.5,
                    "NOX": .555,
                    "RM": 5,
                    "AGE": 55,
                    "DIS": 5.55,
                    "RAD": 5,
                    "TAX": 500,
                    "PTRATIO": 15,
                    "B": 555,
                    "LSTAT": 5.55
                 }
        }

    PREPARE FUNCTION FOR WEBAPPLICATION TO PREDICT FROM HTML FORM, 2:06
        get values from html form: request.form.values()
        Convert to float and store as 'data'.
            data=[float(x) for x in request.form.values()]

        Make an array: np.array(data)
        Convert to two diamensional array: np.array(data).reshape(1,-1)
        Transform to standardize fomat with scalar.transform
            final_input=scalar.transorm(np.array(data).reshape(1,-1))

        Use predict function to predict based on final_input and pick value at index[0]
            output=regmodel.predict(final_input)[0]

        Render output in 'prediction-test' element of 'home.html' page with render_template function
            return render_template("home.html",prediction_text="The House price prediction is {}".format(output))

    DEPLOYMENT 
    By HEROKU, 2:13
        Dineshpatel-GA
        lin-reg-boston-h-pricing
        Create procfile with following command for Heroku instance. (only command in the file) 
        ---
            web: gunicorn app:app
        ---
        gunicorn: Green unicorn is for wsgi applications to run python apps concurrently by running multiple processes on python http server.
        app:app presents 'a file named app.py: an app called 'app' created by Flask in app.py.
    Could not view the file on Heroku. Troubleshooting is in progress.

    DOCKERIZATION:
        Dcoker app will create an image of all of the configuration and create a container which can be run in os or push to a deployment site like Heroku.
        
        1. Create a Dockerfile in the folder.
        2. Give 6 commands, FROM, COPY, WORKDIR, RUN, EXPOSE, and CMD

        FROM python:3.7 
                // On Docker Server, which is on linux, my exsitng python 3.7 image will be used for next line of instructions
        COPY . /app    
                 //copy my all offiles from my current location " . " to a new folder, /app ,on Docker server. 
        WORKDIR /app       
                 //make above directory as a working directory.
        RUN pip install -r requirements.txt     
                //will run my requirements.txt to install all of the lib in a new cotainer.
        EXPOSE $PORT                            
                // Expose a PORT in a  docker conatiner which will eventually be binded to a local IP whereever this app will be launched like at Heroku.
        RUN gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app   
            //gunicorn will help deploy on Heroku and distrobutes the requestes among 4 procersses and bind it to $PORT and open 'app' file and run 'app' app.
            //'bind' The $PORT that we have expose in a container will be binded to a local IP address of wherever this app is lauched.

    Github Action:
        Configure Github action with values taken form Heroku.
        Create Two folders, 1. .github\workflows and inside create main.yaml file.
        In main.yaml copy the code from 
            https://github.com/krishnaik06/bostonhousepricing/blob/main/.github/workflows/main.yaml.
        In main.yaml has three secrets (API name, email, and api key) which will receive the values from Heroku via github files scerets.
         1.  email: ${{ secrets.HEROKU_EMAIL }}
         2.  heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
                # Heroku API key associated with provided user's email.
                # Api Key is available under your Heroku account settings ? API Key ? reveal
        3.   heroku_app_name: ${{ secrets.HEROKU_APP_NAME }}
                # Name of the heroku application to which the build is to be sent.
          
        Get above info from Heroku and provide in github:
        Github > repo  > setigns > Secrets and variables > Actions > new repository secrets.
       
    With Github Action app will be deployed to Heroku automatically.
            




