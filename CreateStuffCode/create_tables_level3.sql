USE All_Levels;

CREATE TABLE VDCS(
vdcs_code CHAR(6),
cattlefeed INT DEFAULT 0,
money DECIMAL(14,2) DEFAULT 0,
milk_quantity DECIMAL(14,2) DEFAULT 0,
village_name VARCHAR(20) NOT NULL,
PRIMARY KEY(vdcs_code)
);

CREATE TABLE VDCS_L(
vdcsl_id CHAR(6),
salary DECIMAL(14,2) DEFAULT 0,
last_paid DECIMAL(14,2) DEFAULT 0,
vdcs_code CHAR(6) NOT NULL,
PRIMARY KEY(vdcsl_id)
,FOREIGN KEY(vdcs_code) REFERENCES VDCS(vdcs_code)
);


CREATE TABLE DF_Works_Under_VDCS(
farmer_identification_id CHAR(6),
vdcs_code CHAR(6) NOT NULL, -- every farmer must belong to a vdcs, therefore NOT NULL
PRIMARY KEY(farmer_identification_id),
FOREIGN KEY(vdcs_code) REFERENCES VDCS(vdcs_code)
);


CREATE TABLE Elects(
farmer_identification_id CHAR(6),
vdcsl_id CHAR(6), -- a farmer can choose not to vote for a representative, therefore NULL is allowed
PRIMARY KEY(farmer_identification_id)
,FOREIGN KEY(vdcsl_id) REFERENCES VDCS_L(vdcsl_id)
);


CREATE TABLE VDCSL_Possesses(
vdcsl_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- every farmer must have a registered aadhar card, therefore NOT NULL
PRIMARY KEY(vdcsl_id)
,FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);