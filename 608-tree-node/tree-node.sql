SELECT
    a.id,
    CASE
        WHEN a.p_id IS NULL THEN 'Root'
        WHEN COUNT(b.id) > 0 THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree a
LEFT JOIN Tree b
    ON a.id = b.p_id
GROUP BY a.id, a.p_id;