from Configs.DbConnection import *
def retrieve_names():
    names=[]
    try:
        with engine.connect() as conn:
            # user engine to execute a sql query
            result = conn.execute(text('Select *' 'from Places'))

            # iterate through returned results from query
            # and add it to out empty list
            # ex of retrieved data: (1, 'Uk')
            for i in result:
                names.append(i[1])
    except Exception as e:
        print(f"There was an issue with executing the following command:"
              f"{e}")
    return names