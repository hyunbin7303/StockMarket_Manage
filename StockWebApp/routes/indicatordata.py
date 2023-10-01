from models.indicatordata import Indicatordata
from flask import jsonify, make_response, Response
from flask_smorest import Blueprint
from schemas import IndicatordataSchema
from repositories.indicatordata_repository import IndicatordataRepository
from di.container import Container
from dependency_injector.wiring import Provide, inject



indicatordata_bp = Blueprint("indicatordata", __name__, url_prefix='/indicatordata', description="Operations on Indicatordata")

@indicatordata_bp.route('/', methods=['GET'])
@indicatordata_bp.response(200, IndicatordataSchema(many=True))
@inject
def get_indicatordata(indicatordata_repo: IndicatordataRepository= Provide[Container.indicatordata_repo]):
    result = indicatordata_repo.get_all()
    return result


@indicatordata_bp.route('/<int:indicator_id>', methods=['GET'])
def get_indicatordata_byId(indicator_id: int, indicatordata_repo: IndicatordataRepository= Provide[Container.indicatordata_repo]):
    result = indicatordata_repo.get_by_id(indicator_id)
    return result


@indicatordata_bp.route('/', methods=['POST'])
@indicatordata_bp.arguments(IndicatordataSchema)
@inject
def post(new_indicatordata, repo: IndicatordataRepository= Provide[Container.indicatordata_repo]):
    data = Indicatordata(**new_indicatordata)
    repo.add(data)
    return Response({}, status=201)

