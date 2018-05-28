SELECT AVG(count) avgPets
FROM (SELECT COUNT(*) count
      FROM pets_pet
      GROUP BY owner_id) pets