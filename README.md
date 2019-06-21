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
  <li>Install the dependencies on requirements-dev.txt with:
    <ul>
      <li>"$ pip3 install -r requirements-dev.txt"</li>
    </ul>
    You may need to update your pip to 19.0.3 in order for it to install correctly. You may do it with:
    <ul>
      <li>"$ pip install -U pip" or something similar (We want to update pip3)</li>
    </ul>
    With the command above you may get an warning "Cache entry deserialization failed, entry ignored". Don't know what it is and why it happens, but it seems it can be fixed by, instead of using pip to upgrade itself, updating it by this link/command:
    <ul>
      <li>"$ curl https://bootstrap.pypa.io/get-pip.py | python3" </li>
    </ul>
    All dependencies must be installed with pip3 (python 3.6.x+).
  </li>
  <li>Run these commands:
    <ul>
      <li>"$ python3 manage.py makemigrations"</li>
      <li>"$ python3 manage.py migrate"</li>
      <li>"$ python3 manage.py runserver"</li>
    </ul>
    Now, the terminal should tell you where the local server was setted up (localhost:8000/ by default). 
    If you get any trouble with css, images, javascript or any other static file, try running:
    <ul>
      <li> "$ python3 manage.py collectstatic" </li>
    </ul>
    These kind of problem is caused because Django uses different approaches to handle static files in development and deployment servers and, since we are using both (the project is beeing served in freel-project.herokuapp.com), it gets confusing sometimes. Anyway, it should work if the tutorial was followed correctly.
  </li>  
</ol>
