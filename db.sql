

SELECT * FROM prices;


SELECT JSON_ARRAYAGG(JSON_OBJECT('inventory', inventory, 'OPEX', OPEX, 'sellthrough', sellthrough, 'cost', cost, 'profitpercentage', profitpercentage , 'perishability', perishability)) from prices;   