import blueprint as blueprint


blueprint = blueprint.Blueprint('jobs_api', __name__, template_folder='templates')

@blueprint.rout
def get_jobs():
    return 'Under construction'