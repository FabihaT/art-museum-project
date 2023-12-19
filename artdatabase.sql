DROP DATABASE IF EXISTS ARTDATABASE;
CREATE DATABASE ARTDATABASE; 
USE ARTDATABASE;

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	Name					varchar(30)	not null,
	Birthdate				varchar(30),
	Date_died				varchar(30),
    Country_of_origin		varchar(30)	not null,
	Main_style				varchar(30)	not null,
	Epoch					varchar(30)	not null,
    Artist_Desc				varchar(30)	not null,
	primary key (Name)
);

INSERT INTO ARTIST (Name, Birthdate, Date_died, Country_of_origin, Main_style, Epoch, Artist_Desc)
VALUES
('Leonardo da Vinci', 'April 15, 1452', 'May 2, 1519', 'Italy', 'Renaissance', 'High Renaissance', 'Painter, Scientist'),
('Claude Monet', 'November 14, 1840', 'December 5, 1926', 'France', 'Impressionism', '19th Century', 'Impressionist Painter'),
('Vincent van Gogh', 'March 30, 1853', 'July 29, 1890', 'Netherlands', 'Post-Impressionism', '19th Century', 'Post-Impressionist Painter'),
('Pablo Picasso', 'October 25, 1881', 'April 8, 1973', 'Spain', 'Cubism', '20th Century', 'Cubist Painter');

DROP TABLE IF EXISTS ARTOBJ;
CREATE TABLE ARTOBJ (
	ArtID					varchar(30)	not null,
	Art_Desc				varchar(30)	not null,
	Title					varchar(50)	not null,
    Artist					varchar(30),
	Art_yr					integer,
	Origin					varchar(30)	not null,
	Epoch					varchar(30)	not null,
	primary key (ArtID),
	foreign key (Artist) references ARTIST(Name)
);

INSERT INTO ARTOBJ (ArtID, Art_Desc, Title, Artist, Art_yr, Origin, Epoch)
VALUES
('444555666', 'Painting', 'Mona Lisa', 'Leonardo da Vinci', 1503, 'Italy', 'Renaissance'),
('777888999', 'Painting', 'Water Lilies', 'Claude Monet', 1916, 'France', 'Impressionism'),
('123456789', 'Painting', 'Starry Night', 'Vincent van Gogh', 1889, 'Netherlands', 'Post-Impressionism'),
('987654321', 'Painting', 'Guernica', 'Pablo Picasso', 1937, 'Spain', 'Cubism');

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

INSERT INTO COLLECTIONS (Name, CType, Description, Address, Phone, Contact_person)
VALUES
('The Louvre', 'Museum', 'World Famous Museum', 'Paris, France', 123456789, 'John Doe'),
('The Met', 'Museum', 'Metropolitan Museum of Art', 'New York, USA', 987654321, 'Jane Smith'),
('National Gallery', 'Museum', 'National Gallery of Art', 'London, UK', 234567891, 'Alice Johnson');

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
('444555666','Oil','Wood Panel','Renaissance'),
('777888999','Oil','Canvas','Impressionism'),
('123456789','Oil','Canvas','Post-Impressionism'),
('987654321','Oil','Canvas','Cubism');

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

INSERT INTO PERMANENT_COLLECTION (CollectID, Date_acq, Status, Cost)
VALUES
('444555666','1804','Exhibited',8000000),
('777888999','1950','In Storage',5000000),
('123456789','1941','Exhibited',7000000);

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
	primary key (Name),
	foreign key (ExID) references ARTOBJ(ArtID)
);

INSERT INTO EXHIBITIONS (Name, ExID, Start_date, End_date)
VALUES
('Impressionist Exhibition', '777888999', '2023-06-01', '2023-09-30'),
('Dutch Masters', '123456789', '2023-10-01', '2024-01-31');

DROP TABLE IF EXISTS KEPT_IN;
CREATE TABLE KEPT_IN (
    ArtID 					varchar(30) not null,
    Collect_name 			varchar(30) not null,
    foreign KEY (ArtID) references ARTOBJ(ArtID),
    foreign key (Collect_name) references COLLECTIONS(Name)
);

INSERT INTO KEPT_IN (ArtID, Collect_name)
VALUES
('444555666', 'The Louvre'),
('777888999', 'The Met'),
('123456789', 'National Gallery');

DROP USER IF EXISTS 'guest'@'localhost';
CREATE USER 'guest'@'localhost';
GRANT SELECT ON artdatabase.* TO 'guest'@'localhost';
FLUSH PRIVILEGES;