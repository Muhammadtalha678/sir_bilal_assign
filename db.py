from sqlmodel import SQLModel, Session, create_engine
class DBConfig:
    def __init__(self,url):
        self.url = url
        self.engine = None
    
    def openConnection(self):
        self.engine = create_engine(url=self.url,pool_pre_ping=True,echo=True)
        try:
            self.engine.connect()
            print("Db connect successfully")
        except Exception as e:
            print(f"error {e}")
            raise Exception(f"Error whie connecting db:{e}")
    def closeConnection(self):
        if self.engine:
            self.engine.dispose()
            print("Db disconnect successfully") 

    def create_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            yield session