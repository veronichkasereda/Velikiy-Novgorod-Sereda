import flask
from flask import Blueprint, jsonify
from flask import make_response

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


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_onejob(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return flask.jsonify({'error': 'No such job'})
    ans = flask.jsonify(
        {
            'jobs': [jobs.to_dict(
                only=(
                    'id', 'job', 'work_size', 'collaborators',
                    'start_date', 'end_date', 'is_finished',
                    'category'
                )
            )]
        }
    )
    return ans


@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404




@blueprint.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
