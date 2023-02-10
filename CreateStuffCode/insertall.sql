USE All_Levels;

SET AUTOCOMMIT=0;
INSERT INTO SMF VALUES ('GUJ','Gujarat',5000000.00,3000000.00);
COMMIT;



SET AUTOCOMMIT=0;
INSERT INTO DMU VALUES ('GUJAND','Anand',90000.00,7),
('GUJSUR','Surat',70000.00,7),
('GUJKUT','Kutch',30000.00,7);
COMMIT;


SET AUTOCOMMIT=0;
INSERT INTO Batch VALUES ('BAT0000001','GUJSUR',10,1000.00,'GUJKUT'),
('BAT0000002','GUJSUR',20,2000.00,'GUJAND'),
('BAT0000003','GUJSUR',30,4000.00,'GUJAND'),
('BAT0000004','GUJAND',40,9000.00,'GUJAND'),
('BAT0000005','GUJAND',50,10000.00,'GUJSUR'),
('BAT0000006','GUJKUT',20,3000.00,'GUJSUR');
COMMIT;

SET AUTOCOMMIT=0;
INSERT INTO Retailers VALUES ('RET0000001','AMUL','GUJAND',50,30000.00,'GUJ'),
('RET0000002','SHREEJI STORES','GUJSUR',50,30000.00,'GUJ'),
('RET0000003','BIG BAZAAR','GUJSUR',100,100000.00,'GUJ'),
('RET0000004','KRISHNA GROCERIES','GUJAND',25,30000.00,'GUJ'),
('RET0000005','YADAV GENERAL STORE','GUJKUT',15,10000.00,'GUJ'),
('RET0000006','SHREE KUBER STORE','GUJSUR',25,30000.00,'GUJ');
COMMIT;

SET AUTOCOMMIT=0;
INSERT INTO VDCS VALUES ('SURBVS',0,5000.00,10,'Bhuvasan'),
('SURSVN',5,5000.00,10,'Sevni'),
('SURLJP',3,5000.00,10,'Lajpor'),
('SURNNN',2,5000.00,10,'Nani Naroli'),
('SURUMP',1,5000.00,10,'Umarpada'),
('KUTBPD',0,5000.00,10,'Bharapur Dufiwali'),
('KUTKVD',5,5000.00,10,'Khavda'),
('KUTMDP',3,5000.00,10,'Madhapar'),
('KUTMND',2,5000.00,10,'Mundra'),
('KUTNKT',1,5000.00,10,'Nakhatrana'),
('ANDBDR',0,5000.00,10,'Bhadran'),
('ANDCNG',5,5000.00,10,'Changa'),
('ANDISN',3,5000.00,10,'Isnav'),
('ANDLNJ',2,5000.00,10,'Lunej'),
('ANDVTV',1,5000.00,10,'Vatav');
COMMIT;

SET AUTOCOMMIT=0;
INSERT INTO Dairy_Farmer VALUES ('FIC001',10,30,0),
('FIC002',20,30,0),
('FIC003',30,30,0),
('FIC004',40,30,0),
('FIC005',50,30,0),
('FIC011',10,30,0),
('FIC012',20,30,0),
('FIC013',30,30,0),
('FIC014',40,30,0),
('FIC015',50,30,0),
('FIC021',10,30,0),
('FIC022',20,30,0),
('FIC023',30,30,0),
('FIC024',40,30,0),
('FIC025',50,30,0),
('FIC031',10,30,0),
('FIC032',20,30,0),
('FIC033',30,30,0),
('FIC034',40,30,0),
('FIC035',50,30,0),
('FIC041',10,30,0),
('FIC042',20,30,0),
('FIC043',30,30,0),
('FIC044',40,30,0),
('FIC045',50,30,0),
('FIC101',10,30,0),
('FIC102',20,30,0),
('FIC103',30,30,0),
('FIC104',40,30,0),
('FIC105',50,30,0),
('FIC111',10,30,0),
('FIC112',20,30,0),
('FIC113',30,30,0),
('FIC114',40,30,0),
('FIC115',50,30,0),
('FIC121',10,30,0),
('FIC122',20,30,0),
('FIC123',30,30,0),
('FIC124',40,30,0),
('FIC125',50,30,0),
('FIC131',10,30,0),
('FIC132',20,30,0),
('FIC133',30,30,0),
('FIC134',40,30,0),
('FIC135',50,30,0),
('FIC141',10,30,0),
('FIC142',20,30,0),
('FIC143',30,30,0),
('FIC144',40,30,0),
('FIC145',50,30,0),
('FIC201',10,30,0),
('FIC202',20,30,0),
('FIC203',30,30,0),
('FIC204',40,30,0),
('FIC205',50,30,0),
('FIC211',10,30,0),
('FIC212',20,30,0),
('FIC213',30,30,0),
('FIC214',40,30,0),
('FIC215',50,30,0),
('FIC221',10,30,0),
('FIC222',20,30,0),
('FIC223',30,30,0),
('FIC224',40,30,0),
('FIC225',50,30,0),
('FIC231',10,30,0),
('FIC232',20,30,0),
('FIC233',30,30,0),
('FIC234',40,30,0),
('FIC235',50,30,0),
('FIC241',10,30,0),
('FIC242',20,30,0),
('FIC243',30,30,0),
('FIC244',40,30,0),
('FIC245',50,30,0);
COMMIT;

