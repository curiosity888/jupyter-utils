def enable():
    """
    Register Jupyter magics for datalab.
    """
    try:
        from datalab.jupyter import register_bq_magic
        register_bq_magic()
    except Exception as e:
        # Если мы не в Jupyter — ничего не делаем
        pass