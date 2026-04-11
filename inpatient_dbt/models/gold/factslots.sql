{{ config(materialized='table') }}

select
    APPOINTMENT_DATE,
    count(*) as total_appointments
from {{ ref('cleaned_slots') }}
group by APPOINTMENT_DATE