SET AUTOCOMMIT=0;
INSERT INTO PW VALUES ('PW001','2022-12-31',20000.00,'GUJSUR'),
('PW002','2022-12-31',20000.00,'GUJSUR'),
('PW003','2022-12-31',20000.00,'GUJSUR'),
('PW004','2022-12-31',20000.00,'GUJSUR'),
('PW005','2022-12-31',20000.00,'GUJSUR'),
('PW006','2022-12-31',20000.00,'GUJSUR'),
('PW007','2022-12-31',20000.00,'GUJSUR'),
('PW008','2022-12-31',20000.00,'GUJSUR'),
('PW009','2022-12-31',20000.00,'GUJSUR'),
('PW010','2022-12-31',20000.00,'GUJSUR'),
('PW011','2023-01-31',20000.00,'GUJKUT'),
('PW012','2023-01-31',20000.00,'GUJKUT'),
('PW013','2023-01-31',20000.00,'GUJKUT'),
('PW014','2023-01-31',20000.00,'GUJKUT'),
('PW015','2023-01-31',20000.00,'GUJKUT'),
('PW016','2023-01-31',20000.00,'GUJKUT'),
('PW017','2023-01-31',20000.00,'GUJKUT'),
('PW018','2023-01-31',20000.00,'GUJKUT'),
('PW019','2023-01-31',20000.00,'GUJKUT'),
('PW020','2023-01-31',20000.00,'GUJKUT'),
('PW021','2023-02-01',20000.00,'GUJAND'),
('PW022','2023-02-01',20000.00,'GUJAND'),
('PW023','2023-02-01',20000.00,'GUJAND'),
('PW024','2023-02-01',20000.00,'GUJAND'),
('PW025','2023-02-01',20000.00,'GUJAND'),
('PW026','2023-02-01',20000.00,'GUJAND'),
('PW027','2023-02-01',20000.00,'GUJAND'),
('PW028','2023-02-01',20000.00,'GUJAND'),
('PW029','2023-02-01',20000.00,'GUJAND'),
('PW030','2023-02-01',20000.00,'GUJAND');
COMMIT;

SET AUTOCOMMIT=0;
INSERT INTO VAHP VALUES ('VAH001','2023-02-01',10000.00,'GUJSUR'),
('VAH002','2023-02-01',10000.00,'GUJSUR'),
('VAH003','2023-02-01',10000.00,'GUJSUR'),
('VAH004','2023-02-01',10000.00,'GUJSUR'),
('VAH005','2023-02-01',10000.00,'GUJSUR'),
('VAH006','2023-02-01',10000.00,'GUJKUT'),
('VAH007','2023-02-01',10000.00,'GUJKUT'),
('VAH008','2023-02-01',10000.00,'GUJKUT'),
('VAH009','2023-02-01',10000.00,'GUJKUT'),
('VAH010','2023-02-01',10000.00,'GUJKUT'),
('VAH011','2023-02-01',10000.00,'GUJAND'),
('VAH012','2023-02-01',10000.00,'GUJAND'),
('VAH013','2023-02-01',10000.00,'GUJAND'),
('VAH014','2023-02-01',10000.00,'GUJAND'),
('VAH015','2023-02-01',10000.00,'GUJAND');
COMMIT;


SET AUTOCOMMIT=0;
insert into VDCS_L values('VDL001','100000','2023-02-01 0:00:00','SURBVS');
insert into VDCS_L values('VDL002','100000','2023-02-01 0:00:00','SURSVN');
insert into VDCS_L values('VDL003','100000','2023-02-01 0:00:00','SURLJP');
insert into VDCS_L values('VDL004','100000','2023-02-01 0:00:00','SURNNN');
insert into VDCS_L values('VDL005','100000','2023-02-01 0:00:00','SURUMP');
insert into VDCS_L values('VDL006','100000','2023-02-01 0:00:00','KUTBPD');
insert into VDCS_L values('VDL007','100000','2023-02-01 0:00:00','KUTKVD');
insert into VDCS_L values('VDL008','100000','2023-02-01 0:00:00','KUTMDP');
insert into VDCS_L values('VDL009','100000','2023-02-01 0:00:00','KUTMND');
insert into VDCS_L values('VDL010','100000','2023-02-01 0:00:00','KUTNKT');
insert into VDCS_L values('VDL011','100000','2023-02-01 0:00:00','ANDBDR');
insert into VDCS_L values('VDL012','100000','2023-02-01 0:00:00','ANDCNG');
insert into VDCS_L values('VDL013','100000','2023-02-01 0:00:00','ANDISN');
insert into VDCS_L values('VDL014','100000','2023-02-01 0:00:00','ANDLNJ');
insert into VDCS_L values('VDL015','100000','2023-02-01 0:00:00','ANDVTV');
COMMIT;

