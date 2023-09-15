# HNGx Stage 2

The API has been hosted [here](https://hngx-stage2.onrender.com/api)

## UML Diagram for the Project

![UML diagram](https://github.com/1dgidi/hngx_step2/blob/documentation/resource/uml.png)

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

## Request and Response Format
### Create a **person**
**Endpoint:** `/api/`

**Method:** `POST`

**Request:**
```http
POST /api/
Content-Type: application/json

{
  "name": <person_name>
}
```
**Response**
```json
{
    "name": <person_name>,
    "id": <person_id>
}
```

### Retrieve a person's details
**Endpoint:** `/api/:person_id`

**Method:** `GET`

**Request:**
```http
GET /api/:person_id
```
**Response**
```json
{
    "name": <person_name>,
    "id": <person_id>
}
```

### Update a person's details
**Endpoint:** `/api/`

**Method:** `PUT`

**Request:**
```http
PUT /api/
Content-Type: application/json

{
  "name": <person_name>
  "id": <person_id>
}
```
**Response**
```json
{}
```
### Delete a person
**Endpoint:** `/api/:person_id`

**Method:** `DELETE`

**Request:**
```http
DELETE /api/:person_id
```
**Response**
```json
{}
```

## Example Usage
### Create a person
**Endpoint:** `/api/`

**Method:** `POST`

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

###  Retrieve the details of a person

**Endpoint:** `/api/:person_id`

**Method:** `GET`

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
