# freelance_project
<h3>Welcome to the freelance project!</h3>
<p>This project was developed as the final test for the discipline SCC-504, object-oriented programming.</p>
<p>We were proposed to develop an platform that could connect an enterprise's short work proposal to students. We used some frameworks to accomplish our goal, such as Django (backend) and Tailwind(frontend). At first, we intended to use Django Rest and offer support to android too, but, due to limited time (about a month) and a whole graduation to worry, we sticked to learning base Django and Tailwind (we had basically no knowledge before this project).</p>

<h3>Setting up a local server</h3>
<ol>
  <li>Set up and activate an virtual env:
    <ul>
      <li>"$ python3 -m venv venv" with this, your are setting the name of your venv to "venv"</li>
      <li>"$ source venv/bin/activate"</li>
    </ul>
    Now, your venvname should appear inside parenthesis at the beggining of your command line
  </li>
  <li>Install the dependencies on requirements-dev.txt. You may need to update your pip to 19.0.3 in order for it to install correctly. You may do it with "$ pip3 install -U pip3". All dependencies must be installed with pip3 (python 3.6.x+). The requirements-dev.txt may be installed with "$ pip3 install -r requirements-dev.txt".
  </li>
  <li>Run these commands: "$ python3 manage.py makemigrations" then "$ python3 manage.py migrate" then "$ python3 manage.py runserver"<br>Now, the terminal should tell you where the local server was setted up (localhost:8000/ by default)</li>
</ol>
