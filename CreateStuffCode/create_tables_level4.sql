USE All_Levels;


-- mapping a dairy farmer to their aadhar card
CREATE TABLE Dairy_Farmer_Possesses(
farmer_identification_id CHAR(6),
aadhar_card_id CHAR(12) NOT NULL, -- every farmer must have a registered aadhar card, therefore NOT NULL
PRIMARY KEY(farmer_identification_id)
,FOREIGN KEY(aadhar_card_id) REFERENCES AADHAR_CARD(aadhar_card_id)
);


-- a dairy farmer account
CREATE TABLE Dairy_Farmer(
farmer_identification_id CHAR(6),
milk_quantity DECIMAL(14,2) DEFAULT 0,
average_milk_quantity DECIMAL(14,2) DEFAULT 0,
cattlefeed DECIMAL(14,2) DEFAULT 0,
PRIMARY KEY(farmer_identification_id)
);