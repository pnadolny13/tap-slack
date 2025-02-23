from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.StringType, required=True),
    th.Property("name", th.StringType),
    th.Property("is_channel", th.BooleanType),
    th.Property("is_group", th.BooleanType),
    th.Property("is_im", th.BooleanType),
    th.Property("created", th.StringType),
    th.Property("creator", th.StringType),
    th.Property("is_archived", th.BooleanType),
    th.Property("is_general", th.BooleanType),
    th.Property("unlinked", th.StringType),
    th.Property("name_normalized", th.StringType),
    th.Property("is_shared", th.BooleanType),
    th.Property("is_ext_shared", th.BooleanType),
    th.Property("is_org_shared", th.BooleanType),
    th.Property("is_pending_ext_shared", th.BooleanType),
    th.Property("shared_team_ids", th.ArrayType(th.StringType)),
    th.Property("pending_shared", th.ArrayType(th.StringType)),
    th.Property("pending_connected_team_ids", th.ArrayType(th.StringType)),
    th.Property("parent_conversation", th.StringType),
    th.Property("is_member", th.BooleanType),
    th.Property("is_private", th.BooleanType),
    th.Property("is_mpim", th.BooleanType),
    th.Property(
        "topic",
        th.ObjectType(
            th.Property("value", th.StringType),
            th.Property("creator", th.StringType),
            th.Property("last_set", th.StringType),
        ),
    ),
    th.Property(
        "purpose",
        th.ObjectType(
            th.Property("value", th.StringType),
            th.Property("creator", th.StringType),
            th.Property("last_set", th.StringType),
        ),
    ),
    th.Property("previous_names", th.ArrayType(th.StringType)),
    th.Property("num_members", th.IntegerType),
).to_dict()
