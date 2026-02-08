from alembic_utils.pg_view import PGView

order_line_items = PGView(
    schema="public",
    signature="order_line_items",
    definition="""
select op.order_id , 
	op.product_id, 
	op.product_count,
	p.product_name, 
	p.description, 
	p.price as unit_price, 
	op.product_count * p.price as order_price
	from order_products op 
join products p 
on op.product_id = p.product_id 
""",
)
