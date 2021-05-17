--DROP TABLE IF EXISTS model_evaluation;
--
--CREATE TABLE model_evaluation(
--    name TEXT PRIMARY KEY,
--    epoch INTEGER,
--    exactMatch FLOAT NOT NULL,
--    f1 FLOAT NOT NULL,
--    loss FLOAT NOT NULL
--);
--
--INSERT INTO model_evaluation VALUES('BiDAF_1', 1, 11.688,24.202, 425.050);
--INSERT INTO model_evaluation VALUES('BiDAF_2', 2, 24.646,41.789, 328.571);
--INSERT INTO model_evaluation VALUES('BiDAF_3', 3, 36.463,57.326, 258.688);
--INSERT INTO model_evaluation VALUES('BiDAF_4', 4, 39.035,60.373, 243.138);
--INSERT INTO model_evaluation VALUES('RNet_1', 1, 15.024,27.211, 408.350);
--INSERT INTO model_evaluation VALUES('RNet_2', 2, 22.646,38.789, 310.555);
--INSERT INTO model_evaluation VALUES('RNet_3', 3, 35.463,50.333, 252.456);
--INSERT INTO model_evaluation VALUES('RNet_4', 4, 40.035,58.321, 230.138);
--
--DROP TABLE IF EXISTS model_info;
--
--CREATE TABLE model_info(
--    id INTEGER PRIMARY KEY,
--    name TEXT NOT NULL,
--    dataset TEXT,
--    word_dimension INTEGER,
--    batch_size INTEGER,
--    character_dimension INTEGER,
--    dropout_rate FLOAT,
--    learning_rate FLOAT,
--    context_len INTEGER
--);
--
--INSERT INTO model_info (name, dataset, word_dimension, batch_size, character_dimension, dropout_rate, learning_rate, context_len)
--VALUES('BiDAF', 'SQuAD', 100, 50, 8, 0.2, 0.5, 150);
--INSERT INTO model_info (name, dataset, word_dimension, batch_size, character_dimension, dropout_rate, learning_rate, context_len)
--VALUES('RNet', 'SQuAD', 150, 60, 8, 0.1, 0.2, 200);
DROP TABLE IF EXISTS fav_answer;
CREATE TABLE fav_answer (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    document_title TEXT NOT NULL,
    score FLOAT,
    answer TEXT NOT NULL,
    concrete_answer TEXT
)