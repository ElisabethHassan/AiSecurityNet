-- Create a table to store past file information
CREATE TABLE past_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ai_probability FLOAT NOT NULL
);
