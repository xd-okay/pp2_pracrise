CREATE OR REPLACE FUNCTION get_contacts(p text)
RETURNS TABLE(id integer, name VARCHAR, number_ph VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT aldiyar.id, aldiyar.name, aldiyar.number_ph FROM phonebook1 aldiyar
                 WHERE aldiyar.name ILIKE '%' || p || '%'
                    OR aldiyar.number_ph ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;




//pagination
CREATE OR REPLACE FUNCTION pagination(limits int, offsets int)
RETURNS TABLE(id integer, name character varying, number_ph character varying) 
LANGUAGE plpgsql AS $$
BEGIN
	RETURN QUERY SELECT * FROM phonebook1
	ORDER BY ID ASC
	LIMIT limits
	OFFSET offsets;
END;
$$; 	`	