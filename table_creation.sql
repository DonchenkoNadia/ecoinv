CREATE TABLE processes (
    process_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    type VARCHAR(255)
);
CREATE TABLE inputs (
    input_id SERIAL PRIMARY KEY,
    process_id INTEGER NOT NULL,
    FOREIGN KEY (process_id) REFERENCES processes (process_id)
);

