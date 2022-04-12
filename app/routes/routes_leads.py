from flask import Blueprint
from app.controllers import controllers_leads

bp = Blueprint("leads", __name__, url_prefix="/leads")


bp.post("")(controllers_leads.create_leads)
bp.get("")(controllers_leads.read_all_leads)
bp.patch("")(controllers_leads.update_all_leads)
bp.delete("")(controllers_leads.delete_all_leads)