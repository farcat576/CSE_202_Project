USE All_Levels;

-- table for Aadhar Card
CREATE TABLE AADHAR_CARD(
aadhar_card_id CHAR(12),
person_name VARCHAR(20) NOT NULL,
age INT NOT NULL,
sex CHAR(1) NOT NULL,
mobile_number CHAR(10) NOT NULL, -- must have a registered mobile number, therefore NOT NULL
address VARCHAR(30) NOT NULL, -- must have a registered address, therefore NOT NULL
bank_account_no CHAR(16), -- can be paid in cash, therefore NULL is allowed
place_of_birth VARCHAR(20), -- can be unknown, therefore NULL is allowed
village_name VARCHAR(20) NOT NULL, -- must belong to a village, therefore NOT NULL
CHECK (sex='M' OR  sex='F'),
PRIMARY KEY(aadhar_card_id)
);


-- mapping a dairy farmer to their aadhar card
CREATE TABLE Dairy_Farmer_Possesses(
farmer_identification_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- every farmer must have a registered aadhar card, therefore NOT NULL
PRIMARY KEY(farmer_identification_id)
,FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);


-- table for Dairy Farmer (a dairy farmer account)
CREATE TABLE Dairy_Farmer(
farmer_identification_id CHAR(6),
milk_quantity DECIMAL(14,2) DEFAULT 0,
average_milk_quantity DECIMAL(14,2) DEFAULT 0,
cattlefeed DECIMAL(14,2) DEFAULT 0,
PRIMARY KEY(farmer_identification_id)
);



-- table for SMF
CREATE TABLE SMF(
state_code CHAR(3),
state_name VARCHAR(30) NOT NULL,
sold DECIMAL(14,2) DEFAULT 0,
cost DECIMAL(14,2) DEFAULT 0,
PRIMARY KEY(state_code)
);

-- table for VDCS
CREATE TABLE VDCS(
vdcs_code CHAR(6),
cattlefeed INT DEFAULT 0,
money DECIMAL(14,2) DEFAULT 0,
milk_quantity DECIMAL(14,2) DEFAULT 0,
village_name VARCHAR(20) NOT NULL,
PRIMARY KEY(vdcs_code)
);

-- table for VDCSL
CREATE TABLE VDCS_L(
vdcsl_id CHAR(6),
salary DECIMAL(14,2) DEFAULT 0,
last_paid DECIMAL(14,2) DEFAULT 0,
vdcs_code CHAR(6) NOT NULL,
PRIMARY KEY(vdcsl_id)
,FOREIGN KEY(vdcs_code) REFERENCES VDCS(vdcs_code)
);

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

-- table for Vet and Animal Husbandry Personnel
CREATE TABLE VAHP(
vah_id CHAR(6),
last_paid DATE,
salary DECIMAL(14,2) DEFAULT 0,
district_code CHAR(6) NOT NULL, -- each VAHP must must be hired by some DMU, therefore NOT NULL
PRIMARY KEY(vah_id),
FOREIGN KEY(district_code) REFERENCES DMU(district_code)
);

-- table for Processing Workers
CREATE TABLE PW(
pw_id CHAR(6),
last_paid DATE,
salary DECIMAL(14,2) DEFAULT 0,
district_code CHAR(6) NOT NULL, -- each VAHP must must be hired by some DMU, therefore NOT NULL
PRIMARY KEY(pw_id),
FOREIGN KEY(district_code) REFERENCES DMU(district_code)
);


-- mapping for which VDCS works under which DMU
CREATE TABLE VDCS_Works_Under_DMU(
district_code CHAR(6) NOT NULL, -- every village must work under some DMU, therefore NOT NULL
vdcs_code CHAR(6), 
PRIMARY KEY(vdcs_code),
FOREIGN KEY(district_code) REFERENCES DMU(district_code)
);

-- mapping for which DMU a VDCSL works for
CREATE TABLE Part_Of(
district_code CHAR(6) NOT NULL, -- every VDCSL must be a part of some DMU, therefore NOT NULL
vdcsl_id CHAR(6), 
PRIMARY KEY(vdcsl_id),
FOREIGN KEY(district_code) REFERENCES DMU(district_code)
);


-- mapping for which VAHP works for which VDCS
CREATE TABLE Works_Here(
vahp_id CHAR(6),
vdcs_code CHAR(6),
PRIMARY KEY(vahp_id),
FOREIGN KEY(vdcs_code) REFERENCES VDCS(vdcs_code)
);


-- table for mapping a Vet and Animal Husbandry Personnel to their Aadhar Card
CREATE TABLE VAHP_Possesses(
vahp_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- every vet and animal husbandry personnel must have a registered aadhar card, therefore NOT NULL
PRIMARY KEY(vahp_id),
FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);


-- table for mapping a Processing Worker to their Aadhar Card
CREATE TABLE PW_Possesses(
pw_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- every processing worker must have a registered aadhar card, therefore NOT NULL
PRIMARY KEY(pw_id),
FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);


-- table for mapping which Dairy Farmer belongs to which VDCS
CREATE TABLE DF_Works_Under_VDCS(
farmer_identification_id CHAR(6),
vdcs_code CHAR(6) NOT NULL, -- every farmer must belong to a vdcs, therefore NOT NULL
PRIMARY KEY(farmer_identification_id),
FOREIGN KEY(vdcs_code) REFERENCES VDCS(vdcs_code)
);

-- table for mapping which VDCSL a Dairy Farmer voted for
CREATE TABLE Elects(
farmer_identification_id CHAR(6),
vdcsl_id CHAR(6), -- a farmer can choose not to vote for a representative, therefore NULL is allowed
PRIMARY KEY(farmer_identification_id)
,FOREIGN KEY(vdcsl_id) REFERENCES VDCS_L(vdcsl_id)
);


--  table for mapping a VDCSL to their Aadhar Card
CREATE TABLE VDCSL_Possesses(
vdcsl_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- every farmer must have a registered aadhar card, therefore NOT NULL
PRIMARY KEY(vdcsl_id)
,FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);


-- table for transaction between the SMF and the Retailers
CREATE TABLE SMF_Transaction(
t_id char(10),
district_code CHAR(6),
amount_sent DECIMAL(14,2) DEFAULT 0,
state_code CHAR(3),
PRIMARY KEY(t_id),
FOREIGN KEY(state_code) REFERENCES SMF(state_code)
,FOREIGN KEY(district_code) REFERENCES DMU(district_code)
);


-- table for retailers
CREATE TABLE Retailers(
retailer_id CHAR(10),
retailer_name VARCHAR(30) NOT NULL,
district_code CHAR(6),
number_of_batches_bought INT DEFAULT 0,
amount_bought DECIMAL(14,2),
state_code CHAR(3),
PRIMARY KEY(retailer_id),
FOREIGN KEY(state_code) REFERENCES SMF(state_code),
FOREIGN KEY(district_code) REFERENCEs DMU(district_code)
);


-- table for mapping which DMU works under which SMF
CREATE TABLE DMU_Works_Under_SMF(
state_code CHAR(6) NOT NULL, -- every DMU must work under an SMF, therefore NOT NULL
district_code CHAR(6), 
PRIMARY KEY(district_code),
FOREIGN KEY(state_code) REFERENCES SMF(state_code)
);

-- table of records of sales made by the SMF
CREATE TABLE Sells(
state_code CHAR(6),
batch_id CHAR(10), 
PRIMARY KEY(batch_id),
FOREIGN KEY(state_code) REFERENCES SMF(state_code)
);