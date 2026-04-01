//Добавляет строку или обновляет если она есть. И удаляет лишние пробелы чтобы не мешало в будущем
CREATE OR REPLACE PROCEDURE upsert_contact( p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    id_max INTEGER;
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook1 WHERE name = trim(p_name)) THEN
        UPDATE phonebook1 SET number_ph = p_phone WHERE name = trim(p_name);
    ELSE
		SELECT MAX(ID) INTO id_max FROM phonebook1;
        INSERT INTO phonebook1(id, name, number_ph) VALUES(id_max+1, trim(p_name), p_phone);
    END IF;
END;

$$;



//Создаём type 
CREATE TYPE user_data AS (name VARCHAR, number_ph VARCHAR);






//Создаём процедуру которая вставляет несколько контактов сразу в мой список контактов

	CREATE OR REPLACE PROCEDURE upsert_contacts(data user_data[])
LANGUAGE plpgsql AS $$
DECLARE
    id_max INTEGER;
DECLARE
    item user_data;
BEGIN
	FOREACH item IN ARRAY data
    LOOP
    IF EXISTS (SELECT 1 FROM phonebook1 WHERE name = trim(item.name)) THEN
        UPDATE phonebook1 SET number_ph = item.number_ph WHERE name = trim(item.name);
    ELSE
		SELECT MAX(ID) INTO id_max FROM phonebook1;
        INSERT INTO phonebook1(id, name, number_ph) VALUES(id_max+1, trim(item.name), item.number_ph);
    END IF;
	END LOOP;
END;

$$;