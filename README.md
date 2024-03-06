
<h1 align="center"> Vending Machine Fastapi </h2>


## Features

- [x] CRUD for users (POST shouldn’t require authentication)
- [x] CRUD for a product model 
- [x] Deposit endpoint so users with a `buyer` role 
- [x]  Buy endpoint (accepts productId, amount of products) so users with a `buyer` role can buy products with the money they’ve deposited.
- [x] Reset endpoint so users with a `buyer` role can reset their depos
- [x] Unit Testing with PyTest
- [x] Database Connection Using SQLAlchemy

<br>

## Dependencies

- Python 3.7+
- Pip
- Other listed in requirements.txt

## Running

- Clone the repo using

```bash
git clone git@github.com:siddythings/vending-machine-fastapi.git
```

- Create a Virtual Environment using

```bash
sudo pip install virtualenv
virtualenv env
```

- Activate the virtualenv

```bash
env\Scripts\activate # for windows
source env/bin/activate # for linux and mac
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Setting up environment variables

| Key     | Value |
| ----------- | ----------- |
| DATABASE_URL   | postgresql://user:password@host:port/db|

- To run the project

```bash
uvicorn main:app
```

- To run in docker

```bash
docker compose up --build
```

- To run Test cases

```bash
python run_test.py
```