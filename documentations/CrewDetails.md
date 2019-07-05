## **CrewDetails.py**
---

- **URL**

  _/api/v1/crewdetails/<film_id>_

- **Method: Type of the request**

  `GET`

- **URL Params**

  _crew_id. An integer represent the ID of a director in our DB_

- **Data Params**

  _a simple integer_

- **Success Response:**

  - **Code:** 1 <br />
    **Message** "OK"  
    **Content:** `{ 'id': ,
                    'name' : ,
                    'bio' : ,
                    'image' :
                    }`

- **Error Response:**

  - **Code:** 0 <br />
    **Message** "KO"  
    **Content:** `None`
  OR
  - **Code:** 0 <br />
    **Message** "Le réalisateur n'existe pas"  
    **Content:** `None`

- **Sample Call:**

  _51.75.141.254/api/v1/crewdetails/18  
  And you will get all the informations about Quentin Tarantino_
