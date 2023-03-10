import flask
from flask import Blueprint
from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')



@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    ans = flask.jsonify(
        {
            'jobs': [item.to_dict(
                only=(
                    'id', 'job', 'work_size', 'collaborators',
                    'start_date', 'end_date', 'is_finished',
                    'category'
                )
            )]
        for item in jobs}
    )
    return ans

