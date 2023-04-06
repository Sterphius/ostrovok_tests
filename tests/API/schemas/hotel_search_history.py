from voluptuous import Schema, PREVENT_EXTRA, Any

hotel_search_history_schema = Schema(
    {
        "status": Any('ok', str),
        "hotel_searches": []
    },
    extra=PREVENT_EXTRA,
    required=True
)
