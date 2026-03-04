from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://neondb_owner:npg_RzHyt7wCvL1B@ep-noisy-field-a8l23qm1-pooler.eastus2.azure.neon.tech/ba_database?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

if __name__ == '__main__':
    try:
        with engine.connect() as conn:
            result = conn.execute(text('Select * from "places"'))
            for i in result:
                #print(i)
                print(f"The name is retrieved is {i[1]}")
    except Exception as e:
        print(f"Connection failed : more details in the following:"
              f"{e}")