SET AUTOCOMMIT=0;
INSERT INTO AADHAR_CARD VALUES ('123456789001','KSHITIJ SHARMA',40,'M','3456789001','xyz','9999999999999999','Bhuvasan','Bhuvasan'),
('123456789002','IKHLAS KHAN',40,'M','3456789002','xyz','9999999999999998','Bhuvasan','Bhuvasan'),
('123456789003','SHWETA SINGH',40,'F','3456789003','xyz','9999999999999997','Bhuvasan','Bhuvasan'),
('123456789004','MANOHAR KUMAR',40,'M','3456789004','xyz','9999999999999996','Bhuvasan','Bhuvasan'),
('123456789005','YASH THAKUR',40,'M','3456789005','xyz','9999999999999995','Bhuvasan','Bhuvasan'),
('123456789011','SONIA GANDHI',40,'F','3456789011','xyz','9999999999999994','Sevni','Sevni'),
('123456789012','NEHA JAIN',40,'F','3456789012','xyz','9999999999999993','Sevni','Sevni'),
('123456789013','SHOBHA GUPTA',40,'F','3456789013','xyz','9999999999999992','Sevni','Sevni'),
('123456789014','ADITYA PANDEY',40,'M','3456789014','xyz','9999999999999991','Sevni','Sevni'),
('123456789015','PRAKHAR SHETH',40,'M','3456789015','xyz','9999999999999990','Sevni','Sevni'),
('123456789021','VIKRAM MODI',40,'M','3456789021','xyz','9999999999999989','Lajpor','Lajpor'),
('123456789022','KSHITIJ KAPADIA',40,'M','3456789022','xyz','9999999999999988','Lajpor','Lajpor'),
('123456789023','VIKRAM SINGH',40,'M','3456789023','xyz','9999999999999987','Lajpor','Lajpor'),
('123456789024','PRAKHAR JOSHI',40,'M','3456789024','xyz','9999999999999986','Lajpor','Lajpor'),
('123456789025','SHWETA GUPTA',40,'M','3456789025','xyz','9999999999999985','Lajpor','Lajpor'),
('123456789031','FARHAN ALI',40,'M','3456789031','xyz','9999999999999984','Nani Naroli','Nani Naroli'),
('123456789032','SONIA THAKUR',40,'F','3456789032','xyz','9999999999999983','Nani Naroli','Nani Naroli'),
('123456789033','MOHAK KUMAR',40,'M','3456789033','xyz','9999999999999982','Nani Naroli','Nani Naroli'),
('123456789034','KUBER GAJJAR',40,'M','3456789034','xyz','9999999999999981','Nani Naroli','Nani Naroli'),
('123456789035','SHREYAS MEHTA',40,'M','3456789035','xyz','9999999999999980','Nani Naroli','Nani Naroli'),
('123456789041','ADITYA PANDYA',40,'M','3456789041','xyz','9999999999999979','Umarpada','Umarpada'),
('123456789042','VARTIKA ZARIWALA',40,'F','3456789042','xyz','9999999999999978','Umarpada','Umarpada'),
('123456789043','FULLARA AMBANI',40,'F','3456789043','xyz','9999999999999977','Umarpada','Umarpada'),
('123456789044','HETVI ACHARYA',40,'F','3456789044','xyz','9999999999999976','Umarpada','Umarpada'),
('123456789045','JAMINI CHOWDHURY',40,'F','3456789045','xyz','9999999999999975','Umarpada','Umarpada'),
('123456789101','RAHUL DAVE',40,'M','3456789101','xyz','9999999999999974','Bharapar Dufiwali','Bharapar Dufiwali'),
('123456789102','JOSHIL DESAI',40,'M','3456789102','xyz','9999999999999973','Bharapar Dufiwali','Bharapar Dufiwali'),
('123456789103','RAHUL THAKUR',40,'M','3456789103','xyz','9999999999999972','Bharapar Dufiwali','Bharapar Dufiwali'),
('123456789104','PRAKHAR SINGH',40,'M','3456789104','xyz','9999999999999971','Bharapar Dufiwali','Bharapar Dufiwali'),
('123456789105','NEHA JAIN',40,'F','3456789105','xyz','9999999999999970','Bharapar Dufiwali','Bharapar Dufiwali'),
('123456789111','FATIMA ANSARI',40,'F','345678111','xyz','9999999999999969','Khavda','Khavda'),
('123456789112','ZAHIDA KHAN',40,'F','345678112','xyz','9999999999999968','Khavda','Khavda'),
('123456789113','HAMIDA REHMAN',40,'F','345678113','xyz','9999999999999967','Khavda','Khavda'),
('123456789114','IKHLAS ALI',40,'M','345678114','xyz','9999999999999966','Khavda','Khavda'),
('123456789115','ADITYA GUPTA',40,'M','345678115','xyz','9999999999999965','Khavda','Khavda'),
('123456789121','ADITYA SINGH',40,'M','345678121','xyz','9999999999999964','Madhapar','Madhapar'),
('123456789122','ADITYA THAKUR',40,'M','345678122','xyz','9999999999999963','Madhapar','Madhapar'),
('123456789123','MINAXI GANJAWALA',40,'F','345678123','xyz','9999999999999962','Madhapar','Madhapar'),
('123456789124','MUNJAL MISTRY',40,'F','345678124','xyz','9999999999999961','Madhapar','Madhapar'),
('123456789125','VARTIKA PATEL',40,'F','345678125','xyz','9999999999999960','Madhapar','Madhapar'),
('123456789131','RAHUL GANDHI',40,'M','345678131','xyz','9999999999999959','Mundra','Mundra'),
('123456789132','HARSHIL POPAT',40,'M','345678132','xyz','9999999999999958','Mundra','Mundra'),
('123456789133','DIVYANSH POPAT',40,'M','345678133','xyz','9999999999999957','Mundra','Mundra'),
('123456789134','YASH SHROFF',40,'M','345678134','xyz','9999999999999956','Mundra','Mundra'),
('123456789135','SHWETA YADAV',40,'F','345678135','xyz','9999999999999954','Mundra','Mundra'),
('123456789141','SUDHANSHU TRIPATHI',40,'M','345678141','xyz','9999999999999953','Nakhatrana','Nakhatrana'),
('123456789142','MADHAV VYAS',40,'M','345678142','xyz','9999999999999952','Nakhatrana','Nakhatrana'),
('123456789143','MOHAK DESAI',40,'M','345678143','xyz','9999999999999951','Nakhatrana','Nakhatrana'),
('123456789144','VIKRAM SINGH',40,'M','345678144','xyz','9999999999999950','Nakhatrana','Nakhatrana'),
('123456789145','HARSH THAKUR',40,'M','345678145','xyz','9999999999999949','Nakhatrana','Nakhatrana'),
('123456789201','KSHITIJ YADAV',40,'M','345678201','xyz','9999999999999948','Bhadran','Bhadran'),
('123456789202','NEHA CHOWDHURY',40,'F','345678202','xyz','9999999999999947','Bhadran','Bhadran'),
('123456789203','HAMIDA ALI',40,'F','345678203','xyz','9999999999999946','Bhadran','Bhadran'),
('123456789204','MUKUND SHETH',40,'M','345678204','xyz','9999999999999945','Bhadran','Bhadran'),
('123456789205','PRAKHAR GANJAWALA',40,'M','345678205','xyz','9999999999999944','Bhadran','Bhadran'),
('123456789211','ANIRUDH PATEL',40,'M','345678211','xyz','9999999999999943','Changa','Changa'),
('123456789212','POORVI PARIKH',40,'F','345678212','xyz','9999999999999942','Changa','Changa'),
('123456789213','MOHAMMED IKHLAS KHAN',40,'M','345678213','xyz','9999999999999941','Changa','Changa'),
('123456789214','DIVYANSH PATEL',40,'M','345678214','xyz','9999999999999940','Changa','Changa'),
('123456789215','NARASHIMHA LAKHANI',40,'M','345678215','xyz','9999999999999939','Changa','Changa'),
('123456789221','SANSKAR ZARIWALA',40,'M','345678221','xyz','9999999999999938','Isnav','Isnav'),
('123456789222','VIKRAM CHOWDHURY',40,'M','345678222','xyz','9999999999999937','Isnav','Isnav'),
('123456789223','SHWETA YADAV',40,'F','345678223','xyz','9999999999999936','Isnav','Isnav'),
('123456789224','SONIA YADAV',40,'F','345678224','xyz','9999999999999935','Isnav','Isnav'),
('123456789225','ADITYA SHARMA',40,'M','345678225','xyz','9999999999999934','Isnav','Isnav'),
('123456789231','RAHUL TRIPATHI',40,'M','345678231','xyz','9999999999999933','Lunej','Lunej'),
('123456789232','NEHA SINGH',40,'F','345678232','xyz','9999999999999932','Lunej','Lunej'),
('123456789233','MOHAK AMBANI',40,'M','345678233','xyz','9999999999999931','Lunej','Lunej'),
('123456789234','PRAKHAR PATEL',40,'M','345678234','xyz','9999999999999930','Lunej','Lunej'),
('123456789235','SHREYAS GUJJAR',40,'M','345678235','xyz','9999999999999929','Lunej','Lunej'),
('123456789241','FARHAN ALI',40,'M','3456789241','xyz','9999999999999928','Vatav','Vatav'),
('123456789242','DEV SINGH',40,'M','345678242','xyz','9999999999999927','Vatav','Vatav'),
('123456789243','RITI CHOWDHURY',40,'F','345678243','xyz','9999999999999926','Vatav','Vatav'),
('123456789244','SHUDHANSHU MITTAL',40,'M','345678244','xyz','9999999999999925','Vatav','Vatav'),
('123456789245','ASHUTOSH PATEL',40,'M','345678245','xyz','9999999999999924','Vatav','Vatav'),
('123456780001','AJAY DEVGN',40,'M','3456780001','xyz','9999999999999923','Bhuvasan','Surat'),
('123456780002','RANBIR KAPOOR',40,'M','3456780002','xyz','9999999999999922','Sevni','Surat'),
('123456780003','KAREENA KAPOOR',40,'F','3456780003','xyz','9999999999999921','Nani Naroli','Surat'),
('123456780004','SHAHRUKH KHAN',40,'M','3456780004','xyz','9999999999999920','Umarpada','Surat'),
('123456780005','SALMAN KHAN',40,'M','3456780005','xyz','9999999999999919','Lajpor','Surat'),
('123456780006','AMIR KHAN',40,'M','3456780006','xyz','9999999999999918','Bhuvasan','Surat'),
('123456780007','AKSHAY KUMAR',40,'M','3456780007','xyz','9999999999999917','Lajpor','Surat'),
('123456780008','ABHISHEK BACHAN',40,'M','3456780008','xyz','9999999999999916','Sevni','Surat'),
('123456780009','PRIYANKA CHOPRA',40,'F','3456780009','xyz','9999999999999915','Umarpada','Surat'),
('123456780010','RANVEER SINGH',40,'M','3456780010','xyz','9999999999999914','Nani Naroli','Surat'),
('123456780011','HRITIK ROSHAN',40,'M','3456780011','xyz','9999999999999913','Bharapar Dufiwali','Kutch'),
('123456780012','ALIA BHATT',40,'F','3456780012','xyz','9999999999999912','Khavda','Kutch'),
('123456780013','SAIF ALI KHAN',40,'M','3456780013','xyz','9999999999999911','Madhapur','Kutch'),
('123456780014','SANJAY DUTT',40,'M','3456780014','xyz','9999999999999910','Mundra','Kutch'),
('123456780015','SHAHID KAPOOR',40,'M','3456780015','xyz','9999999999999909','Nakhatrana','Kutch'),
('123456780016','AMITABH BACHAN',40,'M','3456780016','xyz','9999999999999908','Bharapar Dufiwali','Kutch'),
('123456780017','VARUN DHAWAN',40,'M','3456780017','xyz','9999999999999907','Khavda','Kutch'),
('123456780018','ANIL KAPOOR',40,'M','3456780018','xyz','9999999999999906','Madhapur','Kutch'),
('123456780019','FARHAN AKHTAR',40,'M','3456780019','xyz','9999999999999905','Mundra','Kutch'),
('123456780020','SIDDHARTH MALHOTRA',40,'M','3456780020','xyz','9999999999999904','Nakhatrana','Kutch'),
('123456780021','SUNNY DEOL',40,'M','3456780021','xyz','9999999999999903','Bhadran','Anand City'),
('123456780022','ARJUN KAPOOR',40,'M','3456780022','xyz','9999999999999902','Vatav','Anand City'),
('123456780023','JACKIE SHROFF',40,'M','3456780023','xyz','9999999999999901','Vatav','Anand City'),
('123456780024','TIGER SHROFF',40,'M','3456780024','xyz','9999999999999900','Vatav','Anand City'),
('123456780025','SONU SOOD',40,'M','3456780025','xyz','9999999999999899','Vatav','Anand City'),
('123456780026','SAIF ALI KHAN',40,'M','3456780026','xyz','9999999999999898','Vatav','Anand City'),
('123456780027','JOHN ABRAHAM',40,'M','3456780027','xyz','9999999999999897','Vatav','Anand City'),
('123456780028','RAJKUMMAR RAO',40,'M','3456780028','xyz','9999999999999896','Changa','Anand City'),
('123456780029','KATRINA KAIF',40,'F','3456780029','xyz','9999999999999895','Isnav','Anand City'),
('123456780030','KANGANA RANAUT',40,'F','3456780030','xyz','9999999999999894','Lunej','Anand City'),
('123456790001','DISHA PATANI',40,'M','3456790001','xyz','9999999999999893','Bhuvasan','Surat'),
('123456790002','SHILPA SHETTY',40,'F','3456790002','xyz','9999999999999892','Bhuvasan','Surat'),
('123456790003','AISHWARYA RAI BACHAN',40,'F','3456790003','xyz','9999999999999891','Bhuvasan','Surat'),
('123456790004','VIDYA BALAN',40,'F','3456790004','xyz','9999999999999890','Nani Naroli','Surat'),
('123456790005','SONAKSHI SINHA',40,'F','3456790005','xyz','9999999999999889','Umarpada','Surat'),
('123456790006','KAJOL',40,'F','3456790006','xyz','9999999999999887','Bharapar Dufiwali','Kutch'),
('123456790007','VIVEK OBEROI',40,'M','3456790007','xyz','9999999999999886','Bharapar Dufiwali','Kutch'),
('123456790008','JIMMY SHEIRGILL',40,'M','3456790008','xyz','9999999999999885','Bharapar Dufiwali','Kutch'),
('123456790009','AYUSHMANN KHURANA',40,'M','3456790009','xyz','9999999999999884','Bharapar Dufiwali','Kutch'),
('123456790010','MANOJ BAJPAYEE',40,'M','3456790010','xyz','9999999999999883','Bharapar Dufiwali','Kutch'),
('123456790011','NANA PATEKAR',40,'M','3456790011','xyz','9999999999999882','Anand City','Anand City'),
('123456790012','DEEPIKA PADUKONE',40,'F','3456790012','xyz','9999999999999881','Anand City','Anand City'),
('123456790013','SONAM KAPOOR',40,'F','3456790013','xyz','9999999999999880','Anand City','Anand City'),
('123456790014','MADHURI DIXIT',40,'F','3456790014','xyz','9999999999999879','Anand City','Anand City'),
('123456790015','ANUSHKA SHARMA',40,'F','3456790015','xyz','9999999999999878','Anand City','Anand City'),
('123456710001','PRATUL ADHARVYU',40,'M','3456710001','xyz','9999999999999877','Surat','Bhuvasan'),
('123456710002','PINAL CHOKSI',40,'F','3456710002','xyz','9999999999999876','Surat','Sevni'),
('123456710003','SUDARSINI DALAL',40,'F','3456710003','xyz','9999999999999875','Surat','Lajpor'),
('123456710004','TANISHKA JAIN',40,'F','3456710004','xyz','9999999999999874','Surat','Nani Naroli'),
('123456710005','VEDANG PATEL',40,'M','3456710005','xyz','9999999999999873','Surat','Umarpada'),
('123456710006','DHAWAL KOTECHA',40,'M','3456710006','xyz','9999999999999872','Kutch','Kutch'),
('123456710007','JAGDISH MODI',40,'M','3456710007','xyz','9999999999999871','Kutch','Kutch'),
('123456710008','KRISHNA JAIN',40,'M','3456710008','xyz','9999999999999870','Kutch','Kutch'),
('123456710009','PREETESH CHAUHAN',40,'M','3456710009','xyz','9999999999999869','Kutch','Kutch'),
('123456710010','PRIYADARSHI DIXIT',40,'F','3456710010','xyz','9999999999999868','Kutch','Kutch'),
('123456710011','AGAM CHOWDHURY',40,'M','3456710011','xyz','9999999999999867','Anand City','Bhadran'),
('123456710012','AMIT LAL SINGH YADAV',40,'M','3456710012','xyz','9999999999999866','Anand City','Changa'),
('123456710013','BALCHANDRA MEHTA',40,'M','3456710013','xyz','9999999999999865','Anand City','Isnav'),
('123456710014','CHANDRA NAIK',40,'M','3456710014','xyz','9999999999999864','Anand City','Lunej'),
('123456710015','CHINTAN AGARWAL',40,'M','3456710015','xyz','9999999999999863','Anand City','Vatav');
COMMIT;




