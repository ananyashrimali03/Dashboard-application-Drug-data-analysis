Our webapp now has been deployed at: http://18.118.103.225:8501! (Expires June 2025)

Our Demo video: https://youtu.be/n5SN8jQGWzs

We have done our best to test our web app. If you encounter any issues, please feel free to contact us. We will respond to you promptly :)

Review Assignment Due Date

CMU Interactive Data Science Final Project
Team members:
Contact person: aslabaki@andrew.cmu.edu
yw7@andrew.cmu.edu
ashrimal@andrew.cmu.edu
epetry@andrew.cmu.edu
Work distribution
Yuchen Wang (yw7)

In charge of all content and implementation for Page 3 (Crime Maps Page)
Responsible for the Docker container/image setup and environment configuration
Deployed the web application
Ananya Shrimali (ashrimal)

In charge of all content and implementation for Page 1 (Playground Page)
Responsible for the basic design of the layouts (using Figma posted in the STEP 2: Sketches section)
Enora Petry (epetry)

In charge of all content and implementation for Page 4 (Weather & Crime)
Responsible for exporting the weather data.
Alexandra Slabakis (aslabaki)

Responsible for content and visualization development for Page 2: General History
Built initial data sketches to explore possible weather and crime trends.
Managing team coordination, including meeting scheduling and agenda setting.
Proposal
 A completed proposal. Each student should submit the URL that points to this file in their github repo on Canvas.
Sketches
 Develop sketches/prototype of your project.
Final deliverables
 All code for the project should be in the repo.
 A detailed project report. Each student should submit the URL that points to this file in their github repo on Canvas.
 A 5 minute video demonstration. Upload the video to this github repo and link to it from your report.
How to run
Vscode
Download Docker Desktop from https://www.docker.com/get-started/
Install Dev Container extension in your Vscode
cd to the project root directory and run
docker-compose build
Press Ctrl + Shift + P. Type > Dev Containers: Reopen in Container. Press Enter. (Or you can just click the pop-ups to reopen in container)
If you are going to install more python packages, make sure to involve them into requirements.txt. For example you want to install Scikit-learn and Pytest, the requirements.txt should look like this:
scikit-learn
pytest
Terminal
docker compose up -d --build # build the image and start the container
docker exec -it datascience-dev bash # get into the container
docker compose down # stop the container
Project Structure
.devcontainer/: For VScode Dev Container
data_analysis/: Exploratory Data Analysis scripts
exploratory_data_analysis.ipynb: The EDA script for step_2 (Sketches)
data_clean/: Scripts to clean data, train models, etc.
images/: Images for docs (i.e., Proposal.md, README.md)
model/: Trained models. (i.e., serve for prediction purpose)
pages/: Streamlit pages
1_Playground_Page.py: Dashboard showing basic information of the two datasets.
2_General_History.py: General History with timeline
Trends what's coming down & coming up
A area chart with the frequency of the most frequent crimes
3_Crime_Maps.py
A prediction system to predict the system level based on past crime data
A navigation system that can provide the safer path based on current predicted safety levels.
4_Weather_And_Crime.py
Detailed filters
Season maps - crime by winter/spring/summer/fall
Pattern of prominent crime locations during weather?
Ie: snowing a lot = lots of robberies in shadyside
Trends of particular crimes - top 10 crimes
tests/: Unit testing scripts
utils/
path.py: get specified path from the root directory of this project.
prediction.py: predict the safety level based on the given inputs (for page3).
data.py: get dataframe/geodataframe of the cleaned data.
navigation_map.py: key components of the Page_3.
Dashboard.py: a dashboard page. The Starting point to run the project.
docker-compose.yml: docker-compose.yml
Dockerfile: Dockerfile
requirement.txt: list of python packages to set the container
