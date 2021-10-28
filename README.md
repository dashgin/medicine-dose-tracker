# DevProjects - Medicine dose tracker web app

This is an open source project from [DevProjects](http://www.codementor.io/projects). Feedback and questions are
welcome!
Find the project requirements
here: [Medicine dose tracker web app ](https://www.codementor.io/projects/web/medicine-dose-tracker-b6evlas194)

## Tech/framework used

Built with Django 3.2 and Poetry(package management tool)

[comment]: <> (## Screenshots and demo)

[comment]: <> (Screenshots of your app and/or a link to your live demo)

## Installation

<pre><code>
git clone https://github.com/dashgin/medicine-dose-tracker.git
<br>cd medicine-dose-tracker
<br>poetry install
</code></pre>
after installing all requirements try to run:
<pre><code>
python manage.py migrate && python manage.py createsuperuser <br>
python manage.py runserver
</code></pre>

## For future
<ul>
<li>Make cron job or service to send email or text reminders to the user to take the medicine at the right time.</li>
<li>Make api for project</li>
<li>Make push notifications for remind to the user to take the medicine at the right time.</li>
<li>Re make frontend using react or flutter</li>
<li>Make Mobile application using flutter</li>
</ul>

##License
[MIT](https://choosealicense.com/licenses/mit/)
