USE my_db;

SELECT a.NOMBRE_AEROLINEA, COUNT(*) NUMERO_DE_VUELOS, v.ID_AEROLINEA
FROM vuelos v
	JOIN aerolineas a
		ON v.ID_AEROLINEA = a.ID_AEROLINEA
GROUP BY v.ID_AEROLINEA
ORDER BY NUMERO_DE_VUELOS DESC
LIMIT 1;

# Interjet

# Interjet y Aeromar tienen el mismo numero de vuelos y son los que mas tienen