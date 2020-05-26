# test
- This project requires the below modules:
  - Python - 3.5.4
  - Django - 1.11.13
 
- Once the project is downloaded from git run the following commands to create a database initlization.
  ```
  - python manage.py makemigrations
  - python mange.py migrate
  ```
  then the table will be created in the database.
- After that run the development server on your local by using below command:
  ```
  python manage.py runserver
  ```
- Then run the api functions on your browser from the below url:
  ```
  http://127.0.0.1:8000
  ```
- I created a API function to insert the data from the particular link. 
  - Run the below API url:
  ```
  http://127.0.0.1:8000/load_data
  ```
### API functions
- Return all records:
  - Sample Url: http://127.0.0.1:8000/all_results
- Get records where open price is grether than the close price in between two dates.
  - This api function will accepts two dates, the date is in the format of dd-mm-yyyy
  - sample URL:http://127.0.0.1:8000/open_price_more_than_close_price/01-10-2018/03-10-2018/

- Average trunover between two input dates.
  - This api function will accepts two dates, the date is in the format of dd-mm-yyyy
  - sample URL:http://127.0.0.1:8000/avg_turnover/01-10-2018/03-10-2018/

- Average change in difference between high and low in any two input dates.
  - This api function will accepts two dates, the date is in the format of dd-mm-yyyy
  - sample URL:http://127.0.0.1:8000/avg_high_low/01-10-2018/03-10-2018/

- Month wise average of the open and close price.
  - This api function will accepts two dates, the date is in the format of dd-mm-yyyy
  - sample URL:http://127.0.0.1:8000/month_high_low_avg/01-10-2018/03-10-2018/


