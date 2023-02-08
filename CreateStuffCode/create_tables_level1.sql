USE All_Levels;

-- table for SMF
CREATE TABLE SMF(
state_code CHAR(3),
state_name VARCHAR(30) NOT NULL,
sold DECIMAL(14,2) DEFAULT 0,
cost DECIMAL(14,2) DEFAULT 0,
PRIMARY KEY(state_code)
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


CREATE TABLE DMU_Works_Under_SMF(
state_code CHAR(6) NOT NULL, -- every DMU must work under an SMF, therefore NOT NULL
district_code CHAR(6), 
PRIMARY KEY(district_code),
FOREIGN KEY(state_code) REFERENCES SMF(state_code)
);


CREATE TABLE Sells(
state_code CHAR(6),
batch_id CHAR(10), 
PRIMARY KEY(batch_id),
FOREIGN KEY(state_code) REFERENCES SMF(state_code)
);