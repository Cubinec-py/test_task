# Test task for ProstoPay company to the position of Backend Python Developer.
## Project init steps
First, need to install project requirements:
```bash
pip install -r requirements.txt
```
For correct working second task need to make .env file with DB parameters:
```dotenv
DATABASE_URL=
TEST_DATABASE_URL=
TOKENS_SECRET_KEY=
```

## Task 1
### Make own HashMap class with get and put methods, write tests for it.
To make and check test:
```bash
cd task_1
```
```bash
coverage run -m unittest 
```
```bash
coverage report
```
Here screenshot with results:

![Снимок экрана 2023-07-12 в 20.31.20.png](images%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-12%20%D0%B2%2020.31.20.png)

For more details can make command down, than go to htmlcov folder and watch results in index.html.
```bash
coverage html
```
## Task 2
### Make User pyndantic model, get_async_session which returns AsyncSession sqlalchemy object to interact with db and write tests for it.
To init project need:
```bash
cd task_2
```
```bash
alembic upgrade head
```

To run project run this command, if need to run with reload, add --reload flag to the end:
```bash
uvicorn main:app
```
To make and check test:
```bash
coverage run -m pytest 
```
```bash
coverage report
```
Here screenshot with results:

![<img src="Снимок экрана 2023-07-12 в 20.41.48.png](images%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-07-12%20%D0%B2%2020.41.48.png)

For more details can make command down, than go to htmlcov folder and watch results in index.html.
```bash
coverage html
```
