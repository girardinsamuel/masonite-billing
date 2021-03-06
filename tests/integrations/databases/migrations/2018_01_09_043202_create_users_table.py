from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("users") as table:
            table.increments("id")
            table.string("name")
            table.string("email").unique()
            table.string("password")
            table.boolean("verified")
            table.string("remember_token").nullable()
            table.timestamp("verified_at").nullable()
            table.string("avatar").nullable()
            table.soft_deletes()
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop("users")
