# Delete an Item from a SQLAlchemy Database

*from [adarsh on StackOverflow](http://stackoverflow.com/questions/27158573/how-to-delete-record-by-id-in-flask-sqlalchemy)*

To delete an item from a SQLAlchemy database, just call the `delete` method on an item from a query, then `commit` it.

```python
User.query.filter_by(id=123).delete()
db.session.commit()
```

Also, before implementing this functionality, consider adding a 'disabled', 'inactive', or 'expired' column to the schema instead of actually deleting the item.
