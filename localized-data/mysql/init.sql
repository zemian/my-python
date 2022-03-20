-- create database localized_data;

CREATE TABLE locales (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    lang VARCHAR(5) NOT NULL,
    country VARCHAR(5) NULL,
    encoding VARCHAR(50),
    script VARCHAR(50)
);

CREATE TABLE countries(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    code CHAR(2),
    long_code CHAR(3),
    name VARCHAR(500),
    official_name VARCHAR(500),
    common_name VARCHAR(500),
    flag CHAR(8)
);
CREATE TABLE languages(id INTEGER PRIMARY KEY AUTO_INCREMENT, code CHAR(3), long_code CHAR(4), name VARCHAR(500));
CREATE TABLE currencies(id INTEGER PRIMARY KEY AUTO_INCREMENT, code CHAR(3), name VARCHAR(500));
CREATE TABLE scripts(id INTEGER PRIMARY KEY AUTO_INCREMENT, code CHAR(4), name VARCHAR(500));


CREATE TABLE us_states (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    abbr CHAR(2),
    name VARCHAR(500),
    fips VARCHAR(5),
    is_territory BOOLEAN,
    is_obsolete BOOLEAN,
    is_contiguous BOOLEAN,
    is_continental BOOLEAN,
    statehood_year INTEGER,
    capital VARCHAR(500),
    capital_tz VARCHAR(100),
    ap_abbr VARCHAR(10),
    name_metaphone VARCHAR(100)
);
CREATE TABLE us_states_time_zones (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    abbr CHAR(2),
    time_zone VARCHAR(100)
);

CREATE TABLE tz (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    zone VARCHAR(100),
    format VARCHAR(20),
    is_common BOOLEAN
);
CREATE TABLE tz_countries (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    country CHAR(2),
    time_zone VARCHAR(100)
);