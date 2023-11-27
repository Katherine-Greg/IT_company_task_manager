# IT_Company_task_manager 


## About
It is a Task Manager, which will handle all possible problems during product development in your team. Everyone from the team can create Task and assign this Task to team-members.


## Check it out!
[Task List Project deployed to Render](https://task-manager-ohh7.onrender.com)

## DB Structure
![DB_Structure.jpg](screenshots%2FDB_Structure.jpg)

## Features
- **Create tasks:** Team members can create tasks with deadlines and detailed descriptions.
- **Assign tasks:** Assign tasks to specific team members based on their positions and types of tasks.
- **Update tasks:** Update tasks status, descriptions or add new members to the team.

## Requirements
- Clone the repository:
```
https://github.com/Katherine-Greg/IT_company_task_manager.git
```
- If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
- Apply database migrations:
```
python manage.py makemigrations
python manage.py migrate
```
- Use the following command to load prepared data from fixture to test and debug your code:
```
python manage.py loaddata data.json
```

- After loading data from fixture you can use following superuser (or create another one by yourself):
    - Login: `admin`
    - Password: `Qwert135` 



- Start the development server:
```
python manage.py runserver
```
Feel free to add more data using admin panel, if needed.

Run server, open `http://127.0.0.1:8000/`, check if everything is displayed correctly.


## How to Contribute

- Create a branch for the solution and switch on it:
```
git checkout -b develop
```

Feel free to add more data, and implement new methods and features!

- Save the solution:
```
git commit -am 'Solution'
```
- Push the solution to the repo:
```
git push origin develop
```
- If you created another branch (not develop) use its name instead


Create `New Pull Request`: 
- Go to the original repository on GitHub and click on the `New Pull Request`.
- Provide details about your changes and submit the pull request for review.


## DEMO
![main_page.jpg](screenshots%2Fmain_page.jpg)

![task_list_page.jpg](screenshots%2Ftask_list_page.jpg)

![task_detail_page.jpg](screenshots%2Ftask_detail_page.jpg)

![create_task_page.jpg](screenshots%2Fcreate_task_page.jpg)

![workers_list_page.jpg](screenshots%2Fworkers_list_page.jpg)

![workers_detail_page.jpg](screenshots%2Fworkers_detail_page.jpg)

![positios_list_page.jpg](screenshots%2Fpositios_list_page.jpg)

![positions_detail_page.jpg](screenshots%2Fpositions_detail_page.jpg)

![positions_create_page.jpg](screenshots%2Fpositions_create_page.jpg)