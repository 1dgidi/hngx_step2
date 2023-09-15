# HNGx Stage 2

## UML Diagram for the Project

![UML diagram](https://avatars0.githubusercontent.com/u/29962968?s=400&u=7753a408ed02e51f88a13a5d11014484bc4d80ee&v=4)

## Installation Guide
* Clone this repository [here](https://github.com/1dgidi/hngx_step2.git).
* The master branch is the most stable branch at any given time, ensure you're working from it.

Run the following command to install all dependencies
```shell
pip install -r requirements.txt
```

## Usage
Run the following command to start the application locally.
```shell
uvicorn main:app --reload
```
Connect to the API using Postman on port 8000.

## Deploy the API on Render
1. You may use this repository directly or [create your own repository from](https://github.com/1dgidi/hngx_step1) if you'd like to customize the code.
2. Create a new Web Service on [Render](https://render.com/).
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:endpoint --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

## API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /api/ | To create a person |
| GET | /api/:person_id | To retrieve the details of a single person |
| PUT | /api/ | To update the details of a person |
| DELETE | /api/:person_id | To delete a person |

## Example Usage
**Endpoint:** `/api/`

**Method:** `POST`

**Description:** Create a **person**

**Request:**
```http
POST /api/
Content-Type: application/json

{
  "name": "Mark Essien"
}
```
**Response**
```json
{
    "name": "Mark Essien",
    "id": 1
}
```

**Endpoint:** `/api/:person_id`

**Method:** `GET`

**Description:** Retrieve the details of a **person**

**Request:**
```http
GET /api/1
```
**Response**
```json
{
    "name": "Mark Essien",
    "id": 1
}
```

## Assumptions
It is assumed that the request body is in the JSON format.

## Technologies Used
* [FastAPI](https://fastapi.tiangolo.com/): It is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
* [SQLite](https://www.sqlite.org/index.html): It is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world.
