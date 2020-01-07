# ConfHub back-end

#### Requirements

Python 3.6 or above

## Running the app server

After cloning/pulling from the repo and changing into the directory,

- run `pip install -r requirements.txt`
- run `flask db upgrade`
- run `flask run`

This will start the app server on localhost:5000. Unless pulling new changes,
the server can be subsequently be started by just running `flask run`

### Connecting to the dataset

This only needs to be done when running the app server for the first time. 

Open a new terminal and cd into the repo directory and:

- run `python configure.py` (while the app server is 
running by following the previous section)

## Running the front-end server
Change into "frontend" directory and run
`python -m http.server`

**The app will start running on localhost:8000 and this will be the sole
interface for users to directly interact with the app.**
 
