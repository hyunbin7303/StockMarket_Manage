import string
from models import indicatordata
from flask import request, jsonify, make_response, Response
from flask_smorest import abort, Blueprint
from flask_smorest import Blueprint
from schemas import IndicatordataSchema
from repositories.indicatordata_repository import IndicatordataRepository
from di.container import Container
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject



indicatordata_bp = Blueprint("indicatordata", __name__, description="Operations on Indicatordata")

@indicatordata_bp.route('/indicatordata', methods=['GET'])
@indicatordata_bp.response(200, IndicatordataSchema(many=True))
@inject
def get_indicatordata(indicatordata_repo: IndicatordataRepository= Provide[Container.indicatordata_repo]):
    result = indicatordata_repo.get_all()
    return result


@indicatordata_bp.route('/indicatordata/<int:indicator_id>', methods=['GET'])
def get_indicatordata_byId(indicator_id: int, indicatordata_repo: IndicatordataRepository= Provide[Container.indicatordata_repo]):
    result = indicatordata_repo.get_by_id(indicator_id)
    return result


@indicatordata_bp.route('/indicatordata', methods=['POST'])
@inject
def post(repo: IndicatordataRepository= Provide[Container.indicatordata_repo]):
    indi= indicatordata.Indicatordata(
                     value= request.json['value'],
                     announced_date= request.json['announced_date'],
                     recorded_date = request.json['recorded_date'],
                     date_source=request.json['date_source'])
    repo.add(indi)
    return Response({}, status=201)

