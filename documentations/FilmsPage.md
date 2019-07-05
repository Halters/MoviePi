## **FilmsPage.py**
---

- **URL**

  _/api/v1/films/page/<page>_

- **Method: Type of the request**

  `GET`

- **URL Params**

  _film_id. An integer represent the page of our film's table (refer to the DB diagram)_

- **Data Params**

  _a simple integer_

- **Success Response:**

  - **Code:** 1 <br />
    **Message** "OK"  
    **Content:** `{
                    "data": [
                        {
                            "id": ,
                            "id_tmdb": ,
                            "title": ,
                            "release_date": ,
                            "overview":,
                            "adult": ,
                            "rating":,
                            "image": 
                        }
                    ]
                    }`

- **Error Response:**

  - **Code:** 0 <br />
    **Message** "Pas de film trouvé à l'id demandé"  
    **Content:** `None`

- **Sample Call:**

  _51.75.141.254/api/v1/films/12  
  And you will get all the informations about the movie "Groom Service"_
