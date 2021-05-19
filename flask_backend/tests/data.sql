CREATE TABLE model_evaluation(
    name TEXT PRIMARY KEY,
    epoch INTEGER,
    exactMatch FLOAT NOT NULL,
    f1 FLOAT NOT NULL,
    loss FLOAT NOT NULL
);
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
INSERT INTO model_evaluation VALUES('BiDAF', 1, 11.688,24.202, 425.050);
INSERT INTO model_evaluation VALUES('RNet', 1, 15.024,27.211, 408.350);
INSERT INTO model_info (name, dataset, word_dimension, batch_size, character_dimension, dropout_rate, learning_rate, context_len)
VALUES('BiDAF', 'SQuAD', 100, 50, 8, 0.2, 0.5, 150);
INSERT INTO model_info (name, dataset, word_dimension, batch_size, character_dimension, dropout_rate, learning_rate, context_len)
VALUES('RNet', 'SQuAD', 150, 60, 8, 0.1, 0.2, 200);