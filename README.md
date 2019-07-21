# hello_flask

- [about](#about)
- [getting started](#getting-started)
  - [setup](#setup)
  - [run server](#run-server)

## about
This project is based on the official [flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/) for flask 1.1.x

## getting started

### setup
First you need set the project environment _(virtual environment, secret key, database)_ up, by calling:
```shell
$ make setup
```

> **! Note:**   
> Because `make key` (which is part of `make setup`) sometimes fails, please check that the file `env/var/flaskr-instance/config.py` structure-wise looks like:
> ```python
> SECRET_KEY = \
>     b'\xdfu\xc0\x98\x97\xf3\xee\xeb\xcbU\x14\x8cmS\x86\x96'
> ```
> If not run `make setup` again.

### run server
Noe you can start the server in your local network with:
```shell
$ make run
```