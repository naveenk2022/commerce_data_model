from alembic_utils.pg_trigger import PGTrigger

## Creating a trigger to apply `timestamp_update_on_edit()` to `products` on a row being updated
timestamp_update_apply_products_trigger = PGTrigger(
    schema="public",
    signature="timestamp_update_apply_products_trigger",
    on_entity="public.products",
    is_constraint=False,
    definition="""
BEFORE 
UPDATE 
  on products FOR EACH ROW EXECUTE FUNCTION timestamp_update_on_edit()
""",
)
