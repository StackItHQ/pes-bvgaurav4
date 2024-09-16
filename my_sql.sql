show databases;
create database spread;
use spread;
create table spreadsheet(
	spreadsheet_id varchar(100) not null PRIMARY KEY,
    spreadsheet_name varchar(100),
    owner varchar(100),
    creation_date DATE not null
);

create table spreadsheet_data(
	spreadsheet_id varchar(100) not null,
    data_date DATE not null,
    data_index varchar(100) not null,
    x varchar(100) not null,
    y varchar(100) not null,
    data_value TEXT,
    PRIMARY KEY (spreadsheet_id, data_index,x,y),
    FOREIGN KEY (spreadsheet_id) REFERENCES spreadsheet(spreadsheet_id)
);
--  i forgot cascadings

ALTER TABLE spreadsheet_data DROP FOREIGN KEY spreadsheet_id;

ALTER TABLE spreadsheet_data
ADD CONSTRAINT spreadsheet_id
FOREIGN KEY (spreadsheet_id) REFERENCES spreadsheet(spreadsheet_id)
ON DELETE CASCADE
ON UPDATE CASCADE;