from flask_smorest import Blueprint
from schemas import IndicatorsSchema
from repositories.indicators_repository import IndicatorsRepository
from di.container import Container
from dependency_injector.wiring import Provide, inject

indicators_bp = Blueprint("indicators", __name__, description="Operations on Indicators")

@indicators_bp.route('/indicators', methods=['GET'])
@indicators_bp.response(200, IndicatorsSchema(many=True))
@inject
def get_indicators(indicator_repo: IndicatorsRepository= Provide[Container.indicators_repo]):
    result = indicator_repo.get_all()
    return result


@indicators_bp.route('/indicators/<int:indicator_id>', methods=['GET'])
def get_indicator_byId(indicator_id: int, indicator_repo: IndicatorsRepository= Provide[Container.indicators_repo]):
    result = indicator_repo.get_by_id(indicator_id)
    return result



