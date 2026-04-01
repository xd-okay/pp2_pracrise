CREATE OR REPLACE FUNCTION get_contacts(p text)
RETURNS TABLE(id integer, name VARCHAR, number_ph VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT aldiyar.id, aldiyar.name, aldiyar.number_ph FROM phonebook1 aldiyar
                 WHERE aldiyar.name ILIKE '%' || p || '%'
                    OR aldiyar.number_ph ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;