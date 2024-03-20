CREATE TABLE users  (
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    create_at timestamp default current_timestamp NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE files  (
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) NOT NULL,
    content bytea NOT NULL,
    create_at timestamp default current_timestamp NOT NULL,
    last_modifier timestamp NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE user_files  (
    id INT GENERATED ALWAYS AS IDENTITY,
    
    CONSTRAINT user_fk
    FOREIGN KEY(id)
    REFERENCES users(id)
    ON DELETE SET NULL,
    
    CONSTRAINT file_fk
    FOREIGN KEY(id) 
    REFERENCES files(id)
    ON DELETE SET NULL,
    
    PRIMARY KEY(id)
);

CREATE TABLE logs  (
    id INT GENERATED ALWAYS AS IDENTITY,
    content VARCHAR(255) NOT NULL,
    update_at timestamp default current_timestamp NOT NULL,
    PRIMARY KEY(id)
);