SET AUTOCOMMIT=0;
insert into Part_Of values('VDL001','GUJSUR');
insert into Part_Of values('VDL002','GUJSUR');
insert into Part_Of values('VDL003','GUJSUR');
insert into Part_Of values('VDL004','GUJSUR');
insert into Part_Of values('VDL005','GUJSUR');
insert into Part_Of values('VDL006','GUJKUT');
insert into Part_Of values('VDL007','GUJKUT');
insert into Part_Of values('VDL008','GUJKUT');
insert into Part_Of values('VDL009','GUJKUT');
insert into Part_Of values('VDL010','GUJKUT');
insert into Part_Of values('VDL011','GUJAND');
insert into Part_Of values('VDL012','GUJAND');
insert into Part_Of values('VDL013','GUJAND');
insert into Part_Of values('VDL014','GUJAND');
insert into Part_Of values('VDL015','GUJAND');
COMMIT;

SET AUTOCOMMIT=0;
insert into Dairy_Farmer_Possesses values('FIC001','123456789001');
insert into Dairy_Farmer_Possesses values('FIC002','123456789002');
insert into Dairy_Farmer_Possesses values('FIC003','123456789003');
insert into Dairy_Farmer_Possesses values('FIC004','123456789004');
insert into Dairy_Farmer_Possesses values('FIC005','123456789005');
insert into Dairy_Farmer_Possesses values('FIC011','123456789011');
insert into Dairy_Farmer_Possesses values('FIC012','123456789012');
insert into Dairy_Farmer_Possesses values('FIC013','123456789013');
insert into Dairy_Farmer_Possesses values('FIC014','123456789014');
insert into Dairy_Farmer_Possesses values('FIC015','123456789015');
insert into Dairy_Farmer_Possesses values('FIC021','123456789021');
insert into Dairy_Farmer_Possesses values('FIC022','123456789022');
insert into Dairy_Farmer_Possesses values('FIC023','123456789023');
insert into Dairy_Farmer_Possesses values('FIC024','123456789024');
insert into Dairy_Farmer_Possesses values('FIC025','123456789025');
insert into Dairy_Farmer_Possesses values('FIC031','123456789031');
insert into Dairy_Farmer_Possesses values('FIC032','123456789032');
insert into Dairy_Farmer_Possesses values('FIC033','123456789033');
insert into Dairy_Farmer_Possesses values('FIC034','123456789034');
insert into Dairy_Farmer_Possesses values('FIC035','123456789035');
insert into Dairy_Farmer_Possesses values('FIC041','123456789041');
insert into Dairy_Farmer_Possesses values('FIC042','123456789042');
insert into Dairy_Farmer_Possesses values('FIC043','123456789043');
insert into Dairy_Farmer_Possesses values('FIC044','123456789044');
insert into Dairy_Farmer_Possesses values('FIC045','123456789045');
insert into Dairy_Farmer_Possesses values('FIC101','123456789101');
insert into Dairy_Farmer_Possesses values('FIC102','123456789102');
insert into Dairy_Farmer_Possesses values('FIC103','123456789103');
insert into Dairy_Farmer_Possesses values('FIC104','123456789104');
insert into Dairy_Farmer_Possesses values('FIC105','123456789105');
insert into Dairy_Farmer_Possesses values('FIC111','123456789111');
insert into Dairy_Farmer_Possesses values('FIC112','123456789112');
insert into Dairy_Farmer_Possesses values('FIC113','123456789113');
insert into Dairy_Farmer_Possesses values('FIC114','123456789114');
insert into Dairy_Farmer_Possesses values('FIC115','123456789115');
insert into Dairy_Farmer_Possesses values('FIC121','123456789121');
insert into Dairy_Farmer_Possesses values('FIC122','123456789122');
insert into Dairy_Farmer_Possesses values('FIC123','123456789123');
insert into Dairy_Farmer_Possesses values('FIC124','123456789124');
insert into Dairy_Farmer_Possesses values('FIC125','123456789125');
insert into Dairy_Farmer_Possesses values('FIC131','123456789131');
insert into Dairy_Farmer_Possesses values('FIC132','123456789132');
insert into Dairy_Farmer_Possesses values('FIC133','123456789133');
insert into Dairy_Farmer_Possesses values('FIC134','123456789134');
insert into Dairy_Farmer_Possesses values('FIC135','123456789135');
insert into Dairy_Farmer_Possesses values('FIC141','123456789141');
insert into Dairy_Farmer_Possesses values('FIC142','123456789142');
insert into Dairy_Farmer_Possesses values('FIC143','123456789143');
insert into Dairy_Farmer_Possesses values('FIC144','123456789144');
insert into Dairy_Farmer_Possesses values('FIC145','123456789145');
insert into Dairy_Farmer_Possesses values('FIC201','123456789201');
insert into Dairy_Farmer_Possesses values('FIC202','123456789202');
insert into Dairy_Farmer_Possesses values('FIC203','123456789203');
insert into Dairy_Farmer_Possesses values('FIC204','123456789204');
insert into Dairy_Farmer_Possesses values('FIC205','123456789205');
insert into Dairy_Farmer_Possesses values('FIC211','123456789211');
insert into Dairy_Farmer_Possesses values('FIC212','123456789212');
insert into Dairy_Farmer_Possesses values('FIC213','123456789213');
insert into Dairy_Farmer_Possesses values('FIC214','123456789214');
insert into Dairy_Farmer_Possesses values('FIC215','123456789215');
insert into Dairy_Farmer_Possesses values('FIC221','123456789221');
insert into Dairy_Farmer_Possesses values('FIC222','123456789222');
insert into Dairy_Farmer_Possesses values('FIC223','123456789223');
insert into Dairy_Farmer_Possesses values('FIC224','123456789224');
insert into Dairy_Farmer_Possesses values('FIC225','123456789225');
insert into Dairy_Farmer_Possesses values('FIC231','123456789231');
insert into Dairy_Farmer_Possesses values('FIC232','123456789232');
insert into Dairy_Farmer_Possesses values('FIC233','123456789233');
insert into Dairy_Farmer_Possesses values('FIC234','123456789234');
insert into Dairy_Farmer_Possesses values('FIC235','123456789235');
insert into Dairy_Farmer_Possesses values('FIC241','123456789241');
insert into Dairy_Farmer_Possesses values('FIC242','123456789242');
insert into Dairy_Farmer_Possesses values('FIC243','123456789243');
insert into Dairy_Farmer_Possesses values('FIC244','123456789244');
insert into Dairy_Farmer_Possesses values('FIC245','123456789245');
COMMIT;

