

heroku pg:backups:capture



heroku pg:backups:restore '' DATABASE_URL


heroku pg:backups:restore 'https://s3.amazonaws.com/teaching-toolkit/backup_2018_07_08T02_01_08.sql' DATABASE_URL
