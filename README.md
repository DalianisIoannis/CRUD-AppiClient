# CRUD-AppiClient

Let's suppose we have access to a movies database which is accessible through a REST API on a specific URL. My work proxy and my own credentials are not provided. The database holds the following data:
```bash
-Actors-
o Name (string)
o Date of birth (datetime)

-Directors-
o Name (string)
o Date of birth (datetime)

-Movies-
o Name (string)
o Production year (integer)
o Director (linked to Directors endpoint)
o Actors (linked to Actors endpoint)
```

This project implements the exposed REST API. It fully implements the CRUD(create, read, update, delete) for the endpoints.
## Running
```bash
run_terminal.py
```
## Acknowledgments
The README.md file was created based on the model: https://www.makeareadme.com/.

## License
[MIT](https://choosealicense.com/licenses/mit/)

######################################################################
######################################################################
run_terminal and classMovieDB run on terminal
run flask by executing run_flask.py in terminal
then type urls in browser
