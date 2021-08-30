## Requirements:

* Microsoft Azure account with an active subscription
* Python 3,6+
* Azure CLI

## How to deploy the app using Azure App Service and Postgre SQL

1. Log in via Azure CLI:\
`az login`

2. Clone the repository:\
`git clone https://github.com/anthonybartczak/djangomailer`

3. Inside the `mailer` folder add a `mailguncreds.py` file and its contents:

    ```python
    MAILGUN_API_KEY = "<key>"
    MAILGUN_BASE_URL = "https://api.mailgun.net/v3/<domain>"
    ```

    This can be replaced with Azure ENV variables.

4. Open your terminal in the designated folder and run the following command:\
    `az postgres up --resource-group mailgunres --location westeurope --sku-name B_Gen5_1 --server-name mailgunapp --database-name mailgundb --admin-user <user> --admin-password <password> --ssl-enforcement Enabled --storage-size 5120`

5. Add Azure Cache for Redis to your resource group and add the `REDIS_KEY` in your `settings.py` file.

6. Run the following commands:

    `az webapp up --resource-group mailgunres --location westeurope --plan mailgunplan --sku F1 --name mailgunapp`

    `az webapp config appsettings set --settings DBHOST="mailgunapp" DBNAME="mailgundb" DBUSER="<user>" DBPASS="<password>"`

7. Wait for the job to finish - you should receive the generated JSON response

8. Connect to your app's SSH:\
```https://<app-name>.scm.azurewebsites.net/webssh/host```

7. Run the following commands:
    ```python
    # Change to the app folder
    cd  $APP_PATH

    # Activate the venv
    source /antenv/bin/activate

    # Install requirements
    pip install -r requirements.txt

    # Run database migrations
    python manage.py migrate

    # Create the super user (follow prompts)
    python manage.py createsuperuser

    # Collect static files
    python manage.py collectstatic

    # Set up a Celery worker and a beat
    celery -A azuresite worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

    celery -A azuresite beat -l info
    ```

8. The app is ready to go