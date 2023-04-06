from voluptuous import Schema, PREVENT_EXTRA, Any

holidays_schema = Schema(
    {
        "status": Any('OK', str),
        "holidays": [str]
    },
    extra=PREVENT_EXTRA,
    required=True
)
