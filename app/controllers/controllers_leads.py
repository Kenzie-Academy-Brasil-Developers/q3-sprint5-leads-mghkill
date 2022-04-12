from http import HTTPStatus
from flask import jsonify, request
from datetime import datetime as dt
from sqlalchemy.orm.session import Session
from app.configs.database import db
from app.controllers import possible_key_error, serialize_number
from app.models.models_leads import Leads
from sqlalchemy.exc import IntegrityError

def create_leads():
    data = request.get_json()
    
    try:
            
        serialized_data = serialize_number(data)

        if serialized_data:
            return serialized_data

        data["creation_date"] = dt.now()
        data["last_visit"] = dt.now()

        leads_value = Leads(**data)
        
        session: Session = db.session
        
        session.add(leads_value)
        session.commit()

        return jsonify(leads_value), HTTPStatus.CREATED

    except TypeError:
        return possible_key_error()

    except KeyError:
        return possible_key_error()
        
    except IntegrityError:
        return {"error": "User already exists"}



def read_all_leads():

    session: Session = db.session
    query =  session.query(Leads)
    
    output_leads = query.order_by(Leads.last_visit).all()



    return jsonify(output_leads)



def update_all_leads():

    data = request.get_json()


    email = data["email"]

    session: Session = db.session

    
    output_lead = session.query(Leads).filter(Leads.email == email).first()   


    if not output_lead:
        return {"Error": "Email not found"}, HTTPStatus.NOT_FOUND
    
    # Transformar output_lead ou manipular em dicionario para pegar as keys last_visit e visits, e atualizar seus valores
    
    setattr(output_lead, "visits", 3)

    session.commit()


    return jsonify(output_lead), HTTPStatus.OK



def delete_all_leads():
    data = request.get_json()


    email = data["email"]

    session: Session = db.session

    output_delete_lead = session.query(Leads).filter(Leads.email == email).first()   

    if not output_delete_lead:
        return {"Error": "Email not found"}, HTTPStatus.NOT_FOUND

    session.delete(output_delete_lead)
    session.commit()


    return jsonify(output_delete_lead), HTTPStatus.OK