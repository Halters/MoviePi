## **CrewList.py**
---

- **URL**

  _/api/v1/crewlist/<film_id>_

- **Method: Type of the request**

  `GET`

- **URL Params**

  _film_id. An integer represent the ID of a movie in our DB_

- **Data Params**

  _a simple integer_

- **Success Response:**

  - **Code:** 1 <br />
    **Message** "OK"  
    **Content:** `{ 'id': ,
                    'name' : ,
                    'image' :
                    }`

- **Error Response:**

  - **Code:** 0 <br />
    **Message** "Aucun ID n'es detecté"  
    **Content:** `None`
  OR
  - **Code:** 0 <br />
    **Message** "Le film n'a pas de réalisateur"  
    **Content:** `None`
  OR
  - **Code:** 0 <br />
    **Message** "KO"  
    **Content:** `None`

- **Sample Call:**

  _51.75.141.254/api/v1/crewlist/333  
  And you will get all the informations about Mathieu Kassovitz ("La Haine" 's director)_
