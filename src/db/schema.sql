CREATE TABLE IF NOT EXISTS Situations (
    id TEXT PRIMARY KEY NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Choises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    next_id TEXT NOT NULL,
    FOREIGN KEY (next_id) REFERENCES Situations(id)
);

CREATE TABLE IF NOT EXISTS Choises_Situations (
    choises_id INTEGER NOT NULL,
    situations_id TEXT NOT NULL,
    FOREIGN KEY (situations_id) REFERENCES Situations(id),
    FOREIGN KEY (choises_id) REFERENCES Choises(id)
)