SET AUTOCOMMIT=0;
insert into DF_Works_Under_VDCS values('FIC001','SURBVS');
insert into DF_Works_Under_VDCS values('FIC002','SURBVS');
insert into DF_Works_Under_VDCS values('FIC003','SURBVS');
insert into DF_Works_Under_VDCS values('FIC004','SURBVS');
insert into DF_Works_Under_VDCS values('FIC005','SURBVS');
insert into DF_Works_Under_VDCS values('FIC011','SURSVN');
insert into DF_Works_Under_VDCS values('FIC012','SURSVN');
insert into DF_Works_Under_VDCS values('FIC013','SURSVN');
insert into DF_Works_Under_VDCS values('FIC014','SURSVN');
insert into DF_Works_Under_VDCS values('FIC015','SURSVN');
insert into DF_Works_Under_VDCS values('FIC021','SURLJP');
insert into DF_Works_Under_VDCS values('FIC022','SURLJP');
insert into DF_Works_Under_VDCS values('FIC023','SURLJP');
insert into DF_Works_Under_VDCS values('FIC024','SURLJP');
insert into DF_Works_Under_VDCS values('FIC025','SURLJP');
insert into DF_Works_Under_VDCS values('FIC031','SURNNN');
insert into DF_Works_Under_VDCS values('FIC032','SURNNN');
insert into DF_Works_Under_VDCS values('FIC033','SURNNN');
insert into DF_Works_Under_VDCS values('FIC034','SURNNN');
insert into DF_Works_Under_VDCS values('FIC035','SURNNN');
insert into DF_Works_Under_VDCS values('FIC041','SURUMP');
insert into DF_Works_Under_VDCS values('FIC042','SURUMP');
insert into DF_Works_Under_VDCS values('FIC043','SURUMP');
insert into DF_Works_Under_VDCS values('FIC044','SURUMP');
insert into DF_Works_Under_VDCS values('FIC045','SURUMP');
insert into DF_Works_Under_VDCS values('FIC101','KUTBPD');
insert into DF_Works_Under_VDCS values('FIC102','KUTBPD');
insert into DF_Works_Under_VDCS values('FIC103','KUTBPD');
insert into DF_Works_Under_VDCS values('FIC104','KUTBPD');
insert into DF_Works_Under_VDCS values('FIC105','KUTBPD');
insert into DF_Works_Under_VDCS values('FIC111','KUTKVD');
insert into DF_Works_Under_VDCS values('FIC112','KUTKVD');
insert into DF_Works_Under_VDCS values('FIC113','KUTKVD');
insert into DF_Works_Under_VDCS values('FIC114','KUTKVD');
insert into DF_Works_Under_VDCS values('FIC115','KUTKVD');
insert into DF_Works_Under_VDCS values('FIC121','KUTMDP');
insert into DF_Works_Under_VDCS values('FIC122','KUTMDP');
insert into DF_Works_Under_VDCS values('FIC123','KUTMDP');
insert into DF_Works_Under_VDCS values('FIC124','KUTMDP');
insert into DF_Works_Under_VDCS values('FIC125','KUTMDP');
insert into DF_Works_Under_VDCS values('FIC131','KUTMND');
insert into DF_Works_Under_VDCS values('FIC132','KUTMND');
insert into DF_Works_Under_VDCS values('FIC133','KUTMND');
insert into DF_Works_Under_VDCS values('FIC134','KUTMND');
insert into DF_Works_Under_VDCS values('FIC135','KUTMND');
insert into DF_Works_Under_VDCS values('FIC141','KUTNKT');
insert into DF_Works_Under_VDCS values('FIC142','KUTNKT');
insert into DF_Works_Under_VDCS values('FIC143','KUTNKT');
insert into DF_Works_Under_VDCS values('FIC144','KUTNKT');
insert into DF_Works_Under_VDCS values('FIC145','KUTNKT');
insert into DF_Works_Under_VDCS values('FIC201','ANDBDR');
insert into DF_Works_Under_VDCS values('FIC202','ANDBDR');
insert into DF_Works_Under_VDCS values('FIC203','ANDBDR');
insert into DF_Works_Under_VDCS values('FIC204','ANDBDR');
insert into DF_Works_Under_VDCS values('FIC205','ANDBDR');
insert into DF_Works_Under_VDCS values('FIC211','ANDCNG');
insert into DF_Works_Under_VDCS values('FIC212','ANDCNG');
insert into DF_Works_Under_VDCS values('FIC213','ANDCNG');
insert into DF_Works_Under_VDCS values('FIC214','ANDCNG');
insert into DF_Works_Under_VDCS values('FIC215','ANDCNG');
insert into DF_Works_Under_VDCS values('FIC221','ANDISN');
insert into DF_Works_Under_VDCS values('FIC222','ANDISN');
insert into DF_Works_Under_VDCS values('FIC223','ANDISN');
insert into DF_Works_Under_VDCS values('FIC224','ANDISN');
insert into DF_Works_Under_VDCS values('FIC225','ANDISN');
insert into DF_Works_Under_VDCS values('FIC231','ANDLNJ');
insert into DF_Works_Under_VDCS values('FIC232','ANDLNJ');
insert into DF_Works_Under_VDCS values('FIC233','ANDLNJ');
insert into DF_Works_Under_VDCS values('FIC234','ANDLNJ');
insert into DF_Works_Under_VDCS values('FIC235','ANDLNJ');
insert into DF_Works_Under_VDCS values('FIC241','ANDVTV');
insert into DF_Works_Under_VDCS values('FIC242','ANDVTV');
insert into DF_Works_Under_VDCS values('FIC243','ANDVTV');
insert into DF_Works_Under_VDCS values('FIC244','ANDVTV');
insert into DF_Works_Under_VDCS values('FIC245','ANDVTV');
COMMIT;


