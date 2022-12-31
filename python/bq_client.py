# bq client to perform operation on Bigquery
from google.cloud import bigquery

def init(project):
    client = bigquery.Client(Project=project)
    return client

def create_ds(project,ds_name,ds_location):
    bq_client = init(project=project)
    dataset_id = bigquery.dataset(ds_name)
    dataset_id.location = ds_location
    dataset = bq_client.create_dataset(dataset_id)
    print("Created dataset {}.{}".format(bq_client.project, dataset.dataset_id))

def create_table(project,ds_name,tb_name,schema_file):
    # schema file should be valid comma separated CSV format with following order
    # Column_name,Column_datatype,REQUIRED/NOT REQUIRED
    bq_client = init(project=project)
    with open(schema_file,'r') as file_obj:
        schema_data = file_obj.read().split('\n')
    file_obj.close()
    schema = []
    for column in schema_data:
        column = column.split(',')
        if len(column) == 3:
            schema.append(bigquery.SchemaField(column[0], column[1], mode=column[2]))
        elif len(column) == 2:
            schema.append(bigquery.SchemaField(column[0], column[1]))
    if ds_name in list_datasets(project=project):
        table_id = project+'.'+ds_name+'.'+tb_name
        table = bigquery.Table(table_id, schema=schema)
        table = bq_client.create_table(table)
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )
        return 0
    else:
        return 1

def load_file(project,file_path):
    pass

def query(project,query_string):
    bq_client = init(project=project)
    query_job = bq_client.query(query_string)

def list_datasets(project):
    bq_client = init(project=project)
    datasets = list(bq_client.list_datasets())
    return datasets

def list_tables(project,dataset):
    bq_client = init(project=project)
    if dataset in list_datasets(project):
        tables = list(bq_client.list_tables(dataset))
        return tables
    else:
        print("Dataset Not found")
        return 1
def delete_table(project,dataset,table):
    pass

