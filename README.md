# hello_flask

- [about](#about)
  - [differences from tutorial](#differences-from-tutorial)
- [getting up](#getting-up)

## about
This project is based on the official [flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/) for flask 1.1.x

### differences from tutorial
* mongodb database, instead of sqllite
* dockerized architecture

## getting up

```shell
$ docker-compose up
```

Now you should be able to access two things:

| application                                                     | domain                |
| :-------------------------------------------------------------- | :-------------------- |
| Blog                                                            | http://127.0.0.1:8080 |
| [mongo-express](https://github.com/mongo-express/mongo-express) | http://127.0.0.1:8081 |
