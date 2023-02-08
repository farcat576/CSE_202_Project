USE All_Levels;

-- table for DMU
CREATE TABLE DMU(
district_code CHAR(6),
district_name VARCHAR(30) NOT NULL,
money DECIMAL(14,2) DEFAULT 0,
batch_id_counter INT DEFAULT 1,
PRIMARY KEY(district_code)
);

-- table for transaction recrods between DMU and VDCS
CREATE TABLE DMU_Transaction(
t_id char(10),
district_code CHAR(6) NOT NULL, -- a transaction must occur between a DMU and a VDCS, therefore NOT NULL
vdcs_code CHAR(6) NOT NULL, -- a transaction must occur between a DMU and a VDCS, therefore NOT NULL
amount_sent DECIMAL(14,2) DEFAULT 0,
PRIMARY KEY(t_id)
,FOREIGN KEY(district_code) REFERENCES DMU(district_code)
,FOREIGN KEY(vdcs_code) REFERENCES VDCS(vdcs_code)
);

-- table for batches given by DMU and sold by SMF
CREATE TABLE Batch(
batch_id CHAR(10),
sell_district_code CHAR(6) NOT NULL, -- must be sold in some district, therefore NOT NULL
number_of_products INT DEFAULT 0,
total_price DECIMAL(14,2) DEFAULT 0,
district_code CHAR(6) NOT NULL, -- must be bought from some district, therefore NOT NULL
PRIMARY KEY(batch_id)
,FOREIGN KEY(district_code) REFERENCES DMU(district_code)
,FOREIGN KEY(sell_district_code) REFERENCES DMU(district_code)
);

-- table for vet and animal husbandry personnel
CREATE TABLE VAHP(
vah_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- each VAHP must have an aadhar card, therefore NOT NULL
last_paid DATE,
salary DECIMAL(14,2) DEFAULT 0,
district_code CHAR(6) NOT NULL, -- each VAHP must must be hired by some DMU, therefore NOT NULL
PRIMARY KEY(vah_id),
FOREIGN KEY(district_code) REFERENCES DMU(district_code),
FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);

-- table for processing workers
CREATE TABLE PW(
pw_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- each PW must have an aadhar card, therefore NOT NULL
last_paid DATE,
salary DECIMAL(14,2) DEFAULT 0,
district_code CHAR(6) NOT NULL, -- each VAHP must must be hired by some DMU, therefore NOT NULL
PRIMARY KEY(pw_id),
FOREIGN KEY(district_code) REFERENCES DMU(district_code),
FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);



CREATE TABLE VDCS_Works_Under_DMU(
district_code CHAR(6) NOT NULL, -- every village must work under some DMU, therefore NOT NULL
vdcs_code CHAR(6), 
PRIMARY KEY(vdcs_code),
FOREIGN KEY(district_code) REFERENCES DMU(district_code)
);


CREATE TABLE Part_Of(
district_code CHAR(6) NOT NULL, -- every VDCSL must be a part of some DMU, therefore NOT NULL
vdcsl_id CHAR(6), 
PRIMARY KEY(vdcsl_id),
FOREIGN KEY(district_code) REFERENCES DMU(district_code)
);



CREATE TABLE Works_Here(
vahp_id CHAR(6),
vdcs_code CHAR(6),
PRIMARY KEY(vahp_id),
FOREIGN KEY(vdcs_code) REFERENCES VDCS(vdcs_code)
);


-- table for mapping a vet and animal husbandry personnel to their aadhar card
CREATE TABLE VAHP_Possesses(
vahp_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- every vet and animal husbandry personnel must have a registered aadhar card, therefore NOT NULL
PRIMARY KEY(vahp_id),
FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);


-- table for mapping a processing worker to their aadhar card
CREATE TABLE PW_Possesses(
pw_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- every processing worker must have a registered aadhar card, therefore NOT NULL
PRIMARY KEY(pw_id),
FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);