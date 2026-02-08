from alembic_utils.pg_function import PGFunction

## Creating a function that updates the `last_edited` column of a table
timestamp_update_on_edit = PGFunction(
    schema="public",
    signature="timestamp_update_on_edit()",
    definition="""
RETURNS TRIGGER AS $$ BEGIN NEW.last_edited = now();
RETURN NEW;
END;
$$ language PLPGSQL
""",
)
