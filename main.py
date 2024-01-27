from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy import text
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

class InputPropertySchema(BaseModel):
    property_name: str
    property_value: str

class InputSchema(BaseModel):
    properties: list[InputPropertySchema]

class ProcessSchema(BaseModel):
    name: str
    description: str
    type: str
    inputs: list[InputSchema]

SQLALCHEMY_DATABASE_URL = "postgresql://admin:TheBestPassword@localhost/database"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Process(Base):
    __tablename__ = 'processes'
    process_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)

    inputs = relationship("Input", back_populates="process")

class Input(Base):
    __tablename__ = 'inputs'

    input_id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey('processes.process_id'))

    process = relationship("Process", back_populates="inputs")
    input_properties = relationship("InputProperty", back_populates="input")


class InputProperty(Base):
    __tablename__ = 'input_properties'

    property_id = Column(Integer, primary_key=True)
    input_id = Column(Integer, ForeignKey('inputs.input_id'))
    property_name = Column(String)
    property_value = Column(String)

    # Relationship to Input
    input = relationship("Input", back_populates="input_properties")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/add_process", response_model=ProcessSchema)
def add_process(process: ProcessSchema, db: Session = Depends(get_db)):
    db_process = Process(name=process.name, description=process.description, type=process.type)
    db.add(db_process)
    db.commit()
    db.refresh(db_process)

    response_inputs = []
    for input_data in process.inputs:
        db_input = Input(process_id=db_process.process_id)
        db.add(db_input)
        db.commit()
        db.refresh(db_input)

        response_properties = []
        for prop in input_data.properties:
            db_prop = InputProperty(input_id=db_input.input_id, property_name=prop.property_name, property_value=prop.property_value)
            db.add(db_prop)
            response_properties.append({"property_name": prop.property_name, "property_value": prop.property_value})
        db.commit()
        response_inputs.append({"properties": response_properties})

    return {
        "name": db_process.name,
        "description": db_process.description,
        "type": db_process.type,
        "inputs": response_inputs
    }


@app.get("/test_connection")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # Attempt a simple query to check the database connection
        result = db.execute(text("SELECT version();"))
        version = result.fetchone()
        return {"db_version": version[0]}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0", 
        port=8080, 
        #reload=True, 
        workers=4
    )
	#uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True) 
    server = uvicorn.Server(config=config)
    server.run()