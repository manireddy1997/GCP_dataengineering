# Data Build Tool
## _Docker image setup_


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

The following setps helps you to build docker image with DBT framework.


## Features

- Environment independent
- light weight
- Portable


DBT is a python framework which enables you to create ELT/ETL pipelines with ease and comfort

> Follow the below Instructions
> to create docker image with necessary models 
>

## Installation

It's better to create virtual environment and install all the packages
For Official documentation [DBT docs](https://docs.getdbt.com/).

Download the repository and execute following commands

```sh
docker build -t dbt_de:latest .
```

Wait for the image to be created and then execute following commands

```sh
docker image ls
docker container run -it <image_id> /bin/bash
```