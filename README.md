# RESTful Django API

## What is this repository about?

This repository contains a test sent to me from a company. Those are the instructions :

### Applications API

Create a _small RESTful API_ that allows __uploading__ and __listing__ Android
applications. The API should be built with _Django_ and the _Django Rest Framework_.

When uploading an application you should just provide the file and the API
should be able to _extract the “package name” and “package version code” from the
apk file_.

#### Application API

> GET /api/applications/

    [
        {
            "application": "/media/525db2b8-e9c9-46be-8275-b93e285bfecd.apk",
            "package_name": "com.whatsapp",
            "package_version_code": "1234"
        },
        ...
    ]

#### Requirements:

* Use Django and Django REST Framework
* Add an endpoint which allows listing and uploading Android applications (GET and POST)
* When an application is uploaded the metadata of that application should be extracted with __aapt__
* Your code will be versioned with Git. Either provide us your username on GitLab so we can give you write access to the repository or host it on the platform of your choice and give us read access.
* Within a week, provide us with:
    * a working version of the code
    * bonus: run the Django app in a Docker container with docker-compose

## Getting Started

To start the server, make sure _Docker_ and _Docker-Compose_ are installed on your system then use the following command :

> docker-compose up

Then you can access the API through the following url :

> http://localhost:8000/api/applications

The allowed HTTPs requests are : 
* GET : Get a list of applications
* POST : Upload an application to the server

### Application
____
Represents an APK
____

##### Attributes :
* id _(Number)_ *(Read_only)*: unique identifier
* application _(String)_: APK file path
* package_name _(String)_ *(Read_only)*: APK file name
* package_version_code _(String)_ *(Read_only)*: APK version


