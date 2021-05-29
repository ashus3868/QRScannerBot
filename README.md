# QRScannerBot

To run the above project you need to follow the steps below:

# Step1:
Clone the git repository on to your current directory with the given command,
    git clone https://github.com/ashus3868/QRScannerBot.git
    
# Step 2:
Create a virtual environment on your current project directory and install the requirements.txt,
 # For Linux/Mac:
    cd QRScannerBot
    virtualenv -p python3.8 venv
    source venv/bin/activate
# For Windows
    cd QRScannerBot
    virtualenv -p python3.8 venv
    .\venv\Scripts\activate
    
Now install the dependencies,

    pip install -r requirements.txt
    
# Step 3:
Once, this is done, train the model for rasa and start the rasa server as well as action server if you have it. Also, run the flask application to make your chatbot accessible on website,
# start rasa server and action server parallelly
    rasa train && rasa run -m models --enable-api --cors "*"
and action server on another terminal,

    rasa run actions

# Step 4:
Start the flask application in another terminal,

    python website_app.py
    
# Step 5:
Now generate the QR code for the website and scan it to test it. Before running this script, update the website with the ip address of your system or with the server ip where your flask application is up and running. 

    python main.py
    
# Step 6:
Now the QR code will be generated and stored on your current directory with name "site.png". Now you can scan the QR code and talk to the bot on to the redirected website.



    