SET AUTOCOMMIT=0;
insert into DMU_Works_Under_SMF values('GUJSUR','GUJ');
insert into DMU_Works_Under_SMF values('GUJKUT','GUJ');
insert into DMU_Works_Under_SMF values('GUJAND','GUJ');
COMMIT;


SET AUTOCOMMIT=0;
insert into PW_Possesses values('PW001','123456780001');
insert into PW_Possesses values('PW002','123456780002');
insert into PW_Possesses values('PW003','123456780003');
insert into PW_Possesses values('PW004','123456780004');
insert into PW_Possesses values('PW005','123456780005');
insert into PW_Possesses values('PW006','123456780006');
insert into PW_Possesses values('PW007','123456780007');
insert into PW_Possesses values('PW008','123456780008');
insert into PW_Possesses values('PW009','123456780009');
insert into PW_Possesses values('PW010','123456780010');
insert into PW_Possesses values('PW011','123456780011');
insert into PW_Possesses values('PW012','123456780012');
insert into PW_Possesses values('PW013','123456780013');
insert into PW_Possesses values('PW014','123456780014');
insert into PW_Possesses values('PW015','123456780015');
insert into PW_Possesses values('PW016','123456780016');
insert into PW_Possesses values('PW017','123456780017');
insert into PW_Possesses values('PW018','123456780018');
insert into PW_Possesses values('PW019','123456780019');
insert into PW_Possesses values('PW020','123456780020');
insert into PW_Possesses values('PW021','123456780021');
insert into PW_Possesses values('PW022','123456780022');
insert into PW_Possesses values('PW023','123456780023');
insert into PW_Possesses values('PW024','123456780024');
insert into PW_Possesses values('PW025','123456780025');
insert into PW_Possesses values('PW026','123456780026');
insert into PW_Possesses values('PW027','123456780027');
insert into PW_Possesses values('PW028','123456780028');
insert into PW_Possesses values('PW029','123456780029');
insert into PW_Possesses values('PW030','123456780030');
COMMIT;

