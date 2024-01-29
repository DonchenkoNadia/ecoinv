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

CREATE TABLE input_properties (
    property_id SERIAL PRIMARY KEY,
    input_id INTEGER NOT NULL,
    property_name VARCHAR(255) NOT NULL,
    property_value TEXT NOT NULL,
    FOREIGN KEY (input_id) REFERENCES inputs (input_id)
);

CREATE TABLE outputs (
    output_id SERIAL PRIMARY KEY,
    process_id INTEGER NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    quantity DECIMAL NOT NULL,
    unit VARCHAR(100) NOT NULL,
    FOREIGN KEY (process_id) REFERENCES processes (process_id)
);