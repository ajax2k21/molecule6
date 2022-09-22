## How to Run
## Create A Virtual env (Optional)

~~~
pip install -r requirements.txt
~~~

## navigate( cd ) to the folder containing manage.py file
~~~ 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~
## Test url path
### http://localhost:8000/Molecule/v1.0/LSNSearchAsSDF/

## To Retrieve a particular SDF from LSN Number
~~~
{
  "lsn_arr": ['your LSN number goes here']
}
~~~  

## To Retrieve a particular SDF from LSN (URL)
~~~
type the LSN at the query params
~~~
## Important Note 
### After Cloning this project Update details.json location in your views.py file 
~~~
with open('your directory location where details.json is saved', 'r') as f:
~~~
