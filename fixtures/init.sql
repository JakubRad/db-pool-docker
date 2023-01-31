DROP TABLE IF EXISTS users
;

CREATE TABLE IF NOT EXISTS users
(
    user_id    BIGINT,
    email      VARCHAR(255),
    first_name VARCHAR(64),
    last_name  VARCHAR(64),
    dw_date    TIMESTAMP DEFAULT NOW()
)
;

INSERT INTO users VALUES ('1', 'kubaradziwoniuk@gmail.com', 'Jakub', 'Radziwoniuk')
;
