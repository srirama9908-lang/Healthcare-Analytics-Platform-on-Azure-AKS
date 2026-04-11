{{ config(materialized='table') }}

select 
     {{ validate_date('APPOINTMENT_DATE')}} as is_valid
from {{ ref ('factslots')}}