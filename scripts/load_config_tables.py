from sqlalchemy import create_engine
import pandas as pd


def main():
    df = pd.read_csv('../data/ref_project_division.csv')

    engine = create_engine('postgresql://sampledb:sampledb@localhost:5432/sampledb')
    df.to_sql(name='cfg_instance',
              con=engine,
              if_exists='replace',
              index=False,
              dtype={'': ''})


if __name__ == '__main__':
    main()
