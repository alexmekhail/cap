"""Public teaching example: actor identity is already authenticated by the caller."""


def vulnerable_read(records, actor_id, record_id):
    return records[record_id]  # Deliberately missing object-level authorization.


def authorized_read(records, actor_id, record_id):
    record = records[record_id]
    if record["owner_id"] != actor_id:
        raise PermissionError("Access denied")
    return record