SET AUTOCOMMIT=0;
insert into Sells values('BAT0000001','GUJ');
insert into Sells values('BAT0000002','GUJ');
insert into Sells values('BAT0000003','GUJ');
insert into Sells values('BAT0000004','GUJ');
insert into Sells values('BAT0000005','GUJ');
insert into Sells values('BAT0000006','GUJ');
COMMIT;

SET AUTOCOMMIT=0;
insert into VAHP_Possesses values('VAH001','123456790001');
insert into VAHP_Possesses values('VAH002','123456790002');
insert into VAHP_Possesses values('VAH003','123456790003');
insert into VAHP_Possesses values('VAH004','123456790004');
insert into VAHP_Possesses values('VAH005','123456790005');
insert into VAHP_Possesses values('VAH006','123456790006');
insert into VAHP_Possesses values('VAH007','123456790007');
insert into VAHP_Possesses values('VAH008','123456790008');
insert into VAHP_Possesses values('VAH009','123456790009');
insert into VAHP_Possesses values('VAH010','123456790010');
insert into VAHP_Possesses values('VAH011','123456790011');
insert into VAHP_Possesses values('VAH012','123456790012');
insert into VAHP_Possesses values('VAH013','123456790013');
insert into VAHP_Possesses values('VAH014','123456790014');
insert into VAHP_Possesses values('VAH015','123456790015');
COMMIT;

