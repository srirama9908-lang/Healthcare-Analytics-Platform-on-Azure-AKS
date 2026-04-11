{% macro validate_date(column_name)%}
 case
    when {{column_name}} is null then 'null'
    when {{column_name}} < '1900-01-01' then 'invalid'
    else  {{column_name}}
 end
 {% endmacro %}
