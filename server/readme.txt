
to initiate a virtual environment

- mac / linux 
python3 -m venv venv

- activate 
source venv/bin/activate

- windows 
python -m venv venv

- activate
.\venv\Scripts\activate


- install requirements if not already installed
pip install -r requirements.txt


- make migrations and migrate after every models.py code change
python manage.py makemigrations
python manage.py migrate


- run server 
python manage.py runserver

- deactivate for both windows and linux and mac 
deactivate

