#Exercicio 1

SELECT vendedor, SUM(valor) AS total_vendido, RANK() OVER (ORDER BY SUM(valor) DESC) AS ranqueado
FROM vendas
GROUP BY vendedor;

#Exercicio 2

