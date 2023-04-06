from voluptuous import Schema, PREVENT_EXTRA, Any

covid_restrictions_schema = Schema(
    {
        "status": str,
        "data": {
            "direction": str,
            "visa": str,
            "documents": str,
            "is_avia_open": bool,
            "special_form_needed": bool,
            "has_quarantine": bool,
            "quarantine_duration": Any(int, None),
            "link": str,
            "description": str,
            "has_additional_test": bool,
            "docs_unknown": bool,
            "modified_at": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)
