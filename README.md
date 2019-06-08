# freelance_project
<h3>Welcome to the freelance project!</h3>
<p>This project was developed as the final test for the discipline SCC-504, object-oriented programming.</p>
<p>We were proposed to develop an platform that could connect an enterprise's short work proposal to students. We used some frameworks to accomplish our goal, such as Django (backend) and Tailwind(frontend). At first, we intended to use Django Rest and offer support to android too, but, due to limited time (about a month) and a whole graduation to worry, we sticked to learning base Django and Tailwind (we had basically no knowledge before this project).</p>

<h3>Setting up a local server</h3>
<ol>
  <li>Set up and activate an virtual env: "$ python3 -m venv venvname" then "$ source /pathtoyourvenv/bin/activate"<br>Now, your venvname should appear inside parenthesis at the beggining of your command line</li>
  <li>Install django and python-decouple: "$ pip3 install Django" then "$ pip3 install python-decouple"</li>
  <li>Check if debug is True at freelance_project/freelance/settings.py, if not, set it to True</li>
  <li>Run these commands: "$ python3 manage.py makemigrations" then "$ python3 manage.py migrate" then "$ python3 manage.py runserver"<br>Now, the terminal should tell you where the local server was setted up (here it is localhost:8000/)</li>
</ol>
