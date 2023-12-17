--artdatabase.sql
DROP DATABASE IF EXISTS ARTDATABASE;
CREATE DATABASE ARTDATABASE; 
USE ARTDATABASE;

DROP TABLE IF EXISTS ARTOBJ;
CREATE TABLE ARTOBJ (
	ArtID					varchar(30)	not null,
	Description				varchar(30)	not null,
	Title					varchar(30)	not null,
    Artist					varchar(30),
	Art_yr					integer,
	Origin					varchar(30)	not null,
	Epoch					varchar(30)	not null,
	primary key (ArtID)
	foreign key (Artist) references ARTIST(Name)
);

INSERT INTO ARTOBJ (ArtID, Description, Title, Artist, Art_yr, Origin, Epoch)
VALUES
('111222333','Painting','Elizabeth I (The Hampden Portrait)','George Gower', '1567', 'London', 'Renaissance');

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	Name					varchar(30)	not null,
	Birthdate				varchar(30),
	Date_died				varchar(30),
    Country_of_origin		varchar(30)	not null,
	Main_style				varchar(30)	not null,
	Epoch					varchar(30)	not null,
    Description				varchar(30)	not null,
	primary key (Name)
);

INSERT INTO ARTIST (Name, Birthdate, Date_died, Country_of_origin, Main_style, Epoch, Description)
VALUES
('George Gower','Null Null, 1540','August 30, 1596','London', null, 'Renaissance', 'Portrait Painter');

DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS (
	Name					varchar(30)	not null,
	CType					varchar(30)	not null,
	Description				varchar(30)	not null,
    Address					varchar(30)	not null,
	Phone					integer,
    Contact_person			varchar(30)	not null,
	primary key (Name)
);

DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE (
	sID						varchar(30)	not null,
	Material				varchar(30) not null,
	Height					integer not null,
    Weight					integer not null,
	Style					varchar(30)	not null,
	foreign key (sID) references ARTOBJ(ArtID)
);

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
	pID						varchar(30)	not null,
	Paint_type				varchar(30) not null,
	Draw_on					varchar(30) not null,
	Style					varchar(30) not null,
	foreign key (pID) references ARTOBJ(ArtID)
);

INSERT INTO PAINTING (pID, Paint_type, Draw_on, Style)
VALUES
('111222333','Oil','Canvas','Renaissance');

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
	oID						varchar(30)	not null,
	ObjType					varchar(30) not null,
    Style					varchar(30) not null,
	foreign key (oID) references ARTOBJ(ArtID)
);

DROP TABLE IF EXISTS PERMANENT_COLLECTION;
CREATE TABLE PERMANENT_COLLECTION (
	CollectID				varchar(30)	not null,
	Date_acq				varchar(30) not null,
	Status					varchar(30) not null,
	Cost					integer not null,
	foreign key (CollectID) references ARTOBJ(ArtID)
);

DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED (
	BorrowID				varchar(30)	not null,
	Collection				varchar(30) not null,
	date_borrowed			varchar(30) not null,
	date_return				varchar(30) not null,
	foreign key (BorrowID) references ARTOBJ(ArtID)
);

DROP TABLE IF EXISTS EXHIBITIONS;
CREATE TABLE EXHIBITIONS (
	Name					varchar(30)	not null,
	ExID					varchar(30)	not null,
	Start_date				varchar(30)	not null,
	End_date				varchar(30)	not null,
	primary key (Name)
	foreign key (ExID) references ARTOBJ(ArtID)
);

DROP TABLE IF EXISTS KEPT_IN;
CREATE TABLE KEPT_IN (
	ArtID					varchar(30)	not null,
	Collect_name			varchar(30)	not null,
	foreign key (ArtID) references ARTOBJ(ArtID)
	foreign key (Collect_name) references COLLECTIONS(Name)
);