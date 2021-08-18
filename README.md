# magic-portfolio
magic-portfolio is a POC focused in explore and make a straightforward API with new flask 2.0 and consume third parties services like twitter API.

# Little Demo
https://user-images.githubusercontent.com/4467437/129903678-cd4827e0-acd2-466b-9d7b-3dc9498665f2.mp4



# Fron-end Layer
For create the front-end I used Vue.js and for UI component infrastructure Material Desing and another guidelines.

# Back-end and Service Layer
- Framework for API: Flask 2.0
- Tests with unittest for python
- ORM with SQLAlchemy

# Documentation
- You can find a postman collection and YAML in Docs folder

# How to run the API
First of all we need to create a virtual environment to our flask project, go to api_magic_portfolio folder in your terminal and execute.
  ```
  python3 -m venv
  ```
  Note: make sure you have installed python 3.9 or above
  
After that we gonna need activate our new environment:
  - on windows:
  ```
  .\venv\Scripts\activate
  ```
  - for linux distributions:
  ```
  source venv/bin/activate
  ```

Install all dependencies with:
  ```
  pip install requirements.txt
  ```

Get your API up and running with:
  ```
  python runserve.py
  ```


Use the postman collection or swagger documentation to test the different available endpoints.
![postman_example](https://user-images.githubusercontent.com/4467437/129902618-728c3850-cd45-437b-b9d8-78c0410dedb6.png)


# How to run the Vue Front-End
Go to front_magic_portfolio\magic-portfolio and download the necessary dependencies with:
  ```
  npm install
  ```
  Note: make sure you have installed node 11.2.0 or above

After that you just need to run the front-end application with:
  ```
  npm run serve
  ```

# Future improvements
- Add central log register for tracking the errors and make troubleshooting application problems easily solved.
- Add tokens to the API and management components.
- Change default port, because port 5000 its not recomended for production.
- Verify CORS politics in clients calls to the API.
- Python script to automatically run npm run serve command to generate single page integrated with flask in a blueprint.
- Add Atomic Design to the front-end components.

# Time invested
- 18 hours

# Notes:
- Feel in complete confidence to contribute to this project :)
