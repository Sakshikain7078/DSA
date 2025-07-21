# Write your MySQL query statement below
SELECT distinct author_id  as id
FROM Views
WhERE author_id = viewer_id order by author_id asc;