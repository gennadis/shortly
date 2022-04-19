# Simple URL Shortener

This REST API service brings long URLs shortening and redirectioning from hashed to original URLs.

## Features
- Long URLs shortening
- Hashed to original URL redirection
- Half-end hash customization
- URLs validation

## Run with `Docker`
1. Clone project
```bash
https://github.com/gennadis/shortly.git
cd shortly
```

2. Build the image
```bash
docker-compose build
```

3. Run the container
```bash
docker-compose up -d
```


## Installation
1. Clone project
```bash
https://github.com/gennadis/shortly.git
cd shortly
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Rename `.env.example` to `.env` fill it accordingly.  

5. Create super user
```bash
python manage.py createsuperuser
```

6. Run migrations
```bash
python manage.py migrate
```

7. Run server
```bash
python manage.py runserver
```

## Examples
- List all URLs stored in database
```bash
GET /v1/urls
```

A successful response will return URLs list
```bash
{
    "count": 42,
    "next": "http://127.0.0.1:8000/v1/urls/?page=2",
    "previous": null,
    "results": [
        {
            "long_url": "https://dev.bitly.com/docs/tutorials/shorten-customize-links",
            "hash": "FZkBvIN",
            "created_at": "2022-03-02T15:06:51.552939Z"
        },
    ...  
```

----

- Shorten long URL
```bash
POST /v1/shorten
{
    "long_url": "http://google.com"
}  
```

A successful response will return the shortened link.
```bash
{
    "long_url": "https://dev.bitly.com/docs/tutorials/shorten-customize-links",
    "short_url": "127.0.0.1:8000/FZkBvIN"
}
```

----

- Redirect to original URL
```bash
GET
http://127.0.0.1:8000/FZkBvIN
```

----

- Get details on shortened URL
```bash
GET /v1/urls/FZkBvIN/
```

A successful response will return the shortened link details
```bash
{
    "long_url": "https://dev.bitly.com/docs/tutorials/shorten-customize-links",
    "hash": "FZkBvIN",
    "created_at": "2022-03-02T15:06:51.552939Z"
}
```

----

- Customize shortened URL half-end
```bash
PATCH /v1/urls/FZkBvIN/
{
    "hash": "custom_hash_here",
}
```

A successful response will return the updated shortened link details
```bash
{
    "long_url": "https://dev.bitly.com/docs/tutorials/shorten-customize-links",
    "hash": "custom_hash_here",
    "created_at": "2022-03-02T15:06:51.552939Z"
}
```

----
