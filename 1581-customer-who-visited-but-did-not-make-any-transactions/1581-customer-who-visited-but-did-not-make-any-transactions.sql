SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
LEFT JOIN Transactions t
ON Visits.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY customer_id;