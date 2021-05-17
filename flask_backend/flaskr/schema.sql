DROP TABLE IF EXISTS model_evaluation;

CREATE TABLE model_evaluation(
    name TEXT PRIMARY KEY,
    epoch INTEGER,
    exactMatch FLOAT NOT NULL,
    f1 FLOAT NOT NULL,
    loss FLOAT NOT NULL
);

INSERT INTO model_evaluation VALUES('BiDAF_1', 1, 11.688,24.202, 425.050);
INSERT INTO model_evaluation VALUES('BiDAF_2', 2, 24.646,41.789, 328.571);
INSERT INTO model_evaluation VALUES('BiDAF_3', 3, 36.463,57.326, 258.688);
INSERT INTO model_evaluation VALUES('BiDAF_4', 4, 39.035,60.373, 243.138);

DROP TABLE IF EXISTS model_info;

CREATE TABLE model_info(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dataset TEXT,
    word_dimension INTEGER,
    batch_size INTEGER,
    character_dimension INTEGER,
    dropout_rate FLOAT,
    learning_rate FLOAT,
    context_len INTEGER
);

INSERT INTO model_info (name, dataset, word_dimension, batch_size, character_dimension, dropout_rate, learning_rate, context_len)
VALUES('BiDAF', 'SQuAD', 100, 50, 8, 0.2, 0.5, 150);