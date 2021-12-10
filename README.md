## Rasa Chatbot Playground - A Custom Action Development Environment for IXO Assistant

Rasa Chatbot Playground for Custom Action Development Environment for IXO Assistant to help developers who want to develop custom actions for the IXO assistant through an easy to use playground.
<div style="text-align: center;">
<img src="voff.gif"  width="700"> </img>
</div>

[Here](https://www.youtube.com/watch?v=VcbfcsjBBIg) is a great tutorial on how to create and configure custom actions with a sample 
[repo](https://github.com/RasaHQ/conversational-ai-course-3.x) to illustrate all the required steps.

### Step-wise Installation Guide:
#### 1. Clone Repo:
`git clone repo_url`

#### 2. Create a virtual environment (strongly recommended)
   ##### Ubuntu/macOS
   Create a new virtual environment by choosing a Python interpreter and making a ./venv directory to hold it:
   
    $ python3 -m venv --system-site-packages ./venv

   Activate the virtual environment:
   
    $ source ./venv/bin/activate

  ##### Windows:
   Create a new virtual environment by choosing a Python interpreter and making a .\venv directory to hold it:
   
    python3 -m venv --system-site-packages ./venv
   
   Activate the virtual environment:
   
    .\venv\Scripts\activate

   You can also create an environment using anaconda navigator. For more information, refer to the documentation in the link.
   https://docs.anaconda.com/anaconda/navigator/getting-started/ 

#### 3. Run Docker Images
`cd repo_folder_name`

`docker-compose up`

The following docker containers will be started:
1. rasa open source server - Rasa open source server running on `http://localhost:5005`
2. rasa action server - Rasa action server running on `http://localhost:5055`
3. custom chat bot web interface - Access the web chat bot by going to `http://localhost:5000/`
4. jupyter notebook server - Access the Jupyter Notebook by going to `http://localhost:8888/`

### Training and running the bot:

Once the docker images are running, run the following commands.
1) Log into Rasa Open Source server docker images shell
        
       docker ps - Fetch containerid for the rasa server 
       docker exec -ti <containerid> /bin/bash
       

3) To train:
      
       rasa train
 
4) Restart docker images:
     
       docker-compose build;docker-compose up
 
Now your bot is running and you can give input messages.
 

#### 4) Now open the webpage and the bot widget should be present and working.

`http://localhost:5000/`

================================================================
 




