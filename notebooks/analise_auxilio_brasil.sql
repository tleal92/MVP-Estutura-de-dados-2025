# Análise Auxílio Brasil
# (Executado no Databricks)

-- Total por estado
SELECT uf, SUM(valor_parcela) AS total_pago
FROM auxilio_brasil
GROUP BY uf
ORDER BY total_pago DESC;
