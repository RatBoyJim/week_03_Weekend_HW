DROP TABLE players;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    choice VARCHAR(255),
    won INT,
    drawn INT,
    lost INT
);

