# PBD INTERNATIONAL CLASS MIDTERM PROJECT

## A Proceeding Conference App

### GROUP 3

1. Syafiqo Arashy Octaviano - 2106657821
2. Nafis Azizi Riza - 2106658843
3. Ammar Ash-Shiddiq - 2106656560
4. Azra Batrisyia Hisman - 2106656592
5. Matthew Rizky Hartadi - 2106720941
6. Theirry Nicole Panggabean - 2106721004


### LINK TO DEPLOYED WEBSITE

[Midterm Project](https://midterm-project-group3ki.herokuapp.com/)


### DESCRIPTION

The app that will be developed is a digital proceeding app for an academic conference. The app will display the information about the conference, such as the schedules, submitted papers, events, speakers, authors and room assignments. There is no need to define any authorization roles (e.g. admin, participant, etc.), meaning anyone can read the information without logging in. The app also has high interactivity, in which the modules are linked to one another. This means that users can easily access any other relevant modules from their current one (e.g. access speakers from events).


### LIST OF MODULES AND FEATURES

#### LANDING PAGE

The website will have a landing page module. The landing page module will be the first thing the user will see when they visit the website. It should contain enough information and features that’ll get them familiar with the website.

These features consist of:
- Navbar
    1. The functionality of the navbar is to make users navigate easier between pages/sections on the website 
    2. When the user clicks on a page name on the navbar, it’ll redirect them to each respective page
    3. The navbar should always be visible and usable wherever the user goes around the website
    4. Includes access to Authors page, Submissions page, along with others.
- A Hero Section
    1. The hero section will display an image/illustration to let the users know what Conference Event the website Is dedicated to
- Event Section
    1. A brief overview of the event
    2. A button will be used as a CTA(Call-To-Action) for the user to redirect them to the Events Page
- Speakers Section
    1. A button will be used as a CTA(Call-To-Action) for the user to redirect them to the Speakers Page
- Sessions Section
    1. A button will be used as a CTA(Call-To-Action) for the user to redirect them to the Sessions Page
- Venue Map
    1. the Venue Map section will provide a full map of the Conference Event venue.
    2. This will be implemented in hopes that users that are participating in the venue will have a visual representation of what the venue might be.
- Footer and Sponsors
    1. Located at the bottom of the page, this footer contains details regarding the Conference Event and its sponsors


#### EVENTS PAGE

The events module keeps track of the rundown schedule. This means for each event, the start and end time is recorded as well as its program title, relevant speakers and location. The user is able to interact with certain events. For example, if the event is a parallel session, the user is able to access the parallel sessions page to find out more about said event. On the other hand, if it is a plenary session with a speaker, users are able to interact with the event and find further information on the speaker.

Overall, the data available is:
- Event Id
- Date (Displayed to user): The data is sorted by date. Users can interact by selecting which date they want to look at more closely, and only the sessions available on that day will be shown.
- Start Time
- End Time
- Time (Displayed to user): The start and end times are not shown individually to the user. Instead, it is shown in full.
- Program (Displayed to user): The title of the session
- Speaker (Displayed to user): May be null. Only applies to keynote lectures.
- Place (Displayed to user): Displays the location of the event.
- Is Parallel (Displayed to user): Parallel sessions are listed for users. Although the Boolean value of isParallel itself is not shown to users, they are able to identify which sessions are parallel and which are not, as interacting with the parallel sessions will also lead to the parallel sessions page.
- Is Child: This Boolean value is not explicitly shown to the users, and is mostly used for sorting. This value simply refers to the fact that the event is, in fact, running in parallel.

To implement these features, there would likely need to be a way to implement a sort of table to organize the events, and a filter (e.g. date, subject) to allow ease of access for the users.

URL routing would also need to be implemented towards Speakers and Events, given the user clicks on a certain event.

To conclude, the events module will have its own page where the rundowns are filtered as required by the users, but it will also have interactivity that will lead to sessions and speakers.


#### SPEAKERS PAGE

In the Speakers module, the web will display a list of **speakers** for the events. It is divided into Plenary Speakers and Keynote Speakers. The page will display a picture of the speaker, the same details as the previous part, sessions they will be speaking at (including, date, time, and session name), and an abstract of the topic each speakers are bringing up.

The data displayed would include:
1. Name
2. Respective universities
3. Country of origin

From there, users would be able to see the **session details** of each speaker by clicking the provided arrow in each speakers section.

The data displayed would include:
1. Speakers Profile:
    1. A photo of the speaker
    2. Respective universities
    3. Country of Origin
2. Sessions
    1. Type of speakers (Plenary/Keynote)
    2. Session title/topic
    3. Date and time of session
    4. Location
3. Abstract (an explanation of the topic)


#### SESSIONS PAGE

In the sessions module, the web page will display information about the topics that will be in session in the event. In each of these topics, there will be all the submitted papers related to that topic grouped based on their date of presentation. Each paper contains information about the author, presentation time and also the abstract of the paper. 

The data that will be displayed are:
- Paper id
- Room number
- Session of presentation of the day
- Topics of the paper (displayed to user)
- Submitted paper title (displayed to user)
- The author (displayed to user)
- Date of presentation (displayed to user)
- Time of presentation (displayed to user)
- Location of presentation (displayed to user)
- Start time of presentation (displayed to user)
- End time of presentation (displayed to user)

The data that would be displayed in:
1. Parallel Sessions : 
    1. Topics of the paper
2. Sessions:
    1. Submitted paper title
    2. Author of paper
3. Paper detail:
    1. Paper title
    2. Author
    3. Abstract of paper


#### AUTHORS PAGE

Authors will show a list of alphabetically ordered author names and also a search bar. When the user clicks on the name of the authors, it'll go to the author details page which will show:
1. Author Section
    - Name and Department
2. Submission Section
    - The submission name
    - Details about the zoom meeting
    - Clickable “view details” that will go to Paper Details Page
    
In the paper details page, User can view the Title of the paper and below it are all the contributor(s), the time of the meeting, and also the link. It will also provide the Abstract section where there'll be the background of the paper.


#### SUBMISSIONS PAGE

In the submission modules, the web will display the submitted papers by the authors. The data that will be displayed are:
- Tracks : which category does the paper included into (such as, SCE for Sustainable and Clean Energy, and etc.)
- Submission Title
- Authors
- Submission date
- Last Update date
- Keywords
- Abstract
- Location of the session
- Date and time of the session
- and the chair of the session

To be more interactive, when the user click on the authors, it will be redirected to the author page for the details information.


### INSTRUCTIONS

#### BUILD

The first step in building the app is creating a Django project. Before making the project, a virtual environment should be activated. Once activated, install the required dependencies.

```bash
python -m venv env

# Windows:
env\Scripts\activate.bat
# Unix-based OS (Linux, MacOS):
source ./env/bin/activate

pip install -r requirements.txt
```

The dependencies name that needs to be installed:

- django
- gunicorn
- whitenoise
- psycopg2-binary
- requests
- urllib3

Use the following command to save the dependencies list.

```bash
pip freeze > requirements.txt
```

Once done, create a Django project with the following command:

```bash
django-admin startproject <PROJECT_NAME>
```

Once a project has been initialized, create an app within the project.

```bash
python manage.py startapp <APP_NAME>
```


#### RUN

To run the app locally, use the following code. However, ensure that the virtual environment is up and running beforehand.

```bash
python manage.py runserver
```

Access the app through http://localhost:8000


#### DEPLOY

Create a Procfile with the following script:

```bash
web: gunicorn django_project.wsgi --log-file -
```

Create a new dpl.yml file in the .github/workflows folder

```bash
name: Deploy

on:
  push:
    branches-ignore:
      - template
  pull_request:
    branches-ignore:
      - template

jobs:
  Deployment:
    runs-on: ubuntu-latest
    env:
      HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
      HEROKU_APP_NAME: ${{ secrets.HEROKU_APP_NAME }}
    steps:
    - uses: actions/checkout@v2
    - name: Set up Ruby 2.7
      uses: actions/setup-ruby@v1
      with:
        ruby-version: 2.7
    - name: Install dpl
      run: gem install dpl
    - name: Install Heroku CLI
      run: wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
    - name: Deploy to Heroku
      run: dpl --provider=heroku --app=$HEROKU_APP_NAME --api-key=$HEROKU_API_KEY
    - name: Run migrations on Heroku
      run: heroku run --app $HEROKU_APP_NAME migrate
    - uses: chrnorm/deployment-action@releases/v1
      name: Create GitHub deployment
      with:
        initial_status: success
        token: ${{ github.token }}
        target_url: https://${{ secrets.HEROKU_APP_NAME }}.herokuapp.com
        environment: production
```

Add the following code to settings.py

```python
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

ALLOWED_HOSTS = ["*"]

MIDDLEWARE = [
    ...,
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```

Copy the API Key from Heroku and write the following in Github Secrets-Actions

```bash
(NAME)HEROKU_APP_NAME
(VALUE)MY-APPLICATION
```

The app is now deployed!
