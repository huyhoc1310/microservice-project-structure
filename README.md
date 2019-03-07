# Base microservice source code

Project description here...


### Requirements
- OS: Linux
- Python: 3 or above
- Mysql: 5.7.24 or above
- Docker: 18.09 or above
- Docker-compose: 1.23.1 or above


### Configurations
- Remove extension `.org` from `src/configs/`

  ```
  settings.toml.orig
  ```
- Set required environment variables:
  ```
  cp .env.orig .env
  ```

### Enviroment settings
- Install virtualenv
  ```
  pip install virtualenv
  ```
- Create environment
  ```
  virtualenv venv
  ```
- Activate environment
  ```
  . venv/bin/activate
  ```
- Install dependencies
  ```
  make install
  ```

### Database settings
- Update database metadata in `src/configs/settings.toml`
- Create migrations folder
  ```
  make initdb
  ```
- Run migrations
  ```
  make migrate
  ```

### Run applications
  - To start development server
    ```
    make start
    ```
  - To show all available command
    ```
    make help
    ```

### Run docker
```
docker-compose up -d
```
