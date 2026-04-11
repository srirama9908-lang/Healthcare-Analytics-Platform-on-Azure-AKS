{% snapshot factsnapshot %}

{{
    config(
        target_schema='snapshots',
        unique_key='APPOINTMENT_DATE',
        strategy='check',
        check_cols=['APPOINTMENT_DATE']
    )
}}

select *
from {{ ref('factslots') }}

{% endsnapshot %}