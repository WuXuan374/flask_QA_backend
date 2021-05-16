DROP TABLE IF EXISTS modelEvalutation;

CREATE TABLE modelEvalutation(
    name TEXT PRIMARY KEY,
    exactMatch FLOAT NOT NULL,
    f1 FLOAT NOT NULL
);