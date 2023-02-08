USE All_Levels;

-- an aadhar card
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