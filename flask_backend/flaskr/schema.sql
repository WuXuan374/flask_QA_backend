DROP TABLE IF EXISTS model_evalutation;

CREATE TABLE model_evalutation(
    name TEXT PRIMARY KEY,
    exactMatch FLOAT NOT NULL,
    f1 FLOAT NOT NULL,
    loss FLOAT NOT NULL
);

INSERT INTO model_evalutation VALUES('BiDAF_epoch1', 11.688,24.202, 425.050);
INSERT INTO model_evalutation VALUES('BiDAF_epoch2', 24.646,41.789, 328.571);
INSERT INTO model_evalutation VALUES('BiDAF_epoch3', 36.463,57.326, 258.688);
INSERT INTO model_evalutation VALUES('BiDAF_epoch4', 39.035,60.373, 243.138);