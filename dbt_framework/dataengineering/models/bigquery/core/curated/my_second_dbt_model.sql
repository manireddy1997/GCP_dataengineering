{{ 
    config(
        materialized='table',
        tags="my_second_dbt_model",
        alias='curated')

}}

select id from {{source('bigquery','my_first_dbt_model')}}