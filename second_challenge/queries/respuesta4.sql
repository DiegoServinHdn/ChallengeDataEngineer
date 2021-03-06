USE my_db;

SELECT a.NOMBRE_AEROLINEA, COUNT(*) NUMERO_DE_VUELOS, v.DIA, a.ID_AEROLINEA
FROM vuelos v
	JOIN aerolineas a
		ON v.ID_AEROLINEA = a.ID_AEROLINEA
GROUP BY v.ID_AEROLINEA, v.DIA
HAVING NUMERO_DE_VUELOS > 2
ORDER BY NUMERO_DE_VUELOS DESC;

# No existe ninguna aerolinea con mas de 2 vuelos