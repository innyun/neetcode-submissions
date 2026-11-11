-- Write your query below
select c.customer_id, c.customer_name
from customers c
where exists (
    select o.product_name from orders o where c.customer_id = o.customer_id and o.product_name = 'A'
)
and exists (
    select o.product_name from orders o where c.customer_id = o.customer_id and o.product_name = 'B'
)
and not exists (
    select o.product_name from orders o where c.customer_id = o.customer_id and o.product_name = 'C'
)
order by c.customer_name