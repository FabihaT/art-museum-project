--Query 1:
--First table displays the table names, constraint names, and constraint types (foreign or primary) from the information schema for this database.
SELECT 
    INFORMATION_SCHEMA.TABLES.TABLE_NAME,
    INFORMATION_SCHEMA.TABLE_CONSTRAINTS.CONSTRAINT_NAME,
    INFORMATION_SCHEMA.TABLE_CONSTRAINTS.CONSTRAINT_TYPE
FROM INFORMATION_SCHEMA.TABLES 
INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS ON INFORMATION_SCHEMA.TABLES.TABLE_NAME = INFORMATION_SCHEMA.TABLE_CONSTRAINTS.TABLE_NAME
WHERE TABLES.TABLE_SCHEMA = 'ARTDATABASE';

--Second table shows the trigger name of the update trigger.
SELECT TRIGGER_NAME
FROM INFORMATION_SCHEMA.TRIGGERS
WHERE TRIGGER_SCHEMA = 'ARTDATABASE';

--Query 2:
SELECT *
FROM ARTOBJ
WHERE Art_Desc = 'Sculpture' AND Epoch = 'Renaissance';

--Query 3:
 SELECT Title, Artist, Art_yr
 FROM ARTOBJ, COLLECTIONS, KEPT_IN
 WHERE COLLECTIONS.Cname = KEPT_IN.Collect_name AND KEPT_IN.ArtID = ARTOBJ.ArtID
 ORDER BY Art_yr DESC;

--Query 4:
SELECT ARTOBJ.Art_Desc, ARTOBJ.Title
FROM ARTOBJ
WHERE ARTOBJ.ArtID IN ( SELECT sID
						FROM SCULPTURE
						WHERE ARTOBJ.ArtID = SCULPTURE.sID);

--Query 5:
SELECT ArtID, Title, Draw_on, Artist, Artist_Desc
FROM ((ARTIST JOIN ARTOBJ ON Name = Artist) JOIN PAINTING ON ArtID = pID);

--Query 6:	
--Creates update trigger which checks if updated permanent_collections Date_acq is greater than the Art_yr of artobj table.
DROP TRIGGER IF EXISTS date_acq_update;
CREATE TRIGGER date_acq_update
BEFORE UPDATE ON PERMANENT_COLLECTION
FOR EACH ROW
	SET NEW.Date_acq = IF ((SELECT Art_yr
							FROM ARTOBJ JOIN PERMANENT_COLLECTION ON CollectID = ArtID
							WHERE CollectID = OLD.CollectID) < NEW.Date_acq, NEW.Date_acq, OLD.Date_acq);

--First test case with invalid Date_acq which doesn't update the tuple so Changed rows = 0.
UPDATE PERMANENT_COLLECTION
SET Date_acq = '1540'
WHERE CollectID = '111222333';

--Second test case with valid Date_acq which does update the tuple so Changed rows = 1.
UPDATE PERMANENT_COLLECTION
SET Date_acq = '1700'
WHERE CollectID = '111222333';

--Execute the permanent_collections table after update.
SELECT *
FROM PERMANENT_COLLECTION;
		
--Query 7:
DROP TRIGGER IF EXISTS delete_collections
CREATE TRIGGER delete_collections
AFTER DELETE ON COLLECTIONS
FOR EACH ROW BEGIN
	DELETE FROM KEPT_IN WHERE KEPT_IN.Collect_name = OLD.CName;
