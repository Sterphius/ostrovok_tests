from voluptuous import Schema, PREVENT_EXTRA, Any

hotel_schema = Schema(
    {
        "otahotel_id": str,
        "master_id": int,
        "hotel_name": str,
        "region_id": int,
        "region_name": str,
        "country_code": str,
        "country_name": str,
        "hotel_kind": str,
        "hotel_address": str,
        "slug": str,
        "region_name_en": str,
        "country_name_en": str,
        "is_natdis_critical": bool
    },
    extra=PREVENT_EXTRA,
    required=True
)

region_schema = Schema(
    {
        "id": int,
        "type": str,
        "name": str,
        "country": str,
        "country_code": str,
        "currency_code": str,
        "pretty_slug": str,
        "slug": str,
        "is_sales_closed": bool,
        "is_natdis_critical": bool,
        "name_en": str,
        "country_en": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

hotel_search_schema = Schema(
    {
        "hotels": [hotel_schema],
        "regions": [region_schema]
    },
    extra=PREVENT_EXTRA,
    required=True
)
