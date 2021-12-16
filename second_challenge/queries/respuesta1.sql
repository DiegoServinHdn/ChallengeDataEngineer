USE my_db;

SELECT a.NOMBRE_AEROPUERTO, COUNT(*) NUMERO_DE_MOVIMIENTOS, v.ID_AEROPUERTO
FROM vuelos v
	JOIN aeropuertos a
		ON v.ID_AEROPUERTO = a.ID_AEROPUERTO
GROUP BY v.ID_AEROPUERTO
ORDER BY NUMERO_DE_MOVIMIENTOS DESC
LIMIT 1;

# Benito Juarez

# Benito Juarez y la paz tienen el mismo numero de movimientos y son los que mas tienen