Add a Windows User to a MSSQL Database
======================================

**parts of this script are from [Guish](http://stackoverflow.com/a/30512083)**

To add a user to a Microsoft SQL Database, and have them use Windows Active Directory to login, use the following script. Replace the `@username` and `@database` values on lines 6 and 7 with the appropriate values.

```sql
DECLARE @username AS varchar(50);
DECLARE @database AS varchar(50);
DECLARE @add_user_to_server_script AS varchar(max);
DECLARE @add_user_to_db_script AS varchar(max);

SET @username = 'DOMAIN\username001';
SET @database = 'Test_Database';

SET @add_user_to_server_script = '
    USE [master];
    CREATE LOGIN [{username}] FROM WINDOWS WITH DEFAULT_DATABASE=[master];
'

SET @add_user_to_db_script ='
    USE [{database}];
    CREATE USER [{username}] FOR LOGIN [{username}] WITH DEFAULT_SCHEMA=[dbo];
    USE [{database}];
    ALTER ROLE [db_datareader] ADD MEMBER [{username}];
'

SET @add_user_to_server_script = REPLACE(@add_user_to_server_script, '{username}', @username)
SET @add_user_to_db_script = REPLACE(@add_user_to_db_script, '{username}', @username)
SET @add_user_to_db_script = REPLACE(@add_user_to_db_script, '{database}', @database)

EXECUTE(@add_user_to_server_script)
EXECUTE(@add_user_to_db_script)
```