SET AUTOCOMMIT=0;
insert into VDCS_Works_Under_DMU values('SURBVS','GUJSUR');
insert into VDCS_Works_Under_DMU values('SURSVN','GUJSUR');
insert into VDCS_Works_Under_DMU values('SURLJP','GUJSUR');
insert into VDCS_Works_Under_DMU values('SURNNN','GUJSUR');
insert into VDCS_Works_Under_DMU values('SURUMP','GUJSUR');
insert into VDCS_Works_Under_DMU values('KUTBPD','GUJKUT');
insert into VDCS_Works_Under_DMU values('KUTKVD','GUJKUT');
insert into VDCS_Works_Under_DMU values('KUTMDP','GUJKUT');
insert into VDCS_Works_Under_DMU values('KUTMND','GUJKUT');
insert into VDCS_Works_Under_DMU values('KUTNKT','GUJKUT');
insert into VDCS_Works_Under_DMU values('ANDBDR','GUJAND');
insert into VDCS_Works_Under_DMU values('ANDCNG','GUJAND');
insert into VDCS_Works_Under_DMU values('ANDISN','GUJAND');
insert into VDCS_Works_Under_DMU values('ANDLNJ','GUJAND');
insert into VDCS_Works_Under_DMU values('ANDVTV','GUJAND');
COMMIT;


SET AUTOCOMMIT=0;
insert into VDCSL_Possesses values('VDL001','123456710001');
insert into VDCSL_Possesses values('VDL002','123456710002');
insert into VDCSL_Possesses values('VDL003','123456710003');
insert into VDCSL_Possesses values('VDL004','123456710004');
insert into VDCSL_Possesses values('VDL005','123456710005');
insert into VDCSL_Possesses values('VDL006','123456710006');
insert into VDCSL_Possesses values('VDL007','123456710007');
insert into VDCSL_Possesses values('VDL008','123456710008');
insert into VDCSL_Possesses values('VDL009','123456710009');
insert into VDCSL_Possesses values('VDL010','123456710010');
insert into VDCSL_Possesses values('VDL011','123456710011');
insert into VDCSL_Possesses values('VDL012','123456710012');
insert into VDCSL_Possesses values('VDL013','123456710013');
insert into VDCSL_Possesses values('VDL014','123456710014');
insert into VDCSL_Possesses values('VDL015','123456710015');
COMMIT;


SET AUTOCOMMIT=0;
insert into Works_Here values('VAH001','SURBVS');
insert into Works_Here values('VAH002','SURSVN');
insert into Works_Here values('VAH003','SURLJP');
insert into Works_Here values('VAH004','SURNNN');
insert into Works_Here values('VAH005','SURUMP');
insert into Works_Here values('VAH006','KUTBPD');
insert into Works_Here values('VAH007','KUTKVD');
insert into Works_Here values('VAH008','KUTMDP');
insert into Works_Here values('VAH009','KUTMND');
insert into Works_Here values('VAH010','KUTNKT');
insert into Works_Here values('VAH011','ANDBDR');
insert into Works_Here values('VAH012','ANDCNG');
insert into Works_Here values('VAH013','ANDISN');
insert into Works_Here values('VAH014','ANDLNJ');
insert into Works_Here values('VAH015','ANDVTV');
COMMIT;


SET AUTOCOMMIT=0;
insert into Elects values('FIC001','VDL001');
insert into Elects values('FIC002','VDL001');
insert into Elects values('FIC003','VDL001');
insert into Elects values('FIC004','VDL001');
insert into Elects values('FIC005',NULL);
insert into Elects values('FIC011','VDL002');
insert into Elects values('FIC012','VDL002');
insert into Elects values('FIC013','VDL002');
insert into Elects values('FIC014','VDL002');
insert into Elects values('FIC015',NULL);
insert into Elects values('FIC021','VDL003');
insert into Elects values('FIC022','VDL003');
insert into Elects values('FIC023','VDL003');
insert into Elects values('FIC024','VDL003');
insert into Elects values('FIC025',NULL);
insert into Elects values('FIC031','VDL004');
insert into Elects values('FIC032','VDL004');
insert into Elects values('FIC033','VDL004');
insert into Elects values('FIC034','VDL004');
insert into Elects values('FIC035',NULL);
insert into Elects values('FIC041','VDL005');
insert into Elects values('FIC042','VDL005');
insert into Elects values('FIC043','VDL005');
insert into Elects values('FIC044','VDL005');
insert into Elects values('FIC045',NULL);
insert into Elects values('FIC101','VDL006');
insert into Elects values('FIC102','VDL006');
insert into Elects values('FIC103','VDL006');
insert into Elects values('FIC104','VDL006');
insert into Elects values('FIC105',NULL);
insert into Elects values('FIC111','VDL007');
insert into Elects values('FIC112','VDL007');
insert into Elects values('FIC113','VDL007');
insert into Elects values('FIC114','VDL007');
insert into Elects values('FIC115',NULL);
insert into Elects values('FIC121','VDL008');
insert into Elects values('FIC122','VDL008');
insert into Elects values('FIC123','VDL008');
insert into Elects values('FIC124','VDL008');
insert into Elects values('FIC125',NULL);
insert into Elects values('FIC131','VDL009');
insert into Elects values('FIC132','VDL009');
insert into Elects values('FIC133','VDL009');
insert into Elects values('FIC134','VDL009');
insert into Elects values('FIC135',NULL);
insert into Elects values('FIC141','VDL010');
insert into Elects values('FIC142','VDL010');
insert into Elects values('FIC143','VDL010');
insert into Elects values('FIC144','VDL010');
insert into Elects values('FIC145',NULL);
insert into Elects values('FIC201','VDL011');
insert into Elects values('FIC202','VDL011');
insert into Elects values('FIC203','VDL011');
insert into Elects values('FIC204','VDL011');
insert into Elects values('FIC205',NULL);
insert into Elects values('FIC211','VDL012');
insert into Elects values('FIC212','VDL012');
insert into Elects values('FIC213','VDL012');
insert into Elects values('FIC214','VDL012');
insert into Elects values('FIC215',NULL);
insert into Elects values('FIC221','VDL013');
insert into Elects values('FIC222','VDL013');
insert into Elects values('FIC223','VDL013');
insert into Elects values('FIC224','VDL013');
insert into Elects values('FIC225',NULL);
insert into Elects values('FIC231','VDL014');
insert into Elects values('FIC232','VDL014');
insert into Elects values('FIC233','VDL014');
insert into Elects values('FIC234','VDL014');
insert into Elects values('FIC235',NULL);
insert into Elects values('FIC241','VDL015');
insert into Elects values('FIC242','VDL015');
insert into Elects values('FIC243','VDL015');
insert into Elects values('FIC244','VDL015');
insert into Elects values('FIC245',NULL);
COMMIT;







