from flask import Blueprint, render_template, request, redirect, url_for
from utils.route_utils import calculate_distance_matrix_with_shop, assign_shipments, generate_map
import pandas as pd

optimize_bp = Blueprint('optimize', __name__)

cache = {'excel_data': None, 'assignments': {}}

@optimize_bp.route('/')
def home():
    return render_template('index.html')

@optimize_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            cache['excel_data'] = pd.read_excel(file, sheet_name="Shipments_Data")
            return redirect(url_for('optimize.select_timeslot'))
    return render_template('upload.html')
