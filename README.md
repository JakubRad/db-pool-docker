Task 3 APP
==========

### Authors:
* Jakub Radziwoniuk <kubaradziwoniuk@gmail.com>;

### Pre-requirements:
.env:
```bash
POSTGRES_USER=kuba
POSTGRES_PASSWORD=Kuba1234
POSTGRES_DB=kuba_db

Also, remember about running:

"git fetch && git pull" 

to get always latest repository data.
```

### Installing local environment:
```bash
mkdir Task3

cd Task3

virtualenv -p python3.11 env

# get repository
git clone git@github.com:JakubRad/db-pool-docker.git src

. env/bin/activate

pip install -r requirements.txt

cd src

# here start working with project
...
```

### Running Docker app:
```bash
./run_docker.sh
```

### Dump database (postgres):
```bash
docker exec -t task_3_app_network-postgres-1 pg_dumpall --column-inserts -a -O -U kuba | gzip -9 > kuba_db_dump_$(date +%Y-%m-%d_%H_%M_%S).sql.gz
```

### Enter running database container:
```bash
docker exec -it task_3_app_network-postgres-1 psql -U kuba -d kuba_db
```

example:

```postgresql
psql (15.1 (Debian 15.1-1.pgdg110+1))
Type "help" for help.

kuba_db=# SELECT * FROM users;
 user_id |           email           | first_name |  last_name  |          dw_date
---------+---------------------------+------------+-------------+----------------------------
       1 | kubaradziwoniuk@gmail.com | Jakub      | Radziwoniuk | 2023-01-26 14:39:28.457689
(1 row)

kuba_db=#
```

if you want to dump data into CSV:
```postgresql
kuba_db=# \COPY (SELECT * FROM users) TO '/tmp/users.csv' DELIMITER ',' CSV HEADER;
```

then:
```bash
docker exec -it task_3_app_network-postgres-1
```

```bash
cd /tmp
```

```bash
ls
```

```bash
root@66f6aa346a76:/tmp# head users.csv
user_id,email,first_name,last_name,dw_date
1,kubaradziwoniuk@gmail.com,Jakub,Radziwoniuk,2023-01-31 16:29:56.392441
9322,nsmith@example.net,Adam,Newman,2023-01-31 16:30:02.175871
8834,hawkinsgregory@example.com,Tonya,Malone,2023-01-31 16:30:02.175871
899,wendy94@example.net,Janet,Wyatt,2023-01-31 16:30:02.175871
1828,idawson@example.net,Tyler,Brown,2023-01-31 16:30:02.175871
4691,lowerachel@example.net,Angela,Washington,2023-01-31 16:30:02.175871
6375,john46@example.org,Marilyn,Frazier,2023-01-31 16:30:02.175871
6647,ginagraham@example.net,Kelly,Baker,2023-01-31 16:30:02.175871
8226,james78@example.com,Jacob,Robles,2023-01-31 16:30:02.175871
```

if you want to copy this file to your local machine:
```bash
docker cp task_3_app_network-postgres-1:/tmp/users.csv /path/to/local/
```
