from IPython.core.magic import register_cell_magic
from datalab.bigquery import run_query

def register_bq_magic():
    @register_cell_magic
    def bq(line, cell):
        args = line.split()
        max_gb = 5
        page_size = 20
        df_name = None
    
        for part in args:
            if part.startswith("max_gb="):
                max_gb = float(part.split("=")[1])
            if part.startswith("page_size="):
                page_size = int(part.split("=")[1])
            if part.startswith("df_name="):
                df_name = str(part.split("=")[1])
    
        query = cell
        df = run_query(query, max_gb=max_gb)

        if df_name:
            ipy = get_ipython()
            ipy.user_ns[df_name] = df
        else:
            ipy.user_ns['df_temp'] = df

        display(df)