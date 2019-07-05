## **Users Class Documentation**

_Return a json Object contains all the asked informations._

---

**Data Formating**

_{"keyword" : "value}_

---

- **URL**

  _/users_

- **Method: Type of the request**

  `POST`

- **URL Params**

  _None_

- **Data Params**

  {
  username: string,
  lol: int
  }

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `{ id : 12 }`

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in" }`

  OR

  - **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{ error : "Email Invalid" }`

- **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format (\$.ajax call or a curl request) - this makes life easier and more predictable._>