## **ActorDetails.py**
---

- **URL**

  _/api/v1/actordetails/<actor_id>_

- **Method: Type of the request**

  `GET`

- **URL Params**

  _actor_id. An integer represent the ID of the actor in or DB_

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

- **Sample Call:**

  _51.75.141.254/api/v1/actordetails/37  
  And you will get all the informations about Bruce Willis_
