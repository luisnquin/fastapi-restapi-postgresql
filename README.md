# REST API with FastAPI and PostgreSQL

To have the same data in db:
```
create table CLIENT_DATA (id SERIAL PRIMARY KEY, fullname VARCHAR(50) NOT NULL,email VARCHAR(50) NOT NULL,gender VARCHAR(50) NOT NULL, credit_card VARCHAR(50) NOT NULL,credit_type VARCHAR(50) NOT NULL);

insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Christen Klus', 'cklus1g@cisco.com', 'Female', '3552231300758866', 'jcb');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Swen Cromar', 'scromar1h@last.fm', 'Female', '5602240066702948', 'bankcard');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Kurtis Noblett', 'knoblett1i@bandcamp.com', 'Genderfluid', '4903163479056604', 'switch');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Barri Rappport', 'brappport1j@gov.uk', 'Bigender', '502037203744396450', 'maestro');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Corri Walling', 'cwalling1k@github.com', 'Female', '4903465187953065640', 'switch');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Eugenius Zanetto', 'ezanetto1l@booking.com', 'Agender', '30262573266129', 'diners-club-carte-blanche');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Gram Dorian', 'gdorian1m@npr.org', 'Male', '4917468581803114', 'visa-electron');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Mischa Brazil', 'mbrazil1n@discovery.com', 'Genderqueer', '3562803087558541', 'jcb');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Maiga Baff', 'mbaff1o@pinterest.com', 'Polygender', '5458034263519089', 'mastercard');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Arlana Tarpey', 'atarpey1p@edublogs.org', 'Genderfluid', '5002351203212588', 'mastercard');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Ardelle Clayworth', 'aclayworth1q@purevolume.com', 'Non-binary', '6394721378052718', 'instapayment');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Eberhard Wastall', 'ewastall1r@livejournal.com', 'Polygender', '4017956448658', 'visa');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Auberon Dwelly', 'adwelly1s@sourceforge.net', 'Female', '5436631296550515', 'diners-club-us-ca');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Aurel MacGillacolm', 'amacgillacolm1t@wp.com', 'Genderfluid', '3587898124463706', 'jcb');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Franciska Dunsmuir', 'fdunsmuir1u@ocn.ne.jp', 'Genderqueer', '372301985423757', 'americanexpress');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Suellen Martelet', 'smartelet1v@nationalgeographic.com', 'Male', '5610870243652280490', 'china-unionpay');
insert into CLIENT_DATA (fullname, email, gender, credit_card, credit_type) values ('Bonita Fagence', 'bfagence1w@cam.ac.uk', 'Genderqueer', '3564520281580984', 'jcb');
```

Data generated from <a href="https://mockaroo.com/">mockaroo.com</a>.
<br><br><br>
<img src="https://i.ibb.co/5kp2sKq/postgresql.png" alt="postgresql" width=60>
<hr>

To install all dependencies, in ```./src/```:

```
pip install -r requirements.txt
```

To test it, in the same folder:
```
uvicorn main:app --reload
```

## Screenshots
#### GET
<img src="https://i.ibb.co/mBWfypN/getall.png" alt="getall">
<img src="https://i.ibb.co/6gFMxJ8/getone.png" alt="getone">

#### POST
<img src="https://i.ibb.co/m4sts4X/post.png" alt="post">

#### PUT
<img src="https://i.ibb.co/whG0sk7/put.png" alt="put">

#### DELETE
<img src="https://i.ibb.co/rvKYd7Q/delete.png" alt="delete">

## Source code

<img src="https://i.ibb.co/j49S200/REST-API-with-Fast-API-and-Postgre-SQL.png" alt="REST-API-with-Fast-API-and-Postgre-SQL">
