@ECHO OFF 
cloud_sql_proxy.exe -instances="cloud-sql-237317:europe-west1:database"=tcp:3306 &