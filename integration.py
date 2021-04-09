import subprocess

RESOURCE_GROUP_NAME = str(input('RESOURCE_GROUP_NAME: '))
SERVER_NAME = str(input('SERVER_NAME: '))
DB_NAME = str(input('DB_NAME: '))
ADMIN_USER = str(input('ADMIN_USER: '))
ADMIN_PASSWORD = str(input('ADMIN_PASSWORD: '))
PLAN_NAME = str(input('PLAN_NAME: '))

create_postgre = 'az postgres up --resource-group ' + RESOURCE_GROUP_NAME + \
    ' --location westeurope ' + \
    '--sku-name B_Gen5_1 ' + \
    '--server-name ' + SERVER_NAME + \
    ' --database-name ' + DB_NAME + \
    ' --admin-user ' + ADMIN_USER + \
    ' --admin-password ' + ADMIN_PASSWORD + \
    ' --ssl-enforcement Enabled --storage-size 5120'

create_webapp = 'az webapp up --resource-group ' + RESOURCE_GROUP_NAME + \
    ' --location westeurope ' + \
    '--plan ' + PLAN_NAME + \
    ' --sku F1 ' + \
    ' --name ' + SERVER_NAME

config_webapp = 'az webapp config appsettings set --settings ' + \
    ' DBHOST="' + SERVER_NAME + '" ' \
    ' DBNAME="' + DB_NAME + '" ' \
    ' DBUSER="' + ADMIN_USER + '" ' \
    ' DBPASS="' + ADMIN_PASSWORD + '" '

create_postgre_output = subprocess.run(create_postgre, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
create_postgre_stdout =  create_postgre_output.stdout.decode("utf-8")

create_webapp_output = subprocess.run(create_webapp, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
create_webapp_stdout =  create_webapp_output.stdout.decode("utf-8")

subprocess.run(config_webapp, shell = True)